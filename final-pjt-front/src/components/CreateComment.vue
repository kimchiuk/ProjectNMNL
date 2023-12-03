<template>
  <div>
    <form @submit.prevent="createComment">
      <div class="input-group mb-3">
        <input class="form-control" type="text" v-model.trim="content" />
        <input
          class="btn btn-outline-secondary"
          type="submit"
          value="댓글쓰기"
        />
      </div>
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from "../stores/counter";
import { onMounted, onUpdated, ref } from "vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";

const content = ref("");
const store = useCounterStore();
const route = useRoute();
const router = useRouter();

const createComment = function (payload) {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/articles/comments/${route.params.id}/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      content.value = res.data.content;
      router.go();
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
