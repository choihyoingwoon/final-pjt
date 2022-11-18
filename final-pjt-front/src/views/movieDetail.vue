<template>
  <div class="user-wrap bg-dark">
      <img  :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" class="img" alt="...">
    <div class="user-text" :class="{ activetext : popupView }">
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="poster" alt="...">
        <div style="text-align:left;">
            <h1>{{movie.title}}</h1>
            <!-- <div style="display:flex;">
                <h4>{{movie.genres[0]}}</h4>
                <div v-for="(genre,index) in movie.genres" :key="index" style="margin-right:10px;">
                    <button class="btn btn-success">{{genre}}</button>
                </div>
            </div> -->
            <div>
                <h4>인기 : {{movie.popularity}}</h4>
                <h4>개봉일 : {{movie.release_date}}</h4>
                <h4>평점 : {{movie.vote_average}}</h4>
                <p class="story">{{movie.overview}}</p>
                <button class="btn btn-danger" @click="movieVideo(movie), openYoutube()">예고편 보기</button>
            </div>
        </div>
    </div>
    <div class="user-text popup-view" :class="{ active : popupView }">
      <pop-up @close-popup="openPopup()"></pop-up>
      <button class="btn btn-danger" @click="movieVideo(movie), openYoutube()">예고편 끄기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PopUp from '../components/PopUp.vue'

export default {
    name: 'MovieDetail',
    components:{
    PopUp,
  },
    data(){
        return{
            movie:[],
            video:null,
            popupView:false,
        }
    },
    methods: {
    getDetail1() {
      const movie_id = this.$route.params.id
      // console.log(typeof(movie_id))
      // console.log(movie_id)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/top_movies/'
      })
        .then((res) => {
          // console.log(res.data)
          // console.log(res.data.movie_id)
          const detail = res.data.filter((movie) => {
            return movie.id === Number(movie_id)
          })
          if (detail[0]){
            this.movie = detail[0]
          }
          console.log(this.movie)

        })
    },
    getDetail2() {
      const movie_id = this.$route.params.id
      // console.log(typeof(movie_id))
      // console.log(movie_id)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/now_movies/'
      })
        .then((res) => {
          // console.log(res.data)
          // console.log(res.data.movie_id)
          const detail = res.data.filter((movie) => {
            return movie.id === Number(movie_id)
          })
          if(detail[0]){
            this.movie = detail[0]
          }
        })
    },
    movieVideo(movie){
      console.log(movie)
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
      })
      .then(res=>{
        this.$store.state.movieVideo= res.data.results[0]
      })
      .catch(err=>{
        console.log(err)
      })
    },
    openYoutube(){
        this.popupView=(this.popupView) ? false:true
    }
},
created(){
  if (this.movie){
    this.getDetail2()
  }
  if (this.movie){
    this.getDetail1()
  }
}
}
</script>

<style>
.story{
  font-weight: bold;
}
.user-wrap{
    width:100%;
    position: relative;
    margin-top: 55px;
}
.img{
    /* position:fixed;
    right:0px; */
    width:100%;
    height: 100vh;
    vertical-align: middle;
    opacity: 0.3;
}
.user-text{
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50% );
    color: white;
    display: flex;
    height: 100%;
    margin-top: 100px;
}
.poster{
    height: 60vh;
    width:100%;
    margin-right:20px
}
.popup-view{
  opacity: 0;
  display: none;
  visibility: hidden;
}
.active{
  opacity: 1;
  display: block;
  visibility: visible;
}
.activetext{
  opacity: 1;
  display: none;
  visibility: visible;
}
</style>