import { initializeApp } from 'firebase/app';

// TODO: Replace the following with your app's Firebase project configuration
const firebaseConfig = {
    apiKey: "AIzaSyAxtx_E08rgGWigQs4BrP1us_2Kijl89jw",
    authDomain: "okymapp-e42bb.firebaseapp.com",
    databaseURL: "https://okymapp-e42bb-default-rtdb.firebaseio.com",
    projectId: "okymapp-e42bb",
    storageBucket: "okymapp-e42bb.appspot.com",
    messagingSenderId: "147080091155",
    appId: "1:147080091155:web:bad9f99878aea5cc1811e6",
    measurementId: "G-NQY4L06HWM"
  };

const app = initializeApp(firebaseConfig);



import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging";



// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);

// Add the public key generated from the console here.
messaging.getToken({vapidKey: BDsqeLFFoH0RxAqPrNSLQ1EFPeW8LPlpXA4Y52xVrfg81W3ZegtOQi1OcN0ayN8-_kZ1ME_3rDEJXL_puBMy6D8});

function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');
    }
  })
}