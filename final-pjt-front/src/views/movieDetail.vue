<template>
  <div class="user-wrap bg-dark" style="height:100vh;">
    <img @click="imgclick()"  :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" class="img" alt="...">
    <div class="user-text" :class="{ activetext : popupView,recommendactive:!recommendcheck}">
        <img @click="getRecommendations()" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="poster" alt="..." style="border: 0px;">
        <div style="text-align:left;">
            <h1 style="font-family: 'BMHANNAPro';">{{movie.title}}</h1>
            <div class="d-flex justify-content-between" style="display:flex;  margin-bottom:15px; width:30vw;">
              <div style="display: flex;">
                <div v-for="(genre,index) in movie.genres" :key="index" style="margin-right:10px;">
                  <button class="btn btn-success" style="height:40px; ">{{genrenames[genre]}}</button>
                </div>
              </div>
                <div :class="{'activepick' : isPicked}">
                  <!-- <button @click="[addmymovie(), likelist()]" class="btn btn-danger" style="height:40px; width: 80px; margin-right:10px;" >PICK!</button> -->
                  <i @click="[addmymovie(), likelist()]" class="bi bi-suit-heart" style="cursor: pointer;"></i>
                </div>
                <div :class="{'activepick' : !isPicked}">
                  <!-- <button @click="[addmymovie(), likelist()]" class="btn btn-danger" style="height:40px; width: 80px; margin-right:10px;" >Cancel!</button> -->
                  <i @click="[addmymovie(), likelist()]" class="bi bi-suit-heart-fill" style="cursor: pointer;"></i>
                </div>
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
        <div v-if="me" style="margin-left:20px;">
          <div style="display:flex; flex-direction:column; width:27.5vw">
            <div style="display:flex;">
              <input id='review' @keyup.enter="[addreview(), reviewlist(), reviewlist(), reviewlist()]" type="text" v-model="review_content" style="width: 25vw;">
              <button id="review_submit" @click="[addreview(), reviewlist(), reviewlist()]" type="submit">+</button>
            </div>
            <br>
            <div style="display:flex; justify-content: space-between">
              <h4 style="color:crimson; padding-left:10px;"><b>Review({{review_count}})</b></h4>
              <h5 style="color:crimson; padding-right:10px;"><b>작성자</b></h5>
            </div>
            <div v-for="review in review_list" :key="review.id">
              <div style="display:flex; justify-content: space-between; ">  
                <p style="padding-left: 10px;">{{review.content}}</p>
                <div style="display:flex">
                  <p style="padding-right: 15px;">{{review.user.username}}</p>
                  <p v-if="review.user.username===me.username" style="cursor:pointer;" @click="[delete_review(review), reviewlist(), reviewlist()]">X</p>
                </div>
              </div>
              <hr style="margin-top:0px;">
            </div>
            <div v-if="review_count > 10" style="display:flex; justify-content: center;" >
              <button @click="[prepage(), reviewlist(), reviewlist()]" class="btn btn-outline-danger" style="width: 60px; height: 35px; margin:5px;"> 이전 </button>
              <!-- <button v-for="nowpage in page_list" :key="nowpage" class="btn btn-outline-danger" style="width: 35px; height: 35px; margin:5px;">{{nowpage}}</button> -->
              <button @click="[nextpage(), reviewlist(), reviewlist()]" class="btn btn-outline-danger" style="width: 60px; height: 35px; margin:5px;"> 다음 </button>
            </div>
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
            me: null,
            isPicked: false,
            review_content: null,
            review_list : [],
            page: 1,
            review_count : 0,
            max_page : null,
            page_list : [],
            pick: false,
            mylist : null,
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
          // console.log(res)
          const movie_id = this.$route.params.id
          this.me = res.data
          
          // 나의 like_movies에 해당 영화가 들어있으면 isPicked를 통해 버튼바꾸기
          if (this.me.like_movies.includes(Number(movie_id))) {
            console.log('있어용')
            this.isPicked = true

          } else {
            console.log('없어용')
            this.isPicked = false

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
      // console.log(this.movie.id)
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
        .then((res) => {
          this.isPicked = res.data
          // this.getUserInfo()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    addreview() {
      console.log(this.review_content)
      const token = localStorage.getItem('jwt')
  
      if (!this.review_content) {
        return alert ('리뷰는 한 글자 이상 작성해주세요')
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        data: {
          content: this.review_content,
        },
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res)
          this.review_content=''
        })
    },
    reviewlist() {
      const movie_id = this.$route.params.id
      // console.log(movie_id)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_id}/review/`,
        
      })
        .then((res) => {
          // console.log(222222222)
          // console.log(res)
          this.review_count = res.data.length
          // console.log(this.review_count)
          this.maxpage = Math.ceil(this.review_count / 10)
          // console.log(this.maxpage)
          for (let i=1 ; i<= this.maxpage; i++) {
            this.page_list.push(i)
          }
          // console.log(this.page_list)

          if (this.page === 1) {
            this.review_list = res.data.slice(0, 10)
          } else {
            this.review_list = res.data.slice(this.page*10 -10, this.page*10)
          }
          console.log(this.review_list)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    delete_review(review) {
      const token = localStorage.getItem('jwt')
      const movie_id = this.$route.params.id
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${movie_id}/review/${review.id}/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then(() => {
          console.log('review delete')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    nextpage() {
      // console.log(this.maxpage)
      if (this.page < this.maxpage) {
        return this.page += 1
      }
    },
    prepage() {
      if (this.page > 1) {
        return this.page -= 1
      }
    },
  },
  created(){
    if (this.movie){
      this.getDetail2()
    }
    if (this.movie){
      this.getDetail1()
    }
    this.reviewlist()
    this.getRecommendations()
    this.getUserInfo()
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
    width:30vw;
    margin-right:20px;
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
.activepick{
  display: none;
}

#review {
  width: 500px;
  height: 32px;
  font-size: 15px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-left: 10px;
  /* background-color: rgb(233, 233, 233); */
  /* background: transparent; */
  opacity: 40%;
  color: black;
}

#review_submit {
  outline: none;
  border : 0;
  border-radius: 90%;
  height: 32px;
  width: 35px;
  margin-left: 5px;
  /* background-color: rgb(233, 233, 233); */
  opacity: 50%;
}

i{
  padding-top: px;
  font-size: 40px;
  color: crimson;
}
</style>