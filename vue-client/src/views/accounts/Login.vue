<template>
  <div class="mx-auto " style="width: 300px;">
    <h1 class="fw-bold title-font my-5">로그인</h1>
    <div class="my-3">
      <!-- <label for="username">사용자 이름: </label> -->
      <input style="width: 100%;" type="text" v-model="credentials.username" class="my-3 form-control" id="username" name="username" placeholder="아이디">
      <input style="width: 100%;" type="password" @keypress.enter="login(credentials)" v-model="credentials.password" class="my-3 form-control" id="password" name="password" placeholder="비밀번호">
      <button style="width: 100%;" class="btn main-color-background text-white" @click="login(credentials)">로그인</button>
      <div class="my-4">
        <span class="mx-1">계정이 없으신가요?</span>
        <span class="mx-1 main-color-content fw-bold mini-button" @click="$router.push({ name: 'Signup' })">회원가입</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'login',
    ])
  }
}
</script>