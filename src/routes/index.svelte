<script>
	import { initializeApp } from "firebase/app"


// Add Firebase products that you want to use
import { getMessaging, getToken} from "firebase/messaging"
import { onMount } from "svelte";
import { goto } from '$app/navigation'
const firebaseConfig =  {
  apiKey: "AIzaSyAxtx_E08rgGWigQs4BrP1us_2Kijl89jw",
  authDomain: "okymapp-e42bb.firebaseapp.com",
  databaseURL: "https://okymapp-e42bb-default-rtdb.firebaseio.com",
  projectId: "okymapp-e42bb",
  storageBucket: "okymapp-e42bb.appspot.com",
  messagingSenderId: "147080091155",
  appId: "1:147080091155:web:bad9f99878aea5cc1811e6",
  measurementId: "G-NQY4L06HWM"
};





function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
		localStorage.setItem('permission', permission)
      console.log('Notification permission granted.');
	  goto("/mapa")
    } else{
		localStorage.removeItem('permission')
	}

  })
}
function subscribeUser(token){

	console.log("subscribiendo al usuario",token)
}

let app
let messaging
onMount(() => {
	 app = initializeApp (firebaseConfig)
	messaging = getMessaging (app)
	const permission = localStorage.getItem('permission')
	if (permission){
		goto("/mapa")
	}
})
</script>

<button on:click="{async () => {
	requestPermission()
	const token = await getToken(messaging,{vapidKey: "BDsqeLFFoH0RxAqPrNSLQ1EFPeW8LPlpXA4Y52xVrfg81W3ZegtOQi1OcN0ayN8-_kZ1ME_3rDEJXL_puBMy6D8"});
	subscribeUser(token)
}}">Subscribite</button>