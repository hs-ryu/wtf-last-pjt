<template>
  <div>
    <tr>
      <td @click="goToReviewDetail">{{ review.title }}</td>
      <td>v</td>
      <td>{{ review.username }}</td>
    </tr>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    movieTitle: {
      type: String,
    }
  },
  methods: {
    goToReviewDetail: function () {
      const reviewId = this.review.id
      this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: reviewId }, query: { movieTitle: this.movieTitle}})
    }
  }

}
</script>

<style>

</style>