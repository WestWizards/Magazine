<template lang="pug">
  #home
    div(class='body')




      router-link(to="/magazine") Magazine
</template>

<script>

export default {
  name: 'Home',
  data () {
    return {
      posts: [{'user': 'Steeven'}]
    }
  },
  components: {

  },
  mounted: function () {
    // TODO : faire la requête de l'api
    console.log('debug mounted Home')
  }
}
</script>

<style>
#home {
  width: 100%;
  min-height: 90vh;
}
/* TODO : faire tous les medias queries*/
</style>
