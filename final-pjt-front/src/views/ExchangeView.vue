<template>
  <div>
    <h2>💲 실시간 환율 계산하기</h2>
    <div class="main-box">
      <div class="select-box col-3">
        국가 선택하기
        <select v-model="exchangeRate" class="btn-group" role="group">
          <option v-for="payment in payments" :key="payment" :value="payment">
            {{ payment }}
          </option>
          <br />
        </select>

        <select v-model="situation" class="btn-group">
          <option v-for="option in options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>
      <div class="result-box">
        <h5 class="input" v-if="rate == -1">
          [ 오류 ] 정보를 불러올 수 없습니다.
        </h5>
        <h5 class="input" v-else-if="rate">
          현재 {{ situation }} {{ money1 }} {{ currencyName }}은(는)
          {{ money2 }} 원입니당
        </h5>
        <h5 class="input" v-else>옵션을 먼저 선택해주세요.</h5>

        <div class="money-box">
          {{ nation }} ( {{ currencyCode }} )
          <input
            class="form-control"
            type="text"
            v-model.number="money1"
            @input="updatePayment2(Math.round((money1 * rate) / currencyUnit))"
          />
          {{ currencyName }}
        </div>
        <div class="money-box">
          대한민국 ( KRW )
          <input
            class="form-control"
            type="text"
            v-model.number="money2"
            @input="updatePayment1(Math.round((money2 / rate) * currencyUnit))"
          />
          원
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";
// prettier-ignore
const payments = ref(
  ["미국", "유럽", "일본", "영국","스위스","캐나다","호주","중국","홍콩","스웨덴","뉴질랜드","싱가포르","노르웨이","멕시코","인도","러시아","남아공","터키","브라질","아랍에미리트","바레인","브루나이","체코","덴마크","인도네시아","이스라엘","말레이시아","카타르","사우디","태국","대만","이집트","헝가리","쿠웨이트","폴란드","파키스탄","방글라데시","요르단","카자흐스탄","몽골","베트남"]
);
// 국가 코드
// prettier-ignore
const nationCode = { 미국:"USD", 유럽: "EUR", 일본: "JPY", 영국: "GBP", 스위스: "CHF", 캐나다:"CAD", 호주:"AUD", 중국:"CNY", 홍콩:"HKD", 스웨덴:"SEK", 뉴질랜드:"NZD", 싱가포르:"SGD", 노르웨이:"NOK", 멕시코:"MXN", 인도:"INR", 러시아:"RUB", 남아공:"ZAR", 터키:"TRY", 브라질:"BRL", 아랍에미리트:"AED", 바레인:"BHD", 브루나이:"BND",체코:"CZK",덴마크:"DKK", 인도네시아:"IDR", 이스라엘:"ILS", 말레이시아:"MYR", 카타르:"QAR",사우디:"SAR", 태국:"THB", 대만:"TWD", 이집트:"EGP", 헝가리:"HUF", 쿠웨이트:"KWD", 필리핀:"PHP", 폴란드:"PLN", 파키스탄:"PKR", 방글라데시:"BDT", 요르단:"JOD", 카자흐스탄:"KZT", 몽골:"MNT", 베트남:"VND" };
// 옵션 종류
const options = ref(["매매기준율", "현찰 살 때", "현찰 팔 때"]);

const exchangeRate = ref(null);
const situation = ref("매매기준율");

const rate = ref(null);

const currencyUnit = ref(null);
const currencyName = ref(null);
const currencyCode = ref(null);

// 입력 금액
const money1 = ref(0);
const money2 = ref(0);

// 환율 옵션이 선택되었을 때에 환율 금액 정보 가져오기
watch([exchangeRate, situation], ([selectOption1, selectOption2]) => {
  // 국가가 선택
  if (selectOption1 !== null && selectOption2 !== null) {
    axios({
      url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${nationCode[selectOption1]}`,
      method: "GET",
    })
      .then(({ data }) => {
        currencyUnit.value = data[0]?.currencyUnit || 1;
        currencyName.value = data[0]?.currencyName || 1;
        currencyCode.value = data[0]?.currencyCode || 1;
        nation.value = data[0]?.country || 1;
        if (selectOption2 == "매매기준율") {
          rate.value = data[0]?.basePrice || -1;
        } else if (selectOption2 == "현찰 살때") {
          rate.value = data[0]?.cashBuyingPrice || -1;
        } else {
          rate.value = data[0]?.cashSellingPrice || -1;
        }
        // 환율 기준이 변경된다면 0으로 초기화
        money1.value = 0;
        money2.value = 0;
      })
      .catch((err) => console.log(err));
  }
});

// 환율 업데이트
const updatePayment1 = function (value) {
  money1.value = value.toLocaleString(); // 원단위 ',' 추가
};
const updatePayment2 = function (value) {
  money2.value = value.toLocaleString(); // 원단위 ',' 추가
};

// 아 이거 빼먹엇네...;
const nation = ref(null);
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
.form-control {
  width: 400px;
}
.money-box {
  display: flex;
  align-items: center;
  margin: 5px 15px;
}
.main-box {
  display: flex;
  height: 100%;
  padding: 0px 80px;
}
.select-box {
  border: 2px solid lightgray;
  border-radius: 30px;
  height: 200px;
  display: flex;
  flex-direction: column;
  margin: 20px;
  padding: 30px;
  font-weight: bolder;
}
.result-box {
  display: flex;
  flex-direction: column;
  margin: 20px;
  padding: 20px;
  font-weight: bolder;
  width: 100%;
}
.btn-group {
  margin: 10px;
}
.input {
  margin: 10px;
  color: darkgreen;
  font-weight: bolder;
}
.form-control {
  margin: 5px 10px;
}
</style>
