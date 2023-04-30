<template>
	<div class="home">
		<h1 class="">Home</h1>
		<p>This is the home page. Here, you can keep track of books you want to read, and rate books you've read.</p>
		<h2>To read</h2>
		<div v-if="toread.length">
				<div v-for="(book, index) in toread" :key="index"> <!-- Reference for search https://www.youtube.com/watch?v=0TMy-5srdlA-->
					<div class="singlebook">
						{{ index+1 }}. {{ book.title }} <button type="button" @click="getBookId2(book.title)"><i class="fa-solid fa-check"></i></button>
					</div>
				</div>
			</div>

		<div v-else>There are no books saved. Start adding books from the search page.</div>

		<h2>Completed</h2>
		<div v-if="completed.length">
				<div v-for="(book, index) in completed" :key="index"> <!-- Reference for search https://www.youtube.com/watch?v=0TMy-5srdlA-->
					<div class="singlebookcompleted">
						{{ index+1 }}. {{ book.title }}
					</div>
				</div>
			</div>

		<div v-else>There are no books saved. Click the tick from your added books above.</div>
	</div>
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
			user: null,
			user_id: 0,
			toread: [],
			toreadbooks: [],
			completed: [],
			bookId: 0,
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
			this.getToRead()
			this.getCompleted()
		},

		async getToRead(){
			let response = await fetch("http://localhost:8000/bookapp/getToRead/"+this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.toread = data.userbooks
			console.log("book objects",this.toread)
		},

		async getCompleted(){
			let response = await fetch("http://localhost:8000/bookapp/getCompleted/"+this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.completed = data.userbooks
			console.log("book objects",this.completed)
		},

		async getBookId(bookTitle){
			let response = await fetch("http://localhost:8000/bookapp/getBookId/"+bookTitle, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.bookId = data.bookId
			this.addBookToRead(this.bookId)
		},

		async getBookId2(bookTitle){
			let response = await fetch("http://localhost:8000/bookapp/getBookId/"+bookTitle, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.bookId = data.bookId
			alert("Please refresh the page.")
			this.moveToComplete(this.bookId)
		},

		async moveToComplete(bookId){
			let response = await fetch("http://localhost:8000/bookapp/moveToComplete/"+this.user_id+"/"+bookId, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
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

.home{
    background-color: #a8c4aa;
    padding-top: 2em;
    padding-bottom: 17em;
    padding-left: 10em;
    padding-right: 10em;
    text-align: left;
}

.singlebook, .singlebookcompleted{
	color: rgb(255, 255, 255);
	background-color: #736056;
	margin-top: 2em;
	padding: 1em;
	border-radius: 3em;
}
</style>
