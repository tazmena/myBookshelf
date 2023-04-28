<template>
	<div class="quiz">
		<h1 class="">Quiz</h1>
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
			console.log("Quiz",this.user_id)
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

.quiz h1, .quiz h2, .quiz p {
	color: black;
}
</style>
