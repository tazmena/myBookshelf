<script>
import NavbarLink from "../navbar/NavbarLink.vue";
import { collapsed, toggleNavbar, navbarWidth } from "./state";

export default {
    props: {
    },
    components: { NavbarLink },
    setup() {
        return {collapsed, toggleNavbar, navbarWidth}
    },
    mounted() {
    this.fetchUserData()
    },
    data() {
		return {
            user: null,
			user_id: null,
		};
	},
    methods: {
        async fetchUserData(){
        let response = await fetch("http://localhost:8000/bookapp/user",
        {
            credentials: "include",
            mode: "cors",
            referrerPolicy: "no-referrer",
            method: "GET"
        });
        let data = await response.json()
        this.user = data.user
        this.user_id = data.user_id
        console.log(this.user_id)
        },

        async logUserOut(){
            let response = await fetch("http://localhost:8000/bookapp/logout/" + this.user_id,
            {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                method: "GET"
            });
            document.location.href = "http://localhost:8000/bookapp"; //reference for logout: https://stackoverflow.com/questions/66688275/can-i-have-django-urls-and-vue-routes-in-the-same-project
        }

    },
}
</script>

<template>

    <div class="navbar" :style="{ width : navbarWidth}">
        <h1 class="title">
			<span v-if="collapsed">
				<div></div>
			</span>
			<span v-else>myBookshelf</span>
		</h1>


        <NavbarLink to="/" icon="fas fa-solid fa-house">Home</NavbarLink>
		<NavbarLink to="/recommendations" icon="fas fa-solid fa-book-open">Recommendations</NavbarLink>
		<NavbarLink to="/search" icon="fas fa-solid fa-magnifying-glass">Search</NavbarLink>
        <NavbarLink to="/quiz" icon="fas fa-solid fa-clipboard-question">Quiz</NavbarLink>
        <button id="logout" type="button" @click="logUserOut">
            <span v-if="collapsed">
                <div>LG</div>
            </span>
            <span v-else>Logout</span>
        </button>


        <span class="collapse-icon" :class="{ 'rotate-180': collapsed }" @click="toggleNavbar">
            <i class="fas fa-angle-double-left" />
        </span>
    </div>
</template>

<style>
:root {
	--navbar-bg-color: #736056;
	--navbar-item-hover: #311f1c;
	--navbar-item-active: #a8c4aa;
}
</style>

<style scoped>
    .navbar {
        color: rgb(255, 255, 255);
        background-color: var(--navbar-bg-color);

        float: left;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        bottom: 0;
        padding: 7.5em 0.5em;

        transition: 0.3s ease;

        display: flex;
        flex-direction: column;

    }

    .navbar h1 {
        height: 1em;
        padding-bottom: 1.5em;
        margin-top: -2.5em;
        font-size: 25pt;
    }

    .collapse-icon {
	position: absolute;
	bottom: 0;
	padding: 0.75em;

	color: rgba(255, 255, 255, 0.7);

	transition: 0.2s linear;
    }


    #logout {
        background-color: white;
        color: #311f1c;
        margin-top: 20em;
    }

    .rotate-180 {
	transform: rotate(180deg);
	transition: 0.2s linear;
    }
</style>