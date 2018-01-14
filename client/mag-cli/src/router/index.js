import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Magazine from '@/components/Magazine'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import Recover from '@/components/Recover'
// TODO : add Post component

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/magazine',
      name: 'Magazine',
      component: Magazine
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/recover',
      name: 'Recover',
      component: Recover
    }
  ]
})
