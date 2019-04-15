from django.core.mail import send_mail
from olx_site.celery import app
from celery import shared_task


@shared_task
def send_to_customer(customer_mail):
    send_mail('test', 'test message', 'contactme@dark46.ru', [customer_mail], fail_silently=False)

@shared_task
def grab_olx(customer_url):
    pass

@shared_task
def make_graph(raw_data):
    pass