from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework.views import APIView
from rest_framework import response
from rest_framework.response import Response

from test_app.utils import send_notification



# template rendering
def index(request_iter):
    return  render(request_iter,'index.html')



class NotifyApiView(APIView):
    
    def post(self,request):
        
        title = request.data.get('title')
        body = request.data.get('body')
        send_notification(title,body)
        return Response({'msg':'success'})














def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyAIwJ8vHJz8GUpGrgojhfnRwIuwDIAZuSY",' \
         '        authDomain: "notification-a313d.firebaseapp.com",' \
         '        projectId: "notification-a313d",' \
         '        storageBucket: "notification-a313d.appspot.com",' \
         '        messagingSenderId: "629665376926",' \
         '        appId: "1:629665376926:web:8254c95eba3575d535e98f",' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")