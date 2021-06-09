import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/components/MovieDetail'
import ReviewDetail from '@/views/reviews/ReviewDetail'
import CreateReview from '@/views/reviews/CreateReview'
import UpdateReview from '@/views/reviews/UpdateReview'
import ArticleList from '@/views/community/ArticleList'
import ArticleDetail from '@/components/ArticleDetail'
import UpdateArticle from '@/views/community/UpdateArticle'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import CreateArticle from '@/views/community/CreateArticle'
import Profile from '@/views/accounts/Profile'
import VoteDetail from '@/views/votes/VoteDetail'
import CreateVote from '@/views/votes/CreateVote'
import PageNotFound from '@/components/PageNotFound'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movie/:movieId/reviews/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/movie/:movieId/reviews/create',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/movie/:movieId/reviews/:reviewId/update',
    name: 'UpdateReview',
    component: UpdateReview
  },
  {
    path: '/community',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/community/articles/create',
    name: 'CreateArticle',
    component: CreateArticle,
  },
  {
    path: '/community/articles/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/community/articles/:articleId/update',
    name: 'UpdateArticle',
    component: UpdateArticle
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile/:username',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/movies/:movieId/vote/:voteId',
    name: 'VoteDetail',
    component: VoteDetail,
  },
  {
    path: '/movies/:movieId/votes/create',
    name: 'CreateVote',
    component: CreateVote,
  },
  {
    path: '*',
    redirect: '/404'
  },
  {
    path: '/404',
    component: PageNotFound,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

router.beforeEach((to, from, next) => {
  //1-1. 로그인이 필요한 컴포넌트
  const authPages = [
    'ArticleDetail', 
    'AricleComment',
    'ReviewComment',
    'CreateArticle',
    'UpdateArticle',
    'CreateReview',
    'ReviewDetail',
    'UpdateReview',
    'VoteDetail',
    'CreateVote',
  ]
  //1-2. 로그아웃이 필요한 컴포넌트(로그인 상태가 아닌 경우에 방문해야 하는 컴포넌트)
  // const publicPages = [
  //   'Login', 
  //   'Signup',
  // ]

  //2. 
  // 가려고 하는 곳(to)이 로그인이 필요한 곳인지 여부를 체크
  const authRequired = authPages.includes(to.name)
  // 가려고 하는 곳이 로그인이 필요하지 않은 곳은지 여부를 체크
  // const authNotRequired = publicPages.includes(to.name)
  // 로그인이 되어있는지 여부를 체크하자 -> true / false
  const isLoggedIn = localStorage.getItem('jwt') ? true : false


  //3. 
  //3-1. 만약 로그인이 필요한 컴포넌트인데 로그인이 안되어 있는 경우에 강제로 가려고 하면?
  if (authRequired && !isLoggedIn) {
    // 로그인을 할 수 있도록 (가드) -> Login 컴포넌트로 보내자
    next({ name: 'Login' })
  //3-2. 만약 로그인이 필요하지 않은 컴포넌트인데 로그인이 되어있는 상태에서 강제로 가려고 하면?
  } 
  // else if (authNotRequired && isLoggedIn) {
  //   next({ name: 'MovieList' })
  // //3-3. 전부 아니라면
  // } 
  else {
    // 가던 길을 가자
    next()
  }
})