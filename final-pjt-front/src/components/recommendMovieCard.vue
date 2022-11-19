<template>
    <div class="cardmoves" >
  <img :class="{showdata : moviedata}" @click="clickrecard" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" style="  height: 360px; width:240px; border-radius: 20px; border: 1.5px solid white;" alt="...">
  <div class="explain" :class="{showdata : !moviedata}" @click="clickrecard">
    <h4>{{movie.title}}</h4>
    <p>{{movie.overview}}</p>
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
.showdata{
    display: none;
    height: 300px;
}
.explain{
    border: 1.5px solid white;
    white-space: normal;
    height: 360px;
  width:240px;
  padding: 5px;
  padding-bottom: 15px;
  color: white;
  background-color: rgb(33, 37, 41);
  overflow: hidden;
  margin: 0;
  border-radius: 20px;
  word-break:keep-all;
  font-family: 'BMHANNAAir';
}
</style>