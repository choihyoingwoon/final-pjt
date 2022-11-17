<template>
  <div style="display: auto; display: flex;">
    <b-container class="bg-dark" fluid style="padding:15px; padding-top:65px; ">
      <b-col align-self="center">
          <h1 style="color:white;">영화 목록</h1>
          <MovieCard
              v-for="movie in topmoviesList" :key="movie.pk"
              :movie="movie"
          />
      </b-col>
      <p>{{movie}}</p>
    </b-container>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
export default {
  name: 'MovieView',

  data() {
      return {
          movie:null,
      }
  },
  components: { MovieCard },
  computed: {
      topmoviesList() {
          // console.log(this.$store.state.movieList)
          return this.$store.state.topmoviesList
      },
  },
}
</script>

<style>
.flex {
  display: flex;
}
</style>
