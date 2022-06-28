import { app } from '$lib/firebase-config';

import { getMessaging, getToken, onMessage } from 'firebase/messaging';

// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);

function showNotification(notification) {
	// Let's check if the browser supports notifications
	if (!('Notification' in window)) {
		alert('This browser does not support desktop notification');
	}

	// Let's check whether notification permissions have already been granted
	else if (Notification.permission === 'granted') {
		// If it's okay let's create a notification
		console.log(notification);
		new Notification(notification.title, {
			body: notification.body,
			tag: 'background-message',
			onclick: () => {
				// window.location.href('http://localhost:3000/contacto');
			}
			// icon: notification.image
		});
	}

	// Otherwise, we need to ask the user for permission
	else if (Notification.permission !== 'denied') {
		Notification.requestPermission().then(function (permission) {
			// If the user accepts, let's create a notification
			if (permission === 'granted') {
				new Notification(notification);
			}
		});
	} else {
		console.log('Permission is denied');
	}

	// At last, if the user has denied notifications, and you
	// want to be respectful there is no need to bother them anymore.
}

export async function requireNotificationsPermission() {
	console.log('requireNotificationsPermission');

	try {
		console.log('Requesting permission...');
		const permission = await Notification.requestPermission();

		if (permission === 'granted') {
			console.log('Notification permission granted.');
		} else {
			console.log(permission);
			console.log('Unable to get permission to notify.');
		}

		const token = await getToken(messaging, {
			vapidKey:
				'BP8_D_npDOb3N4RStB3mF1WS-5VQTkjyMaHN3FUb0wBxIOHt7YDvnJhUyOf7XR3xTn9Zuk9_SSq0m96OYKwyGEo'
		});

		console.log('token', token);

		onMessage(messaging, async (payload) => {
			console.log('Message received. ', payload.notification);
			showNotification(payload.notification);
		});
	} catch (error) {
		console.error(error);
		console.log('Error while getting notifications permission');
	}
}
