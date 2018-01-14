<template lang="pug">
  #login
    .login-form
      h2.title Connexion
      .flex-item
        mu-text-field.email(v-model="formModel.email" label="Email" type="text")
        i.material-icons(v-if="resError") error
      .flex-item
        mu-text-field.password(v-model="formModel.password" label="Password" type="password")
        i.material-icons(v-if="resError") error
      .flex-item
          mu-checkbox.remember(v-model="formModel.isRemember" label="Se souvenir de moi")
          span
            router-link.recover(to="/recover") Mot de passe oublié ?
      mu-raised-button.submit(secondary v-on:click="signin") Se connecter
      p
        span Pas encore inscrit ?
        router-link.signup(to="/signup") Cliquer ici.
</template>

<script>
// import AuthService from '../services/AuthService'
import axios from 'axios'

export default {
  data () {
    return {
      formModel: { 'email': '', 'password': '', 'isRemember': false },
      resError: false
    }
  },
  methods: {
    signin: function () {
      // TODO : form validation directly in HTML
      // TODO : loading animation
       // Find a better way to do that
      let that = this

      // TODO : use service (or utils) to globalize all validations in app
      axios.post('http://localhost:5000/login', this.formModel)
      .then(res => {
        // TODO : popup succes
        localStorage.setItem('user', res)
        that.$store.commit('toggleAuth')
        that.$router.push('/magazine')
      })
      .catch(e => {
        // TODO : popup of failed login, refresh form, handle status code
        this.resError = true
        console.log(e.response)
      })
    }
  },
  mounted: function () {
    // TODO : do better Auth Guard ?
    // TODO :
    if (localStorage.getItem('user')) {
      this.$router.push('/home')
    }
  }
}
</script>

<style lang="stylus">
  #login
    display grid
    grid-template-columns minmax(300px, 400px)
    grid-template-rows minmax(60vh, 75vh)
    justify-content center
    align-content center
    width 100%
    height 85vh

  .login-form
    display grid
    width 100%
    text-align center
    border 3px solid #616161
    border-radius 15px
    padding 30px
    grid-template-column 40vw
    grid-template-rows 15% auto auto auto auto auto

  .flex-item
    display flex
    flex-direction row
    justify-content space-between

  #login .flex-item i
    color red
</style>
