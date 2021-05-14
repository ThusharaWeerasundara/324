import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2, task_pb2_grpc


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

    def __init__(self):
        # TODO: initialise attributes to store our tasks.
        self.tasklist = task_pb2.Tasks()
        pass

    def addTask(self, request, context):
        logging.info(f"adding task {request.description}")

        length = len(self.tasklist.tasks)
        task = task_pb2.Task(id = length, description = request.description)
        self.tasklist.tasks.append(task)
        return length
        # TODO: implement this!

    def delTask(self, request, context):
        logging.info(f"deleting task {request.id}")
        # TODO: implement this!


        noOfTasks = len(self.tasklist.tasks)   #get total number of tasks

        for i in range(noOfTasks):  #iterate through all tasks till find a match

            if(self.tasklist.tasks[i].id == request.id):   #if found a match, remove and return it

                print("Removed taskID: ", self.tasks.tasks[i].id)
                return self.tasklist.tasks.pop(i)                
               
                
        print("Task not found!!")   #if no matches print this
        return

    def listTasks(self, request, context):
        logging.info("returning task list")
        # TODO: implement this!
        return self.tasklist


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
