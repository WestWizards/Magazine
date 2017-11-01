<template lang="pug">
  #home
    .news-carousel
      .inner-carousel
        div Image 1
        div Image 2
        div Image 3
      button.btnPrev Précédent
      button.btnNext Suivant
    .discover Discover
    .trends Trends
    .about About
</template>

<script>
import HomeService from '../services/HomeService'

// TODO : Carousel : https://www.w3schools.com/howto/howto_js_slideshow.asp
export default {
  name: 'Home',
  data () {
    return {
      news: []
    }
  },
  mounted: function () {
    HomeService.getNews((res) => {
      // TODO : bind returned news with props (use vuex for immutable data)
    })
  }
}
</script>

<style lang='stylus'>
  @import '../styles/home'
</style>
