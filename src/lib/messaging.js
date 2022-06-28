import { app } from '$lib/firebase-config';

import { getMessaging, getToken, onMessage } from 'firebase/messaging';

// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);

async function requestPermission() {
	console.log('Requesting permission...');
	const permission = await Notification.requestPermission();
	if (permission === 'granted') {
		console.log('Notification permission granted.');
	} else {
		console.log(permission);
		console.log('Unable to get permission to notify.');
	}
}

export async function requireNotificationsPermission() {
	try {
		await requestPermission();
		const token = await getToken(messaging, {
			vapidKey:
				'BP8_D_npDOb3N4RStB3mF1WS-5VQTkjyMaHN3FUb0wBxIOHt7YDvnJhUyOf7XR3xTn9Zuk9_SSq0m96OYKwyGEo'
		});

		onMessage(messaging, async (payload) => {
			console.log('Message received. ', payload);
		});

		console.log(token);
	} catch (error) {
		console.error(error);
		console.log('Error while getting notifications permission');
	}
}
