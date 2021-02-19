export const state = () => ({
    messages: []
})

export const mutations = {
    clearMessages(state) {
        state.messages = []
    },
    setMessages(state, messages) {
        state.messages = messages
    },
    addMessage(state, message) {
        state.messages.push(message)
    }
}

export const getters = {
    messages(state) {
        return state.messages
    }
}