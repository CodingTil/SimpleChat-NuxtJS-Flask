<template>
    <v-card class="ma-2 card d-flex flex-column">
        <v-form v-model="valid" ref="form">
            <v-container>
                <v-col>
                    <v-container>
                        <v-text-field
                            v-model="userInfo.name"
                            :rules="nameRules"
                            :counter="maximumLength"
                            label="Name"
                            required
                            rounded
                            flat
                            background-color="primary"
                            color="tertiary"
                        ></v-text-field>
                    </v-container>

                    <v-container>
                        <v-btn
                            :disabled="!valid"
                            depressed
                            color="tertiary primary--text"
                            @click="validateAndLogin"
                            large
                            block
                        >
                        Login
                        </v-btn>
                    </v-container>
                </v-col>
            </v-container>
        </v-form>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            valid: false,
            userInfo: {
                name: ''
            },
            nameRules: [
                v => !!v || 'Name is required.',
                v => (v && v.length <= this.maximumLength) || 'Name must be less than ' + this.maximumLength + ' characters.',
            ],
        }
    },
    methods: {
        async validateAndLogin() {
            if(this.$refs.form.validate()) {
                await this.loginUser(this.userInfo)
            }
        },
        async loginUser(loginInfo) {
            try {
                await this.$auth.loginWith('local', {
                    data: {
                        name: loginInfo.name
                    }
                })
            }catch(e) {
                // TODO SNACKBAR
                console.log(e)
            }
        }
    },
    props: {
        maximumLength: {
            type: Number,
            default: 16
        }
    }
}
</script>

<style>

</style>