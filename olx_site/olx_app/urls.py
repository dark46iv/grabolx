from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import olx_app.views
from olx_app.views import RequestAnalysisPage

urlpatterns = [
    path('', RequestAnalysisPage.as_view(), name='index'),
    ]