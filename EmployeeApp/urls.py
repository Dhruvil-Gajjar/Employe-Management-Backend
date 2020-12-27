from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.conf.urls.static import static

from . import views


router = routers.DefaultRouter()


urlpatterns = [
    # REST framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Department
    url(r'^department/$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    # Employee
    url(r'^employee/$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),

    # Save Image
    url(r'^SaveFile$', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
