importScripts("https://www.gstatic.com/firebasejs/7.19.0/firebase-app.js");
importScripts(
    "https://www.gstatic.com/firebasejs/7.19.0/firebase-messaging.js",
);
// For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics.

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
const firebaseConfig = {

    apiKey: "AIzaSyAIwJ8vHJz8GUpGrgojhfnRwIuwDIAZuSY",
  
    authDomain: "notification-a313d.firebaseapp.com",
  
    projectId: "notification-a313d",
  
    storageBucket: "notification-a313d.appspot.com",
  
    messagingSenderId: "629665376926",
  
    appId: "1:629665376926:web:8254c95eba3575d535e98f",
  
    measurementId: "G-DB1W6CS53E"
  
  };
  
firebase.initializeApp(firebaseConfig)

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
messaging.usePublicVapidKey("BKuTAmwBTcXi6rotuJfSJklMjItJhLj6tNifXRDP_tKhUtJ4rD_c0CU1LqPkkE7-IJOnye41t-dbdG71xMmhKz4");

messaging.setBackgroundMessageHandler(function(payload) {
    console.log(
        "[firebase-messaging-sw.js] Received background message ",
        payload,
    );
    // Customize notification here
    const notificationTitle = "Notification";
    const notificationOptions = {
        body: "Please check, you have notification.",
    };

    return self.registration.showNotification(
        notificationTitle,
        notificationOptions,
    );
});