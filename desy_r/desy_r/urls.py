"""desy_r URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from reports import views, api
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'students', api.StudentViewSet)
router.register(r'instructors', api.InstructorViewSet)
router.register(r'drives', api.DriveViewSet)
router.register(r'objective', api.ObjectiveViewSet)
router.register(r'courses', api.CourseViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^classes/all', views.all_classes),
    url(r'^classes/current', views.current_classes),
    url(r'^drives/$', views.display),
    url(r'^drive/create/$', views.create_drive),
    url(r'^drive/detail/(?P<pk>.*)/$', views.drive_detail),
    url(r'^drive/update/(?P<pk>.*)/$', views.update_drive),
    url(r'^drive/delete/(?P<pk>.*)/$', views.delete_drive),
    url(r'^forms/form/$', views.form),
    url(r'^forms/form_advanced/$', views.form_advanced),
    url(r'^forms/form_validation/$', views.form_validation),
    url(r'^forms/form_wizard/$', views.form_wizard),
    url(r'^forms/form_upload/$', views.form_upload),
    url(r'^forms/form_buttons/$', views.form_buttons),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^students/all/', views.all_students),
    url(r'^students/current', views.current_students),
    url(r'^students/(?P<pk>\d*)/', views.student_detail),
    url(r'^calendar/', views.calendar_page),
    #url(r'^students/(?P<pk>.*)/$'),
]
