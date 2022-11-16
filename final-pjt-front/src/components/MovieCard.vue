<template>
    <div class="cardmove" >
  <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card" alt="...">
  </div>
</template>

<script>
export default {
name: 'MovieCard',
props: {
      movie: Object
    }
};
</script>

<style>
.card{
  width:100%;
  height: 100%;
  position: absolute; top:0; left:0;
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
  border-radius: 20px;
  padding: 0;
  margin: 20px;
  background-color: black;
  display: flex;
  justify-content: center;
  border: 1.5px solid white;
}
</style>
