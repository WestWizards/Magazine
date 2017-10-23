<template lang="pug">
  #magazine
    div(v-for="post in posts")
      p {{post.titre}}
      //- TODO : url of post (add client route "/posts/:id")
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      posts: []
    }
  },
  created: function () {
    axios.get(`http://localhost:5000/posts`)
    .then(res => {
      this.posts = res.data
    })
    .catch(e => {
      console.log(e)
    })
  },
  mounted: function () {

  }
}
</script>

<style lang="css">
#magazine {
  width:100%;
  min-height:90vh;
}
</style>
