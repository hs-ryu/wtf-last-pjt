<template>
  <div class="dark-mode-content">
    <div class="mx-auto" style="width: 700px;">
      <h1 style="text-align: left;" class="fw-bold title-font">{{ article.title }}</h1>
      <div style="text-align: left;">
        <div class="d-inline" v-if="article.categories=='1'">
          <h5 class="d-inline">[공지]</h5>
        </div>
        <div class="d-inline" v-else-if="article.categories=='2'">
          <h5 class="d-inline">[건의]</h5>
        </div>
        <div class="d-inline" v-else>
          <h5 class="d-inline">[일상]</h5>
        </div>
        <h5 class="mx-2 d-inline">|</h5>
        <h5 class="d-inline">{{ article.username }}</h5>
        <h5 class="mx-2 d-inline">|</h5>
        <h5 class="d-inline">{{$moment(article.created_at).format('YYYY.MM.DD h:mm a')}}</h5>
        <button style="border-color: #CE93D8" class="ms-2 d-inline btn btn-sm main-color-content custom-button-reverse" @click="goToProfile">프로필</button>
      </div>
      <hr>
      <div style="width: 700px; text-align: left; word-break: break-all;" class="mb-5">
        {{ article.content }}
      </div>
      <div class="d-flex justify-content-between">
        <div>
          <button class="btn d-inline" v-if="article.like_users && article.like_users.includes(decoded.user_id)" @click="getLikeStatus"><i class="fas fa-heart fa-lg" style="color:#CE93D8;"></i></button>
          <button class="btn d-inline" v-else @click="getLikeStatus"><i class="far fa-heart fa-lg" style="color:#CE93D8;"></i></button>
          <p v-if="article.like_users" class="d-inline">{{ article.like_users.length }}명이 이 글을 좋아합니다.</p>
        </div>
        <div v-if="loginedUser==(article.username)">
          <button class="mx-2 btn main-color-background text-white" @click="goToUpdateArticle">수정</button>
          <!-- <button class="btn main-color-background text-white" @click="deleteArticle">삭제</button> -->
          <button type="button" class="btn main-color-background text-white" data-bs-toggle="modal" data-bs-target="#articleDeleteModal">
              삭제
            </button>
        </div>
        <!-- <button class="btn main-color-background text-white" @click="deleteArticle">삭제</button>   -->
      </div>
      <hr>
    </div>

    <div style="width: 700px;" class="mx-auto">
      <div v-if="comments.length">
        <h5 style="text-align: left" class="my-3">댓글 ({{ comments.length }})</h5>
        <ArticleComment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        :articleId="articleId"
        @comment-deleted="getArticleComments"
        @modify-activate="getArticleComments"
        />
      </div>
      <div v-else>
        <p>댓글이 아직 없어요. 첫번째 댓글을 쓸 수 있는 절호의 찬스! 🤘</p>
      </div>
      <div class="mt-5 d-flex align-items-center">
        <input type="text" style="width: 600px" v-model="commentContent" class="d-inline my-3 form-control" id="comment" name="comment" placeholder="댓글을 입력해주세요" @keypress.enter="createComment">
        <!-- <input style="width: 600px" v-model="commentContent" type="text" name="comment" id="comment" @keypress.enter="createComment" placeholder="댓글을 작성해주세요"> -->
        <input class="mx-1 btn main-color-background text-white d-inline" @click="createComment" type="submit" value="작성">
      </div>
    </div>

    <div class="modal fade" id="articleDeleteModal" tabindex="-1" aria-labelledby="articleDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="articleDeleteModal">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteArticle">삭제</button>
          </div>
        </div>
      </div>
    </div>

    <button style="border-color: #CE93D8" class="my-2 btn main-color-content custom-button-reverse" @click="$router.push({ name: 'ArticleList' })">목록</button>


      <!-- <button @click="deleteArticle">삭제</button>
      <button @click="goToUpdateArticle">수정</button>
    <div>
      <p>{{ article.like_users.length }}명이 좋아합니다.</p>
      <button v-if="article.like_users.includes(userId)" @click="getLikeStatus">좋아요취소</button>
      <button v-else @click="getLikeStatus">좋아요</button>
    </div> -->
    <!-- <div>
      <h2>댓글목록</h2>
      <label for="comment">댓글작성</label>
      <input v-model="commentContent" type="text" name="comment" id="comment">
      <input @click="createComment" type="submit" value="작성">
      <ArticleComment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        :articleId="articleId"
        @comment-deleted="getArticleComments"
        @modify-activate="getArticleComments"
      />
    </div>
    {{ comments }} -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import ArticleComment from '@/components/ArticleComment'
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'ArticleDetail',
  components: {
    ArticleComment,
  },
  data: function () {
    return {
      articleId: this.$route.params.articleId,
      article: {},
      commentContent: '',
      comments: [],
    }
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
  methods: {
    // path('articles/<int:article_pk>/', views.getarticle, name='getarticle'),
    getArticleDetail: function() {
      const headers = this.config
      axios({
        url: SERVER.URL + `/community/articles/${this.articleId}`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArticleComments: function () {
      const headers = this.config
      axios({
        // path('articles/<int:article_pk>/comments/', views.getallcomments, name='getallcomments'),
        url: SERVER.URL + `/community/articles/${this.articleId}/comments/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        // console.log(res.data)
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteArticle: function () {
      const headers = this.config
      axios({
        // path('articles/<int:article_pk>/deletearticle/', views.deletearticle, name='deletearticle'),
        url: SERVER.URL + `/community/articles/${this.articleId}/deletearticle/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        this.$router.push({ name: 'ArticleList' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToUpdateArticle: function () {
      this.$router.push({ name: 'UpdateArticle', params: { articleId: this.articleId }, query: { article: this.article }})
    },
    createComment: function () {
      const commentItem = {
        content: this.commentContent,
      }
      // 모델 변경 후 길이 수정 필요
      if (commentItem.content) {
        const headers = this.config
        axios({
          // path('articles/<int:article_pk>/createcomment/', views.createcomment, name='createcomment'),
          url: SERVER.URL + `/community/articles/${this.articleId}/createcomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getArticleComments()
          // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    getLikeStatus: function () {
      const headers = this.config
      axios({
        // 'articles/<int:article_pk>/likes/'
        url: SERVER.URL + `/community/articles/${this.articleId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        // const { likeCount } = res.data
        // this.likeCount = likeCount
        // this.likeStatus = liked
        this.getArticleDetail()
      })
    },
    goToProfile: function () {
      const userName = this.article.username
      this.$router.push({ name: 'Profile', params: { username: userName }})
    },
  },
  created: function () {
    this.getArticleDetail()
    // 현선 추가
    this.getArticleComments()
    // console.log(this.decoded)
  },
}
</script>

<style>

</style>