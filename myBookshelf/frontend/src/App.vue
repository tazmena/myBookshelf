<template>
  <Navbar />
  <div :style="{ 'margin-left': navbarWidth }" :user=user :user_id=user_id> 
    <router-view />
  </div>
</template>


<script lang="js">
import Navbar from './components/navbar/Navbar.vue';
import { navbarWidth } from './components/navbar/state';
export default {
  components: { Navbar },
  setup() {
    return { navbarWidth }
  },
  created() {
    this.fetchUserData()
  },
  data() {
    return {
      user: null,
      user_id: null,
    }
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
    }
  }
}
</script>


