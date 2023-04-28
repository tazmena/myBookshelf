<template>
	<div class="home">
		<h1>Home</h1>
		<p>This is the home page, from here, you can track the books you'd like to read, and rate the ones you've read. </p>
		<h2>To read</h2>
		<h2>Completed</h2>
	</div>
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
			user: null,
			user_id: 0,
		};
	},
	methods: {

	},

	async mounted() {
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

};
</script>

<style>
body {
	background-color: #fff8ef;
}

.home h1, .home p, .home h2 {
	color: black;
	text-align: left;
}

.home{
	background-color: #a8c4aa;
	padding-top: 2em;
	padding-bottom: 17em;
	padding-left: 10em;
	padding-right: 10em;
	text-align: left;
}
</style>
