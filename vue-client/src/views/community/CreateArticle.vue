<template>
  <div class="dark-mode-content">
    <h1 class="mb-4 title-font">게시글 작성</h1>
    <div class="mx-auto" style="width: 600px;">
      <div class="d-flex my-3">
        <select v-model="categories" name="categories" id="categories" class="form-select" aria-label="Default select example">
          <option disabled value="">말머리</option>
          <option v-if="loginSuperStatus" value="1">공지</option>
          <option value="2">건의</option>
          <option value="3">일상</option>
        </select>
      </div>
      <input type="text" v-model.trim="title" class="my-3 form-control" id="title" name="title" placeholder="제목">
      <!-- <input class="mb-3" style="width: 600px;" v-model.trim="title" type="text" name="title" id="title" placeholder="제목"> -->
      <!-- <input v-model.trim="content" type="text" name="content" id="content"> -->
      <textarea v-model.trim="content" class="form-control" id="content" rows="8" placeholder="내용"></textarea>
      <!-- <textarea v-model.trim="content" name="content" id="content" cols="70" rows="7" placeholder="내용"></textarea> -->
      <br>
      <div class="d-flex justify-content-end">
        <input class="mx-2 btn main-color-background text-white" @click="createArticle" type="submit" value="작성">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>
    <!-- <label for="title">글 제목</label>
    <input v-model.trim="title" type="text" name="title" id="title">
    <label for="categories">분류</label>
    <select v-model="categories" name="categories" id="categories">
      <option disabled value="">분류를 선택해 주세요</option>
      <option value="1">공지사항</option>
      <option value="2">건의사항</option>
      <option value="3">자유글</option>
    </select>
    <label for="content">글 내용</label>
    <input v-model.trim="content" type="text" name="content" id="content">
    <input @click="createArticle" type="submit" value="작성"> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      title: '',
      categories: '',
      content: '',
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState({
      'loginSuperStatus': 'isSuperuser',
    })
  },
  methods: {
    createArticle: function () {
      const headers = this.config
      const articleItem = {
        title: this.title,
        categories: this.categories,
        content: this.content,
      }
      // console.log(articleItem)
      // 모델 변경 후 길이 수정 필요
      if (articleItem.title && articleItem.categories && articleItem.content) {
        // path('createarticle/', views.createarticle, name='createarticle'),
        axios({
          url: SERVER.URL + '/community/createarticle/',
          method: 'post',
          data: articleItem,
          headers,
        })
        .then((res) => {
          // console.log(res)
          // '/community/articles/:articleId',
          this.$router.push({ name: 'ArticleDetail', params: { articleId: res.data.id } })
        })
        .catch((err) => {
          console.log(err)
        })
      }
      else{
        if (!articleItem.title) {
          alert("글의 제목을 입력해주세요!")
        } else if (!articleItem.categories) {
          alert("카테고리를 입력해주세요!")
        } else if (!articleItem.content) {
          alert("글의 내용을 입력해 주세요!")
        }
      }
    
    }
  }
}
</script>

<style>

</style>