<template>
  <div>
    <div>
      <h2>🔍 회원님에게 높은 금리의 상품을 추천해드립니다</h2>
      <h4>찾으시는 옵션을 선택해서 상품을 추천 받아 보세요</h4>
    </div>
    <div class="selbox">
      <div class="select">
        <div class="select-title">
          <h5>상품 종류를 선택해주세요</h5>
        </div>
        <div class="select-box">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              id="depositRadio"
              name="productType"
              v-model="isDepositSelected"
            /><label class="form-check-label"> 예금</label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              id="savingsRadio"
              name="productType"
              v-model="isSavingsSelected"
            />
            <label class="form-check-label">적금</label>
          </div>
        </div>
      </div>

      <div class="select">
        <div class="select-title">
          <h5>기준 금리를 선택하세요</h5>
        </div>
        <div class="select-box">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              id="standardRateRadio"
              name="rateType"
              v-model="isTopSelected"
            />
            <label class="form-check-label">우대 금리 기준</label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              id="maxPreferredRateRadio"
              name="rateType"
              v-model="isTopSelectedTop"
            />
            <label class="form-check-label">최대 우대 금리 기준</label>
          </div>
        </div>
      </div>
    </div>

    <div>
      <div class="result" v-if="isDepositSelected && isTopSelected">
        <div class="card" style="width: 24rem" v-for="item in topdeposits1">
          <p class="bank">{{ item.kor_co_nm }}</p>
          <p @click="depositDetail(item)" class="title">
            {{ item.fin_prdt_nm }}
          </p>
          <p class="rate">{{ item.intr_rate }}%</p>
        </div>
      </div>
      <div class="result" v-else-if="isDepositSelected && isTopSelectedTop">
        <div class="card" style="width: 24rem" v-for="item in topdeposits2">
          <p class="bank">{{ item.kor_co_nm }}</p>
          <p @click="depositDetail(item)" class="title">
            {{ item.fin_prdt_nm }}
          </p>
          <p class="rate">{{ item.intr_rate2 }}%</p>
        </div>
      </div>
      <div class="result" v-else-if="isSavingsSelected && isTopSelected">
        <div class="card" style="width: 24rem" v-for="item in topsavings1">
          <p class="bank">{{ item.kor_co_nm }}</p>
          <p @click="savingsDetail(item)" class="title">
            {{ item.fin_prdt_nm }}
          </p>
          <p class="rate">{{ item.intr_rate }}%</p>
        </div>
      </div>
      <div class="result" v-else-if="isSavingsSelected && isTopSelectedTop">
        <div class="card" style="width: 24rem" v-for="item in topsavings2">
          <p class="bank">{{ item.kor_co_nm }}</p>
          <p @click="savingsDetail(item)" class="title">
            {{ item.fin_prdt_nm }}
          </p>
          <p class="rate">{{ item.intr_rate2 }}%</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProductsStore } from "../stores/products";
import { ref } from "vue";
import { useRouter } from "vue-router";

const productStore = useProductsStore();
const router = useRouter();

// 예금 상품 - 옵션
const depositOptionMap = productStore.depositOptions.reduce((map, option) => {
  map[option.fin_prdt_cd] = option;
  return map;
}, {});

const mergedDeposit = productStore.deposits.map((deposit) => {
  const option = depositOptionMap[deposit.id];
  return {
    id: deposit.id,
    fin_prdt_cd: deposit.fin_prdt_cd,
    fin_prdt_nm: deposit.fin_prdt_nm,
    kor_co_nm: deposit.kor_co_nm,
    spcl_cnd: deposit.spcl_cnd,
    mtrt_int: deposit.mtrt_int,
    join_deny: deposit.join_deny,
    join_member: deposit.join_member,
    join_way: deposit.join_way,
    intr_rate: option ? option.intr_rate : 0,
    intr_rate2: option ? option.intr_rate2 : 0,
    save_trm: option ? option.save_trm : null,
  };
});

