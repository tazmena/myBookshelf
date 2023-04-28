<template>
	<div class="quiz">
		<h1>Quiz</h1>
		<p>This is the quiz page. Here, you can select your favourite books so that you can get better recommendations! </p>
		<p>To start off, please search using the search bar below.</p>
		<p>You can select a total of 5 books.</p>

		<div class="search">
			<input type="search" placeholder="Search here..." />
			<button class="searchbutton" type="button">Search</button>
		</div>
	</div>
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
		};
	},
	methods: {

	},

	async mounted() {
		try {
			let response = await fetch("http://localhost:8000/bookapp/user", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
		} catch (e) {
			window.location.href = "http://localhost:8000/bookapp";
		}
	},

};
</script>

<style>
body {
	background-color: #fff8ef;
}
.quiz h1, .quiz p {
	color: black;
}

.quiz{
	background-color: #a8c4aa;
	padding-top: 2em;
	padding-bottom: 17em;
	padding-left: 10em;
	padding-right: 10em;
	text-align: left;
}

.searchbutton{
	color: white;
	margin-left: 1em;
}

.search{
	padding-bottom: 1em;
}
</style>
