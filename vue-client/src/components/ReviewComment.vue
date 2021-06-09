<template>
  <div class="my-1">
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex align-items-center">
        <span class="fw-bold me-4">{{ comment.username }}</span>
        <span :class="{hide: modifyActivate}">{{ comment.content }}</span>
        <input type="text" style="width: 600px; height: 30px;" class="my-3 form-control" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent">
        <!-- <input style="width: 700px; height: 30px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text"> -->
        <span class="mini-button mini-button-content mx-2" :class="{hide: !modifyActivate}" @click="updateMode">수정</span>
      </div>
      <div class="d-flex align-items-center">
        <span class="mx-2" :class="{hide: modifyActivate}">{{$moment(comment.created_at).format('YYYY.MM.DD h:mm a')}}</span>
        <div class="d-flex" v-if="decoded.username==comment.username">
          <span class="mini-button mini-button-content mx-1" :class="{hide: modifyActivate}" @click="updateMode">수정</span>
          <span :class="{hide: modifyActivate}" class="mini-button mini-button-content mx-1">|</span>
          <span class="mini-button mini-button-content mx-1" :class="{hide: modifyActivate}" data-bs-toggle="modal" data-bs-target="#reviewCommentDeleteModal">삭제</span>
          <!-- <button class="mx-1 btn btn-sm main-color-background text-white" @click="updateMode">수정</button> -->
          <!-- <button :class="{hide: modifyActivate}" class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button> -->
        </div>
      </div>
    </div>

    <div class="modal fade" id="reviewCommentDeleteModal" tabindex="-1" aria-labelledby="reviewCommentDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="reviewCommentDeleteModal" style="color: black;">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" style="color: black;">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer" style="color: black;">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteComment">삭제</button>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex">
        <p class="fw-bold me-4">{{ comment.username }}</p>
        <p :class="{hide: modifyActivate}">{{ comment.content }}</p>
        <input style="width: 500px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
      </div>
      <div class="d-flex">
        <p>(작성시각)</p>
        <div v-if="loginedUser=(comment.username)">
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="updateMode">수정</button>
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'ReviewComment',
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    reviewId: {
      type: String,
    }
  },
  data: function () {
    return {
      modifyActivate: false,
      updatedContent: '',
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'decoded'
    ]),
  },
  methods: {
    getReviewComments: function () {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId * 1}/getcomments/`,
        method: 'get',
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
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId * 1}/${commentId}/deletecomment/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        // this.getReviewComments()
        this.$emit('comment-deleted')
        // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
      })
    },
    updateMode: function () {
      // console.log(this.modifyActivate)
      if (!this.modifyActivate) {
        this.modifyActivate = true // 수정창 열림
        this.$emit('modify-activate')
      } else {
        const commentContent = this.updatedContent ? this.updatedContent : this.comment.content
        // console.log(commentContent)
        const commentItem = {
          content: commentContent,
        }
        // 모델 변경 후 길이 수정 필요  
        if (commentItem.content) {
          const headers = this.config
          const commentId = this.comment.id
          axios({
            url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId * 1}/${commentId}/updatecomment/`,
            method: 'put',
            data: commentItem,
            headers,
          })
          .then(() => {
            // 여기 필요할듯
            this.$emit('modify-activate')
          })
          .catch((err) => {
            console.log(err)
          })
        }
        this.modifyActivate = false
        this.$emit('modify-activate')
      }
    },
    updateContent: function (event) {
      this.updatedContent = event.target.value
    }
  },
}
</script>

<style>
.hide {
  display: none;
}
</style>