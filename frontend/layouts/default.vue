<template>
  <v-app>
    <AppHeader />
    <v-main>
      <v-container fluid fill-height>
        <Nuxt />
      </v-container>
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script>
import AppHeader from "../components/AppHeader";
import AppFooter from "../components/AppFooter";

export default {
  components: {
    AppHeader,
    AppFooter
  }  
}
</script>

<style lang="scss">
.card {
  position: absolute !important;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>
