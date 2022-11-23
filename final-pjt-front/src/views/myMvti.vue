<template>
  <div class="signup" :class="{'bodyheight': check}" style="background-color:black"><br>
    <h1 style="font-family: 'BMHANNAPro';">MVTI (<span style="color:green">M</span>o<span style="color:green">V</span>ie <span style="color:green">T</span>ype <span style="color:green">I</span>ndicator) 테스트</h1>
    <hr>
    <br>
    <div style="display:flex; width:710px; margin: auto;">
        <img src="@/assets/tree.png" alt="" style="width:100px;">
        <div>
            <div style="display:flex; justify-content: center;" >
                <h3 style="font-family: 'BMHANNAPro';">당신의</h3>
                <h3 style="font-family: 'BMHANNAPro'; padding-left:10px; color:green">MVTI</h3>
                <h3 style="font-family: 'BMHANNAPro';">는 무엇인가요?🤔</h3>
            </div>
                <h2 style="font-family: 'BMHANNAPro';">궁금하다면 좋아하는 <span style="color:red">장르</span>를 골라주세요!</h2>
        </div>
        <img src="@/assets/tree.png" alt="" style="width:100px;">
    </div>
    <div id="select_genre">
        <div id="select_genre_one">
            <button id="one_btn" @click="select1" :class="{'select' : horror, 'nonselect': !horror}" style="font-family: 'BMHANNAPro';" >공포</button>
            <br>
            <h3>VS</h3>
            <br>
            <button id="one_btn" @click="select2" :class="{'select' : comedy , 'nonselect': !comedy}" style="font-family: 'BMHANNAPro';">코미디</button>
        </div>

        <div id="select_genre_one">
            <button id="one_btn" @click="select3" :class="{'select' : romance , 'nonselect': !romance}"  style="font-family: 'BMHANNAPro';">로맨스</button>
            <br>
            <h3>VS</h3>
            <br>
            <button id="one_btn" @click="select4" :class="{'select' : thriller , 'nonselect': !thriller}" style="font-family: 'BMHANNAPro';">스릴러</button>
        </div>
        <div id="select_genre_one">
            <button id="one_btn" @click="select5" :class="{'select' : drama , 'nonselect': !drama}" style="font-family: 'BMHANNAPro';">드라마</button>
            <br>
            <h3>VS</h3>
            <br>
            <button id="one_btn" @click="select6" :class="{'select' : sf , 'nonselect': !sf}" style="font-family: 'BMHANNAPro';">SF</button>
        </div>
        <div id="select_genre_one">
            <button id="one_btn" @click="select7" :class="{'select' : action , 'nonselect': !action}" style="font-family: 'BMHANNAPro';">액션</button>
            <br>
            <h3>VS</h3>
            <br>
            <button id="one_btn" @click="select8" :class="{'select' : animation , 'nonselect': !animation}" style="font-family: 'BMHANNAPro';">애니메이션</button>
        </div>
    </div>
    <button class="btn btn-outline-danger" @click="[check_mymvti(), mvti_movie1(), mvti_movie2(), mvti_movie3(), mvti_movie4()]" style="width: 50%;">나의 MVTI 확인하기!</button><br>
    <div v-if="check" >
        <br>
        <h3>.</h3>
        <h3>.</h3>
        <h3>.</h3>
        <h1 style="text-decoration: underline overline; text-underline-position: under; font-family: 'BMHANNAPro'; margin-top: 30px; "> 당신의 MVTI는 <b>✨{{mymvti}}✨ </b></h1>
        <br>
        <div id=mvtibox style="text-align:center;">
            <div style="display:flex; flex-direction: column; margin-bottom: 20px; width: 600px; margin:auto; align-items: center;">
                <div style="display:flex">
                    <h2 style="text-align: left; margin-left: 3%; margin-top: 30px; color:green; font-family: 'BMHANNAPro';">{{mymvti}}</h2>
                    <h2 style="text-align: left; width:350px;; 3%; margin-top: 30px; font-family: 'BMHANNAPro';">들의 취향을 저격할 영화!</h2>
                </div>
                <i @click="[mvti_movie1(), mvti_movie2(), mvti_movie3(), mvti_movie4()]" style="width:20%; margin-left:10px; margin-top:22px; cursor: pointer; " class="bi bi-arrow-clockwise"></i>
            </div>
            <div>
                <div style="margin: auto; width: 1150px; display:flex; padding-left: 15px;">
                    <div style="height: 45vh;">
                        <img style="border:0px;" @click="getDetail(movie1)" v-if="movie1" :src="`https://image.tmdb.org/t/p/original/${movie1.poster_path}`" class="poster cardmove" alt="...">
                    </div>
                    <div style="height: 45vh;">
                        <img style="border:0px;" @click="getDetail(movie2)" v-if="movie2" :src="`https://image.tmdb.org/t/p/original/${movie2.poster_path}`" class="poster cardmove" alt="...">
                    </div>
                    <div style="height: 45vh;">
                        <img style="border:0px;" @click="getDetail(movie3)" v-if="movie3" :src="`https://image.tmdb.org/t/p/original/${movie3.poster_path}`" class="poster cardmove" alt="...">
                    </div>
                    <div style="height: 45vh;">
                        <img style="border:0px;" @click="getDetail(movie4)" v-if="movie4" :src="`https://image.tmdb.org/t/p/original/${movie4.poster_path}`" class="poster cardmove" alt="...">
                    </div>
                </div>
            </div>
        </div>
        <hr>
    </div>

  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'myMvti',
    data() {
        return{
            horror : false,
            comedy : false,
            romance : false,
            thriller : false,
            drama : false,
            sf : false,
            action : false,
            animation : false,
            mymvti_list : ['', '', '', ''],
            check: false,
            mymvti: '',
            movie1_list : [],
            movie2_list : [],
            movie3_list : [],
            movie4_list : [],
            movie1 : null,
            movie2 : null,
            movie3 : null,
            movie4 : null,
        }
    },
    computed: {
        topmoviesList() {
          return this.$store.state.topmoviesList
        },
    },
    methods: {
        select1() {
            this.horror = !this.horror
            if (this.horror) {
                this.comedy = false
            }
            console.log(this.horror)
            if (!this.mymvti_list.includes('horror')) {
                this.mymvti_list[0] = 'horror'
            } else {
                this.mymvti_list[0] = ''
            }
        },
        select2() {
            this.comedy = !this.comedy
            if (this.comedy) {
                this.horror = false
            }
            if (!this.mymvti_list.includes('comedy')) {
                this.mymvti_list[0] = 'comedy'
            } else {
                this.mymvti_list[0] = ''
            }
        },
        select3() {
            this.romance = !this.romance
            if (this.romance) {
                this.thriller = false
            }
            if (!this.mymvti_list.includes('romance')) {
                this.mymvti_list[1] = 'romance'
            } else {
                this.mymvti_list[1] = ''
            }
        },
        select4() {
            this.thriller = !this.thriller
            if (this.thriller) {
                this.romance = false
            }
            if (!this.mymvti_list.includes('thriller')) {
                this.mymvti_list[1] = 'thriller'
            } else {
                this.mymvti_list[1] = ''
            }
        },
        select5() {
            this.drama = !this.drama
            if (this.drama) {
                this.sf = false
            }
            if (!this.mymvti_list.includes('drama')) {
                this.mymvti_list[2] = 'drama'
            } else {
                this.mymvti_list[2] = ''
            }
        },
        select6() {
            this.sf = !this.sf
            if (this.sf) {
                this.drama = false
            }
            if (!this.mymvti_list.includes('sf')) {
                this.mymvti_list[2] ='sf'
            } else {
                this.mymvti_list[2] = ''
            }
        },
        select7() {
            this.action = !this.action
            if (this.action) {
                this.animation = false
            }
            if (!this.mymvti_list.includes('action')) {
                this.mymvti_list[3] = 'action'
            } else {
                this.mymvti_list[3] = ''
            }
        },
        select8() {
            this.animation = !this.animation
            if (this.animation) {
                this.action = false
            }
            if (!this.mymvti_list.includes('animation')) {
                this.mymvti_list[3] = 'animation'
            } else {
                this.mymvti_list[3] = ''
            }
        },
        check_mymvti() {
            console.log(this.mymvti_list)
            // console.log(this.mymvti_list[0])
            for (let i=0; i< 4; i++) {
                if (this.mymvti_list[i] == '') {
                    return alert('4개의 장르를 선택해 주세요!')
                }
            }
            this.check = true
            let final_mvti = ''
            this.mymvti_list.map((genre) =>
                 final_mvti += genre[0].toUpperCase()
            )
            // console.log(final_mvti)
            this.mymvti = final_mvti

        },
        mvti_movie1(){
            this.movie1_list = []
            if (this.mymvti_list[0] === 'horror') {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 27){
                            this.movie1_list.push(this.topmoviesList[i])
                        }
                    }
                } 
                console.log(this.movie1_list)
                return this.movie1 = _.sample(this.movie1_list)
                
            } else {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 35){
                            this.movie1_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie1 = _.sample(this.movie1_list)
            }
        },
        mvti_movie2(){
            this.movie2_list = []
            if (this.mymvti_list[1] === 'romance') {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 10749){
                            this.movie2_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie2 = _.sample(this.movie2_list)
            } else {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 53){
                            this.movie2_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie2 = _.sample(this.movie2_list)
            }
        },
        mvti_movie3(){
            this.movie3_list = []
            if (this.mymvti_list[2] === 'drama') {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 18){
                            this.movie3_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie3 = _.sample(this.movie3_list)
            } else {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 878){
                            this.movie3_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie3 = _.sample(this.movie3_list)
            }
        },
        mvti_movie4(){
            this.movie4_list = []
            if (this.mymvti_list[3] === 'action') {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 28){
                            this.movie4_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie4 = _.sample(this.movie4_list)
            } else {
                for(let i=0; i<this.topmoviesList.length; i++){
                    for (const num in this.topmoviesList[i].genres){
                        if (this.topmoviesList[i].genres[num] === 16){
                            this.movie4_list.push(this.topmoviesList[i])
                        }
                    }
                }
                return this.movie4 = _.sample(this.movie4_list)
            }
        },
        getDetail(movie) {
            this.$router.push({ name: 'detail', params: { id: `${movie.id}`}})
        }
    },
    created() {
        this.mvti_movie1()
        this.mvti_movie2()
        this.mvti_movie3()
        this.mvti_movie4()
    }
}
</script>

