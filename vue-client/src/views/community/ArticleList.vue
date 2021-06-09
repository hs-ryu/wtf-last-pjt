<template>
  <div class="mx-auto dark-mode-content" style="width: 1000px;">
    <h1 class="fw-bold title-font">커뮤니티</h1>
    <div class="my-2 d-flex justify-content-end">
      <button class="mx-2 btn btn-sm main-color-background text-white" @click="goToCreateArticle">게시글 작성</button>
    </div>
    <!-- {{ articles }} -->
    <div style="width: 1000px; height: 400px;" class="mx-auto">
      <table class="table content-font dark-mode-content">
        <thead>
          <tr class="text-center">
            <th scope="col">글번호</th>
            <th scope="col">말머리</th>
            <th scope="col">글제목</th>
            <th scope="col">글쓴이</th>
            <th scope="col">날짜</th>
            <!-- <th scope="col">좋아요</th> -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, idx) in displayArticles" :key="idx">
            <th class="text-center" scope="row">{{ article.id }}</th>
            <td v-if="article.categories==1" class="text-center" scope="row">공지</td>
            <td v-else-if="article.categories==2" class="text-center" scope="row">건의</td>
            <td v-else class="text-center" scope="row">일상</td>
            <td class="text-start" @click="goToArticleDetail(article.id)" v-if="article.title.length > 15">
              {{ article.title.substr(0,5) + '...' }} <p v-if="article.comment_count>0" class="d-inline">({{ article.comment_count }})</p>
            </td>
            <td class="text-start mini-button" @click="goToArticleDetail(article.id)" v-else>
              {{ article.title }} <p v-if="article.comment_count>0" class="d-inline">({{ article.comment_count }})</p>
            </td>
            <td class="text-center mini-button" @click="goToProfile(article.username)">
              {{ article.username }}
            </td>
            <td class="text-center">{{ article.created_at.substring(0,10) }}</td>
            <!-- <td class="text-center">{{ article.like_users.length }}</td> -->
          </tr>
        </tbody>
      </table>
    </div>
    <nav aria-label="Page navigation example" class="my-5">
      <ul class="pagination justify-content-center">
        <li class="page-item">
          <button type="button" class="text-dark page-link" v-if="page != 1" @click="page--"> Previous </button>
        </li>
        <li class="page-item" v-for="(pageNumber,idx) in pages.slice(page-1, page+5)" :key=idx>
          <button type="button" class="text-dark page-link"  @click="page=pageNumber">{{ pageNumber }}</button>
        </li>
        <li class="page-item">
          <button type="button" @click="page++" v-if="page < pages.length" class="text-dark page-link"> Next </button>
        </li>
      </ul>
    </nav>
    <!-- {{ articles }} -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapState, mapGetters } from 'vuex'

export default { 
  name: 'ArticleList',
  components: {
  },
  data: function () {
    return {
      articles: [],
      page: 1,
			perPage: 9,
			pages: [],	
    }
  },
  methods: {
    getAllArticles: function () {
      axios({
        // path('articles/', views.getallarticles, name='getallarticles'),
        url: SERVER.URL + '/community/articles/',
        method: 'get',
      })
      .then((res) => {
        this.articles = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToArticleDetail: function (articleId) {
      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'ArticleDetail', params: { articleId }})
      }
    },
    goToCreateArticle: function () {
      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'CreateArticle' })
      }
    },
    goToProfile: function (username) {
      console.log(username)
      const userName = username
      this.$router.push({ name: 'Profile', params: { username: userName }})
    },
    setPages: function () {
      let numberOfPages = Math.ceil(this.articles.length / this.perPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.pages.push(index)
      }
    },
    paginate: function (articles) {
      let page = this.page
      let perPage = this.perPage
      let from = (page * perPage) - perPage;
      let to = (page * perPage)
      return articles.slice(from, to)
    }

  },

  computed: {
    displayArticles () {
      return this.paginate(this.articles);
    },
    ...mapState([
      'username',
      'userId',
    ]),
    ...mapGetters([
      'isLoggedIn'
    ])
  },
  watch: {
    articles () {
      this.setPages()
    }
  },
  created: function () {
    this.getAllArticles()
    console.log(this.username)
  }
}
</script>

<style>

</style>