<template>
  <div>
    <div class="top-box">
      <h2>💬 리뷰 게시판</h2>
      <RouterLink :to="{ name: 'create' }" class="btn btn-outline-success"
        >리뷰 작성하기</RouterLink
      >
    </div>
    <ReviewList />
  </div>
</template>

<script setup>
import ReviewList from "../components/ReviewList.vue";
import { onMounted, ref } from "vue";
import axios from "axios";
import { useCounterStore } from "../stores/counter";

const store = useCounterStore();

onMounted(() => {
  store.getArticles();
});
</script>

<style scoped>
h2 {
  height: 100px;
  display: flex;
  align-items: flex-end;
  padding: 20px;
  font-weight: bolder;
  margin: 0px;
}
.top-box {
  display: flex;
  border-bottom: 2px solid lightgray;
  align-items: baseline;
}
.btn {
  margin: 0px 10px;
}
</style>
