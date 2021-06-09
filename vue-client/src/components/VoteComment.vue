<template>
  <div class="my-1">
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex justify-content-center align-items-center">
        <button v-if="comment.choice" class="btn btn-danger me-4" type="button" disabled></button>
        <button v-else class="btn btn-primary me-4" type="button" disabled></button>
        <div class="justify-content-center me-3">
          <p style="width: 100px;" align="left" class="fw-bold m-0 ">{{ comment.username }}</p>
        </div>
        <div>
          <p align="center" class="m-0">{{ comment.content }}</p>
        </div>
      </div>
      <div class="d-flex align-items-center">
        <!-- <button class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button> -->
        <span class="me-1">({{$moment(comment.created_at).format('YYYY.MM.DD h:mm a')}})</span>
        <span v-if="decoded.username==comment.username" class="fw-bold mx-1 mini-button mini-button-content" data-bs-toggle="modal" data-bs-target="#voteCommentDeleteModal">삭제</span>
      </div>
    </div>
    <div class="modal fade" id="voteCommentDeleteModal" tabindex="-1" aria-labelledby="voteCommentDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="voteCommentDeleteModal" style="color: black;">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" style="color: black;">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer" >
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteComment">삭제</button>
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

export default {
  name: "VoteComment",
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    voteId: {
      type: String,
    },
  },
  data: function () {
    return {
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'decoded',
    ])
  },
  methods: {
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
    deleteComment: function () {
      const headers = this.config
      const commentId = this.comment.id
      // path('<int:movie_pk>/votes/<int:vote_pk>/<int:votecomment_pk>/deletevotecomment/', views.deletevotecomment, name='deletevotecomment'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/` + `${commentId}/` + 'deletevotecomment/',
        method: 'delete',
        headers,
      })
      .then(() => {
        // this.getReviewComments()
        // this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
        this.$emit('comment-deleted')
        this.$emit('plz-update-detail')
      })
    },
  }
}
</script>

<style>

</style>