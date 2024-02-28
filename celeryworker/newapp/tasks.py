from celery import shared_task

@shared_task
def task1():
    print("Task1 standalone")
    return

@shared_task
def task2():
    print("Task2 standalone")
    return