<template>
  <div class="dark-mode-content">
    <!-- <p>{{vote}}</p> -->
    <h5 class="title-font">[{{ movieTitle }}]</h5>
    <h1 class="fw-bold title-font">{{vote.title}}</h1>
    <p style="font-size:13px;">{{$moment(vote.created_at).format('YYYY.MM.DD h:mm a')}}</p>
    <br>
    <div style="width: 600px;" class="mx-auto row">
      <h3 class="col">{{ vote.option_one }}</h3>
      <h3 class="col">vs</h3>
      <h3 class="col">{{ vote.option_two }}</h3>
    </div>
    <p class="my-2"> 총 {{ vote.option_one_count + vote.option_two_count }}명 참여중!</p>
    <div v-if="(vote.option_one_count+vote.option_two_count)" class="d-flex justify-content-center">
      <div class="progress my-2" style="height: 40px; width: 700px">
        <div class="progress-bar bg-primary" role="progressbar" :style="{width: scoreone + '%'}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_one }}  :  {{scoreone}}% ({{vote.option_one_count}} 명)</div>
        <div class="progress-bar bg-danger" role="progressbar" :style="{width: scoretwo + '%'}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_two }}  :  {{ scoretwo }}% ({{vote.option_two_count}} 명)</div>
      </div>
    </div>
    <div v-else class="d-flex justify-content-center">
      <div class="progress my-2" style="height: 40px; width: 700px">
        <div class="progress-bar bg-primary" role="progressbar" :style="{width: 0}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_one }}  :  {{scoreone}}% ({{vote.option_one_count}} 명)</div>
        <div class="progress-bar bg-danger" role="progressbar" :style="{width: 0}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_two }}  :  {{ scoretwo }}% ({{vote.option_two_count}} 명)</div>
      </div>
    </div>
    <br>
    <div class="d-flex justify-content-center">
      <!-- <button v-if="vote.username==decoded.username" type="button" class="btn main-color-background text-white" data-bs-toggle="modal" data-bs-target="#voteDeleteModal">
        투표삭제
      </button> -->
      <span class="mx-1 mini-button mini-button-content" v-if="vote.username==decoded.username" data-bs-toggle="modal" data-bs-target="#voteDeleteModal">삭제</span>
      <span class="mx-1 mini-button-content" v-if="vote.username==decoded.username">|</span>
      <span class="mx-1 mini-button mini-button-content" @click="$router.push({ name: 'MovieDetail', params: { movieId: movieId } })">목록</span>
    </div>
    <div style="width: 850px;" class="mx-auto">
      <hr>
      <!-- {{ comments }}
      {{ CommentExist }} -->
      <div v-if="comments.length">
        <h3 style="text-align: left" class="my-3">{{ comments.length }}개의 댓글</h3>
        <VoteComment
          v-for="(comment,idx) in comments"
          :key="idx"
          :comment="comment"
          :movieId="movieId"
          :voteId="voteId"
          @comment-deleted="getVoteComments"
          @plz-update-detail="getVoteDetail"
        />
      </div>

      <div v-else>
        <p>당신의 의견을 기다리고 있어요 🤘</p>
      </div>
      <div class="my-5 d-flex align-items-center justify-content-center">
        <input class="mx-1 btn btn-sm btn-primary" @click="createCommentOne" type="submit" value="왼쪽!">
        <input v-if="CommentExist" style="width: 500px; height: 30px;" type="text" class="my-3 form-control" disabled readonly id="disabledComment" name="disabledComment" placeholder="투표는 한 번만 가능합니다.">
        <input v-else style="width: 500px; height: 30px;" type="text" v-model="commentContent" class="my-3 form-control" id="comment" name="comment" placeholder="당신의 생각은?">
        <!-- <input style="width: 500px; height: 30px;" v-model="commentContent" type="text" name="comment" id="comment" placeholder="당신의 생각은?"> -->
        <input class="mx-1 btn btn-sm btn-danger" @click="createCommentTwo" type="submit" value="오른쪽!">
      </div>
    </div>

    <div class="modal fade" id="voteDeleteModal" tabindex="-1" aria-labelledby="voteDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="voteDeleteModal" style="color: black;">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" style="color: black;">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteVote">삭제</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'
import VoteComment from '@/components/VoteComment'

export default {
  name: 'VoteDetail',
  components: {
    VoteComment,
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'decoded',
    ]),
    CommentExist: function () {
      const result = this.comments.some((comment) => {
        return comment.username === this.decoded.username
      })
      return result
    }
  },
  data: function () {
    return {
      vote: {},
      // movieTitle: this.$route.query.movieTitle,
      movieId: this.$route.params.movieId,
      voteId: this.$route.params.voteId,
      comments: [],
      commentContent: '',
      scoreone: 0,
      scoretwo: 0,
      movieTitle: this.$route.query.movieTitle

      // comments: [],
      // likeCount: 0,
      // likeStatus: false,
      // likeStatus: this.review.like_users.includes('userId'),
    }
  },
  methods: {
    getVoteDetail: function () {
      const headers = this.config
      // path('<int:movie_pk>/votes/<int:vote_pk>/', views.getvote, name='getvote'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.vote = res.data
        this.scoreone = (this.vote.option_one_count/(this.vote.option_one_count + this.vote.option_two_count) * 100).toFixed(1)
        this.scoretwo = (this.vote.option_two_count/(this.vote.option_one_count + this.vote.option_two_count) * 100).toFixed(1)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getVoteComments: function () {
      const headers = this.config
      // path('<int:movie_pk>/votes/<int:vote_pk>/votecomments/', views.getvotecomments, name='getallvotecomments'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/` + 'votecomments/',
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

    deleteVote: function() {
      const headers = this.config
      // path('<int:movie_pk>/<int:vote_pk>/deletevote/', views.deletevote, name='deletevote'),
      axios({
        url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/${this.voteId}/deletevote/`,
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
    // //여기서부터 다시
    createCommentOne: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
        choice : 0
      }
      // 모델 변경 후 길이 수정 필요
      if (commentItem.content.length > 10) {
        alert("댓글의 제목이 너무 길어요!")
      }
      else if (commentItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/votes/${this.voteId}/createvotecomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getVoteComments()
          this.getVoteDetail()
          // this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: this.voteId }})
        })
        .catch(() => {
        })
      } else {
        alert('댓글의 내용을 적어주세요!')
      }
    },
    createCommentTwo: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
        choice : 1
      }
      if (commentItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/votes/${this.voteId}/createvotecomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getVoteComments()
          this.getVoteDetail()
          // this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: this.voteId }})
        })
        .catch(() => {
        })
      }
    },
  },
  created: function () {
    this.getVoteDetail()
    this.getVoteComments()
  }

}
</script>

<style>

</style>