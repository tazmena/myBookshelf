<template>
	<div class="quiz">
		<h1>Quiz</h1>
        <p>This is the quiz page. Here, you can select your favourite books so that you can get better recommendations! </p>
        <p>To start off, please search using the search bar below.</p>
        <p>We recommend you select a total of 5 books.</p>

		<div>
			<div class="search">
            	<input type="search" placeholder="Search here..." v-model="searchinput" />
        	</div>
		</div>

		<div class="reset">
			<button type="button" @click="retakeQuiz">Retake</button>
		</div>
		<p>Clicking the retake quiz will reset your previous results.</p>

		<div v-if="searchinput.length">
			<div v-if="allBooks.length">
				<div v-for="(book, index) in allBooks" :key="index"> <!-- Reference for search https://www.youtube.com/watch?v=0TMy-5srdlA-->
					<div class="singlebook">
						{{ index+1 }}. {{ book.title }} <button type="button" @click="getBookId(book.title)">Add</button>
					</div>
				</div>
			</div>

			<div v-else>That book is not found, please search something else.</div>

		</div>

		<div v-else>
			<div v-if="likedBooks.length">
				<div v-for="(book, index) in likedBooks" :key="index"> <!-- Reference for search https://www.youtube.com/watch?v=0TMy-5srdlA-->
					<div class="singlebook">
						{{ index+1 }}. {{ book.title }}
					</div>
				</div>
			</div>
			<div v-else><p></p></div>

		</div>

	</div>

	
</template>

<script lang="js">
import router from "../router";

export default {
	data() {
		return {
			searchinput: '',
			user: null,
			user_id: 0,
			books: [],
			bookId: 0,
			likedBooks: []
		};
	},
	computed: {
		allBooks(){
			if (this.searchinput.trim().length > 0){
				return this.books.filter((book) => book.title.toLowerCase().includes(this.searchinput.trim().toLowerCase()))
			}
			return this.books
		}
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
			this.getQuizResults()
		},

		async getBookData(){
			let response = await fetch("http://localhost:8000/bookapp/searchbooks", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.books = data.books
			console.log(this.books)
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
			this.addBook(this.bookId)
		},

		async addBook(bookId){
			let response = await fetch("http://localhost:8000/bookapp/addBook", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "POST",
				body: JSON.stringify({user_id: this.user_id, book_id: bookId}),
			});
			let data = await response.json();
			alert("Book has been added.");
		},

		async retakeQuiz(){
			let response = await fetch("http://localhost:8000/bookapp/resetQuiz", {
				credentials: "include",
				mode: "cors",
				method: "DELETE",
				body: JSON.stringify({ user_id: this.user_id }),
			});
			let data = await response.json();
			alert("Quiz has been reset!")
		},

		async getQuizResults(){
			let response = await fetch("http://localhost:8000/bookapp/getQuizResults/"+this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.likedBooks = data.books
		},
	},

	async mounted() {
		this.fetchUserData()
		this.getBookData()
	},

};
</script>

<style>
body{
	background-color: #fff8ef;
}

.quiz h1, .quiz h2, .quiz p {
	color: black;
	margin-bottom: 1em;
}

.quiz{
    background-color: #a8c4aa;
    padding-top: 2em;
    padding-bottom: 17em;
    padding-left: 10em;
    padding-right: 10em;
    text-align: left;
	border-radius: 5em;

}

.search{
    padding-bottom: 1em;
}

.search input{
	width: 53em;
	height: 3em;
	background-color: white;
	color: #311f1c;
}

.singlebook{
	color: rgb(255, 255, 255);
	background-color: #736056;
	margin-top: 2em;
	padding: 1em;
	border-radius: 3em;
}

button {
	background-color: #311f1c;
}

</style>
