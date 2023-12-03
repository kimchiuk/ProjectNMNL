<template>
  <div class="box">
    <!-- 전체 박스 -->
    <div class="total-box">
      <!-- 메인 박스 = carousel + welcome profile -->
      <div class="main-box">
        <!-- carousel -->
        <div class="carousels col-9">
          <div id="carouselExampleIndicators" class="carousel slide">
            <div class="carousel-indicators">
              <button
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide-to="0"
                class="active"
                aria-current="true"
                aria-label="Slide 1"
              ></button>
              <button
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide-to="1"
                aria-label="Slide 2"
              ></button>
              <button
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide-to="2"
                aria-label="Slide 3"
              ></button>
            </div>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img
                  src="@/assets/home03.jpg"
                  class="d-block w-100 object-fit-fill border rounded"
                  alt="#"
                />
              </div>
              <div class="carousel-item">
                <img
                  src="@/assets/home02.png"
                  class="d-block w-100 object-fit-fill border rounded"
                  alt="#"
                />
              </div>
              <div class="carousel-item">
                <img
                  src="@/assets/home01.jpg"
                  class="d-block w-100 object-fit-fill border rounded"
                  alt="#"
                />
              </div>
            </div>
            <button
              class="carousel-control-prev"
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide="prev"
            >
              <span
                class="carousel-control-prev-icon"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button
              class="carousel-control-next"
              type="button"
              data-bs-target="#carouselExampleIndicators"
              data-bs-slide="next"
            >
              <span
                class="carousel-control-next-icon"
                aria-hidden="true"
              ></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
        <!-- profile -->
        <div class="profile col-3">
          <h4>환영합니다 😊</h4>
          <h3 class="user">{{ store.userInfo.username }} 님</h3>
          <hr />
          <h3 class="mention1">
            단순 저축만으로는 현명하게 자산을 관리할 수 있을까요??
          </h3>
          <hr />
          <h4 class="mention2">
            NMNL 서비스를 통해 예적금 상품을 한 눈에 모아보고 관심 상품을
            등록하여 나에게 맞는 상품을 바로바로 비교해보세요 !!
          </h4>
        </div>
      </div>

      <!-- 바로가기 -->
      <div class="go-to">
        <!-- 게시판 바로가기 -->
        <div class="reviews">
          <p>✍ 상품 리뷰 둘러보기</p>
          <img class="img" src="@/assets/review.png" alt="#" />
          <button class="btn btn-warning" @click="gotoReview">바로가기</button>
        </div>

        <!-- 환율 바로가기 -->
        <div class="exchange">
          <p>💰 실시간 환율</p>
          <img class="img" src="@/assets/exchange.jpg" alt="#" />
          <button class="btn btn-warning" @click="gotoExchange">
            바로가기
          </button>
        </div>

        <!-- 은행 찾기 바로가기 -->
        <div class="banks">
          <p>🧩 주변 은행 찾기</p>
          <img class="img" src="@/assets/map.png" alt="#" />
          <button class="btn btn-warning" @click="gotoMap">바로가기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useCounterStore } from "../stores/counter";

const router = useRouter();
const store = useCounterStore();

// 게시판 바로 가기
const gotoReview = () => {
  router.push({ name: "reviews" });
};

// 환율 바로 가기
const gotoExchange = () => {
  router.push({ name: "exchange" });
};

// 지도 바로가기
const gotoMap = () => {
  router.push({ name: "searchbank" });
};
</script>

<style scoped>
.total-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-bottom: 50px;
}
.main-box {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: center;
  padding: 50px 100px;
}
.carousels {
  padding: 20px;
}
.profile {
  padding: 30px;
  margin: 20px;
  border: 10px double rgba(45, 67, 45, 0.219);
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.go-to {
  padding: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  background-color: rgb(238, 238, 238);
  border-radius: 30px;
  margin: 0px 100px;
}
.img {
  width: 100%;
  height: 250px;
  border-radius: 20px;
  margin-bottom: 10px;
}

p {
  text-align: center;
  font-weight: bolder;
  font-size: larger;
  color: rgb(41, 19, 122);
}
.reviews,
.exchange,
.banks {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0px 30px;
}
.d-block {
  height: 500px;
  width: 300px;
}
.user {
  font-weight: bolder;
  background-color: lightgray;
  border-radius: 20px;
  padding: 20px;
}
.mention1 {
  text-align: center;
  font-style: italic;
  font-weight: bolder;
}
.mention2 {
  text-align: center;
  font-style: italic;
}
</style>
