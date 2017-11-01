<template lang="pug">
  #login Connexion
    .login-form
      input.txtUsername(v-model="formModel.email" placeholder="email" type="text")
      input.txtPassword(v-model="formModel.password" placeholder="password" type="password")
      div {{formModel}}
</template>

<script>
import AuthService from '../services/AuthService'

export default {
  data () {
    return {
      formModel: { 'email': '', 'password': '' }
    }
  },
  methods: {
    signin: function () {
      // TODO : form validation directly in HTML
      console.log(this.formModel)
      AuthService.login(this.formModel, (res) => {
        if (res.err) {
          // TODO : popup of failed login
          console.log(res.err)
        } else {
          // TODO : redirect to the right route, home or magazine by default
          // TODO : popup of success login
          this.$route.push('/home')
        }
      })
    }
  },
  mounted: function () {
    console.log('debug mounted Login')
  }
}
</script>

<style>
  #login {
    width:100%;
    min-height:90vh;
  }
</style>
