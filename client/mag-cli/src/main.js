// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

// TODO : implement vuex for state management
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'

// TODO : Discuss about Material Design based UIs
import MuseUI from 'muse-ui'
import 'muse-ui/dist/muse-ui.css'
import 'muse-ui/dist/theme-carbon.css' // use carbon theme

Vue.use(Vuex)
Vue.use(MuseUI)

window.onbeforeunload = function () {
  localStorage.removeItem('user')
}

const store = new Vuex.Store({
  state: {
    count: 0,
    isAuth: false
  },
  mutations: {
    increment (state) {
      state.count++
    },
    toggleAuth (state) {
      state.isAuth = !state.isAuth
    }
  }
})

console.log(store.state.isAuth)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})
