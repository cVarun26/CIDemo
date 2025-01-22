import unittest
from task_manager import TaskManager
import time

class TestTaskManager(unittest.TestCase):

    def setUp(self):
    
        self.manager = TaskManager()

    #Unit tests

    def test_add_task(self):
      
        self.manager.add_task(1, "Test Task")
        task = self.manager.get_task(1)
        self.assertEqual(task["name"], "Test Task")
        self.assertFalse(task["completed"])

    def test_add_task_duplicate(self):
        
        self.manager.add_task(1, "Test Task")
        with self.assertRaises(ValueError):
            self.manager.add_task(1, "Another Task")

    def test_mark_completed(self):
       
        self.manager.add_task(1, "Test Task")
        self.manager.mark_completed(1)
        task = self.manager.get_task(1)
        self.assertTrue(task["completed"])

    def test_get_task_not_found(self):
      
        with self.assertRaises(KeyError):
            self.manager.get_task(999)

    # Integration Test
    def test_add_and_complete_task_integration(self):
      
        
        self.manager.add_task(1, "Test Task")
        task = self.manager.get_task(1)
        self.assertEqual(task["name"], "Test Task")
        self.assertFalse(task["completed"])

       
        self.manager.mark_completed(1)
        task = self.manager.get_task(1)
        self.assertTrue(task["completed"])

     # Performance Test
    def test_large_number_of_tasks(self):
        start_time = time.time()
        for i in range(1000):
            self.manager.add_task(i, f"Task {i}")
        end_time = time.time()
        print(f"Time taken to add 1000 tasks: {end_time - start_time}s")
        self.assertEqual(len(self.manager.tasks), 1000)

if __name__ == '__main__':
    unittest.main()
