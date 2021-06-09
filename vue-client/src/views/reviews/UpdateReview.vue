<template>
  <div style="mx-auto" class="dark-mode-content">
    <div class="mt-5 d-flex justify-content-center align-items-center">
      <div style="max-width: 300px;">
        <img style="width: 100%;" :src="'https://image.tmdb.org/t/p/w500' + moviePosterPath" alt="movieTitle">
      </div>
      <div class="mx-4" style="width: 500px; text-align: left;">
        <h3 class="fw-bold pb-4 title-font">리뷰 수정</h3>
        <div class="startRadio">
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="0.5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 0.5개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="1" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 1개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="1.5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 1.5개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="2" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 2개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="2.5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 2.5개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="3" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 3개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="3.5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 3.5개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="4" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 4개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="4.5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 4.5개</span></span>
          </label>
          <label class="startRadio__box">
            <input type="radio" name="star" id="" value="5" @change="updateRank">
            <span class="startRadio__img"><span class="blind">별 5개</span></span>
          </label>
        </div>
        <!-- <br>
        <label for="title">제목</label> -->
        <input type="text" :value="review.title" class="my-3 form-control" id="title" name="title" @change="updateTitle">
        <!-- <input style="width: 500px;" :value="review.title" @change="updateTitle" type="text" name="title" id="title"> -->
        <!-- <label for="content">내용</label> -->
        <!-- <br> -->
        <!-- <input v-model.trim="content" type="text" name="content" id="content"> -->
        <textarea :value="review.content" class="form-control" id="content" rows="8" @change="updateContent"></textarea>
        <!-- <textarea :value="review.content" @change="updateContent" name="content" id="content" cols="58" rows="7"></textarea> -->
        <br>
        <div class="d-flex justify-content-end">
          <input class="mx-2 btn main-color-background text-white" @click="updateReview" type="submit" value="수정">
          <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
        </div>
      </div>
    </div>
    <!-- <h1>리뷰 수정</h1>
    <label for="title">글 제목</label>
    <input :value="review.title" @change="updateTitle" type="text" name="title" id="title">
    <label for="rank" min="0.5" max="5" step="0.5">평점</label>
    <input :value="review.rank" @change="updateRank" type="number" name="rank" id="rank">
    <label for="content">글 내용</label>
    <input :value="review.content" @change="updateContent" type="text" name="content" id="content">
    <input @click="updateReview" type="submit" value="리뷰 수정"> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'UpdateReview',
  data: function () {
    return {
      review: this.$route.query.review,
      moviePosterPath: this.$route.query.moviePosterPath,
      movieId: this.$route.params.movieId,
      title: '',
      rank: 0,
      content: '',
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ])
  },
  methods: {
    updateTitle: function (event) {
      // console.log(event.target.value)
      this.title = event.target.value
      // console.log(this.title)
    },
    updateRank: function (event) {
      this.rank = event.target.value
    },
    updateContent: function (event) {
      this.content = event.target.value
    },
    updateReview: function () {
      // params: { movieId: this.movieId, reviewId: this.reviewId }, query: { review: this.review, moviePosterPath: this.moviePosterPath }
      const movieId = this.$route.params.movieId
      const reviewId = this.$route.params.reviewId
      const title = this.title ? this.title : this.review.title
      const rank = this.rank ? this.rank : this.review.rank
      const content = this.content ? this.content : this.review.content
      const headers = this.config
      const reviewItem = {
        title,
        rank,
        content,
      }
      // console.log(reviewItem.title)
      // 모델 변경 후 길이 수정 필요
      if (reviewItem.title && reviewItem.rank && reviewItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${movieId}/reviews/${reviewId}/updatereview/`,
          method: 'put',
          data: reviewItem,
          headers,
        })
        .then(() => {
          // console.log(this.movieId)
          this.title = ''
          this.rank = 0
          this.content = ''
          this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.review.id}, query: { moviePosterPath: this.moviePosterPath }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style scoped lang="scss">
.blind {
  position: absolute;
  overflow: hidden;
  margin: -1px;
  padding: 0;
  width: 1px;
  height: 1px;
  border: none;
  clip: rect(0, 0, 0, 0);
}

.startRadio {
  display: inline-block;
  overflow: hidden;
  height: 40px;
  &:after {
    content: "";
    display: block;
    position: relative;
    z-index: 10;
    height: 40px;
    // background: url('data:image/png;base64,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'),
    //   repeat-x 0 0;
    background: url("data:image/png;base64,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")
      repeat-x 0 0;
    background-size: contain;
    pointer-events: none;
  }
  &__box {
    position: relative;
    z-index: 1;
    float: left;
    width: 20px;
    height: 40px;
    cursor: pointer;
    input {
      opacity: 0 !important;
      height: 0 !important;
      width: 0 !important;
      position: absolute !important;

      &:checked + .startRadio__img {
        background-color: #CE93D8;
      }
    }
  }
  &__img {
    display: block;
    position: absolute;
    right: 0;
    width: 500px;
    height: 40px;
    pointer-events: none;
  }
}
</style>