const URL = process.env.VUE_APP_SERVER_URL

export default {
  URL,
  ROUTES: {
    signup: '/accounts/signup/',
    login: '/accounts/api-token-auth/',
    verify_user: '/accounts/verify-user/',
    getUserName: '/accounts/userinfo/',
    getAllMovies: '/movies/getmovies/',
    getPopularMovies: '/movies/getpopularmovies/',
    getNowShowing: '/movies/getnowshowing/',
    reviews: '/movies/',

    // 플랫폼 영화들
    getPlatformMovies: '/movies/',

    // 서치
    searchMovies: '/movies/searchmovies/',

    votes: '/movies/',
  }
}