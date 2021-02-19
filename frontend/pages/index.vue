<template>
  <div>
    <div v-if="$auth.loggedIn">
      <ChatRoom />
    </div>
    <div v-else>
      <LoginForm />
    </div>
  </div>
</template>

<script>
import ChatRoom from "../components/ChatRoom";
import LoginForm from "../components/LoginForm";

export default {
  components: {
    ChatRoom,
    LoginForm
  },

  head() {
    return {
      title: "SimpleChatApp",
      meta: [
        {
          hid: "description",
          name: "description",
          content: "A very simplistic Chat App"
        }
      ]
    }
  }
}
</script>

<style>

</style>
