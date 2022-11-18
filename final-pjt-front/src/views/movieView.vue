<template>
  <div style="display: flex;">
    <b-container class="bg-dark" fluid style="padding:15px; padding-top:65px; ">
      <b-col align-self="center">
          <h1 style="color:white;">최신영화</h1>
          <div>
            <div class="movie_list" >
              <NowMovieCard
                  v-for="movie in nowmoviesList" :key="movie.pk"
                  :movie="movie"
              />
            </div>

          </div>
      </b-col>
      <br>
      <b-col align-self="center">
        <h1 style="color:white;">영화 목록</h1>
        <div style="text-align:center;">

          <div class="list"> 
            <MovieCard
                v-for="movie in topmoviesList" :key="movie.pk"
                :movie="movie"
            />
          </div>
        </div>
      </b-col>
      <p>{{movie}}</p>
    </b-container>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import NowMovieCard from '@/components/NowMovieCard'
export default {
  name: 'MovieView',

  data() {
      return {
          movie:null,
      }
  },
  components: { MovieCard, NowMovieCard },
  computed: {
      topmoviesList() {
          return this.$store.state.topmoviesList
      },
      nowmoviesList() {
          return this.$store.state.nowmoviesList
      },
  },
}
</script>

<style>
.movie_list {
    display: flex;
    overflow-x: scroll;
    scroll-behavior: smooth;
    height: 450px;;
    overflow-y:hidden;
    white-space: nowrap;
    }
.movie_list::-webkit-scrollbar{
    background-color: rgb(33, 37, 41);
    
}
.movie_list::-webkit-scrollbar-thumb{
    background-color: white;
}
.list{
  /* justify-content: center;
  display: flex;
  justify-content: center;
  align-items: center; */
  display: inline-block;
  padding-left: 20px;
}
</style>
