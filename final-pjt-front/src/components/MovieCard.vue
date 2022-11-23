<template>
    <div class="cardmove" @click="getDetail(movie)" >
  <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="imgs card" style="height: 360px; width:240px; border-radius: 20px; border:0px;" alt="...">
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
.card{
  width:100%;
  height: 100%;
  position: absolute; top:0; left:0;
  border: 2px solid white;
  margin:0;
}
.cardmove:hover{
    transform: scale(1.1);
    
}
.cardmove{
  transition: all 0.17s linear;
  overflow: hidden;
  height: 360px;
  width:240px;
  float:left;
  padding: 0;
  margin: 20px;
  display: flex;
  justify-content: center;
  

}
.imgs{
  margin: 0;
  padding: 0;
  
}
</style>