<style>

#select_genre{
    display: flex;
    justify-content: center;
}

#select_genre_one{
    display: flex;
    flex-direction: column;
    margin: 50px;
    /* border: 10px solid rgb(213, 247, 212); */
    border-radius: 10%;
}

.select {
    background-color: rgb(220, 53, 69);
    color: white;
}
.nonselect{
    background-color : rgb(33, 37, 41);
    color: white;
}

#one_btn {
    width: 150px;
    height: 70px;
    font-size: 20px;
    /* color: white; */
    margin: 0.5px;
    border-radius: 20px;
    /* background-color:rgb(220,53,69); */
    /* color: rgb(220,53,69); */
    border: 2px solid white;
    /* outline-color: bisque ; */
}
#one_btn:hover{
    filter: brightness(150%);
    
}

.poster{
    border: 2px solid white;
    height: 360px; 
    width:240px;
    margin-right:20px;
    border-radius: 20px;
    /* justify-items: center;  */
}

/* .cardmove{
    transition: all 0.17s linear;
    overflow: hidden;
    height: 360px;
    width:240px;
    float:left;
    padding: 0;
    margin: 20px;
    display: flex;
} */
    .cardmove:hover{
        transform: scale(1.1);
        
    }
    .bodyheight{
        height: 100%;
    }

#mvtibox{
    border : 3px solid white;
    /* padding-bottom: 50px; */
    margin-left : 200px;
    margin-right : 200px;
}


</style>