// 우대 금리가 높은 예금 top3
const topdeposits1 = mergedDeposit
  .filter((deposit) => deposit.intr_rate !== null)
  .sort((a, b) => b.intr_rate - a.intr_rate)
  .slice(0, 3);

// 최고 우대 금리가 높은 예금 top3
const topdeposits2 = mergedDeposit
  .filter((deposit) => deposit.intr_rate2 !== null)
  .sort((a, b) => b.intr_rate2 - a.intr_rate2)
  .slice(0, 3);

// 적금 상품 - 옵션
const savingsOptionMap = productStore.savingsOptions.reduce((map, option) => {
  map[option.fin_prdt_cd] = option;
  return map;
}, {});

const mergedSavings = productStore.savings.map((saving) => {
  const option = savingsOptionMap[saving.id];
  return {
    id: saving.id,
    fin_prdt_cd: saving.fin_prdt_cd,
    fin_prdt_nm: saving.fin_prdt_nm,
    kor_co_nm: saving.kor_co_nm,
    spcl_cnd: saving.spcl_cnd,
    mtrt_int: saving.mtrt_int,
    join_deny: saving.join_deny,
    join_member: saving.join_member,
    join_way: saving.join_way,
    intr_rate: option ? option.intr_rate : 0,
    intr_rate2: option ? option.intr_rate2 : 0,
    save_trm: option ? option.save_trm : null,
  };
});

// 우대 금리가 높은 예금 top3
const topsavings1 = mergedSavings
  .filter((saving) => saving.intr_rate !== null)
  .sort((a, b) => b.intr_rate - a.intr_rate)
  .slice(0, 3);

// 최고 우대 금리가 높은 예금 top3
const topsavings2 = mergedSavings
  .filter((saving) => saving.intr_rate2 !== null)
  .sort((a, b) => b.intr_rate2 - a.intr_rate2)
  .slice(0, 3);

const isDepositSelected = ref(false);
const isSavingsSelected = ref(false);

const isTopSelected = ref(false);
const isTopSelectedTop = ref(false);

// 예금 상세 페이지로 이동
const depositDetail = (item) => {
  router.push({
    name: "deposit_detail",
    params: {
      fin_prdt_cd: item.fin_prdt_cd,
    },
  });
};

// 적금 상세 페이지로 이동
const savingsDetail = (item) => {
  router.push({
    name: "saving_detail",
    params: {
      fin_prdt_cd: item.fin_prdt_cd,
    },
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
h4 {
  text-align: center;
  font-weight: bolder;
  font-style: italic;
  color: rgb(148, 148, 40);
  margin: 20px;
}
h5 {
  text-align: center;
  font-weight: bolder;
  font-style: italic;
  color: gray;
  margin: 25px;
}
.selbox {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.select-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding-bottom: 25px;
  height: 20px;
}
.select {
  width: 60%;
  font-size: x-large;
  display: flex;
  flex-direction: column;
  /* border: 3px solid lightgray; */
  border-radius: 30px;
  margin: 5px;
}
.select-title {
  height: 80px;
  margin: 0px;
}
label {
  margin: 0px 5px;
  font-weight: bold;
  color: rgb(56, 77, 56);
}
.result {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 30px;
}
.card {
  margin: 10px;
  text-align: center;
  justify-content: center;
  padding: 20px;
  border: 8px double rgba(56, 77, 56, 0.548);
  border-radius: 30px;
}
.bank {
  padding: 10px;
  font-weight: bold;
  color: gray;
}
.title {
  background-color: rgba(211, 211, 211, 0.466);
  border-radius: 30px;
  padding: 20px;
  width: 100%;
  font-size: large;
  font-weight: bolder;
}
.rate {
  font-size: xx-large;
  font-weight: bolder;
  font-style: italic;
  color: rgb(9, 107, 107);
}
</style>
