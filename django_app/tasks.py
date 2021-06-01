import datetime
from time import sleep
from celery import shared_task, Task
from django.core.mail import EmailMessage
from django_app.models import Poll
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class CallbackTask(Task):
    def on_success(self, retval, task_id, *args, **kwargs):
        channel_layer = get_channel_layer()
        if not channel_layer:
            print("Not found")
            return

        async_to_sync(channel_layer.group_send)(
            "finished_tasks",
            {
                'type': 'task_message',
                'message': f'Finished Task {task_id}.  Result is {retval}, Args is {args} Current time is {datetime.datetime.now()}'
            }
        )
        print("success")


@shared_task(name="send_email_tasks")
def send_email(emails: list):
    message_content = "Тест надсилання листів"
    msg = EmailMessage("Лабораторна робота 3", message_content, 'savosko2021@gmail.com', emails)
    msg.send()
    return "successful"


@shared_task(name="some_long_work", base=CallbackTask)
def long_work(time):
    sleep(time)
    count_entity = Poll.objects.count()
    return count_entity
