<template lang="pug">
  #magazine
</template>

<script>
import MagazineService from '../services/MagazineService'

export default {
  data () {
    return {

    }
  },
  mounted: function () {
    MagazineService.getNumbersMag((res) => {
      console.log(res)
    })
  }
}
</script>

<style lang="css">
#magazine {
  width:100%;
  min-height:90vh;
}
</style>
