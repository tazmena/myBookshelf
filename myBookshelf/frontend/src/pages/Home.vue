<template>
	<div class="home">
		<h1 class="">Home</h1>
		<p>This is the home page. Here, you can keep track of books you want to read, and rate books you've read.</p>
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
			this.getUserObj()
		},
		async getUserObj(){
			let response = await fetch("http://localhost:8000/bookapp/user/"+this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.user = data.user
			console.log("Home",this.user)
		},

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

.home{
    background-color: #a8c4aa;
    padding-top: 2em;
    padding-bottom: 17em;
    padding-left: 10em;
    padding-right: 10em;
    text-align: left;
}
</style>
