import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useCartStore = defineStore(
  "cart",
  () => {
    const depositCart = ref([]);

    const depositCartList = function (id, id2, like) {
      if (like === true) {
        depositCart.value.push({ product: id, user: id2 });
      } else {
        depositCart.value = depositCart.value.filter(
          (item) => !(item.product === id && item.user === id2)
        );
      }
    };

    const savingsCart = ref([]);

    const savingsCartList = function (id, id2, like) {
      if (like === true) {
        savingsCart.value.push({ product: id, user: id2 });
      } else {
        savingsCart.value = savingsCart.value.filter(
          (item) => !(item.product === id && item.user === id2)
        );
      }
    };

    return { depositCart, depositCartList, savingsCart, savingsCartList };
  },
  { persist: true }
);
