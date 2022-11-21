<template>
  <div class="signup bg-dark">
    <br>
    <h1 style="color:white; font-family: 'BMHANNAPro';">My Page</h1>
    <br>
    <hr style="width: 100;">
    <br>
    <div>
        <h3 style="margin-left:0px; font-family: 'BMHANNAPro';">{{userName}}님이 담아놓은 영화들🎬</h3>
        <!-- <button class="btn btn-danger" style="width:100px; height: 40px; margin-right:10px;">선택 삭제</button> -->
        <button @click="alldelete" class="btn btn-danger" style="width:100px; height: 38px; ">전체 삭제</button>
        <div>
            <MovieCard
                v-for="movie in likeList" :key="movie.id"
                :movie="movie"
            />
        </div>
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
    methods: {
        alldelete() {
            this.$store.dispatch('alldelete')
        }
    }
}
</script>

<style>

</style>