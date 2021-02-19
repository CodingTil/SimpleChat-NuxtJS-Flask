<template>
  <v-card class="ma-2 card d-flex flex-column">
    <!-- Card Title -->
    <v-card-title>
      {{ this.$auth.user }}
    </v-card-title>

    <v-divider></v-divider>

    <!-- Messages -->
    <v-list id="messageList" class="overflow-y-auto mt-auto">
      <v-list-item v-for="msg in messages" :key="msg.id">
        <Message :message="msg" :isSender="isSender(msg)" />
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <!-- Send Messages -->
    <v-form v-model="valid" ref="form">
      <v-container>
        <v-row justify="center">
          <v-col :cols="10">
            <v-text-field
              v-model="message"
              :rules="messageRules"
              :counter="maximumLength"
              required
              rounded
              flat
              background-color="primary"
              color="tertiary"
              @keyup.enter="validateAndSend"
            />
          </v-col>
          <v-col :cols="1">
            <v-btn
              :disabled="!valid"
              color="tertiary"
              @click="validateAndSend"
              icon
              large
              fab
            >
              <v-icon>mdi-message</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>


<script>
import Message from "../components/Message"
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      valid: false,
      message: '',
      messageRules: [
        v => !!v,
        v => (v && v.length <= this.maximumLength) || 'Message must be less than ' + this.maximumLength + ' characters.'
      ]
    }
  },
  components: {
    Message
  },
  methods: {
    async validateAndSend() {
      if(this.$refs.form.validate()) {
        await this.$axios.post('/api/message', {
          message: this.message
        }).then(result => {
              if(result.status === 200) {
                // Reset Input Field
                this.message = ''
                // Set the new messages
                this.$store.commit("messages/addMessage", result.data)
                // Scroll list to bottom
                var objDiv = document.getElementById("messageList");
                objDiv.scrollTop = objDiv.scrollHeight;
              }else {
                this.$auth.logout()
              }
          })
          .catch(error => {
              this.$auth.logout()
          })
      }
    },
    isSender(msg) {
      return msg.sender.localeCompare(this.$auth.user) === 0
    }
  },
  props: {
    maximumLength: {
      type: Number,
      default: 1024
    }
  },
  mounted: function () {
    var fetch_loop
    var fetch = function(obj) {
      obj.$axios.get('/api/message')
          .then(result => {
              if(result.status === 200) {
                obj.$store.commit("messages/setMessages", result.data)
                console.log(result)
              }else {
                window.clearInterval(fetch_loop)
                obj.$auth.logout()
              }
          })
          .catch(error => {
              window.clearInterval(fetch_loop)
              obj.$auth.logout()
          })
    }
    // Fetch new messages
    fetch(this)

    // Scroll list to bottom
    var objDiv = document.getElementById("messageList");
    objDiv.scrollTop = objDiv.scrollHeight;

    // Fetch new messages loop
    fetch_loop = window.setInterval(() => {
      if(!this.$auth.loggedIn) {
        window.clearInterval(fetch_loop)
      }else {
        fetch(this)
      }
    }, 10 * 1000)
  },
  computed: {
    messages() {
      return this.$store.state.messages.messages
    }
  }
}
</script>

<style>
</style>