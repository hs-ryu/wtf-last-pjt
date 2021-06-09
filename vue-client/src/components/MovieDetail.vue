<template>
  <div style="text-align: center">
    <!-- {{ movie }} -->
    <h1 class="m-4 title-font dark-mode-content">{{ movie.title }}</h1>
    <div class="d-flex justify-content-center align-items-center">
      <div class="img-container">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
      </div>
      <div class="mx-4" style="width: 500px; text-align: left;">
        
        <div class="video-container" v-if="movie.trailer">
          <iframe width="560" height="315" class="m-2" :src="'https://www.youtube.com/embed/' + movie.trailer" frameborder="0" allowfullscreen></iframe>
        </div>
        <br>

        <p style="font-size: 14px;" class="dark-mode-content">{{ movie.overview }}</p>
        <span class="dark-mode-content">개봉일: {{ movie.release_date }} / 장르: </span>
        <span v-for="(genre, idx) in genres" :key="'genre'+ idx">
          <span class="dark-mode-content"> {{ genre }}</span>
        </span>
        <p class="dark-mode-content">평점: {{ movie.rank_average.toFixed(1) }}⭐</p>
        <div class="d-inline" v-if="isLoggedIn">
          <button class="btn d-inline" v-if="movie.like_users && movie.like_users.includes(decoded.user_id)" @click="getLikeStatus"><i class="fas fa-heart fa-lg " style="color:#CE93D8;"></i></button>
          <button class="btn d-inline" v-else @click="getLikeStatus"><i class="far fa-heart fa-lg" style="color:#CE93D8;"></i></button>
        </div>
        <div class="d-inline" v-else>
          <i class="d-inline fas fa-heart fa-lg" style="color:#CE93D8;"></i>
        </div>
        <p class="d-inline dark-mode-content" >{{ movie.like_users.length }}명이 이 영화를 좋아합니다.</p>
        <div class="d-flex">
          <div v-if="netflix" class="m-1" style="max-width: 35px; ">
            <a v-if="netflix" :href="netflix" target="_blank"><img img class="rounded" style="width: 100%" src="@/assets/netflix_logo.png" alt="netflix logo"></a>
          </div>
          <div v-if="watcha" class="m-1" style="max-width: 35px;">
            <a v-if="watcha" :href="watcha" target="_blank"><img img class="rounded" style="width: 100%" src="@/assets/watcha_logo.png" alt="watcha logo"></a>
          </div>
          <div v-if="wavve" class="m-1" style="max-width: 35px;">
            <a v-if="wavve" :href="wavve" target="_blank"><img img class="rounded" style="width: 100%" src="@/assets/wavve_logo.png" alt="wavve logo"></a>
          </div>
          <div v-if="naver" class="m-1" style="max-width: 35px;">
            <a v-if="naver" :href="naver" target="_blank"><img class="rounded" style="width: 100%" src="@/assets/naver_logo.png" alt="naver logo"></a>
          </div>
        </div>

      </div>
    </div>
      <hr>
    
    <!-- <div style="width: 1000px;" class="mx-auto">
      <div class="m-2" v-if="reviews.length">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">글 제목</th>
              <th scope="col">평점</th>
              <th scope="col">작성자</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(review, idx) in reviews" :key="idx +'1'">
              <td @click="goToReviewDetail(review.id)" v-if="review.title.length > 15">{{ review.title.substr(0,15) + '...'}}</td>
              <td @click="goToReviewDetail(review.id)" v-else>{{ review.title }}</td>
              <td>{{ review.rank }}</td>
              <td>{{ review.username }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="m-5" v-else>
        <p>리뷰가 아직 없어요. 첫번째 글을 쓸 수 있는 절호의 찬스! 🤘</p>
      </div>
      <div class="d-flex justify-content-center">
        <button class="mx-2 btn main-color-background text-white" @click="goToCreateReview">리뷰 작성하기</button>
      </div>
    </div> -->

    <!-- <hr>
    <div style="width: 1000px;" class="mx-auto">
      <div class="m-2" v-if="votes.length">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">제목</th>
              <th scope="col">당신의 선택은?</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(vote, idx) in votes" :key="idx +'2'">
              <td @click="goToVoteDetail(vote.id)" v-if="vote.title.length > 15">{{ vote.title.substr(0,15) + '...' }}</td>
              <td @click="goToVoteDetail(vote.id)" v-else>{{ vote.title }}</td>
              <td v-if="vote.option_one.length + vote.option_two.length > 20">{{ vote.option_one.substr(0,10) + '...' }}   VS   {{ vote.option_two.substr(0,10) + '...' }}</td>
              <td v-else>{{ vote.option_one }}   VS   {{ vote.option_two }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="m-5" v-else>
        <p>투표가 아직 없어요. 첫번째 투표를 등록해 보세요! 🤘</p>
      </div>
      <div class="d-flex justify-content-center">
        <button class="mx-2 btn main-color-background text-white" @click="goToCreateVote">투표 만들기</button>
      </div>
      <button style="border-color: #CE93D8" class="my-2 btn main-color-content" @click="$router.push({ name: 'MovieList' })">목록</button>
    </div> -->

    <!-- <button style="border-color: #CE93D8" class="my-2 btn main-color-content" @click="$router.push({ name: 'MovieList' })">목록</button> -->
    <div style="width: 1000px; height: 400px;" class="mx-auto">
      <div class="my-2 d-flex justify-content-around">
        <div>
          <h3 class="fw-bold title-font dark-mode-content" style="text-align: left;">리뷰 목록</h3>
          <div class="m-2" style="height: 250px;" v-if="reviews.length">
            <table style="width: 450px;" class="table table-hover content-font">
              <thead>
                <tr>
                  <th scope="col" class="dark-mode-content">글제목</th>
                  <th scope="col" class="dark-mode-content">평점</th>
                  <th scope="col" class="dark-mode-content">작성자</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(review, idx) in displayReviews" :key="idx +'1'">
                  <td class="mini-button dark-mode-content" @click="goToReviewDetail(review.id)" v-if="review.title.length > 15">{{ review.title.substr(0,15) + '...'}}</td>
                  <td class="mini-button dark-mode-content" @click="goToReviewDetail(review.id)" v-else>{{ review.title }}</td>
                  <!-- <td>{{ review.rank }}</td> -->
                  <td v-if="review.rank === 0.5"><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 1"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 1.5"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 2"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 2.5"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 3"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 3.5"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 4"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else-if="review.rank === 4.5"><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star-half star fa-la" style="color:#CE93D8;"></i></td>
                  <td v-else><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i><i class="fas fa-star star fa-la" style="color:#CE93D8;"></i></td>
                  <td class="dark-mode-content">{{ review.username }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-else class="my-5 dark-mode-content">
            <p>리뷰가 아직 없어요. 첫번째 글을 쓸 수 있는 절호의 찬스! 🤘</p>
          </div>
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link" v-if="reviewsPage != 1" @click="reviewsPage--"> Previous </button>
              </li>
              <li class="text-dark page-item" v-for="(pageNumber,idx) in reviewsPages.slice(reviewsPage-1, reviewsPage+5)" :key=idx>
                <button type="button" class="text-dark page-link"  @click="page=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="reviewsPage++" v-if="reviewsPage < reviewsPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
          <div class="d-flex justify-content-center">
            <button v-if="reviewExist" class="mx-2 btn btn-sm main-color-background text-white" @click="$router.push({ name: 'ReviewDetail', params: { movieId: movie.id, reviewId: reviewExist }, query: { moviePosterPath: movie.poster_path, movieTitle: movie.title } })">내 리뷰 보러가기</button>
            <button v-else class="mx-2 btn btn-sm main-color-background text-white" @click="goToCreateReview">리뷰 작성하기</button>
          </div>
        </div>
        
        <div class="dark-mode-content">
          <h3 class="fw-bold title-font" style="text-align: left;">투표 목록</h3>
          <div class="m-2" style="height: 250px;" v-if="votes.length">
            <table style="width: 450px;" class="table table-hover content-font">
              <thead>
                <tr>
                  <th scope="col" class="dark-mode-content">제목</th>
                  <th scope="col" class="dark-mode-content">당신의 선택은?</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(vote, idx) in displayVotes" :key="idx +'2'">
                  <td class="mini-button dark-mode-content" @click="goToVoteDetail(vote.id)" v-if="vote.title.length > 15">{{ vote.title.substr(0,15) + '...' }}</td>
                  <td class="mini-button dark-mode-content" @click="goToVoteDetail(vote.id)" v-else>{{ vote.title }}</td>
                  <td class="dark-mode-content" v-if="vote.option_one.length + vote.option_two.length > 20">{{ vote.option_one.substr(0,10) + '...' }}   VS   {{ vote.option_two.substr(0,10) + '...' }}</td>
                  <td v-else class="dark-mode-content">{{ vote.option_one }}   VS   {{ vote.option_two }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-else class="my-5">
            <p class="dark-mode-content">투표가 아직 없어요. 첫번째 투표를 등록해 보세요! 🤘</p>
          </div>
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link dark-mode-content" v-if="votesPage != 1" @click="votesPage--"> Previous </button>
              </li>
              <li class="page-item dark-mode-content" v-for="(pageNumber,idx) in votesPages.slice(votesPage-1, votesPage+5)" :key=idx>
                <button type="button" class="text-dark page-link dark-mode-content"  @click="votesPage=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="votesPage++" v-if="votesPage < votesPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
          <div class="d-flex justify-content-center">
            <button class="mx-2 btn btn-sm main-color-background text-white" @click="goToCreateVote">투표 만들기</button>
          </div>
        </div>
      </div>
    </div>

    <button style="border-color: #CE93D8" class="custom-button-reverse my-2 btn main-color-content" @click="$router.push({ name: 'MovieList' })">목록</button>
      
  
  
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

// import ReviewItem from '@/components/ReviewItem'

export default {
  name: 'MovieDetail',
  components: {
    // ReviewItem
  },
  data: function () {
    return {
      movie: {},
      movieId: this.$route.params.movieId,
      netflix: '',
      watcha: '',
      wavve: '',
      naver: '',
      reviews: [],
      votes: [],
      genres: [],

      reviewsPage: 1,
      votesPage: 1,
			reviewsPerPage: 5,
			votesPerPage: 5,
			reviewsPages: [],	
			votesPages: [],	
    }
  },
  watch: {
    Reviews () {
      this.setReviewPages()
    },
    Votes () {
      this.setVotePages()
    }
  },
  computed: {
    ...mapGetters([
      'config',
      'isLoggedIn',
    ]),
    ...mapState([
      'userId',
      'decoded',
    ]),
    displayReviews () {
      return this.reviewPaginate(this.reviews)
    },
    displayVotes () {
      return this.votePaginate(this.votes)
    },
    Reviews () {
      return this.reviews
    },
    Votes () {
      return this.votes
    },
    reviewExist: function () {
      const result = this.displayReviews.find((review) => {
        return review.username === this.decoded.username
      })
      if (result){
        return result.id
      }
      else {
        return false
      }
    },
  },
  methods: {
    getMovieDetail: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies + `${this.movieId}/`,
        method: 'get',
      })
      .then((res) => {
        this.movie = res.data
        this.netflix = res.data.netflix
        this.watcha = res.data.watcha
        this.wavve = res.data.wavve
        this.naver = res.data.naver
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviews: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/`,
        method: 'get',
      })
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },


    setReviewPages: function () {
      let numberOfPages = Math.ceil(this.reviews.length / this.reviewsPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.reviewsPages.push(index)
      }
    },
    setVotePages: function () {
      let numberOfPages = Math.ceil(this.votes.length / this.votesPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.votesPages.push(index)
      }
    },
    reviewPaginate: function (reviews) {
      let reviewsPage = this.reviewsPage
      let reviewsPerPage = this.reviewsPerPage
      let from = (reviewsPage * reviewsPerPage) - reviewsPerPage
      let to = (reviewsPage * reviewsPerPage)
      return reviews.slice(from, to)
    },
    votePaginate: function (votes) {
      let votesPage = this.votesPage
      let votesPerPage = this.votesPerPage
      let from = (votesPage * votesPerPage) - votesPerPage
      let to = (votesPage * votesPerPage)
      return votes.slice(from, to)
    },

    goToCreateReview: function () {
      const movieTitle = this.movie.title
      const moviePosterPath = this.movie.poster_path
      // console.log(moviePosterPath)
      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'CreateReview', params: { movieId: this.movieId }, query: { movieTitle: movieTitle, moviePosterPath: moviePosterPath }})
      }
    },

    getLikeStatus: function () {
      const headers = this.config
      axios({
        // 'getmovies/<int:movie_pk>/likes/
        url: SERVER.URL + `/movies/getmovies/${this.movieId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        this.getMovieDetail()
      })
    },
    goToReviewDetail: function (reviewId) {
      const movieTitle = this.movie.title
      const moviePosterPath = this.movie.poster_path
      // console.log(moviePosterPath)

      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: reviewId }, query: { movieTitle: movieTitle, moviePosterPath: moviePosterPath }})
      }
      // console.log(movieTitle)
    },

    // 굳!!!!
    getVotes: function () {
      // path('<int:movie_pk>/votes/', views.getallvotes, name='getallvotes'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/`,
        method: 'get',
      })
      .then((res) => {
        this.votes = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToVoteDetail: function (voteId) {
      const movieId = this.movieId
      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'VoteDetail', params: { movieId: movieId, voteId: voteId }, query: { movieTitle: this.movie.title }})
      }
      // console.log(movieId)
    },
    goToCreateVote: function () {
      if (! this.isLoggedIn) {
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'Login' })
      } else {
        this.$router.push({ name: 'CreateVote', params: { movieId: this.movieId }, query: { movieTitle: this.movie.title }})
      }
    },
    getGenreList: function () {
      axios({
        // 'getgenre/<int:movie_pk>/'
        url: SERVER.URL + '/movies/getgenre/' + `${this.movieId}/`,
        method: 'get',
      })
      .then((res) => {
        this.genres = res.data.genres
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.getMovieDetail()
    this.getReviews()
    this.getVotes()
    this.getGenreList()
  }

}
</script>

<style>

.star {
  color : gold;
}

.img-container {
  max-width: 380px;
}
img {
  width: 100%;
}
.video-container {
  position: relative;
  height: 0;
  padding-bottom: 56.25%;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>