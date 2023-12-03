import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();
    const token = ref(null);
    const articles = ref([]);
    const comments = ref([]);
    const userInfo = ref("");
    const like_articles = ref([]);

    const getUserInfo = () => {
      axios({
        method: "GET",
        url: `${API_URL}/dj-rest-auth/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          userInfo.value = response.data;
          console.log(userInfo);
        })
        .catch((err) => console.log(err.response));
    };

    const login = function (payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log("로그인이 완료되었습니다");
          // console.log(res.data);
          token.value = res.data.key;
          router.push({ name: "home" });
          getUserInfo();
        })
        .catch((err) => {
          alert("로그인정보가 일치하지 않습니다.");
          console.log(err);
        });
    };

    const logout = function () {
      axios({
        method: "POST",
        url: `${API_URL}/dj-rest-auth/logout/`,
        headers: {
          Authorization: token.value,
        },
      });
      token.value = null;
      userInfo.value = null;
    };

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const email = payload.email;
      const age = payload.age;
      const money = payload.money;
      const salary = payload.salary;

      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/registration/`,
        data: {
          username,
          password1,
          password2,
          email,
          age,
          money,
          salary,
        },
      })
        .then((res) => {
          console.log("회원가입이 완료되었습니다.");
          userInfo.value = {
            username: payload.username,
            email: payload.email,
            age: payload.age,
            money: payload.money,
            salary: payload.salary,
          };
          const password = password1;
          login({ username, password });
          getUserInfo();
        })
        .catch((err) => {
          alert(
            "이미 있는 아이디 이거나 비밀번호가 일치하지 않습니다. 다시 확인해주세요"
          );
          console.log(err);
        });
    };

    const updateUser = function (payload) {
      const username = payload.username;
      const email = payload.email;
      const age = payload.age;
      const money = payload.money;
      const salary = payload.salary;

      axios({
        method: "put",
        url: `http://127.0.0.1:8000/accounts/update/${userInfo.value.pk}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: {
          email: email,
          age: age,
          money: money,
          salary: salary,
        },
      })
        .then((res) => {
          userInfo.value = {
            username: payload.username,
            email: payload.email,
            age: payload.age,
            money: payload.money,
            salary: payload.salary,
          };
          getUserInfo();
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getArticles = () => {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/articles/",
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getUser = () => {
      axios({
        method: "get",
      });
    };

    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    return {
      getUserInfo,
      signUp,
      updateUser,
      login,
      logout,
      getArticles,
      token,
      isLogin,
      articles,
      comments,
      userInfo,
      like_articles,
    };
  },
  { persist: true }
);
