from celery import task


global_value = 0
@task
def add(x):
    return global_value+x