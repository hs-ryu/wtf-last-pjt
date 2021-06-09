<template>
  <div>
    <div style="max-width: 500px;" class="mx-auto">
      <img class="rounded" style="width: 100%" src="@/assets/404_page.jpg" alt="404-page">
      <h4 class="my-3 title-font">요청하신 페이지를 찾을 수 없습니다.</h4>
      <button @click="$router.push({ name: 'MovieList' })" class="my-3 btn btn-lg main-color-background text-white">메인으로 돌아가기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageNotFound',
}
</script>

<style>

</style>