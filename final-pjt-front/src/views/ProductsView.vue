<template>
  <div>
    <h2>🔑 금융 상품 조회</h2>

    <div class="btn-box">
      <div class="search-btn">
        <div>
          <span
            :class="[
              select == 0
                ? 'btn btn-success btn-lg'
                : 'btn btn-outline-success btn-lg',
            ]"
            @click="select = 0"
            >예금 상품 조회</span
          >
        </div>
        <div>
          <span
            :class="[
              select == 1
                ? 'btn btn-success btn-lg'
                : 'btn btn-outline-success btn-lg',
            ]"
            @click="select = 1"
            >적금 상품 조회</span
          >
        </div>
      </div>

      <div>
        <RouterLink :to="{ name: 'recommend' }" class="btn btn-outline-warning">
          상품 추천 받기
        </RouterLink>
      </div>
    </div>

    <div v-if="deposits" class="list-box">
      <div class="boxes" v-show="select === 0">
        <div v-for="deposit in deposits" :key="deposit.id">
          <div class="card" style="width: 16rem">
            <div @click="depositDetail(deposit)" class="card-body">
              <p class="card-subtitle mb-2 text-body-secondary">
                {{ deposit.kor_co_nm }}
              </p>
              <p class="card-title">
                {{ deposit.fin_prdt_nm }}
              </p>
              <p class="card-text">{{ deposit.join_member }}</p>
              <p class="rate">
                {{
                  depositOptions.filter(
                    (option) => option.fin_prdt_cd === deposit.id
                  )[0].intr_rate
                }}%
              </p>
            </div>
          </div>
        </div>
      </div>
      <div v-if="savings" class="boxes" v-show="select === 1">
        <div v-for="saving in savings" :key="saving.id">
          <div class="card" style="width: 16rem">
            <div @click="savingDetail(saving)" class="card-body">
              <p class="card-subtitle mb-2 text-body-secondary">
                {{ saving.kor_co_nm }}
              </p>
              <p class="card-title">
                {{ saving.fin_prdt_nm }}
              </p>
              <p class="card-text">{{ saving.join_member }}</p>
              <p class="rate">
                {{
                  savingsOptions.filter(
                    (option) => option.fin_prdt_cd === saving.id
                  )[0].intr_rate
                }}%
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from "pinia";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import { useProductsStore } from "../stores/products";

const router = useRouter();
const store = useProductsStore();

const select = ref(0);
const { deposits, savings, depositOptions, savingsOptions } =
  storeToRefs(store);

const depositDetail = (product) => {
  router.push({
    name: "deposit_detail",
    params: {
      fin_prdt_cd: product.fin_prdt_cd,
    },
  });
};

const savingDetail = (product) => {
  console.log(product.fin_prdt_cd);
  router.push({
    name: "saving_detail",
    params: { fin_prdt_cd: product.fin_prdt_cd },
  });
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
.card {
  border-radius: 20px;
  text-align: center;
  margin: 10px;
  height: 250px;
  border: 6px double rgba(45, 67, 45, 0.322);
}
.search-btn {
  display: flex;
}
.btn-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  align-items: end;
  text-align: center;
  padding: 10px 100px;
}
.btn {
  margin: 15px;
}

.list-box {
  margin: 10px;
  padding: 0px 20px;
}
.boxes {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  border-radius: 20px;
  padding: 20px;
  background-color: rgb(238, 238, 238);
}
.card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.card-title {
  font-weight: bolder;
  font-size: large;
}
.rate {
  font-size: x-large;
  font-weight: bolder;
  color: gray;
}
</style>
