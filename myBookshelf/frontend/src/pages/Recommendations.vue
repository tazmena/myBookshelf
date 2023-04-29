<template>
	<div class="recommendation">
		<h1 class="">Recommendations</h1>
		<p>This is the recommendations page, here, we will be suggesting your future read!</p>
		<h2>Based off of quiz results:</h2>
		<div class="recommendations">
			<div v-if="recs.length">
				<div v-for="(recommendation, index) in recs" :key="index"> <!-- Reference for search https://www.youtube.com/watch?v=0TMy-5srdlA-->
					<div class="singleRec">
							<p>{{ index+1 }}. {{ recommendation.title }}</p>
							<p>Author: {{ recommendation.author }}</p>
							<p>Rating: {{ recommendation.rating }}/5</p>
							<p>Genres: {{ recommendation.genres }}</p>
					</div>
				</div>
			</div>

			<div v-else>There are no recommendations yet, please take the quiz!</div>
		</div>
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
			this.getRecommendation()
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
			this.recs = data.allrecs
			console.log("Recsss",this.recs)
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

.singleRec{
	color: rgb(255, 255, 255);
	background-color: #736056;
	margin-top: 2em;
	padding: 1em;
	border-radius: 3em;}

.singleRec p{
	color: white;
}
</style>
