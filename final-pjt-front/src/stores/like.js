import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";
import { useCounterStore } from "./counter";

export const useLikeStore = defineStore(
  "like",
  () => {
    const like = ref(false);
    const store = useCounterStore;

    const likeBtn = function (user, token, id) {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/articles/${user}/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          if (res.data.status == "unliked") {
            like.value = false;
          } else {
            like.value = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return { like, store, likeBtn };
  },
  { persist: true }
);
