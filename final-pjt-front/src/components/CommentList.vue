<template>
  <div>
    <div v-for="comment in comments" :key="comment.id">
      <div class="card w-60 mb-1">
        <span class="card-body" v-if="!comment.updated"
          ><form @submit="switchComment(comment.id)">
            <div class="comment-box">
              <span class="card-body">{{ comment.content }}</span
              ><br />
            </div>
            <div class="btn-box">
              <div>
                <span class="time"
                  >{{ comment.created_at.slice(0, 10) }}
                  {{ comment.created_at.slice(11, 19) }}</span
                >
              </div>
              <div v-show="comment.user === store.userInfo.pk">
                <input
                  class="btn btn-light btn-sm"
                  type="submit"
                  value="수정"
                />
                <input
                  class="btn btn-light btn-sm"
                  @click="deleteComment(comment.id)"
                  type="submit"
                  value="삭제"
                />
              </div>
            </div>
          </form>
        </span>

        <span class="card-body" v-else>
          <form
            @submit.prevent="
              switchComment(comment.id),
                updateComment(comment.id, comment.content)
            "
          >
            <div class="comment-box">
              <input
                class="card-body"
                type="text"
                v-model="comment.content"
              /><br />
            </div>
            <div class="btn-box">
              <div>
                <span class="time"
                  >{{ comment.created_at.slice(0, 10) }}
                  {{ comment.created_at.slice(11, 19) }}</span
                >
              </div>
              <div v-show="comment.user === store.userInfo.pk">
                <input
                  class="btn btn-light btn-sm"
                  type="submit"
                  value="완료"
                />
                <input
                  class="btn btn-light btn-sm"
                  @click="deleteComment(comment.id)"
                  type="submit"
                  value="삭제"
                />
              </div>
            </div>
          </form>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "../stores/counter";
import { useRoute } from "vue-router";
import { onMounted, onUpdated, ref, watch, nextTick } from "vue";
import axios from "axios";
const store = useCounterStore();
const route = useRoute();
const comments = ref([]);
// const content = ref("");

const switchComment = function (id) {
  // updatecontent.value = !updatecontent.value;
  comments.value = comments.value.map((comment) => {
    if (comment.id === id) {
      comment.updated = !comment.updated;
    }
    return comment;
  });
};

const fetchComments = () =>
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1/articles/comments/${route.params.id}`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      comments.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });

const deleteComment = function (id) {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/api/v1/articles/comment/${id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      // console.log(res.data);
      fetchComments();
    })
    .catch((err) => {
      console.log(err);
    });
};

const updateComment = function (id, content) {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/api/v1/articles/comment/${id}/`,
    data: {
      content,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      nextTick(() => fetchComments());
      // switchComment();
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  fetchComments();
});
</script>

<style scoped>
.card-body {
  display: flex;
  flex-direction: column;
  padding: 0px 5px;
}
.comment-box {
  display: flex;
  align-items: end;
  padding: 5px;
}
.btn-box {
  display: flex;
  justify-content: space-between;
  margin: 3px;
}
.time {
  font-size: small;
  color: lightgray;
  font-style: italic;
}
</style>
