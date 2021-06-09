<template>
  <div>
    
    <div style="max-width: 300px;" class="mx-auto">
      <img style="width: 100%" src="@/assets/logo_main.png" alt="main-logo">
    </div>

    <div class="d-flex justify-content-center mb-4">
      <input @input="fetchMovies" class="form-control m-3" style="width: 700px;" type="search" placeholder="보고싶은 영화를 검색해주세요" aria-label="Search">
    </div>
    <div v-if="inputValue">
      <div class="mx-auto" style="width: 1000px; height: 1000px;">
        <div v-if="searchMovies.length">
          <div class="card-group row row-cols-6">
            <SearchMovieItem
              v-for="(searchMovie, idx) in searchMovies"
              :key="idx + '0'"
              :searchMovie="searchMovie"
            />
          </div>
        </div>
        <div v-else style="height: 100px;">
          <h5 class="my-4 dark-mode-content">검색 결과가 존재하지 않습니다.</h5>
        </div>
      </div>
    </div>
    <div v-else>


      <div class="mx-auto" style="width: 1000px;">
        <div class="d-flex justify-content-between">
          <h4 class="title-font d-inline" style="text-align: left;">{{ platformvalue.charAt(0).toUpperCase() + platformvalue.slice(1)}} 상영 영화</h4>
          <div class="d-flex align-items-end title-font">
            <p class="mini-button" :class="{'d-inline mx-3 mb-1 div2 black': !clickedOne, 'd-inline mx-3 mb-1 div2 gray dark-mode-text' : clickedOne}" @click="setPlatform('netflix')">Netflix</p>
            <p class="mini-button" :class="{'d-inline mx-3 mb-1 div2 black': !clickedTwo, 'd-inline mx-3 mb-1 div2 gray dark-mode-text' : clickedTwo}" @click="setPlatform('watcha')">Watcha</p>
            <p class="mini-button" :class="{'d-inline mx-3 mb-1 div2 black': !clickedThree, 'd-inline mx-3 mb-1 div2 gray dark-mode-text' : clickedThree}" @click="setPlatform('wavve')">Wavve</p>
            <p class="mini-button" :class="{'d-inline mx-3 mb-1 div2 black': !clickedFour, 'd-inline mx-3 mb-1 div2 gray dark-mode-text' : clickedFour}" @click="setPlatform('naver')">Naver</p>
          </div>
        </div>
        <swiper class="swiper" :options="swiperOption">
          <PlatformMovieItem2
          v-for="(platformMovie, idx) in platformMovies"
          :key="idx + 'platform'"
          :platformMovie="platformMovie"
          class="hover_effect_box hover_effect_1"
          />
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
        <br>


        <h4 class="title-font" style="text-align: left;">{{ today.getHours() }}시의 인기 영화</h4>
        <swiper class="swiper" :options="swiperOption">
          <PopularMovieItem2
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '9'"
          :popularMovie="popularMovie"
          class="hover_effect_box hover_effect_1"
          />
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
        <br>


        <h4 class="title-font" style="text-align: left;">Now Showing</h4>
        <!-- <p>{{ nowShowingMovies }}</p> -->
        <swiper class="swiper" :options="swiperOption">
          <NowShowingItem2
            v-for="(nowShowingMovie, idx) in nowShowingMovies"
            :key="idx + '8'"
            :nowShowingMovie="nowShowingMovie"
            class="hover_effect_box hover_effect_1"
          />
          <!-- <div class="swiper-pagination" slot="pagination"></div> -->
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
        <br>
        

        
        <!-- <h2>전체영화목록</h2> -->
        <h4 class="title-font" style="text-align: left;">전체 영화 목록</h4>
        <div class="d-flex justify-content-center card-group row row-cols-6">
          <MovieItem
            v-for="(movie, idx) in allMovies"
            :key="idx + '3'"
            :movie="movie"
          />
        </div>
      </div>


      <!-- 원래 nowshowing -->
      <!-- <div class="card-group">
        <NowShowingItem
          v-for="(nowShowingMovie, idx) in nowShowingMovies"
          :key="idx + '1'"
          :nowShowingMovie="nowShowingMovie"
        />
      </div> -->
      <!-- <h2>{{ today.getHours() }}시의 인기영화</h2> -->
      <!-- <p>{{ popularMovies }}</p> -->
      <!-- <div class="card-group">
        <PopularMovieItem
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '2'"
          :popularMovie="popularMovie"
        />
      </div> -->
      <!-- 플랫폼상영 -->
      <!-- <h2>현재 {{ platformvalue }}에서 상영중인 영화입니다</h2> -->
      <!-- <div>
        <div>
          <p class="d-inline mx-3" @click="setPlatform('netflix')">netflix</p>
          <p class="d-inline mx-3" @click="setPlatform('watcha')">watcha</p>
          <p class="d-inline mx-3" @click="setPlatform('wavve')">wavve</p>
          <p class="d-inline mx-3" @click="setPlatform('naver')">naver</p>
        </div>
      </div> -->
      <!-- <div class="card-group">
        <PlatformMovieItem
          v-for="(platformMovie, idx) in platformMovies"
          :key="idx + '3'"
          :platformMovie="platformMovie"
        />
      </div> -->
      


      <!-- <h2>전체영화목록</h2> -->
      <!-- <div class="card-group">
        <MovieItem
          v-for="(movie, idx) in allMovies"
          :key="idx + '3'"
          :movie="movie"
        />
      </div> -->
    </div>
      
  </div>
