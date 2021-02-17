<template>
  <div style="width: 100%; height: 100%" ref="picturesContainer">
    <vue-waterfall-easy 
      :imgsArr="imgsArr" 
      @scrollReachBottom="getData" 
      :maxCols="3"
      :gap="1" :mobileGap="1"
      :imgWidth="imgWidth"
      ref="waterfall"
      :srcKey="'thu_url'" :hrefKey="'ori_url'"
      :reachBottomDistance="300">
    </vue-waterfall-easy>
  </div>
</template>


<style lang="scss">
* {
  padding: 0;
  margin: 0;
}
</style>

<script>
import vueWaterfallEasy from 'vue-waterfall-easy'
import { mapState, mapActions } from 'vuex'


export default {
  data() {
    return {
      imgsArr: [],
      imgWidth: 200
    }
  },
  components: {
    vueWaterfallEasy
  },
  methods: {
    ...mapActions([
      'fetchProfile'
    ]),
    getData() {
      if (this.imgsArr.length == this.profile.length)
        this.$refs.waterfall.waterfallOver()
      this.imgsArr = this.imgsArr.concat(this.profile.slice(this.imgsArr.length, this.imgsArr.length + 10))
    },
  },
  computed: {
    ...mapState({
      profile: 'profile'
    })
  },
  async created() {
    await this.fetchProfile()
    this.imgWidth = this.$refs.picturesContainer.clientWidth / 3
    this.getData()
  }
}
</script>