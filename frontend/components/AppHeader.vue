<template>
  <v-app-bar app dense color="tertiary">
    <v-btn text color="primary" to="/">SimpleChat</v-btn>
    <v-spacer />

    <v-btn text color="info" v-if="$auth.loggedIn" @click="$auth.logout()">
      Logout
    </v-btn>
    <v-btn text color="primary" to="/about">About</v-btn>
  </v-app-bar>
</template>

<script>
export default {
    name: "AppHeader",
}
</script>

<style>

</style>