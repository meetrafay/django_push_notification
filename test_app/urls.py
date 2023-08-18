from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from django.urls import path

from test_app.views import NotifyApiView

urlpatterns = [
    # Only allow creation of devices by authenticated users
    path('devices', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('notify_api/', NotifyApiView.as_view(), name='NotifyApiView'),
    # ...
]