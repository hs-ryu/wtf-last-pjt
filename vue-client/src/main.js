import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
import VueMoment from 'vue-moment'
import VueDarkMode from '@vue-a11y/dark-mode'

Vue.use(VueDarkMode)


Vue.use(VueMoment)
Vue.use(VueAwesomeSwiper)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
