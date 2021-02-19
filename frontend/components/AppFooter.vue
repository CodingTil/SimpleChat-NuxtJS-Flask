<template>
    <v-footer padless>
        <v-card
        flat
        tile
        width="100%"
        color="secondary"
        class="text-center"
        >
            <v-card-text class="primary--text">
                <v-btn
                    plain
                    href='https://github.com/CodingTil'
                    target="_blank"
                    color="tertiary"
                >
                    <v-icon>
                        mdi-github
                    </v-icon>
                </v-btn>
                {{ new Date().getFullYear() }} — <strong>CodingTil</strong>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
export default {

}
</script>

<style>

</style>