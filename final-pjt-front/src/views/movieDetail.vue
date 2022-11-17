<template>
  <div>
    <p>{{movie}}</p>
  </div>
</template>

<script>
export default {
    name: 'MovieDetail',
    data:{
        movie:null
    },
    methods: {
    getDetail() {
      const movie_id = this.$route.params.id
      // console.log(typeof(movie_id))
      // console.log(movie_id)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/'
      })
        .then((res) => {
          // console.log(res.data)
          // console.log(res.data.movie_id)
          const detail = res.data.filter((movie) => {
            return movie.id === Number(movie_id)
          })
          this.movie = detail[0]
          console.log(this.movie)
        })
    }
},
created(){
    this.getDetail()
}
}
</script>

<style>

</style>