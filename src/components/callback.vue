<template>
  <div class="spinner">
    <img src="../assets/loading.svg" alt="loading..."/>
  </div>
</template>

<script>
  export default {
    name: 'callback',
    props: ['auth'],
    data () {
      this.auth.handleAuthentication()
      return {}
    }
  }
</script>


//Just like you did in the previous part you need to change your callback URL in Auth0 dashboard to point to http://localhost:8000/callback

