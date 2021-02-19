<template>
    <v-container>
        <v-card
            elevation="3"
            outlined
            max-width="60%"
            :class="isSender ? 'align-left' : 'align-right'"
            :color="isSender ? 'tertiary primary--text' : 'primary secondary--text'"
        >
            <v-card-title class="headline">
                {{ message.sender }}
            </v-card-title>
            <v-card-subtitle :class="isSender ? 'primary--text' : 'black--text'">
                {{ message.message }}
            </v-card-subtitle>
        </v-card>
    </v-container>
</template>

<script>
export default {
    props: ["message", "isSender"]
}
</script>

<style>
.align-right {
    float: right;
}

.align-left {
    float: left;
}
</style>