from django.conf.urls import include, url

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^index.html$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', RedirectView.as_view(url="/static/index.html")),
]