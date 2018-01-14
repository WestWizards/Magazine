<template lang="pug">
  #app
    app-nav.nav(isAuth=this.isAuth)
    router-view.content-app
    app-footer.footer
</template>

<script>
import AppNav from './components/layout/AppNav'
import AppFooter from './components/layout/AppFooter'

export default {
  data () {
    return {
      name: 'app',
      isAuth: false
    }
  },
  mounted: function () {
    // TODO : vérifier si l'user est déjà connecté pour faire isAuth = true
  },
  components: {
    AppNav, AppFooter
  }
}
</script>

<style lang='stylus'>
  // TODO : Test grid-template-areas property

  #app
    display grid
    grid-template-columns 100%
    grid-template-rows 10vh auto 5vh

  .nav
    grid-colum-start 1
    grid-row-start 1
  .content-app
    grid-colum-start 1
    grid-row-start 2
  .footer
    grid-colum-start 1
    grid-row-start 3
</style>
