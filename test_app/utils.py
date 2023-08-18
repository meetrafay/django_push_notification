from fcm_django.models import FCMDevice
from .models import Notification
from firebase_admin.messaging import Message, Notification as notify

def send_notification(title, body):
    devices = FCMDevice.objects.all()  # Get all devices or filter based on your needs
    
    notification = Notification.objects.create(title=title, body=body)
    
    # Create a message with notification data
    message = Message(
        notification=notify(title=title, body=body),
        data={
            'title': title,
            'body': body,
            # 'custom_key': 'custom_value',  # Add any additional custom data
        }
    )
    
    # Send the message to devices
    a = devices.send_message(message)
    print(a)
