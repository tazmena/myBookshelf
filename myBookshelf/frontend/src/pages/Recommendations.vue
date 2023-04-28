<template>
	<div class="recommendation">
		<h1 class="">Recommendations</h1>
		<p>This is the recommendations page, here, we will be suggesting your future read!</p>
		<h2>Based off of quiz results:</h2>
		<p>{{ recs }}</p>
		<h2>Based off of ratings</h2>
	</div>
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
			user: null,
			user_id: 0,
			recs: []
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
			console.log("Recommendations",this.user_id)
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
			console.log("Recommendations",this.user)
		},
		async getRecommendation(){
			let response = await fetch("http://localhost:8000/bookapp/recommendations/"+this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.recs = data.recs
			console.log("Recsss",this.recs)
		}

	},

	async mounted() {
		this.fetchUserData()
		this.getRecommendation()
	},

};
</script>

<style>
body{
	background-color: #fff8ef;
}

.recommendation h1, .recommendation h2, .recommendation p {
	color: black;
}

.recommendation{
    background-color: #a8c4aa;
    padding-top: 2em;
    padding-bottom: 17em;
    padding-left: 10em;
    padding-right: 30em;
    text-align: left;
}
</style>
