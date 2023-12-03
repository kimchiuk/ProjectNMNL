<template>
  <div class="total">
    <div class="title-box">
      <h5>금융 상품에 대한 리뷰를 작성해보세요 !!</h5>
    </div>
    <div class="article-form">
      <form @submit.prevent="createArticle">
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
          <input class="btn btn-outline-warning" type="submit" value="동록" />
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useCounterStore } from "../stores/counter";

const store = useCounterStore();
const title = ref("");
const content = ref("");

const router = useRouter();

const createArticle = () => {
  axios({
    method: "POST",
    url: "http://127.0.0.1:8000/api/v1/articles/",
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
      router.push({ name: "reviews" });
    })
    .catch((err) => {
      console.log(err);
    });
};

// 뒤로 가기 함수
const goBack = () => {
  router.push({ name: "reviews" });
};
</script>

<style scoped>
.total {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title-box {
  width: 80%;
  border-bottom: 5px solid lightgray;
  padding: 20px;
  margin: 10px 40px;
}
h5 {
  font-size: x-large;
  font-weight: bolder;
}
.article-form {
  width: 800px;
  margin: 20px;
  padding: 40px;
  border: 5px double lightgray;
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
</style>
