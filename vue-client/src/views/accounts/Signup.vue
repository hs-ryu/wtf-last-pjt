<template>
  <div class="mx-auto dark-mode-content" style="width: 300px;">
    <h1 class="fw-bold title-font my-5">회원가입</h1>
    <div class="my-3">
      <!-- <label for="username">사용자 이름: </label> -->
      <input style="width: 100%;" type="text" v-model="credentials.username" class="my-3 form-control" id="username" name="username" placeholder="아이디">
      <input style="width: 100%;" type="password" v-model="credentials.password" class="my-3 form-control" id="password" name="password" placeholder="비밀번호">
      <input style="width: 100%;" type="password" v-model="credentials.passwordConfirmation" @keypress.enter="signup(credentials)" class="my-3 form-control" id="password" name="password" placeholder="비밀번호 확인">
      <button style="width: 100%;" class="btn main-color-background text-white" @click="signup(credentials)">회원가입</button>
      <div class="my-4">
        <span class="mx-1">이미 가입하셨나요?</span>
        <span class="mx-1 main-color-content fw-bold mini-button" @click="$router.push({ name: 'Login' })">로그인</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'signup',
    ])
  }
}
</script>