</template>
<script>
import MovieItem from '@/components/MovieItem'
// import PopularMovieItem from '@/components/PopularMovieItem'
import PopularMovieItem2 from '@/components/PopularMovieItem2'
// import NowShowingItem from '@/components/NowShowingItem'
import NowShowingItem2 from '@/components/NowShowingItem2'
import SearchMovieItem from '@/components/SearchMovieItem'
// import PlatformMovieItem from '@/components/PlatformMovieItem'
import PlatformMovieItem2 from '@/components/PlatformMovieItem2'
import { mapActions, mapState, mapGetters } from 'vuex'
// SwiperSlide 
import { Swiper } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'


export default {
  name: 'MovieList',
  components: {
    MovieItem,
    // PopularMovieItem,
    PopularMovieItem2,
    // NowShowingItem,
    NowShowingItem2,
    SearchMovieItem,
    // PlatformMovieItem,
    PlatformMovieItem2,
    Swiper,
    // SwiperSlide,
  },
  data: function () {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 0,
        slidesPerGroup: 4,
        loopedSlides: 6,
        // autoplay: {
        //   delay: 6000,
        //   waitForTransition: true,
        // },
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        }
      },
    }
  },
  methods: {
    ...mapActions([
      'getAllMovies',
      'getPopularMovies',
      'getNowShowing',
      'fetchMovies',
      'getPlatformMovies',
      'setPlatform',
      'resetInputValue',
    ]),
  },
  computed: {
    ...mapState([
      'allMovies',
      'popularMovies',
      'nowShowingMovies',
      'searchMovies',
      'inputValue',
      'platformMovies',
      'platformvalue',
      'today',
      'clickedOne',
      'clickedTwo',
      'clickedThree',
      'clickedFour',
    ]),
    ...mapGetters([
      'movieLength',
      'inputLength',
    ])
  },
  created: function () {
    this.getNowShowing()
    this.getAllMovies()
    this.getPopularMovies()
    this.getPlatformMovies(this.platformvalue)
    this.resetInputValue()
    console.log(this.inputValue)
  },
}
</script>

