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
						<div class="rate">
							<input type="radio" id="star5" :name="book.title"  @click="this.saveRating(5, index)"/>
							<label for="star5" title="text">5 stars</label>
							<input type="radio" id="star4" :name="book.title"  @click="this.saveRating(4, index)"/>
							<label for="star4" title="text">4 stars</label>
							<input type="radio" id="star3" :name="book.title"  @click="this.saveRating(3, index)"/>
							<label for="star3" title="text">3 stars</label>
							<input type="radio" id="star2" :name="book.title"  @click="this.saveRating(2, index)"/>
							<label for="star2" title="text">2 stars</label>
							<input type="radio" id="star1" :name="book.title"  @click="this.saveRating(1, index)"/>
							<label for="star1" title="text">1 star</label>
						</div>
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
			currentBook: '',
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
			let response = await fetch("http://localhost:8000/bookapp/moveToComplete", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "PUT",
				body: JSON.stringify({ user_id: this.user_id, book_id: bookId}),
			});
			let data = await response.json();
		},

		async saveRating(value, bookIndex){
			console.log("Rating changed")
			console.log(this.completed[bookIndex].title)
            //let valueOfrate = document.querySelector('input[name="index"]:checked').value; //Reference: https://stackoverflow.com/questions/9618504/how-to-get-the-selected-radio-button-s-value
			let response = await fetch("http://localhost:8000/bookapp/saveRating", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "POST",
				body: JSON.stringify({ user_id: this.user_id, bookTitle: this.completed[bookIndex].title, ratingVal: value}),
			});
			let data = await response.json();
			alert("Rating has been saved.")
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
	margin-bottom: 1em;
}

.home{
    background-color: #a8c4aa;
    padding-top: 2em;
    padding-bottom: 17em;
    padding-left: 10em;
    padding-right: 10em;
    text-align: left;
	border-radius: 5em;
}

.singlebook, .singlebookcompleted{
	color: rgb(255, 255, 255);
	background-color: #736056;
	margin-top: 2em;
	padding: 1em;
	border-radius: 3em;
}

*{
    margin: 0;
    padding: 0;
}
.rate {
    float: right;
    height: 46px;
    padding: 0 10px;
}
.rate:not(:checked) > input {
    position:absolute;
    top:-9999px;
}
.rate:not(:checked) > label {
    float:right;
    width:1em;
    overflow:hidden;
    white-space:nowrap;
    cursor:pointer;
    font-size:30px;
    color:#ccc;
}
.rate:not(:checked) > label:before {
    content: '★ ';
}
.rate > input:checked ~ label {
    color: #ffc700;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
    color: #deb217;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
    color: #c59b08;
}
</style>
