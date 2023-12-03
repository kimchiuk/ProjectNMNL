<template>
  <div class="total-box">
    <div class="topnav">
      <div class="id col-1">No.</div>
      <div class="title col-4">Title</div>
      <div class="content col-6">Content</div>
      <div class="detail col-6">Detail</div>
    </div>
    <div>
      <ReviewListItem
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import ReviewListItem from "@/components/ReviewListItem.vue";

const store = useCounterStore();
console.log(store.articles);
</script>

<style scoped>
.total-box {
  padding: 10px 30px;
}
.topnav {
  display: flex;
  flex-direction: row;
  border-bottom: 3px solid gray;
  padding: 20px 10px 10px 10px;
  font-weight: bolder;
}
.id title content {
  padding: 0px 20px;
}
</style>
