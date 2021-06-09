import Vue from 'vue'
import Vuex from 'vuex'

import SERVER from '@/api/drf.js'
import axios from 'axios'
import router from '../router'

import jwt_decode from 'jwt-decode'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    clickedOne: true,
    clickedTwo: false,
    clickedThree: false,
    clickedFour: false,
    allMovies: [],
    popularMovies: [],
    nowShowingMovies: [],
    authToken: localStorage.getItem('jwt'),
    username: '손님',
    isSuperuser: false,
    userId: -1,
    decoded: '',
    today: new Date(),

    // 검색
    inputValue: '',
    searchMovies : [],
    
    // 플랫폼 영화
    platformvalue: 'netflix',
    platformMovies : [],

    //투표 댓글
    // choice: 0,

  },
  getters: {
    // 로그인상태 확인 boolean 값
    isLoggedIn: function (state) {
      return state.authToken ? true : false
    },
    config: function (state) {
      return {
        Authorization: `JWT ${state.authToken}`
      }
    },
    movieLength: function (state) {
      if (state.searchMovies) {
        return state.searchMovies.Length
      }
    },
    inputLength: function (state) {
      if (state.inputValue) {
        return state.inputValue.Length
      }
    }
  },
  mutations: {
    SET_TOKEN: function (state, token) {
      state.authToken = token
      state.decoded = localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem('jwt')
      state.authToken = ''
      state.decoded = ''
      state.username = ''
    },
    // token 디코딩하여 username 가져오기
    GET_USERNAME: function (state) {
      state.decoded = jwt_decode(state.authToken)
      // 로그인 되어 있으면 디코딩해서 넣고, 아니면 손님으로
      if (state.authToken) {
        state.username = state.decoded.username
        state.userId = state.decoded.user_id
        // console.log(state.decoded)
      } else {
        state.decoded = ''
        state.username = '손님'
        state.userId = -1
      }
    },
    GET_USER_INFO: function (state, issuperuser, userid) {
      state.isSuperuser = issuperuser
      state.userId = userid
    },
    GET_ALL_MOVIES: function (state, allmovies) {
      state.allMovies = allmovies
    },
    GET_POPULAR_MOVIES: function (state, popularmovies) {
      state.popularMovies = popularmovies
    },
    GET_NOW_SHOWING: function (state, nowShowingMovies) {
      state.nowShowingMovies = nowShowingMovies
    },

    // 검색
    SET_INPUT_VALUE : function (state, inputValue) {
      state.inputValue = inputValue
    },
    SET_SEARCH_MOVIES: function (state, searchMovies) {
      state.searchMovies = searchMovies
    },
    GET_PLATFORM_MOVIES: function (state, platformMovies) {
      state.platformMovies = platformMovies
    },
    SET_PLATFORM: function(state, platform) {
      state.platformvalue = platform
    },
    RESET_INPUT_VALUE: function (state) {
      state.inputValue = ''
    },
  },
  actions: {
    /* 인증 & 권한 */
    getUserName: function ({ commit }) {
      commit('GET_USERNAME')
    },
    login: function ({ commit, dispatch }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        commit('SET_TOKEN', res.data.token)
        axios({
          url: SERVER.URL + SERVER.ROUTES.verify_user,
          method: 'post',
          data: {
            token: this.state.authToken,
          }
        })
        .then((res) => {
          console.log(res.data)
          dispatch('get_user_info')
          // const userId = res.data.user_id
          // const issuperuser = res.data.issuperuser
          this.state.userId = res.data.user_id
          this.state.isSuperuser = res.data.issuperuser
          // console.log(this.state.userId)
          // console.log(this.state.isSuperuser)
          // console.log(this.state.username)
        })
        router.push({ name: 'MovieList' })
      })
      .catch(() => {
        alert('비밀번호가 틀렸습니다.')
      })
    },
    get_user_info: function ({ state, commit }) {
      if (state.authToken) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.verify_user,
          method: 'post',
          data: {
            token: state.authToken,
          }
        })
        .then((res) => {
          // console.log(res.data)
          commit('GET_USER_INFO', res.data.issuperuser, res.data.user_id)
          // const username = res.data.username ? res.data.username : '손님'
          // const userId = res.data.user_id ? res.data.user_id : null
          // const issuperuser = res.data.issuperuser ? res.data.issuperuser : false
          // this.state.username = username
          // this.state.userId = userId
          // this.state.isSuperuser = issuperuser
          // console.log(this.state.username)
          // console.log(this.state.userId)
          // console.log(this.state.isSuperuser)
        })
      }
    },
    logout: function ({ commit }, credentials) {
      commit('REMOVE_TOKEN')
      // console.log(credentials)
      credentials.username = ''
      credentials.password = ''
      router.push({ name: 'MovieList' })
    },
    signup: function (context, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: 'post',
        data: credentials,
      })
      .then(() => {
        router.push({ name: 'Login' })
      })
      .catch((err) => {
        if (err.response.status==401) {
          alert('비밀번호가 일치하지 않습니다.')
        } else {
          alert('이미 존재하는 아이디 입니다.')
        }
      })
    },
    /* 전체 영화 조회 */
    getAllMovies: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies,
        method: 'get',
      })
      .then((res) => {
        commit('GET_ALL_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    /* 인기 영화 조회 */
    getPopularMovies: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPopularMovies,
        method: 'get'
      })
      .then((res) => {
        commit('GET_POPULAR_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    /* 현재상영중 영화 조회 */
    getNowShowing: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getNowShowing,
        method: 'get',
      })
      .then((res) => {
        commit('GET_NOW_SHOWING', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setPlatform: function ({ commit, state }, platform) {
      commit('SET_PLATFORM', platform)
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPlatformMovies + platform + '/',
        method: 'get',
      })
      .then((res) => {
        commit('GET_PLATFORM_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })

      if (platform === "netflix") {
        state.clickedOne = true
        state.clickedTwo = false
        state.clickedThree = false
        state.clickedFour = false
      } else if (platform === "watcha") {
        state.clickedOne = false
        state.clickedTwo = true
        state.clickedThree = false
        state.clickedFour = false
      } else if (platform === "wavve") {
        state.clickedOne = false
        state.clickedTwo = false
        state.clickedThree = true
        state.clickedFour = false
      } else {
        state.clickedOne = false
        state.clickedTwo = false
        state.clickedThree = false
        state.clickedFour = true
      }

    },

    // 검색 
    fetchMovies: function ({ commit, state }, event) {
      commit('SET_INPUT_VALUE', event.target.value)
      axios({
        url: SERVER.URL + SERVER.ROUTES.searchMovies + state.inputValue + '/',
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        commit('SET_SEARCH_MOVIES', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    resetInputValue: function({commit}) {
      commit('RESET_INPUT_VALUE')
    },

    getPlatformMovies: function ({ commit }, platform) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPlatformMovies + platform + '/',
        method: 'get',
      })
      .then((res) => {
        commit('GET_PLATFORM_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },



  },
  modules: {
  }
})