<style lang="scss" scoped>
  // @import './base.scss';
  .black {
    color: rgb(201, 195, 195);
  }
  .gray {
    color: rgb(0, 0, 0);
  }
  .row {
    --bs-gutter-x: 0 !important; 
  }
  .hover_effect_box {
  width: 400px;
  overflow: hidden;
  position: relative;
  text-align: center;
  -webkit-box-shadow: 1px 1px 2px #e6e6e6;
  -moz-box-shadow: 1px 1px 2px #e6e6e6;
  box-shadow: 1px 1px 2px #e6e6e6;
  cursor: default;
  background: rgb(255, 255, 255);
  box-sizing: initial;
}
.hover_effect_box .caption {
  width: 200px;
  height: 300px;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
}
.hover_effect_box .content_bg {
  display: block;
  position: relative;
}
.hover_effect_box .caption_title {
  text-transform: uppercase;
  color: #fff;
  text-align: center;
  position: relative;
  font-size: 22px;
  font-weight: bold;
  padding: 10px;
  /* background: rgba(0, 0, 0, 0.8); */
  margin: 20px 0 0 0;
}
.hover_effect_box .caption_desc {
    font-size: 0.9em;
    font-weight: bold;
    line-height: 1.5;
    position: relative;
    color: #fff;
    padding: 30px 20px 40px;
    text-align: center;
}
.hover_effect_box .caption_link {
  display: inline-block;
  text-decoration: none;
  padding: 7px 14px;
  background: #000;
  color: #fff;
  text-transform: uppercase;
  -webkit-box-shadow: 0 0 1px #000;
  -moz-box-shadow: 0 0 1px #000;
  box-shadow: 0 0 1px #000;
}
.hover_effect_box .caption_link:hover {
  -webkit-box-shadow: 0 0 5px #000;
  -moz-box-shadow: 0 0 5px #000;
  box-shadow: 0 0 5px #000;
}

.hover_effect_1 .content_bg {
  -webkit-transition: all 0.2s linear;
  -moz-transition: all 0.2s linear;
  -o-transition: all 0.2s linear;
  -ms-transition: all 0.2s linear;
  transition: all 0.2s linear;
}
.hover_effect_1 .caption {
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
  opacity: 0;
  background-color: rgba(66, 63, 58, 0.7);
  -webkit-transition: all 0.4s ease-in-out;
  -moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -ms-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
}
.hover_effect_1 .caption_title {
  -webkit-transform: translateY(-100px);
  -moz-transform: translateY(-100px);
  -o-transform: translateY(-100px);
  -ms-transform: translateY(-100px);
  transform: translateY(-100px);
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
  opacity: 0;
  -webkit-transition: all 0.2s ease-in-out;
  -moz-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  -ms-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
.hover_effect_1 .caption_desc {
  -webkit-transform: translateY(100px);
  -moz-transform: translateY(100px);
  -o-transform: translateY(100px);
  -ms-transform: translateY(100px);
  transform: translateY(100px);
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
  opacity: 0;
  -webkit-transition: all 0.2s linear;
  -moz-transition: all 0.2s linear;
  -o-transition: all 0.2s linear;
  -ms-transition: all 0.2s linear;
  transition: all 0.2s linear;
}
.hover_effect_1:hover .content_bg {
  // -webkit-transform: scale(1.1,1.1);
  // -moz-transform: scale(1.1,1.1);
  // -o-transform: scale(1.1,1.1);
  // -ms-transform: scale(1.1,1.1);
  // transform: scale(1.1,1.1);
}
.hover_effect_1 .caption_link {
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
  opacity: 0;
  -webkit-transition: all 0.2s ease-in-out;
  -moz-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  -ms-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
.hover_effect_1:hover .caption {
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=100)";
  filter: alpha(opacity=100);
  opacity: 1;
}
.hover_effect_1:hover .caption_title,
.hover_effect_1:hover .caption_desc,
.hover_effect_1:hover .caption_link {
  -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=100)";
  filter: alpha(opacity=100);
  opacity: 1;
  -webkit-transform: translateY(0px);
  -moz-transform: translateY(0px);
  -o-transform: translateY(0px);
  -ms-transform: translateY(0px);
  transform: translateY(0px);
}
.hover_effect_1:hover .caption_desc {
  -webkit-transition-delay: 0.1s;
  -moz-transition-delay: 0.1s;
  -o-transition-delay: 0.1s;
  -ms-transition-delay: 0.1s;
  transition-delay: 0.1s;
}
.hover_effect_1:hover .caption_link {
  -webkit-transition-delay: 0.2s;
  -moz-transition-delay: 0.2s;
  -o-transition-delay: 0.2s;
  -ms-transition-delay: 0.2s;
  transition-delay: 0.2s;
}

.swiper-button-prev {
  color: white;
  opacity: 0.5;
}

.swiper-button-next {
  color: white;
  opacity: 0.5;
}
</style>