from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def print_message_to_terminal():
    print(f"{50 * '-'} Sending welcome email by background task... {50 * '-'}")