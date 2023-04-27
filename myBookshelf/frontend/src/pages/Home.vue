<template>
	<div class="home">
	</div>




	<div>
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

.home h1, .home p {
	color: black;
	text-align: left;
}

.home{
	background-color: #a8c4aa;
	height: 80%;
	width: 80%;
}
</style>
