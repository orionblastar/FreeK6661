from django.conf.urls import include, url

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
url(r'^$', RedirectView.as_view(url="/static/index.html")),
]