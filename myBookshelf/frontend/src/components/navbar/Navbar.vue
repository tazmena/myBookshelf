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
		<NavbarLink to="/profile" icon="fas fa-solid fa-circle-user">Profile</NavbarLink>
        <NavbarLink to="/quiz" icon="fas fa-solid fa-clipboard-question">Quiz</NavbarLink>

        <span class="collapse-icon" :class="{ 'rotate-180': collapsed }" @click="toggleNavbar">
            <i class="fas fa-angle-double-left" />
        </span>
    </div>
</template>

<style>
:root {
	--navbar-bg-color: #c59fc9;
	--navbar-item-hover: #c1e0f7;
	--navbar-item-active: #cfbae1;
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

    .rotate-180 {
	transform: rotate(180deg);
	transition: 0.2s linear;
    }
</style>