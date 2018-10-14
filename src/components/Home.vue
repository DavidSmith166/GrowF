<template>
    <main role="main">
      <div class="jumbotron">
        <h1>Django - Auth0 - Vue</h1>
        <p class="lead">This demo application uses Django and Django REST Framework for backend, Vue for the frontend and Auth0 for handling user's authentication</p>
        <a class="btn btn-lg btn-primary" href="" role="button">View tutorial</a>
      </div>

    <h4 v-if="!authenticated">
      You are not logged in! Please <a class="btn btn-primary" @click="auth.login()">Log In</a> to continue.
    </h4>
    </main>
</template>    


<script>
  export default {
    name: 'home',
    props: ['auth', 'authenticated'],
 }
</script>

