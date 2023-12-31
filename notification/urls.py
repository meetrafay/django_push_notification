"""
URL configuration for notification project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)


from test_app.views import *
urlpatterns = [
    path('',index,name='index'),
    path("notification/",include('test_app.urls')),
    path('firebase-messaging-sw.js', showFirebaseJS, name="show_firebase_js"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/devices/', FCMDeviceAuthorizedViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='fcmdevice-detail'),
]
