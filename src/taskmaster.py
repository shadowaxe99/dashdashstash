import time


def execute_task(task):
    print('Executing task:', task)
    # Code to execute the task
    time.sleep(5)
    print('Task execution completed.')


if __name__ == '__main__':
    task = 'Task 1'
    execute_task(task)