<template>
  <div class="signup" style="text-align:left; padding-left:50px; background-color: black;" :class="{'hinonactive': !hi, 'hiactive': hi}">
    <span v-if="!(arr.length !=0 || genrearr.length !=0)">
      <img v-if="!nodata" src="@/assets/loading.gif" alt="" style="width:200px; filter: invert(100%); margin-left: 40vw; margin-top: 20vh; margin-bottom: 10px;">
      <div v-if="nodata" style="text-align:center;">
      <img src="@/assets/noResult.png" alt="" style="margin-top:50px; margin-bottom:20px; filter: invert(100%);">
      <h1 style="font-family: 'BMHANNAPro'; color: white;">검색 결과가 없습니다. </h1>
    </div>
    </span>
    <span>
      <br>
      <div style="display:flex; flex-direction:column;">
        <div style="width:100%;" v-if="arr.length !=0">
          <h1 style="font-family: 'BMHANNAPro';">'{{this.$route.params.searchtext}}'이(가) 제목에 포함된 영화</h1>
              <MovieCard
                v-for="movie in arr"
                :key="movie.id" 
                :movie="movie"
              />
            </div>
        <div style="width:100%;" v-if="genrearr.length !=0">
          <h1 style="font-family: 'BMHANNAPro';">'{{this.$route.params.searchtext}}'이(가) 장르인 영화</h1>
          <MovieCard
            v-for="movie in genrearr"
            :key="movie.id" 
            :movie="movie"
          />
        </div>
      </div>
    </span>

  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name:'searchPage',
  components: { 
    MovieCard, 
  },
  data:function(){
    return{
      arr:[],
      genrearr:[],
      realgenre:null,
      hi:false,
      nodata:false,
    }
  },
    computed: {
      topmoviesList() {
          return this.$store.state.topmoviesList
      },
      nowmoviesList() {
          return this.$store.state.nowmoviesList
      },
      genrenames() {
        
        const genrelist =  {28 : "액션", 16:"애니메이션",
        35:"코미디", 80:"범죄", 18:"드라마",
        10751:"가족", 14:"판타지", 27:"공포",
        10402:"음악",  10749:"로맨스", 878:"SF",
        53:"스릴러", 10752:"전쟁"}
        return genrelist
  
        }
  },
  methods:{
    changetime(){
      this.nodata=true
      this.search()
    this.genresearch()
    this.heightative()
    },
    heightative(){
      if (this.arr.length <4 && this.genrearr.length<4){
        this.hi=false
      } else{
        this.hi=true
      }
    },
    search(){
      this.arr=[]
      for(let i=0; i<this.topmoviesList.length; i++){
          if (this.topmoviesList[i].title.includes(this.$route.params.searchtext)){
            this.arr.push(this.topmoviesList[i])
          }
      }
    },
    genresearch(){
        this.genrearr=[]
        const genre_nums = [28, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 10749, 878,
      53, 10752]
      for (const genre_num in genre_nums) {
        if (this.genrenames[genre_nums[genre_num]] === this.$route.params.searchtext) {
          this.realgenre=genre_nums[genre_num]
        }
      }
        for(let i=0; i<this.topmoviesList.length; i++){
            if (this.topmoviesList[i].genres.includes(this.realgenre)){
              this.genrearr.push(this.topmoviesList[i])
            }
        }
      },
  },
  created(){
    this.search()
    this.genresearch()
    this.heightative()
    setTimeout(this.changetime,2000)
  }
}
</script>

<style>
.hiactive{
  height:100%
}
.hinonactive{
  height: 100vh
}
.searchmovie_list {
    white-space: nowrap;
    }
</style>