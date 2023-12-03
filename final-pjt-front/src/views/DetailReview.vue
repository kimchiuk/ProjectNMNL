<template>
  <div class="total-box">
    <div class="article-box col-8">
      <form @submit="deleteReview()">
        <div v-if="article">
          <h3>{{ article.title }}</h3>
          <div class="info-box">
            <div class="like">
              <div
                v-show="like"
                @click="likeBtn(store.userInfo.pk, store.token)"
              >
                ❤
              </div>
              <div
                v-show="!like"
                @click="likeBtn(store.userInfo.pk, store.token)"
              >
                🤍
              </div>
            </div>
            <div>
              <p>
                {{ article.created_at.slice(0, 10) }}
                {{ article.created_at.slice(11, 19) }} 작성
              </p>
              <p>
                {{ article.updated_at.slice(0, 10) }}
                {{ article.updated_at.slice(11, 19) }} 수정
              </p>
            </div>
          </div>
          <h5>{{ article.content }}</h5>
        </div>
        <div class="btn-box" v-if="article?.user === store.userInfo.pk">
          <input class="btn btn-outline-danger" type="submit" value="삭제" />
          <RouterLink
            class="btn btn-outline-warning"
            :to="{
              name: 'update',
              query: { article: article?.title, content: article?.content },
            }"
            >수정</RouterLink
          >
        </div>
      </form>
    </div>

    <div class="comment-box col-4">
      <CommentList />
      <CreateComment />
      <div class="go-back">
        <button class="btn btn-outline-dark" @click="goBack">목록으로</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import CreateComment from "../components/CreateComment.vue";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter, RouterLink } from "vue-router";
import CommentList from "../components/CommentList.vue";
import { useLikeStore } from "../stores/like";

const props = defineProps({
  article: Object,
});

const store = useCounterStore();
const likeStore = useLikeStore();
const article = ref(null);
const route = useRoute();
const router = useRouter();
const like = ref(false);
const likes = ref(article?.likes);
const goBack = () => {
  router.push({ name: "reviews" });
};
const deleteReview = function () {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      alert("삭제되었습니다.");
      router.push({ name: "reviews" });
      // router.back()
    })
    .catch((err) => {
      console.log(err);
    });
};

const likeBtn = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data.status);
      console.log(store.articles);
      if (res.data.status === "unliked") {
        like.value = false;
      } else {
        like.value = true;
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      article.value = res.data;
      like.value = res.data.liked;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>
.total-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding: 50px;
}
.comment-box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
h3 {
  font-weight: bolder;
  border-bottom: 3px solid rgb(45, 67, 45);
}
p {
  color: gray;
  font-style: italic;
  padding: 0px 30px;
  margin: 10px 0px;
}
h5 {
  height: 300px;
  border: 1px solid lightgray;
  border-radius: 30px;
  margin: 20px;
  padding: 20px;
}
.btn-box {
  display: flex;
  justify-content: center;
}
.btn {
  margin: 5px;
}
.go-back {
  display: flex;
  justify-content: flex-end;
}
.info-box {
  display: flex;
  justify-content: space-between;
  padding: 0px 40px;
}
.like {
  margin: 5px;
  display: flex;
  justify-content: center;
  font-size: xx-large;
}
</style>
