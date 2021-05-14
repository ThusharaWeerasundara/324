"""TODO:
    E/16/388
    Server implementation

    * implement state transitions and list task for given list of states
"""
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from pprint import pformat
from typing import Mapping, List, Tuple

import grpc
from google.protobuf import (
    empty_pb2,
    wrappers_pb2,
)
from grpc import server

import task_pb2
import task_pb2_grpc

class TaskapiImpl:

    def __init__(self, taskfile: str):        #constructor to initialize file to store tasks, taskid and Lock object
        self.taskfile = taskfile              
        self.task_id = 0
        self.lock = threading.Lock()
        self.states = {
                        0: "OPEN",
                        1: "ASSIGNED",
                        2: "PROGRESSING",
                        3: "DONE",
                        4: "CANCELLED"
                    }						#task state mappings

    def __enter__(self):
        """Load tasks from self.taskfile"""
        with open(self.taskfile, mode="rb") as t:  #use context manager to read taskfile
            tasklist = task_pb2.Tasks()         #new Tasks object to hold tasks
            tasklist.ParseFromString(t.read())  #read from taskfile
            logging.info(f"Loaded data from {self.taskfile}")         
            self.tasks: Mapping[int, task_pb2.Task] = {t.id : t for t in tasklist.pending}  #store in tasks dictionary, task id as key and task as value
                        
            if(len(self.tasks) != 0):
                self.task_id = max(self.tasks.keys()) + 1  #get the id of next task after read from file
            else:
                self.task_id = 0

        return self     #retun the class

    #to save and load tasks to and from a file.
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""

        with open(self.taskfile, mode="wb") as t:   #use context manager to erite to taskfile
            tasks = task_pb2.Tasks(pending = self.tasks.values())   #store tasks in the 'tasks' dictonary
            t.write(tasks.SerializeToString())                      #write it to taskfile
            logging.info(f"Saved data to {self.taskfile}")


    @staticmethod	#static method to decide whether state transitions are possible or not
    def transition(current_state: int, next_state: int):
        if current_state == 0 and (next_state == 0 or next_state == 1 or next_state == 4):	#transitions from OPEN state
            return True
        elif current_state == 1 and (next_state == 1 or next_state == 2):	#transitions from ASSIGNED state
            return True
        elif current_state == 2 and (next_state == 2 or next_state == 3 or next_state == 4):	#transitions from PROGRESSING state
            return True
        #self loops for DONE and CANCELLED are useleff because those tasks are already completed or neglected

        else:	#for invalid transtions
            return False
    



    #Implement TaskapiImpl.editTask RPC that edits an existing task. 
    def editTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task:    #method to edit tasks
        
        logging.debug(f"editTask parameters {pformat(request)}")

        MAXLEN = 1024   #maximum description limit

        #get id and r=description given by user
        idno = request.id    

        nextState = request.state
        
        if len(request.description) > MAXLEN:  #if user input description exceed maximum limit, it is invalid
            msg = 'Length of `Task Description` cannot be more than 1024 characters'
            context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()

       
        with self.lock:   #need a lock to prevent data races. data race occurs when access stored values in "tasks" dictionary
            ids = self.tasks.keys() #get already stored task ids. need mutual exclusion

            if idno not in ids:     #if user given task id is not stored, it is invalid

                msg = 'id number is invalid'
                context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return task_pb2.Task()  

            task = self.tasks[idno]  #get stored task
            curState = task.state 	#get current state
            

            if TaskapiImpl.transition(curState, nextState):	#check whether transition is possible or not?

                self.tasks[idno] = request 		#If possible update the task and return it
                logging.info(f"next state : {request.state}")
                return self.tasks[idno]
           
            else:  #for invalid transitions
                
                first = self.states.setdefault(curState, "an Unknown")   
                second = self.states.setdefault(nextState, "an Unknown")
                msg = f"invalid transition from {first} state to {second} state" #error message format
                context.set_details(msg)	#set error 
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return task_pb2.Task()	#return empty tasks for error scenarios


    def addTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task: #method to add a new task
        
        logging.debug(f"addTask parameters {pformat(request)}")
            
        MAXLEN = 1024   #maximum description limit

        if len(request.value) > MAXLEN:     #if user input description exceed maximum limit, it is invalid
            msg = 'Length of `Task Description` cannot be more than 1024 characters'
            context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()


        with self.lock: #need a lock to prevent data races. data race occurs when access "tasks" dictionary and task_id variable
            t = task_pb2.Task(id=self.task_id, description=request.value, state = task_pb2.TaskState.Value('OPEN'))  #create a new task for added description
            #state of new tasks are always OPEN
            self.tasks[self.task_id] = t #store the new task


            self.task_id += 1 #increment task id
            
            logging.info(f"Added task {t}")   
            return t #return new task


    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> task_pb2.Task: #method to delete a task

        if request.value not in self.tasks.keys():   #if user given task id is not stored, it is invalid
            msg = 'id number is invalid'
            context.set_details(msg)        #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()

        with self.lock:     #need a lock to prevent data races. data race occurs when access stored values in "tasks" dictionary
            logging.debug(f"delTask parameters {pformat(request)}")
            return self.tasks.pop(request.value) #if no given id is valid, delete and send the required task

#EX3 return a list of tasks that are in the specified states.If TaskQuery.selected is empty, return a list of all tasks.
    def listTasks(self, request: task_pb2.TaskQuery, context) -> task_pb2.Tasks:
        
        logging.debug(f"listTasks parameters {pformat(request)}")
        
        if not request.selected:	#if no states were choosen as inputs
            return task_pb2.Tasks(pending = self.tasks.values())

        requiredStates: List[task_pb2.TaskState] = request.selected	#get given states
        requiredTasks: List[task_pb2.Task] = [task for task in self.tasks.values() if task.state in requiredStates] #get required tasks by list comprehension
        return task_pb2.Tasks(pending=requiredTasks)	#return list


TASKFILE = "tasklist.protobuf"
if __name__ == "__main__":
    Path(TASKFILE).touch()
    logging.basicConfig(level=logging.DEBUG)

    with ThreadPoolExecutor(max_workers=1) as pool, TaskapiImpl(
        TASKFILE
    ) as taskapiImpl:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(taskapiImpl, taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
