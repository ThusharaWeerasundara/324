import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2, task_pb2_grpc


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

    def __init__(self):     #constructor
        # TODO: initialise attributes to store our tasks.
        self.tasks = task_pb2.Tasks() #initialize tasks attribute
        pass

    def addTask(self, request, context):    #method to add a task
        logging.info(f"adding task {request.description}")
        # TODO: implement this!

        length = len(self.tasks.tasks)      #get length of tasks. assume task id is the index of the place where it is going to added
        print("Added taskID: ", length,)    
        task = task_pb2.Task(id = length, description = request.description)  #get corresponding task by passing correct parameters
        self.tasks.tasks.append(task)  #add above task

        return task_pb2.Id(id = task.id)    #return added task ID
        

    def delTask(self, request, context):    #method to delete a task
        logging.info(f"deleting task {request.id}")
        # TODO: implement this!
        
        noOfTasks = len(self.tasks.tasks)   #get total number of tasks

        for i in range(noOfTasks):  #iterate through all tasks till find a match

            if(self.tasks.tasks[i].id == request.id):   #if found a match, remove and return it

                print("Removed taskID: ", self.tasks.tasks[i].id)
                deleted = self.tasks.tasks.pop(i)                
                return task_pb2.Task(id = deleted.id, description = deleted.description)
                
        print("Task not found!!")   #if no matches print this
        return
        

    def listTasks(self, request, context):      #methid to return a list of tasks
        logging.info("returning task list")
        # TODO: implement this!
        return self.tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with ThreadPoolExecutor(max_workers=1) as pool:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
