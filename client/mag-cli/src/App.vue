<template lang="pug">
  #app
    app-nav
    router-view
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

<style>

</style>
