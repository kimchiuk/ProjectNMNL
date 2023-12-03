<template>
  <div>
    <h2>👩‍🦰 내 프로필</h2>
    <div class="profileview">
      <!-- 전체 박스 -->
      <div class="total-box">
        <!-- 프로필 박스 -->
        <div class="profile-box col-4">
          <h3>{{ userInfo.username }} 님의 프로필</h3>
          <RouterLink
            class="btn btn-outline-success"
            :to="{ name: 'updateUser' }"
            >개인정보 수정하기</RouterLink
          >
          <div class="myinfo">
            <h4>기본 정보</h4>
            <h5>이메일 : {{ userInfo.email }}</h5>
            <!-- <h5>나이 : {{ userInfo.age }}</h5>
            <h5>자산 : {{ userInfo.money }}</h5>
            <h5>연봉 : {{ userInfo.salary }}</h5> -->
          </div>
        </div>

        <div class="info-box col-7">
          <!-- 장바구니 -->
          <div>
            <!-- 예금 -->
            <div>
              <h4>좋아요 한 예금 상품목록</h4>
              <!-- 목록 -->
              <div class="list">
                <div v-for="deposit in productStore.deposits" :key="deposit.id">
                  <div v-for="like in depositsLikeList">
                    <div v-if="like.product === deposit.id">
                      <RouterLink
                        class="card"
                        :to="{ path: `/depositdetail/${deposit.fin_prdt_cd}` }"
                        >{{ deposit.fin_prdt_nm }}</RouterLink
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 적금 -->
            <div>
              <h4>좋아요 한 적금 상품목록</h4>
              <!-- 목록 -->
              <div class="list">
                <div v-for="saving in productStore.savings" :key="saving.id">
                  <div v-for="like in savingsLikeList">
                    <div v-if="like.product === saving.id">
                      <RouterLink
                        class="card"
                        :to="{ path: `/savingdetail/${saving.fin_prdt_cd}` }"
                        >{{ saving.fin_prdt_nm }}</RouterLink
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 작정한 게시글 -->
          <h4>작성한 게시글 목록</h4>
          <div>
            <div v-for="article in store.articles" :key="article.id">
              <div v-if="article.user == userInfo.pk">
                <RouterLink
                  class="card"
                  :to="{ path: `/reviews/${article.id}` }"
                  >{{ article.title }}</RouterLink
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "../stores/counter";
import { useProductsStore } from "../stores/products";
import { useRouter, RouterLink } from "vue-router";
import { useCartStore } from "../stores/cart";

const store = useCounterStore();
const cartStore = useCartStore();
const productStore = useProductsStore();
const userInfo = store.userInfo;

const depositsLikeList = cartStore.depositCart.filter(
  (v) => v.user === store.userInfo.pk
);
const savingsLikeList = cartStore.savingsCart.filter(
  (v) => v.user === store.userInfo.pk
);
</script>

<style scoped>
.profileview {
  display: flex;
  justify-content: center;
}
h2 {
  height: 100px;
  display: flex;
  align-items: flex-end;
  padding: 20px;
  font-weight: bolder;
  border-bottom: 2px solid lightgray;
}
h3 {
  font-weight: bolder;
  font-size: xx-large;
  margin-bottom: 20px;
}
h4 {
  font-weight: bolder;
  color: rgb(45, 67, 45);
  font-style: italic;
}
h5 {
  margin: 20px 5px;
}
.list {
  display: flex;
  flex-direction: row;
  margin-bottom: 20px;
}

.myinfo {
  margin: 30px 0px;
  background-color: aliceblue;
  padding: 30px;
  border-radius: 30px;
}
.total-box {
  width: 80%;
  display: flex;
  justify-content: center;
}
.profile-box {
  border-radius: 30px;
  margin: 20px;
  padding: 20px;
}
.info-box {
  margin: 20px;
  padding: 30px;
}

.card {
  padding: 20px;
  margin: 5px;
  text-decoration: none;
}
</style>
