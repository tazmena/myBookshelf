<template>
	<div class="home">
		<h1 class="">Home</h1>
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
			console.log("Home",this.user_id)
		}

	},

	async mounted() {
		this.fetchUserData()
	},

};
</script>

<style>
body{
	background-color: #fff8ef;
}

.home h1, .home h2, .home p {
	color: black;
}
</style>
