<template>
  <div class="total-box">
    <div class="login-box">
      <h4>로그인 해주세요</h4>
      <form @submit.prevent="login">
        <label for="username">username</label><br />

        <input
          class="form-control"
          type="text"
          id="username"
          v-model.trim="username"
        /><br />

        <label for="password">password</label><br />
        <input
          class="form-control"
          type="password"
          id="password"
          v-model.trim="password"
        /><br />
        <div class="button">
          <input class="btn btn-outline-primary" type="submit" value="Login" />
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password = ref(null);

const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.login(payload);
};
</script>

<style scoped>
.total-box {
  display: flex;
  justify-content: center;
}
.login-box {
  margin: 40px;
  width: 350px;
  border: 2px solid darkgray;
  border-radius: 30px;
  padding: 30px;
  font-weight: bolder;
}
label,
input {
  margin: 5px;
}
h4 {
  text-align: center;
  margin-bottom: 20px;
}
.button {
  display: flex;
  justify-content: end;
}
</style>
