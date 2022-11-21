<template>
  <div class="user-wrap bg-dark" style="height:100%">
    <img @click="imgclick()"  :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" class="img" alt="...">
    <div class="user-text" :class="{ activetext : popupView,recommendactive:!recommendcheck}">
        <img @click="getRecommendations()" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="poster" alt="...">
        <div style="text-align:left;">
            <h1 style="font-family: 'BMHANNAPro';">{{movie.title}}</h1>
            <div style="display:flex;  margin-bottom:15px;">
                <div v-for="(genre,index) in movie.genres" :key="index" style="margin-right:10px;">
                    <button class="btn btn-success" style="height:40px; ">{{genrenames[genre]}}</button>
                </div>
                <button v-if="!Picked" @click="addmymovie" class="btn btn-danger" style="height:40px; width: 80px; margin-right:10px;">PICK!</button>
                <button v-else @click="addmymovie" class="btn btn-danger" style="height:40px; width: 80px; margin-right:10px;">Cancel!</button>
            </div>
            <div style="font-family:'BMHANNAAir';">
                <h4 >인기 : {{movie.popularity}}</h4>
                <h4>개봉일 : {{movie.release_date}}</h4>
                <h4>평점 : {{movie.vote_average}}점</h4>
                <p style="word-break:keep-all">{{movie.overview}}</p>
                <button class="btn btn-danger" style="font-family: 'BMDOHYEON';" @click="movieVideo(movie), openYoutube()">예고편 보기</button>
                <button class="btn btn-danger" style="font-family: 'BMDOHYEON';" @click="getRecommendations()">비슷한 영화 추천</button>
              </div>
        </div>
    </div>
    <div class="popup-view" :class="{ active : popupView }">
      <pop-up @close-popup="openPopup()"></pop-up>
      <button class="btn btn-danger" style="font-family: 'BMDOHYEON';" @click="movieVideo(movie), openYoutube()">예고편 끄기</button>
    </div>
    <b-col class="reco" align-self="center" :class="{recommendactive:recommendcheck}">
          <div>
            <h3 style="color:white; font-family: 'BMHANNAPro';">
              {{movie.title}}과(와) <span style="color:red"><img src="@/assets/sparkling.gif" style="height:30px; margin:0; padding:0;" alt="">비슷한<img src="@/assets/sparkling.gif" style="height:30px; margin:0; padding:0;" alt=""></span> 영화
            </h3>
            
            <div class="movie_list" style="display:scroll;" >
              <recommendMovieCard
                  v-for="movie in recommendations" :key="movie.pk"
                  :movie="movie"
              />
            </div>
            <button class="btn btn-danger"  @click="imgclick()" style="width:50%; font-family: 'BMDOHYEON';">추천 영화 끄기</button>
          </div>
      </b-col>
  </div>
</template>


<script>
import axios from 'axios'
import PopUp from '../components/PopUp.vue'
import recommendMovieCard from '@/components/recommendMovieCard'
import VueJwtDecode from 'vue-jwt-decode'

export default {
    name: 'MovieDetail',
    components:{
    PopUp,recommendMovieCard,
    },
    computed: {
      genrenames() {  
        const genrelist =  {28 : "액션", 12:"모험", 16:"애니메이션",
        35:"코미디", 80:"범죄", 99:"다큐멘터리", 18:"드라마",
        10751:"가족", 14:"판타지", 36:"역사", 27:"공포",
        10402:"음악", 9648:"미스터리", 10749:"로맨스", 878:"SF",
        10770:"TV 영화", 53:"스릴러", 10752:"전쟁", 37:"서부"}
        return genrelist
      },
      Picked() {
        return this.isPicked
      }
    },
    data(){
        return{
            movie:[],
            video:null,
            popupView:false,
            recommendcheck:true,
            recommendations:[],
            me: [],
            isPicked: '',
        }
    },
    methods: {
      getGenres:function(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/top_movies/',
      })
      .then(res=>{
        this.$store.state.topmoviesList = res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
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
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
      })
      .then(res=>{
        this.$store.state.movieVideo= res.data.results[0]
        this.recommendcheck= true
        console.log(this.$store.state.movieVideo)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getRecommendations(){
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/similar?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR&page=2`,
      })
      .then(res=>{
        this.recommendations= res.data.results
        this.recommendcheck= !this.recommendcheck
        console.log(this.recommendations)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    openYoutube(){
        this.popupView=(this.popupView) ? false:true
    },
    clickRecommend(){
      this.recommendcheck= !this.recommendcheck
    },
    imgclick(){
      this.recommendcheck=true
      this.popupView=false
    },
    getUserInfo() {
      const token = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(token)
      // console.log(info)
      // const user_id = info.user_id
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/mypage/',
        data: {
          info
        },
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res)
          this.me = res.data
          console.log(this.me)
          if (this.me.like_movies.includes(this.movie.id)) {
            this.isPicked = true
            console.log(1)
          } else {
            this.isPicked = false
            console.log(0)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    addmymovie(){
      // this.$store.dispatch('addMovie', this.movie)
      const token = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(token)
      const item = {
        meId : info.user_id,
        movieId : this.movie.id,
      }
      // console.log(item)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${info.user_id}/${this.movie.id}/likes/`,
        data: {
          item,
        },
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then(() => {
          this.getUserInfo()
        })
        .catch((err) => {
          console.log(err)
        })
    }
},
created(){
  this.getUserInfo()
  if (this.movie){
    this.getDetail2()
  }
  if (this.movie){
    this.getDetail1()
  }
  this.getRecommendations()
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
.reco{
  position:absolute;
    top: 10%;
    width:100%;
    display: block;
}
.poster{
    height: 50vh;
    width:100%;
    margin-right:20px
}
.popup-view{
      position:absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50% );
    color: white;
    display: flex;
    height: 100%;
    margin-top: 100px;
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
.recommendactive{
  opacity: 1;
  display: none;
  visibility: visible;
}
.mid{
  top: 50%;
}
</style>