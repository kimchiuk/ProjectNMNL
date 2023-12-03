import { useCounterStore } from "../stores/counter";
import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";

import ExchangeView from "../views/ExchangeView.vue";
import SearchBankView from "../views/SearchBankView.vue";

import ReviewView from "../views/ReviewView.vue";
import CreateReview from "../views/CreateReview.vue";
import DetailReview from "../views/DetailReview.vue";

import ProfileView from "../views/ProfileView.vue";
import UpdateUserView from "../views/UpdateUserView.vue";
import UpdateReview from "../views/UpdateReview.vue";
import SignUpView from "../views/SignUpView.vue";
import LoginView from "../views/LoginView.vue";

import ProductsView from "../views/ProductsView.vue";
import DepositDetailView from "../views/DepositDetailView.vue";
import SavingsDetailView from "../views/SavingsDetailView.vue";

import RecommendView from "../views/RecommendView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 메인 페이지
    {
      path: "/",
      name: "home",
      component: HomeView,
    },

    //  예적금 조회 페이지
    {
      path: "/products",
      name: "products",
      component: ProductsView,
    },
    //  예금 상세
    {
      path: "/depositdetail/:fin_prdt_cd",
      name: "deposit_detail",
      component: DepositDetailView,
    },
    //  적금 상세
    {
      path: "/savingdetail/:fin_prdt_cd",
      name: "saving_detail",
      component: SavingsDetailView,
    },

    //  환율 정보 페이지
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
    //  은행 지도 페이지
    {
      path: "/searchbank",
      name: "searchbank",
      component: SearchBankView,
    },

    // 프로필 페이지
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
    },
    // 프로필 수정
    {
      path: "/profile/update",
      name: "updateUser",
      component: UpdateUserView,
    },
    // 회원가입
    {
      path: "/signup",
      name: "signup",
      component: SignUpView,
    },
    // 로그인
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },

    // 게시판 페이지
    {
      path: "/reviews",
      name: "reviews",
      component: ReviewView,
    },
    // 게시글 작성 페이지
    {
      path: "/create",
      name: "create",
      component: CreateReview,
    },
    // 게시글 상세 페이지
    {
      path: "/reviews/:id",
      name: "detail",
      component: DetailReview,
    },
    // 게시글 수정 페이지
    {
      path: "/reviews/:id/update",
      name: "update",
      component: UpdateReview,
    },

    // 추천 페이지
    {
      path: "/recommend",
      name: "recommend",
      component: RecommendView,
    },
  ],
});

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (
    (to.name === "review" && !store.isLogin) ||
    (to.name === "detail" && !store.isLogin) ||
    (to.name === "create" && !store.isLogin) ||
    (to.name === "profile" && !store.isLogin)
  ) {
    window.alert("로그인이 필요합니다.");
    return { name: "login" };
  }
  if (
    (to.name === "signup" && store.isLogin) ||
    (to.name === "login" && store.isLogin)
  ) {
    window.alert("이미 로그인이 되어있습니다.");
    return { name: "home" };
  }
});
export default router;
