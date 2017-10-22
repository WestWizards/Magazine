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
      login: {}
    }
  },
  methods: {
    signin: function () {
      // TODO: valider les identifiants
      axios.post('http://localhost:5000/login', this.login)
      .then(function (res) {
        console.log(res)
        // TODO : store auth jwt
      })
      .catch(function (err) {
        console.log(err)
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
