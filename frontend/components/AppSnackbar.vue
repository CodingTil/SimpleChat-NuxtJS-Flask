<template>
  <div class="text-center">
    <v-snackbar
      v-for="(snackbar, index) in snackbars.filter(s => s.showing)"
	  :key="index"
      v-model="snackbar.showing"
      :timeout="snackbar.timeout"
      :color="snackbar.color"
      :style="`bottom: ${(index * 60) + 8}px`"
    >
      {{snackbar.text}}
	  <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="snackbar.showing = false"
        >
          Close
        </v-btn>
      </template>
	</v-snackbar>
  </div>
</template>

<script>
  import { mapState } from 'vuex';
  export default {
    computed: {
      ...mapState({
        snackbars: state => state.snackbar.snackbars
      })
    },
  }
</script>

<style>

</style>