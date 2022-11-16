<template>
  <div style="display: auto; display: flex; ">
    <b-container class="bg-dark" fluid style="padding:15px; padding:auto; ">
      <b-col align-self="center">
          <MovieCard
              v-for="movie in moviesList" :key="movie.pk"
              :movie="movie"
          />
      </b-col>
    </b-container>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieView',

  // data() {
  //     return {
  //         moviesList : []
  //     }
  // },
  components: { MovieCard },
  computed: {
      moviesList() {
          // console.log(this.$store.state.movieList)
          return this.$store.state.moviesList
      }
  },
}
</script>

<style>
.flex {
  display: flex;
}
</style>
