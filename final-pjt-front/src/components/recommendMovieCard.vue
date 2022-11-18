<template>
    <div class="cardmoves" >
  <img :class="{showdata : moviedata}" @click="clickrecard" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" style="  height: 360px; width:240px; border-radius: 20px; border: 1.5px solid white;" alt="...">
  <div class="explain" :class="{showdata : !moviedata}" @click="clickrecard">
    <h4>{{movie.title}}</h4>
    <div>{{movie.overview}}</div>
  </div>
  </div>
</template>

<script>
export default {
name: 'MovieCard',
props: {
      movie: Object
    },
data(){
    return{
        moviedata:false
    }
},
methods:{
    clickrecard(){
        this.moviedata= !this.moviedata
    }
}
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
  border-radius: 20px;
  padding: 0;
  margin: 20px;
  background-color: black;
  justify-content: center;
  border: 1.5px solid white;
}
.showdata{
    display: none;
}
.explain{
    border: 1.5px solid white;
    white-space: normal;
    height: 360px;
  width:240px;
  padding: 10px;
  color: white;
  background-color: rgb(33, 37, 41);
  overflow: hidden;
  margin: 0;
  border-radius: 20px;
}
</style>