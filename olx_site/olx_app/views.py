from django.shortcuts import render
from olx_app.models import RequestAnalysisForm
from django.views.generic import View
from django.db.models import signals
from olx_app.tasks import send_to_customer

# Create your views here.


class RequestAnalysisPage(View):

    def dispatch(self, request, *args, **kwargs):

        if request.method == "POST":

            request_analysis = RequestAnalysisForm(request.POST)

            if request_analysis.is_valid():
                request_analysis.save()
            send_to_customer.delay('test@yandex.ru')
            return render(request, 'index.html', {'formset': request_analysis})

        else:

            request_analysis = RequestAnalysisForm()

            return render(request, 'index.html', {'formset': request_analysis})

