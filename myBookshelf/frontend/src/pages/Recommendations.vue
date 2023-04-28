<template>
	<div class="recommendations">
		<h1>Recommendations</h1>
		<p>Get your book recommendations here!</p>
		<h2>Based off your quiz results:</h2>
		<h2>Based off your ratings</h2>
		{{ recs }}
	</div>


	<div>
	</div>
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
			recs: [],
			user: null,
			user_id: 0
		};
	},
	computed: {
	},
	methods: {
		async fetchUserData(){
			let response = await fetch("http://localhost:8000/bookapp/user", {
			credentials: "include",
			mode: "cors",
			referrerPolicy: "no-referrer",
			method: "GET",
		});
		let data = await response.json();
		this.user = data.user 
		this.user_id = data.user_id
		},

		async recommendToUser(){
			let response = await fetch("http://localhost:8000/bookapp/recommend/" + this.user_id, {
			credentials: "include",
			mode: "cors",
			referrerPolicy: "no-referrer",
			method: "GET",
		});
		let data = await response.json()
		this.recs = data.recs
		console.log(this.recs)
		}

	},

	async mounted() {
		this.fetchUserData()
		this.recommendToUser()
	},

};
</script>

<style>
body {
	background-color: #fff8ef;
}
.recommendations h1, .recommendations p, .recommendations h2 {
	color: black;
}

.recommendations{
	background-color: #a8c4aa;
	padding-top: 2em;
	padding-bottom: 17em;
	padding-left: 10em;
	padding-right: 10em;
	text-align: left;
}


</style>
