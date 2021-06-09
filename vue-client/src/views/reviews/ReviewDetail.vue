<template>
  <div style="mx-auto">
    <div class="mt-5 d-flex justify-content-center align-items-center dark-mode-content">
      <div style="max-width: 300px;">
        <img style="width: 100%;" :src="'https://image.tmdb.org/t/p/w500' + moviePosterPath" :alt="movieTitle">
      </div>
      <div class="mx-4" style="width: 500px; height: 450px; text-align: left;">
        <h2 class="d-inline title-font">{{ review.username }}님의 리뷰 📝</h2>
        <!-- <button class="d-inline mx-2 btn btn-sm main-color-background text-white" @click="goToProfile" type="submit" value="작성">프로필</button> -->
        <button style="border-color: #CE93D8" class="ms-2 d-inline btn btn-sm main-color-content custom-button-reverse" @click="goToProfile">프로필</button>
        <div class="my-2">
          <h5 class="d-inline">{{ review.title }}</h5>
        </div>
        <div>
          <p class="d-inline">{{$moment(review.created_at).format('YYYY.MM.DD h:mm a')}} | </p>
          <p v-if="review.rank === 0.5" class="d-inline"><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 1" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 1.5" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 2" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 2.5" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 3" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 3.5" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 4" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else-if="review.rank === 4.5" class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></p>
          <p v-else class="d-inline"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></p>

        </div>
        <!-- <p>{{ review }}</p> -->
        <hr style="border-style: dotted">
        <div style="height: 270px;">
          <p style="word-break: break-all;">{{ review.content }}</p>
        </div>
        <!-- {{ review }} -->
        <div class="d-flex justify-content-between">
          <div>
            <button class="btn d-inline" v-if="review.like_users && review.like_users.includes(decoded.user_id)" @click="getLikeStatus"><i class="fas fa-heart fa-lg" style="color:#CE93D8;"></i></button>
            <button class="btn d-inline" v-else @click="getLikeStatus"><i class="far fa-heart fa-lg" style="color:#CE93D8;"></i></button>
            <p v-if="review.like_users" class="d-inline">{{ review.like_users.length }}명이 이 리뷰를 좋아합니다.</p>
          </div>
          <div v-if="decoded.username==review.username">
            <button class="mx-2 btn main-color-background text-white" @click="goToUpdate">수정</button>
            <!-- <button class="btn main-color-background text-white" @click="deleteReview">삭제</button> -->
            <button type="button" class="btn main-color-background text-white" data-bs-toggle="modal" data-bs-target="#reviewDeleteModal">
              삭제
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="dark-mode-content">
      <div style="width: 850px;" class="mx-auto">
        <hr>
        <div v-if="comments.length">
          <h3 style="text-align: left" class="my-3">{{ comments.length }}개의 댓글</h3>
          <ReviewComment
            v-for="(comment, idx) in comments"
            :key="idx"
            :comment="comment"
            :movieId="movieId"
            :reviewId="reviewId"
            @comment-deleted="getReviewComments"
            @modify-activate="getReviewComments"
          />
        </div>
        <div v-else>
          <p>댓글이 아직 없어요. 첫번째 댓글을 쓸 수 있는 절호의 찬스! 🤘</p>
        </div>
        <div class="mt-5">
          <input type="text" style="width: 600px" v-model="commentContent" class="d-inline my-3 form-control" id="comment" name="comment" placeholder="댓글을 입력해주세요" @keypress.enter="createComment">
          <!-- <input style="width: 750px" @keypress.enter="createComment" v-model="commentContent" type="text" name="comment" id="comment" placeholder="댓글을 작성해주세요"> -->
          <input class="mx-1 btn btn-sm main-color-background text-white" @click="createComment" type="submit" value="작성">
        </div>
      </div>
    </div>
    <div class="modal fade" id="reviewDeleteModal" tabindex="-1" aria-labelledby="reviewDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="reviewDeleteModal">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteReview">삭제</button>
          </div>
        </div>
      </div>
    </div>
    <button style="border-color: #CE93D8" class="my-2 custom-button-reverse btn main-color-content" @click="$router.push({ name: 'MovieList' })">메인으로</button>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import ReviewComment from '@/components/ReviewComment'
import { mapGetters, mapState } from 'vuex'



export default {
  name: 'ReviewDetail',
  components: {
    ReviewComment,
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState({
      'userId': 'userId',
      'loginedUser': 'username',
      'decoded': 'decoded',
    }),
  },
  data: function () {
    return {
      review: {},
      movieTitle: this.$route.query.movieTitle,
      movieId: this.$route.params.movieId,
      moviePosterPath: this.$route.query.moviePosterPath,
      reviewId: this.$route.params.reviewId,
      comments: [],
      commentContent: '',
      // likeCount: 0,
      // likeStatus: false,
      // likeStatus: this.review.like_users.includes('userId'),
    }
  },
  methods: {
    getReviewDetail: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.review = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviewComments: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/getcomments/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteReview: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/deletereview/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId}})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToUpdate: function () {
      this.$router.push({ name: 'UpdateReview', params: { movieId: this.movieId, reviewId: this.reviewId }, query: { review: this.review, moviePosterPath: this.moviePosterPath }})
    },
    createComment: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
      }
      // 모델 변경 후 길이 수정 필요
      if (commentItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/createcomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getReviewComments()
          // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
      else {
        alert('댓글의 내용을 적어주세요!')
      }
    },
    // path('<int:movie_pk>/reviews/<int:review_pk>/likes/', views.likereview, name='likereview'),
    getLikeStatus: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + `/movies/${this.movieId}/reviews/${this.reviewId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        // const { likeCount } = res.data
        // this.likeCount = likeCount
        // this.likeStatus = liked
        this.getReviewDetail()
      })
    },
    // updateLikeStatus: function () {
    //   this.likeStatus = this.review.like_users.includes(this.userId)
    // }
    goToProfile: function () {
      const userName = this.review.username
      this.$router.push({ name: 'Profile', params: { username: userName }})
    },
    // goToReviewDetail: function () {
    //   const reviewId = this.review.id
    //   this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: reviewId }, query: { movieTitle: this.movieTitle}})
    // }
  },
  created: function () {
    this.getReviewDetail()
    this.getReviewComments() // 댓글목록 가져오는 함수
    // this.updateLikeStatus()
    // console.log(this.review.like_users)
  },
}
</script>

<style>
/* button :focus {
  border: none;
  outline: none;
}
button :hover{ 	
  border: none;
  outline: none;
  } */
</style>