from celery import shared_task

@shared_task
def task1():
    print("Task1 django codebase")
    return

@shared_task
def task2():
    print("Task2 django codebase")
    return
