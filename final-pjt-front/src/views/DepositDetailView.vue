<template>
  <div>
    <h2>🎁 예금 상품 정보 페이지</h2>

    <div class="total-box">
      <div class="titile-box">
        <h3 class="title">
          {{ product.fin_prdt_nm }}
        </h3>
      </div>

      <div class="like">
        <div
          v-if="!like"
          @click="
            cartStore.depositCartList(
              product.id,
              counterStoer.userInfo.pk,
              like
            ),
              toggle()
          "
        >
          ❤
        </div>
        <div
          v-else
          @click="
            cartStore.depositCartList(
              product.id,
              counterStoer.userInfo.pk,
              like
            ),
              toggle()
          "
        >
          🤍
        </div>
      </div>

      <div class="product-box">
        <div class="info-box col-8">
          <table class="info-content">
            <tr>
              <th>은행</th>
              <td>{{ product.kor_co_nm }}</td>
            </tr>
            <tr>
              <th>우대조건</th>
              <td>{{ product.spcl_cnd }}</td>
            </tr>
            <tr>
              <th>만기 후 이자율</th>
              <td>{{ product.mtrt_int }}</td>
            </tr>
            <tr>
              <th>가입제한</th>
              <td>
                {{
                  product.join_deny == 1
                    ? "제한없음"
                    : product.join_deny == 2
                    ? "서민전용"
                    : "일부제한"
                }}
              </td>
            </tr>
            <tr>
              <th>가입 대상</th>
              <td>{{ product.join_member }}</td>
            </tr>
            <tr>
              <th>가입 방법</th>
              <td>{{ product.join_way }}</td>
            </tr>
          </table>
        </div>

        <div class="option-box">
          <p class="info">상품 옵션 정보</p>
          <div class="table-box">
            <table class="option-content">
              <tr>
                <th>저축 기간(월)</th>
                <th>저축 금리</th>
                <th>최대 우대금리</th>
              </tr>
              <tr v-for="optlist in optionList" :key="optlist.id">
                <td>{{ optlist.save_trm }}</td>
                <td>{{ optlist.intr_rate }}</td>
                <td>{{ optlist.intr_rate2 }}</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>

    <div class="btn-box">
      <button class="btn btn-warning" @click="goBack">뒤로 가기</button>
    </div>
  </div>
</template>

<script setup>
import { useProductsStore } from "@/stores/products.js";
import { useCounterStore } from "../stores/counter";
import { useCartStore } from "../stores/cart";
import { useRoute, useRouter } from "vue-router";
import { computed } from "@vue/reactivity";
import { ref } from "vue";

const store = useProductsStore();
const counterStoer = useCounterStore();
const cartStore = useCartStore();
const route = useRoute();
const router = useRouter();

const prdtCd = route.params.fin_prdt_cd;
const like = ref(false);

const product = computed(() => {
  return store.deposits?.filter((product) => product.fin_prdt_cd === prdtCd)[0];
});

const filterCart = computed(() => {
  return cartStore.depositCart.filter(
    (v) => v.product === product.value.id && v.user === counterStoer.userInfo.pk
  );
});

const optionList = computed(() => {
  return store.depositOptions?.filter(
    (option) => product.value.id === option.fin_prdt_cd
  );
});

const toggle = function () {
  like.value = !like.value;
};

// 뒤로 가기 함수
const goBack = () => {
  router.go(-1);
};
</script>

<style scoped>
h2 {
  height: 100px;
  display: flex;
  align-items: flex-end;
  padding: 20px;
  font-weight: bolder;
  border-bottom: 2px solid lightgray;
}
.total-box {
  display: flex;
  flex-direction: column;
}
.product-box {
  display: flex;
  justify-content: center;
  align-items: start;
}

.titile-box {
  display: flex;
  justify-content: center;
}
.title {
  border: 3px solid rgb(45, 67, 45);
  padding: 30px;
  border-radius: 30px;
  margin: 20px;
  text-align: center;
  font-weight: bolder;
  width: 60%;
}

.info-content {
  margin: 30px;
}
.info-content td {
  border: 1px solid #ddd;
  padding: 20px;
}
.info-content th {
  border: 1px solid #ddd;
  text-align: center;
  width: 150px;
  background-color: #f2f2f2;
}

.option-box {
  text-align: center;
  margin-top: 30px;
}
.option-box th {
  background-color: #f2f2f2;
  border: 1px solid #ddd;
  padding: 15px;
}
.option-content td {
  border: 1px solid #ddd;
  padding: 20px;
}
.btn-box {
  margin: 30px;
  text-align: center;
}

.info {
  font-weight: bolder;
  font-size: x-large;
}
.like {
  margin: 5px;
  display: flex;
  justify-content: center;
  font-size: xx-large;
}
</style>
