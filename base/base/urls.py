from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from core import views

# Examples:
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^admin/', admin.site.urls),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
]