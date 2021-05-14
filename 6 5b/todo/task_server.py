"""TODO:
    E/16/388
    Server implementation

    * Implement error handling in TaskapiImpl methods
    * Implement saveTasks, loadTasks
    * Implement TaskapiImpl.editTask (ignoring write conflicts)
    * Fix data race in TaskapiImpl.addTask
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging
from pprint import pformat
from typing import Mapping, Sequence, Tuple
import threading

from google.protobuf import (
    any_pb2,
    api_pb2,
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    source_context_pb2,
    struct_pb2,
    timestamp_pb2,
    type_pb2,
    wrappers_pb2,
)
from grpc import server, StatusCode
import task_pb2, task_pb2_grpc


class TaskapiImpl:

    def __init__(self, taskfile: str):        #constructor to initialize file to store tasks, taskid and Lock object
        self.taskfile = taskfile              
        self.task_id = 0
        self.lock = threading.Lock()


    #4. Complete TaskapiImpl.__enter__ and TaskapiImpl.__exit__ to save and load tasks to and from a file.
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

    #4. Complete TaskapiImpl.__enter__ and TaskapiImpl.__exit__ to save and load tasks to and from a file.
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""

        with open(self.taskfile, mode="wb") as t:   #use context manager to erite to taskfile
            tasks = task_pb2.Tasks(pending = self.tasks.values())   #store tasks in the 'tasks' dictonary
            t.write(tasks.SerializeToString())                      #write it to taskfile
            logging.info(f"Saved data to {self.taskfile}")

    #5. Implement TaskapiImpl.editTask RPC that edits an existing task. 
    def editTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task:    #method to edit tasks
        
        logging.debug(f"editTask parameters {pformat(request)}")

        MAXLEN = 1024   #maximum description limit

        #get id and r=description given by user
        idno = request.id           
        descript = request.description
        
        if len(descript) > MAXLEN:  #if user input description exceed maximum limit, it is invalid
            msg = 'Length of `Task Description` cannot be more than 1024 characters'
            context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()

        #6. What happens if editTask is called on the same task by two clients simultaneously? Suggest a possible solution.
        with self.lock:   #need a lock to prevent data races. data race occurs when access stored values in "tasks" dictionary
            ids = self.tasks.keys() #get already stored task ids. need mutual exclusion

            if idno not in ids:     #if user given task id is not stored, it is invalid
                msg = 'id number is invalid'
                context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return task_pb2.Task()  

            self.tasks[idno] = request  #if no problems, store the new description in "tasks" dictionary for given task id

            return self.tasks[idno]     #return edited task 


    def addTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task: #method to add a new task
        
        logging.debug(f"addTask parameters {pformat(request)}")
            
        MAXLEN = 1024   #maximum description limit

        if len(request.value) > MAXLEN:     #if user input description exceed maximum limit, it is invalid
            msg = 'Length of `Task Description` cannot be more than 1024 characters'
            context.set_details(msg)    #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()

        #7. There is a subtle error in the provided implementation of addTask called a data race. How can we fix this problem?
        #9. Impose a critical section in your implementation of addTask to ensure proper mutual exclusion.
        with self.lock: #need a lock to prevent data races. data race occurs when access "tasks" dictionary and task_id variable
            t = task_pb2.Task(id=self.task_id, description=request.value)  #create a new task for added description
            print("new task  :")  #display new task
            print(t)
            self.tasks[self.task_id] = t #store the new task
            self.task_id += 1 #increment task id
   
            return t #return new task


    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> task_pb2.Task: #method to delete a task

        if request.value not in self.tasks.keys():   #if user given task id is not stored, it is invalid
            msg = 'id number is invalid'
            context.set_details(msg)        #use context to set message and code for error and then return uninitialized task object
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return task_pb2.Task()

        with self.lock:     #need a lock to prevent data races. data race occurs when access stored values in "tasks" dictionary
            logging.debug(f"delTask parameters {pformat(request)}")
            return self.tasks.pop(request.value)    #if no given id is valid, delete and send the required task


    def listTasks(self, request: empty_pb2.Empty, context) -> task_pb2.Tasks:
        
        logging.debug(f"listTasks parameters {pformat(request)}")
        with self.lock:     #need a lock to prevent data races

            return task_pb2.Tasks(pending=self.tasks.values())      #return stored tasks


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
