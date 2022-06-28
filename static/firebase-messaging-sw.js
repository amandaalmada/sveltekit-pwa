// [START initialize_firebase_in_sw]
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
if ('undefined' === typeof window) {
	importScripts('https://www.gstatic.com/firebasejs/9.8.4/firebase-app-compat.js');
	importScripts('https://www.gstatic.com/firebasejs/9.8.4/firebase-messaging-compat.js');

	// Initialize the Firebase app in the service worker by passing in the
	// messagingSenderId.
	firebase.initializeApp({
		apiKey: 'AIzaSyAxtx_E08rgGWigQs4BrP1us_2Kijl89jw',
		authDomain: 'okymapp-e42bb.firebaseapp.com',
		databaseURL: 'https://okymapp-e42bb-default-rtdb.firebaseio.com',
		projectId: 'okymapp-e42bb',
		storageBucket: 'okymapp-e42bb.appspot.com',
		messagingSenderId: '147080091155',
		appId: '1:147080091155:web:bad9f99878aea5cc1811e6',
		measurementId: 'G-NQY4L06HWM'
	});

	// Retrieve an instance of Firebase Messaging so that it can handle background
	// messages.
	const messaging = firebase.messaging();
	// [END initialize_firebase_in_sw]

	// If you would like to customize notifications that are received in the
	// background (Web app is closed or not in browser focus) then you should
	// implement this optional method.
	// [START background_handler]
	messaging.onBackgroundMessage(function (payload) {
		console.log('[firebase-messaging-sw.js] Received background message ', payload);
		// Customize notification here
		const notificationTitle = payload.notification.title;
		const notificationOptions = {
			body: payload.notification.body
		};

		return self.registration.showNotification(notificationTitle, notificationOptions);
	});
	// [END background_handler]
}
