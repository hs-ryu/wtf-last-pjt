<template>
  <div class="dark-mode-content">
    <div class="mx-auto" style="width: 600px;">
      <h5 class="fw-bold title-font">[{{ movieTitle }}]</h5>
      <h1 class="fw-bold title-font">투표 생성</h1>
      <!-- <label for="title">제목</label> -->
      <div class="my-3">
        <input style="width: 100%;" type="text" v-model.trim="title" class="my-3 form-control" id="title" name="title" placeholder="주제">
        <!-- <input style="width: 500px;" v-model.trim="title" type="text" name="title" id="title"> -->
        <div class="row g-2">
          <input type="text" v-model.trim="optionone" class="col m-1 form-control" name="optionone" id="optionone" placeholder="옵션1">
          <input type="text" v-model.trim="optiontwo" class="col m-1 form-control" name="optiontwo" id="optiontwo" placeholder="옵션2" @keypress.enter="createVote(title, optionone, optiontwo)">
        </div>
      </div>
      <!-- <label for="optionone">첫번째</label>
      <input style="width: 500px;" v-model.trim="optionone" type="text" name="optionone" id="optionone"> -->
      <!-- <br> -->
      <!-- <label for="optiontwo">두번째</label>
      <input style="width: 500px;" v-model.trim="optiontwo" type="text" name="optiontwo" id="optiontwo">
      <br> -->
      <div class="d-flex justify-content-center">
        <input class="mx-2 btn main-color-background text-white" @click="createVote(title, optionone, optiontwo)" type="submit" value="작성">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CreateVote',
  data: function () {
    return {
      title: '',
      rank: 0,
      optionone: '',
      optiontwo:'',
      movieId: this.$route.params.movieId,
      movieTitle: this.$route.query.movieTitle,
    }
  },
  computed: {
    ...mapGetters([
      'config',
    ])
  },
  methods: {
    createVote: function (title, optionone, optiontwo) {
      const headers = this.config
      const VoteItem = {
        title: title,
        option_one: optionone,
        option_two: optiontwo,
      }
      // 모델 변경 후 길이 수정 필요
      if (VoteItem.title.length > 15){
        alert("투표의 제목이 너무 길어요!")
      }
      else if (VoteItem.title && VoteItem.option_one && VoteItem.option_two) {
        // path('<int:movie_pk>/createvote/', views.createvote, name='createvote'),
        axios({
          url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/createvote/`,
          method: 'post',
          data: VoteItem,
          headers,
        })
        .then((res) => {
          this.title = ''
          this.optionone = ''
          this.optiontwo = ''
          // '/:movieId/vote/:voteId'
          this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: res.data.id }, query: { movieTitle: this.movieTitle }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
      else {
        if (!VoteItem.title) {
          alert("만드실 투표의 제목을 입력해주세요!!")
        } else if (!VoteItem.optionone) {
          alert("만드실 투표의 첫번째 주제를 적어주세요!!")
        } else if (!VoteItem.optiontwo) {
          alert("만드실 투표의 두번째 주제를 적어주세요!!")
        }
      }
    }
  }
}
</script>

<style>

</style>