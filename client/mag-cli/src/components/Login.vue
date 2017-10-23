<template lang="pug">
  #login Connexion
    input(v-model="login.username" placeholder="username" type="text")
    input(v-model="login.password" placeholder="password" type="password")
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      login: {},
      auth: false
    }
  },
  methods: {
    signin: function () {
      // TODO: valider les identifiants (tester : veevalidate)
      axios.post('http://localhost:5000/login', this.login)
      .then( res => {
        console.log(res)
        localStorage.setItem('token', res.jwt)
        this.auth = true
      })
      .catch( e => {
        console.log(e)
      })
    }
  },
  mounted: function () {
    // TODO : faire la requête de l'api
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
