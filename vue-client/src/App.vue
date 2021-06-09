<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <!-- <a class="navbar-brand" href="#">LOGO</a> -->
          <span style="max-width: 35px; ">
            <a class="navbar-brand" href=""><img img class="rounded" style="width: 100%;" src="@/assets/logo_square.png" alt="WTF-logo" @click="$router.push({ name: 'MovieList' })"></a>
          </span>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex justify-content-between align-items-center">
              <span class="d-flex">
                <li class="nav-item px-2 ms-2" style="font-size: 13pt;">
                  <router-link :to="{ name: 'MovieList' }">홈</router-link>
                </li>
                <li class="nav-item px-2" style="font-size: 13pt;">
                  <router-link :to="{ name: 'ArticleList' }">커뮤니티</router-link>
                </li>
                <DarkMode/>
              </span>
            </ul>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex justify-content-end align-items-center">

            </ul>
            <span class="d-flex align-items-center mx-2">
              <li class="mb-0 nav-item px-2 justify-content-end" style="list-style:none; font-size: 13pt;">
                <p class="mb-0 fw-bold" v-if="isLoggedIn">{{ decoded.username }}님, 오늘 영화 한 편 어떠세요? 🍿</p>
                <p class="mb-0 fw-bold" v-else>로그인 하시면 더 많은 기능을 이용할 수 있어요! 😉</p>
              </li>
            </span>
            <span v-if="isLoggedIn" class="d-flex align-items-center">
              <span class="fw-bold mini-button mx-2" data-bs-toggle="modal" data-bs-target="#logoutModal" style="font-size: 13pt;">로그아웃</span>
              <router-link :to="{ name: 'Profile', params: { username: decoded.username }}" class="mx-3"><h3 class="d-inline"><i class="fas fa-user-circle"></i></h3></router-link>
              <!-- <router-link :to="{ name: 'Profile', params: { username }}" class="mx-2">Mypage</router-link> -->
              <a v-if="isSuperuser" :href="adminPageURL" class="mx-2"><h3 class="d-inline"><i class="fas fa-cog"></i></h3></a>
              <!-- <a v-if="isSuperuser" :href="adminPageURL" class="mx-2">SYSTEM</a> -->
            </span>
            <span v-else class="d-flex align-items-centercd u">
              <router-link :to="{ name: 'Signup' }" class="mx-2">회원가입</router-link>
              <!-- <router-link :to="{ name: 'Login' }" class="mx-2">로그인</router-link> -->
              <span class="mx-2 fw-bold mini-button" style="font-size: 17px;" data-bs-toggle="modal" data-bs-target="#loginModal">
                로그인
              </span>
            </span>
          </div>
        </div>
      </nav>
      <!-- login Modal -->
      <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h4 class="my-3 fw-bold modal-title mx-auto" style="color: black;" id="loginModalLabel">로그인</h4>
            </div>
            <div class="modal-body">
              <form>
                <div class="mb-3">
                  <input type="text" class="form-control" id="username" v-model="credentials.username" placeholder="아이디">
                </div>
                <div class="mb-3">
                  <input
                    class="form-control" 
                    type="password" 
                    id="password"
                    placeholder="비밀번호" 
                    v-model="credentials.password"
                  >
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" style="width: 100%;" class="text-center btn main-color-background text-white" data-bs-dismiss="modal" @click="login(credentials)">로그인</button>
              <div class="my-4 mx-auto">
                <span class="mx-1">계정이 없으신가요?</span>
                <span class="mx-1 main-color-content fw-bold" data-bs-dismiss="modal" @click="$router.push({ name: 'Signup' })">회원가입</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- logout Modal -->
      <div class="modal fade" id="logoutModal" tabindex="-1" aria-labelledby="logoutModal" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="logoutModal">알림</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              로그아웃 하시겠습니까?
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
              <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="logout(credentials)">로그아웃</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'
import SERVER from '@/api/drf.js'
import DarkMode from '@/components/DarkMode'

export default {
  name: 'App',
  components: {
    DarkMode
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
      adminPageURL: SERVER.URL + '/admin/'
    }
  },
  methods: {
    ...mapActions([
      'logout',
      'get_user_info',
      'login',
      'getUserName',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
    ]),
    ...mapState([
      'userId',
      'isSuperuser',
      'username',
      'decoded',
    ])
  },
  watch: {
    isLoggedIn: function () {
      this.getUserName()
      this.get_user_info()
    }
  },
  created: function () {
    this.getUserName()
    // this.get_user_info()
    // console.log(this.isLoggedIn)
  },
  mounted: function () {
    this.getUserName()
    // this.get_user_info()
    // console.log(this.username)
    // console.log(this.username)
    // console.log(this.userId)
    // console.log(this.isSuperuser)
    // console.log(this.decoded)
  }
}
</script>
<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Nanum Gothic', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* #nav {
  padding: 30px;
} */

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #CE93D8;
}

.main-color-content {
  color: #CE93D8;
}

.main-color-background {
  background-color: #CE93D8;
}

.custom-button {
  background-color: #CE93D8;
  color: white;
}

.custom-button-reverse:hover {
  color: #CE93D8;
}

.mini-button {
  cursor: pointer;
}

.mini-button-content {
  color: gray;
}

.title-font {
  font-family: 'Noto Sans KR', sans-serif;
}




</style>
