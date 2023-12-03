<template>
  <div class="total">
    <div class="title-box">
      <h3>내 리뷰 수정하기</h3>
    </div>

    <div class="article-form">
      <form @submit.prevent="updateArticle">
        <div class="title">
          <label for="title">제목</label>
          <input
            class="form-control"
            type="text"
            id="title"
            v-model.trim="title"
          />
        </div>

        <div class="content">
          <label for="content">내용</label>
          <textarea
            class="form-control"
            id="content"
            v-model.trim="content"
          ></textarea>
        </div>
        <div class="btn-box">
          <button class="btn btn-outline-secondary" @click="goBack">
            취소
          </button>
          <input class="btn btn-outline-warning" type="submit" value="수정" />
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter, useRoute } from "vue-router";
import { useCounterStore } from "../stores/counter";
const route = useRoute();
const router = useRouter();

const store = useCounterStore();
const title = ref(route.query.article);
const content = ref(route.query.content);

const updateArticle = () => {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      router.push({ path: `/reviews/${route.params.id}` });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.total {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title-box {
  font-weight: bolder;
  border-bottom: 3px solid rgb(45, 67, 45);
  margin-top: 20px;
  padding: 10px;
}
h5 {
  font-size: x-large;
  font-weight: bolder;
}
.article-form {
  width: 800px;
  margin: 20px;
  padding: 40px;
  border: 5px double gray;
  border-radius: 30px;
}
.title {
  display: flex;
  flex-direction: column;
  margin: 20px;
}
.content {
  display: flex;
  flex-direction: column;
  margin: 20px;
}
.btn-box {
  display: flex;
  justify-content: center;
}
.btn {
  margin: 0px 5px;
}
textarea {
  height: 300px;
}
label {
  font-weight: bold;
  font-style: italic;
  margin: 5px;
}
.form-control {
  color: lightgray;
}
</style>
