<template>
  <div>
    <div class="aitem">
      <div class="articleid col-1">{{ article.id }}</div>
      <div class="articletitle col-4">{{ article.title }}</div>
      <div class="articlecontent col-6">{{ article.content }}</div>

      <RouterLink
        class="articledetail col-1"
        :to="{ name: 'detail', params: { id: article.id } }"
        :article="article"
      >
        보기
      </RouterLink>
      <hr />
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  article: Object,
});
</script>

<style scoped>
.aitem {
  display: flex;
  flex-direction: row;
  border: 1px solid white;
  font-weight: bolder;
}

.articleid {
  background-color: antiquewhite;
  text-align: center;
  padding: 10px 20px;
}
.articletitle {
  padding: 10px 20px;
}
.articlecontent {
  padding: 10px 20px;
}
.articledetail {
  text-align: left;
  padding: 10px 0px;
  text-decoration: none;
  color: blueviolet;
}
</style>
