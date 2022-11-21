<template>
  <div class="bg-dark">
    <br>
    <button @click="ddd">확인용</button>
    <h1 style="color:white;">My Page</h1>
    <div v-for="movie in likeList" :key="movie.id">
        <p>{{movie.title}}</p>
    </div>
    <br>

  </div>
</template>

<script>
export default {
    name: "myPage",
    computed: {
        likeList() {
            return this.$store.state.likelist
        }
    },
    methods: {
        ddd() {
            console.log(this.$store.state.likeList)
        }
    }
}
</script>

<style>

</style>