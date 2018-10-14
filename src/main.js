import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import App from './App'
import router from './router'
import $backend from './backend'
 
Vue.prototype.$backend = $backend
Vue.config.productionTip = false
Vue.use(BootstrapVue);

const vue = new Vue({
  router,
  render: h => h(App)
})

vue.$mount('#app')
