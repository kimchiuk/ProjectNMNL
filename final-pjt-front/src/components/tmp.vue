<template>
    <div>
        {{ productStore.deposits[2] }}
        <br>

        {{ counterStore.userInfo.pk }}
        <form>
            <div @click="cartStore.cartList(productStore.deposits[2].id, counterStore.userInfo.pk, like), toggle()">버튼</div>
            
            {{ cartStore.cart }}
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useProductsStore } from '../stores/products'
import { useCounterStore } from '../stores/counter';
import { useCartStore } from '../stores/cart'

const counterStore = useCounterStore()
const productStore = useProductsStore()
const cartStore = useCartStore()
const { cart } =
  storeToRefs(cartStore);

const like = ref(true);

const toggle = function () {
    like.value = !like.value
}



</script>

<style lang="scss" scoped>

</style>