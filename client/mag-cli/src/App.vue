<template lang="pug">
  #app
    app-nav
    router-view.content-app
    app-footer
</template>

<script>
import AppNav from './components/layout/AppNav'
import AppFooter from './components/layout/AppFooter'

export default {
  data () {
    return {
      name: 'app'
    }
  },
  components: {
    AppNav, AppFooter
  }
}
</script>

<style lang='stylus'>
  // TODO : mettre les 3 blocs dans une grille
  .content-app
    padding-top 10vh !important //TODO : find best way to offset sticky header
</style>
