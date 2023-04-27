<template>
  <div>
    <button type="button" @click="logOutUser">Logout</button>
    {{ user_id }}
  </div>
</template>

<script lang="js">
export default {
  data() {
    return {
      user: null,
      user_id: null,
    }
  },
  methods: {
    async logOutUser(){
      let response = await fetch("http://localhost:8000/bookapp/logout/" + this.user_id ,
      {
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        method: "GET"
      });
      console.log(this.user_id)
    },
  }
}
</script>

