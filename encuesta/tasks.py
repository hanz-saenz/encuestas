from celery import shared_task

@shared_task
def suma(a, b):
    print("------------------------------------------------------")
    print("------------------ Mi primera Tarea ------------------")
    print("------------------------------------------------------")
    return a + b