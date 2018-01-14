<template lang="pug">
  #nav
    mu-appbar.inner-nav
      .flex-item(slot="left")
        mu-icon-button(icon="menu" @click="toggle(true)")
        h2
          router-link(to="/home") MasterMind
      div(v-if="!checkAuth" slot="right")
        mu-raised-button.login-btn(icon="account_box" label="login" v-on:click="redirectLogin" secondary)
      .flex-item( v-else slot="right")
        mu-avatar.nav-button(icon="folder" secondary v-on:click="")
        mu-raised-button.nav-button(secondary v-on:click="logout") logout
    mu-drawer(:open="open" :docked="docked" @close="toggle()")
      mu-list(@itemClick="docked ? '' : toggle()")
        mu-list-item(title="Menu Item 1")
        mu-list-item(title="Menu Item 2")
        mu-list-item(title="Menu Item 3")
</template>

<script>
// TODO : Replace title navbar with Mastermind logo and make it clickable (redirect home)
import AuthService from '../../services/AuthService'

export default {
  name: 'AppNav',
  data () {
    return {
      open: false,
      docked: true
    }
  },
  methods: {
    logout: function () {
      AuthService.logout()
      this.$store.commit('toggleAuth')
      this.$router.push('/login')
    },
    redirectLogin: function () {
      this.$router.push('/login')
    },
    openAccountDropdown: function () {
      // TODO : add dropdown menu for account settings (Muse-UI dropdown)
    },
    toggle: function (flag) {
      this.open = !this.open
      this.docked = !flag
    }
  },
  computed: {
    checkAuth: function () {
      return this.$store.state.isAuth
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

  .flex-item
    display flex
    align-items center
  .nav-button
    margin 0px 5px 0px 5px

  .mu-overlay
    background-color transparent
</style>
