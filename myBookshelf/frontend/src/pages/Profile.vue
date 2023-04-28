<template>
	<div class="profile">
		<h1 class="">Profile</h1>
		<h2>Edit your profile</h2>
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
			console.log("Profile",this.user_id)
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

.profile h1, .profile h2, .profile p {
	color: black;
}

.profile{
    background-color: #a8c4aa;
    padding-top: 4em;
    padding-bottom: 25em;
    padding-left: 10em;
    padding-right: 40em;
    text-align: left;
}
</style>
