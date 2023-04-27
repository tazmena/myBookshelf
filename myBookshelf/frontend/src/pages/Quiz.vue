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
		};
	},
	computed: {
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
</style>
