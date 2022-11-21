<template>
  <div class="signup bg-dark">
    <br>
    <h1 style="color:white;">My Page</h1>
    <br>
    <div>
        <h3 style="margin-left:0px;">{{userName}}님이 담아놓은 영화들🎬</h3>
        <MovieCard
            v-for="movie in likeList" :key="movie.id"
            :movie="movie"
        />
    </div>
    <br>

  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue';

export default {
    name: "myPage",
    components: {
        MovieCard,
    },  
    computed: {
        likeList() {
            return this.$store.state.likeList
        },
        userName() {
            return this.$store.state.user
        }
    },
}
</script>

<style>

</style>