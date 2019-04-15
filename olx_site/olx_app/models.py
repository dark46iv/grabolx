from django.db import models
from django.forms import ModelForm
from django.db.models import signals
from olx_app.tasks import send_to_customer

# Create your models here.


class RequestAnalysis(models.Model):

    parsing_url = models.CharField(max_length=256)
    email = models.EmailField()


class RequestAnalysisForm(ModelForm):

    class Meta:
        model = RequestAnalysis
        fields = ['parsing_url', 'email']


def customer_give_order(sender, instance, signal, *args, **kwargs):
    send_to_customer.delay('test@yandex.ru')


signals.post_save.connect(customer_give_order)
