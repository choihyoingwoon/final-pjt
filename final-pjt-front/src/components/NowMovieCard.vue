<template>
    <div class="cardmoves" @click="getDetail(movie)" >
  <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="imgs card" style="height: 360px; width:240px; border-radius: 20px;" alt="...">
  </div>
</template>

<script>
export default {
name: 'MovieCard',
props: {
      movie: Object
    },
methods:{
  getDetail(movie) {
    this.$router.push({ name: 'detail', params: { id: `${movie.id}`}})
  }
},
};
</script>

<style>
.cardmoves:hover{
    transform: scale(1.1);
    
}
.cardmoves{
  transition: all 0.17s linear;
  height: 360px;
  width:240px;
  float:left;
  padding: 0;
  margin: 20px;
  justify-content: center;

}
</style>