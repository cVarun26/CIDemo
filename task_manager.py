class TaskManager:
    def __init__(self):
        self.tasks={}
    
    def add_task(self, task_id, task_name):
         if task_id in self.tasks:
             raise ValueError("Task already exists")
         self.tasks[task_id] = {"name":task_name,"completed":False}

    def get_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found")
        return self.tasks[task_id]
    
    def mark_completed(self, task_id): #function
        if task_id not in self.tasks:
            raise KeyError("Task not found")
        self.tasks[task_id]["completed"]=True
        return self.tasks[task_id]
