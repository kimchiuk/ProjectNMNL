import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useProductsStore = defineStore(
  "products",
  () => {
    const router = useRouter();

    const deposits = ref([]);
    const savings = ref([]);
    const depositOptions = ref([]);
    const savingsOptions = ref([]);

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/deposit/",
    })
      .then((res) => {
        deposits.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/savings/",
    })
      .then((res) => {
        savings.value = res.data;
        // console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/deposit_option/",
    })
      .then((res) => {
        depositOptions.value = res.data;
        // console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/savings_option/",
    })
      .then((res) => {
        savingsOptions.value = res.data;
        // console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    return {
      deposits,
      savings,
      depositOptions,
      savingsOptions,
    };
  },
  { persist: true }
);
