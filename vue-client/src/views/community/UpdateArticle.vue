<template>
  <div>
    <h1 class="mb-4 title-font dark-mode-content">게시글 수정</h1>
    <div class="mx-auto" style="width: 600px;">
      <div class="d-flex my-3">
        <select :value="article.categories" @change="updateCategories" name="categories" id="categories" class="form-select" aria-label="Default select example">
          <option disabled value="">말머리</option>
          <option v-if="loginSuperStatus" value="1">공지</option>
          <option value="2">건의</option>
          <option value="3">일상</option>
        </select>
      </div>
      <input type="text" :value="article.title" @change="updateTitle" class="my-3 form-control" id="title" name="title" placeholder="제목">
      <!-- <input class="mb-3" style="width: 600px;" :value="article.title" @change="updateTitle" type="text" name="title" id="title" placeholder="제목"> -->
      <!-- <input v-model.trim="content" type="text" name="content" id="content"> -->
      <textarea :value="article.content" @change="updateContent" class="form-control" id="content" rows="8" placeholder="내용"></textarea>
      <!-- <textarea :value="article.content" @change="updateContent" name="content" id="content" cols="70" rows="7" placeholder="내용"></textarea> -->
      <br>
      <div class="d-flex justify-content-end">
        <input class="mx-2 btn main-color-background text-white" @click="updateArticle" type="submit" value="수정">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>

    <!-- <h1>글 수정</h1>
    <label for="title">글 제목</label>
    <input :value="article.title" @change="updateTitle" type="text" name="title" id="title">
    <label for="categories">분류</label>
    <select :value="article.categories" @change="updateCategories" name="categories" id="categories">
      <option disabled value="">분류를 선택해 주세요</option>
      <option value="1">공지사항</option>
      <option value="2">건의사항</option>
      <option value="3">자유글</option>
    </select>
    <label for="content">글 내용</label>
    <input :value="article.content" @change="updateContent" type="text" name="content" id="content">
    <input @click="updateArticle" type="submit" value="수정"> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'UpdateArticle',
  data: function () {
    return {
      article: this.$route.query.article,
      title: '',
      categories: '',
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
      console.log(EventTarget)
      this.title = event.target.value
    },
    updateCategories: function (event) {
      console.log(event.target.value)
      this.categories = event.target.value
    },
    updateContent: function (event) {
      this.content = event.target.value
    },
    updateArticle: function () {
      const articleId = this.$route.params.articleId
      const title = this.title ? this.title : this.article.title
      const categories = this.categories ? this.categories : this.article.categories
      const content = this.content ? this.content : this.article.content
      const headers = this.config
      const articleItem = {
        title: title,
        categories: categories,
        content: content,
      }
      // console.log(articleItem)
      // 모델 변경 후 길이 수정 필요
      if (articleItem.title.length > 15){
          alert("글의 제목이 너무 길어요!")
      }
      else if (articleItem.title && articleItem.categories && articleItem.content) {
        axios({
          // path('articles/<int:article_pk>/updatearticle/', views.updatearticle, name='updatearticle'),
          url: SERVER.URL + `/community/articles/${articleId}/updatearticle/`,
          method: 'put',
          data: articleItem,
          headers,
        })
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'ArticleDetail', params: { articleId: articleId}})
        })
        .catch((err) => {
          console.log(err)
        })
      } 
    }   
  }
}
</script>

<style>

</style>