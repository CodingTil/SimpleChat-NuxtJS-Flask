<template>
  <v-app-bar app dense color="tertiary">
    <v-btn text color="primary" to="/">SimpleChat</v-btn>
    <v-spacer />

    <v-btn text color="info" v-if="$auth.loggedIn" @click="logout">
      Logout
    </v-btn>
    <v-btn text color="primary" to="/about">About</v-btn>
  </v-app-bar>
</template>

<script>
export default {
    methods: {
      logout() {
        this.$auth.logout()
        this.$store.dispatch('snackbar/setSnackbar', {color: 'info', text: "Logged out"})
      }
    }
}
</script>

<style>

</style>