import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  components: {
    'app': App
  }
})
