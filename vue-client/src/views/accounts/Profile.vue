<template>
  <div style="width: 1000px" class="mx-auto dark-mode-content">
    <div class="mb-3 d-flex justify-content-between align-items-center">
      <div>
        <h2 class="fw-bold title-font" style="text-align: left">{{userProfile.username}}님의 프로필</h2>
      </div>
      <div class="d-flex justify-content-between">
        <h5 class="title-font mx-3">팔로워 {{ userProfile.followers.length }} | 팔로잉 {{ userProfile.followings.length }}</h5>
        <div class="mx-3" v-if="userProfile.user_id!==decoded.user_id">
          <button class="mx-2 btn main-color-background text-white" v-if="userProfile.followers && userProfile.followers.includes(decoded.user_id)" @click="updateFollowStatus">unfollow</button>
          <button class="mx-2 btn main-color-background text-white" v-else @click="updateFollowStatus">follow</button>
        </div>
      </div>
    </div>
    <h5 v-if="userProfile.favorite_genre=='없음'" class="my-3 title-font" style="text-align: left;">💡 좋아하는 영화에 '좋아요'를 누르시면 선호 장르를 분석해드려요!</h5>
    <h4 v-else class="my-3 title-font" style="text-align: left;">[선호 장르] {{ userProfile.favorite_genre }}</h4>
    <h4 class="title-font" style="text-align: left;">좋아요 한 영화</h4>
    <div v-if="userProfile.like_movies.length" class="card-group mb-5 row row-cols-6">
      <div v-for="(movie, idx) in userProfile.like_movies" :key="idx + 'movie'">
        <div class="mb-1">
          <div class="card text-center mt-1 border-light h-100" style="width: 170px;">
            <div class="card-body p-0" style="flex-grow: 0; color: black;">
              <img :src="'http://image.tmdb.org/t/p/w200/' + movie.poster_path" @click="$router.push({ name: 'MovieDetail', params: {movieId: movie.id}})" style="object-fit: cover; height:250px" class="card-img-top rounded mx-auto d-block" :alt="movie.title">
              <!-- <p class="card-title m-0">{{ movie.title }}</p> -->
              <p class="card-title m-0" v-if="movie.title.length > 8">
                {{ movie.title.substr(0,8) + '...' }}
              </p>
              <p class="card-title m-0" v-else>
                {{ movie.title }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="my-5"><p>좋아요 한 영화가 없습니다.</p></div>

    <div class="my-2 d-flex justify-content-between">
      <div>
        <h4 class="fw-bold title-font" style="text-align: left;">작성한 리뷰</h4>
        <div class="m-2" v-if="(userProfile.create_reviews || 0).length">
          <table style="width: 450px;" class="table dark-mode-content">
            <thead>
              <tr>
                <th scope="col">영화</th>
                <th scope="col">제목</th>
                <th scope="col">평점</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(review, idx) in displayReviews" :key="idx +'1'">
                <!-- <td>{{ review.movie }}</td> -->
                <td class="text-start" v-if="review.movie.length > 8">
                  {{ review.movie.substr(0,8) + '...' }}
                </td>
                <td class="text-start" v-else>
                  {{ review.movie }}
                </td>
                <!-- <td @click="goToReviewDetail(review.id)">{{ review.title }}</td> -->
                <td class="text-start" v-if="review.title.length > 8">
                  {{ review.title.substr(0,8) + '...' }}
                </td>
                <td class="text-start" v-else>
                  {{ review.title }}
                </td>
                <td v-if="review.rank === 0.5" class="text-start"><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 1" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 1.5" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 2" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 2.5" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 3" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 3.5" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 4" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else-if="review.rank === 4.5" class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                <td v-else class="text-start"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
              </tr>
            </tbody>
          </table>

          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link" v-if="reviewsPage != 1" @click="reviewsPage--"> Previous </button>
              </li>
              <li class="text-dark page-item" v-for="(pageNumber,idx) in reviewsPages.slice(reviewsPage-1, reviewsPage+5)" :key=idx>
                <button type="button" class="text-dark page-link"  @click="reviewsPage=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="reviewsPage++" v-if="reviewsPage < reviewsPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
        </div>
        <div v-else class="my-5">
          <p>작성한 리뷰가 없습니다.</p>
        </div>
      </div>
      <div>
        <h4 class="fw-bold title-font" style="text-align: left;">작성한 게시글</h4>
        <div class="m-2" v-if="(userProfile.create_articles||0).length">
          <table style="width: 450px;" class="table dark-mode-content">
            <thead>
              <tr>
                <th scope="col">카테고리</th>
                <th scope="col">제목</th>
                <th scope="col">날짜</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(article, idx) in displayArticles" :key="idx +'2'">
                <td v-if="article.categories==2">
                  건의
                </td>
                <td v-else>
                  일상
                </td>
                <td class="text-start" v-if="article.title.length > 8">
                  {{ article.title.substr(0,8) + '...' }}
                </td>
                <td class="text-start" v-else>
                  {{ article.title }}
                </td>
                <td>{{$moment(article.created_at).format('YYYY.MM.DD')}}</td>
              </tr>
            </tbody>
          </table>
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link" v-if="articlesPage != 1" @click="articlesPage--"> Previous </button>
              </li>
              <li class="page-item" v-for="(pageNumber,idx) in articlesPages.slice(articlesPage-1, articlesPage+5)" :key=idx>
                <button type="button" class="text-dark page-link"  @click="articlesPage=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="articlesPage++" v-if="articlesPage < articlesPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
        </div>
        <div v-else class="my-5">
          <p>작성한 게시글이 없습니다.</p>
        </div>
      </div>
    </div>
    
    <!-- 회원탈퇴 -->
    <!-- <button class="btn main-color-background text-white" @click="deleteAccount">회원탈퇴</button> -->
    <button v-if="userProfile.username==decoded.username" class="btn main-color-background text-white" data-bs-toggle="modal" data-bs-target="#deleteAccountModal">회원탈퇴</button>

    <div class="modal fade" id="deleteAccountModal" tabindex="-1" aria-labelledby="deleteAccountModal" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="deleteAccountModal" style="color: black;">알림</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="color: black;">
              정말로 탈퇴하시겠습니까? 😢
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                <span style="font-color: black;">취소</span>
              </button>
              <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteAccount">회원탈퇴</button>
            </div>
          </div>
        </div>
      </div>
    <!-- {{ userProfile }} -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'Profile',
  data: function () {
    return {
      userName: this.$route.params.username,
      userProfile: {},
      reviewsPage: 1,
      articlesPage: 1,
			reviewsPerPage: 6,
			articlesPerPage: 6,
			reviewsPages: [],	
			articlesPages: [],	
    }
  },
  computed: {
    ...mapState({
      'loginedUserId': 'userId',
      'decoded': 'decoded',
    }),
    ...mapGetters([
      'config',
    ]),
    displayReviews () {
      return this.reviewPaginate(this.userProfile.create_reviews)
    },
    displayArticles () {
      return this.articlePaginate(this.userProfile.create_articles)
    },
    Reviews () {
      return this.userProfile.create_reviews
    },
    Articles () {
      return this.userProfile.create_articles
    }
  },
  watch: {
    Reviews () {
      this.setReviewPages()
    },
    Articles () {
      this.setArticlePages()
    }
  },
  methods: {
    ...mapActions ([
      'logout',
    ]),
    getUserProfile: function () {
      axios({
        // path('<int:user_id>/', views.profile, name='profile'),
        url: SERVER.URL + `/accounts/${this.userName}/`,
        method: 'get',
      })
      .then((res) => {
        this.userProfile = res.data
        // console.log(this.userProfile)
      })
    },
    updateFollowStatus: function () {
      const headers = this.config
      axios({
        // path('<int:user_pk>/follow/', views.follow, name='follow'),
        url: SERVER.URL + `/accounts/${this.userProfile.user_id}/follow/`,
        method: 'post',
        headers,
      })
      .then(() => {
        // const { likeCount } = res.data
        // this.likeCount = likeCount
        // this.likeStatus = liked
        this.getUserProfile()
      })
    },
    setReviewPages: function () {
      let numberOfPages = Math.ceil(this.userProfile.create_reviews.length / this.reviewsPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.reviewsPages.push(index)
      }
    },
    setArticlePages: function () {
      let numberOfPages = Math.ceil(this.userProfile.create_articles.length / this.articlesPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.articlesPages.push(index)
      }
    },
    reviewPaginate: function (reviews) {
      let reviewsPage = this.reviewsPage
      let reviewsPerPage = this.reviewsPerPage
      let from = (reviewsPage * reviewsPerPage) - reviewsPerPage;
      let to = (reviewsPage * reviewsPerPage)
      return reviews.slice(from, to)
    },
    articlePaginate: function (articles) {
      let articlesPage = this.articlesPage
      let articlesPerPage = this.articlesPerPage
      let from = (articlesPage * articlesPerPage) - articlesPerPage;
      let to = (articlesPage * articlesPerPage)
      return articles.slice(from, to)
    },
    deleteAccount: function () {
      const userId = this.userProfile.user_id
      const headers = this.config
      axios({
        // path('deleteaccount/<int:user_id>/', views.deleteaccount)
        url: SERVER.URL + `/accounts/deleteaccount/${userId}/`,
        method: 'delete',
        headers,
      })
      .then((res) => {
        const credentials = {
          username : res.data.username,
          password : res.data.password
        }
        this.logout(credentials)
        // this.$router.push({ name: 'MovieList' })
      })

    }
  },
  created: function () {
    this.getUserProfile()
  }
}
</script>

<style>

</style>