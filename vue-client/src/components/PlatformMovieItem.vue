<template>
  <div class="d-flex justify-content-center mb-1 ">
    <!-- <div class="card text-center mt-1 border-light">
      <div class="card-body p-0">
        <img :src="'http://image.tmdb.org/t/p/w200/' + platformMovie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
        <p class="card-title m-0" @click="goToDetail">{{ platformMovie.title }}</p>
      </div>
    </div> -->
    <div class="mb-1" @click="goToDetail">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0" >
          <div class="hover_effect_box hover_effect_1">
            <div class="content_bg" >
              <img :src="'http://image.tmdb.org/t/p/w200/' + platformMovie.poster_path" style="width: 200px;  height: 300px; object-fit: cover;  z-index: 0;" class="card-img-top rounded mx-auto d-block" alt="">
            </div>
            <div class="caption">
              <p class="caption_title">
                <br>
                {{ platformMovie.title }}
              </p>
              <div class="caption_desc">
                평점 : {{ platformMovie.rank_average.toFixed(1) }}<br>
                개봉일 : {{ platformMovie.release_date }}<br>
                <br>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PlatformMovieItem',
  props: {
    platformMovie: {
      type: Object,
    }
  },
  methods: {
    goToDetail: function () {
      const popularMovieId = this.platformMovie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: popularMovieId}})
    }
  }
}
</script>

<style>
/* .hover_effect_box { */
  /* width: 400px;
   overflow: hidden; */
  /* position: relative;
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
  padding: 10px; */
  /* background: rgba(0, 0, 0, 0.8); */
  /* margin: 20px 0 0 0;
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
.hover_effect_1:hover .content_bg { */
  /* -webkit-transform: scale(1.1,1.1);
  -moz-transform: scale(1.1,1.1);
  -o-transform: scale(1.1,1.1);
  -ms-transform: scale(1.1,1.1);
  transform: scale(1.1,1.1); */
/* }
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
} */
</style>