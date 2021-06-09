<template>
  <div>
    <!-- 원래 코드 -->
    <!-- <img :src="'http://image.tmdb.org/t/p/w200/' + popularMovie.poster_path" alt="" @click="goToDetail">
    <h3 @click="goToDetail">{{ popularMovie.title }}</h3>
    <p>{{ popularMovie.content }}</p> -->

    <div class="mb-1" @click="goToDetail">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0" >
          <div class="hover_effect_box hover_effect_1">
            <div class="content_bg" >
              <img :src="'http://image.tmdb.org/t/p/w200/' + popularMovie.poster_path" style="width: 200px;  height: 300px; object-fit: cover;  z-index: 0;" class="card-img-top rounded mx-auto d-block" alt="">
            </div>
            <div class="caption">
              <p class="caption_title">
                <br>
                {{ popularMovie.title }}
              </p>
              <div class="caption_desc">
                평점 : {{ popularMovie.rank_average.toFixed(1) }}<br>
                개봉일 : {{ popularMovie.release_date }}<br>
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
  name: 'PopularMovieItem',
  props: {
    popularMovie: {
      type: Object,
    }
  },
  methods: {
    goToDetail: function () {
      const popularMovieId = this.popularMovie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: popularMovieId}})
    }
  }

}
</script>

<style>

</style>