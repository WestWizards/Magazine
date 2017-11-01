// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

// TODO : implement vuex for state management
import Vue from 'vue'
import App from './App'
import router from './router'

// TODO : Discuss about Material Design based UIs
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
import 'muse-ui/dist/theme-carbon.css' // use carbon theme

Vue.use(MuseUI)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
