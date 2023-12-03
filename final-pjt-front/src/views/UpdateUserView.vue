<template>
  <div class="total-box">
    <div>
      <h4>개인정보 수정</h4>
    </div>

    <div class="signup-box">
      <form @submit.prevent="updateUser">
        <label for="username">아이디</label>
        <input
          class="form-control"
          type="text"
          name="val"
          v-model.trim="username"
        /><br />

        <label for="email">이메일</label>
        <input
          class="form-control"
          type="text"
          id="email"
          v-model.trim="email"
        /><br />

        <label for="age">나이</label>
        <input
          class="form-control"
          type="text"
          id="age"
          v-model.trim="age"
        /><br />

        <label for="money">자산</label>
        <input
          class="form-control"
          type="text"
          id="money"
          v-model.trim="money"
        /><br />

        <label for="salary">연봉</label>
        <input
          class="form-control"
          type="text"
          id="salary"
          v-model.trim="salary"
        /><br />

        <br />

        <div class="button">
          <button class="btn btn-outline-secondary" @click="goBack">
            돌아가기
          </button>
          <input
            class="btn btn-outline-warning"
            type="submit"
            value="수정완료"
          />
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "../stores/counter";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useCounterStore();

const username = ref(store.userInfo.username);
const email = ref(store.userInfo.email);
const age = ref(store.userInfo.age);
const money = ref(store.userInfo.money);
const salary = ref(store.userInfo.salary);

const updateUser = function () {
  const payload = {
    username: username.value,
    email: email.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  };
  store.updateUser(payload);
};

const goBack = () => {
  router.push({ name: "profile" });
};
</script>

<style scoped>
.total-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.signup-box {
  margin: 20px;
  width: 500px;
  border: 7px double darkgray;
  border-radius: 30px;
  padding: 40px;
  font-weight: bolder;
}

h4 {
  text-align: center;
  padding-top: 30px;
  font-size: xx-large;
  font-weight: bolder;
}
label {
  margin: 10px;
}
.button {
  display: flex;
  justify-content: center;
}
.btn {
  margin: 0px 10px;
}
</style>
