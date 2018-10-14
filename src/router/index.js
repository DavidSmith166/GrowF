import Vue from 'vue'
import Router from 'vue-router'
import App from './App'

import Portfolio from '@/components/Portfolio'
import createPortfo from '@/components/createPortfo'


import callback from '@/components/callback'
import Home from '@/components/Home'




Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'App',
      component: App,
    },
  ],
});





const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/portfolio-list',
    name: 'Portfolio',
    component: Portfolio
  },
  {
    path: '/product-create',
    name: 'createPortfo',
    component: createPortfo
  },
  {
    path: '/product-update/:pk',
    name: 'PortfolioUpdate',
    component: createPortfo
  },
  {
    path: '/callback',
    name: 'callback',
    component: callback
  }]
const router = new Router({
  mode: 'history',
  routes
})  