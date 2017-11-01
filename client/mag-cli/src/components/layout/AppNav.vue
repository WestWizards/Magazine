<template lang="pug">
  #nav
    mu-appbar.inner-nav(title="MasterMind")
      mu-icon-button(icon="menu" slot="left")
      div(slot="right" v-if="!checkAuth()")
        mu-raised-button.nav-button(secondary v-on:click="redirectLogin") login
        mu-raised-button.nav-button(secondary v-on:click="redirectSignup") signup
      div(slot="right" v-else)
        mu-raised-button.nav-button(secondary v-on:click="openAccountDropdown") account
        mu-raised-button.nav-button(secondary v-on:click="logout") logout
</template>

<script>
// TODO : Replace title navbar with Mastermind logo and make it clickable (redirect home)
import AuthService from '../../services/AuthService'

export default {
  name: 'AppNav',
  data () {
    return {

    }
  },
  methods: {
    checkAuth: function () {
      return AuthService.isAuth()
    },
    logout: function () {
      AuthService.logout()
    },
    redirectLogin: function () {
      this.$router.push('/login')
    },
    redirectSignup: function () {
      this.$router.push('/signup')
    },
    openAccountDropdown: function () {
      // TODO : add dropdown menu for account settings (Muse-UI dropdown)
    }
  },
  mounted: function () {
    // TODO : Init menu content and bind side nav
  }
}
</script>

<style lang="stylus">
  #nav
    width 100%
    position fixed

  .inner-nav
    height 10vh

  .nav-button
    margin 0px 5px 0px 5px
</style>
