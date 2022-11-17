<template>
  <div class="user-wrap bg-dark">
    <div class="user-image" >
        <img  :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" class="img" alt="...">
    </div>
    <div class="user-text">
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="poster" alt="...">
        <div style="text-align:left;">
            <h1>{{movie.title}}</h1>
            <div style="display:flex;">
                <div v-for="genre in movie.genres" :key="genre" style="margin-right:10px;">
                    <button class="btn btn-success">{{genre}}</button>
                </div>
            </div>
            <hr>
            <div>
                <h4>인기 : {{movie.popularity}}</h4>
                <h4>개봉일 : {{movie.release_date}}</h4>
                <h4>평점 : {{movie.vote_average}}</h4>
                <p>{{movie.overview}}</p>
                <button @click="openYoutube()">예고편 보기</button>
            </div>
        </div>
    </div>
    <div class="popup-view" :class="{ active : popupView }">
      <pop-up @close-popup="openPopup()"></pop-up>
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
        })
    },
    movieVideo(){
        console.log(this.movie.id)
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
      })
      .then(res=>{
        this.$store.state.movieVideo= res.data.results
        console.log(res.data.results)
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
    this.getDetail()
    this.movieVideo()

}
}
</script>

<style>
.user-wrap{
    width:100%;
    position: relative;
    margin-top: 55px;
}
.img{
    width:100%;
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
</style>