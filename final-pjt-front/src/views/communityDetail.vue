<template>
  <div class="signup bg-dark" style="height:300vh; font-family: 'BMHANNAAir';">
    <div class="commutext">
      <div :class="{'active1': update}">
        <div style="text-align: center;">
          <h1 style="font-family: 'BMHANNAPro';">{{communityDetail.title}}</h1>
        </div>
        <hr>
        <div class="d-flex justify-content-between">
          <h4>작성자 : {{communityDetail.user.username}}</h4>
          <div>
            <h6>작성일자 : {{communityDetail.created_at}}</h6>
            <h6>수정일자 : {{communityDetail.updated_at}}</h6>
          </div>
        </div>
        <hr>
        <div style="width:90%; height:400px; margin: auto; padding: 10px;">
          <h3>{{communityDetail.content}}</h3>
        </div>
      </div>

      <div style="font-family: 'BMHANNAPro';" class="commucreate" :class="{'active1': !update}">
        <div>
            <h4>Title</h4>
            <input placeholder="제목" type="text" v-model.trim="title"/>
        </div>
        <div>
          <hr>
            <h4>Content</h4>
            <textarea style="height:200px; width:100%" type="text" v-model.trim="content"></textarea>
        </div>
        <button class="btn btn-success" @click="updatecommunity()">수정 완료</button>
      </div>

      <div class="d-flex justify-content-between">
        <button class="btn btn-success col-1" @click="back" style="font-family: 'BMDOHYEON';">목록</button>
        <div class="col-2" style="display:flex;" v-if="communityDetail.user.username===me" :class="{'active1': update}">
          <button @click="deletecomunity(communityDetail)" class="btn btn-danger" style="margin-right:10px; font-family: 'BMDOHYEON';" >삭제</button>
          <button class="btn btn-success" @click="updatestate" style="font-family: 'BMDOHYEON';">수정</button>
        </div>
      </div>
      <hr>
      <div :class="{'active1': update}">
        <h1 style="display:flex; font-family: 'BMHANNAPro';">댓글({{commentList.length}})</h1>
          <input v-if="me" @keyup.enter="[createComment(),getComment(),getComment()]" style="width:100%; margin-bottom: 10px;" placeholder="댓글(악플은 안돼용)" type="text" v-model.trim="comment">

        <div v-for="comment in commentList"
        :key="comment.id" style="display:flex; padding: 10px; border-bottom: 1px solid white ; border-top: 1px solid white ;" class="d-flex justify-content-between" :class="{'soojungbg':!soojung}">
          <div>
            <div  style="padding-top:15px;">
              <h3>{{comment.content}}</h3>
              <div v-show="!soojung" :class="{'soojung': comment.id !=index && !soojung}">
            <input  @keyup.enter="[soojungComment(comment),getComment(),getComment()]" style="width:100%; margin-bottom: 10px;" placeholder="Enter 누르면 수정" type="text" v-model.trim="commentsoojung">
        </div>
            </div>
          </div>
          <div style="display:flex;">
            <div style="margin-right:10px;">
              <div style="text-align: right;">일자 : {{comment.created_at}}</div>
              <div style="text-align: right;">작성자 : {{comment.user.username}}</div>
            </div>
            <div class="d-grid gap-2" v-if="comment.user.username===me">
              <button class="butt bg-dark" @click="[deletecomment(comment),getComment(),getComment(),getComment()]">
                <!-- <i class="bi bi-trash3"></i> -->
                <p>X</p>
              </button>
              <button class="butt bg-dark" @click="soojungstate(comment)">
                <!-- <i class="bi bi-trash3"></i> -->
                <p>수정</p>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'
export default {
  name:'communityDetail',
  computed: {
      username() {
          return this.$store.state.user
      },
    },
  data:function(){
    return{
      title:null,
      content:null,
      update:false,
      me:null,
      soojung:true,
      comment:null,
      changecontent:null,
      commentList:[],
      communityDetail:[],
      commentsoojung:null,
      index:null,
    }
  },
  // computed: {
  //     communityDetail() {
  //         return this.$store.state.communityDetail
  //     },
  //   },
    methods:{
      updatecommunity:function(){
        const community={
          title:this.title,
          content:this.content,
        }
        axios({
        method: "put",
        url: `http://127.0.0.1:8000/community/${this.communityDetail.id}/`,
        data:community,
        headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
      })
      .then(()=>{
        this.communityDetail.title=this.title
        this.communityDetail.content=this.content
        this.update=false 

      })
      },  
      updatedata(){
        this.title=this.communityDetail.title
        this.content=this.communityDetail.content
      },
      deletecomunity:function(communityDetail){
        axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/${communityDetail.id}/`,
        headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
      })
      .then(()=>{
        this.$router.push({ name: "community" });
      })
      },  
      back(){
        this.$router.push({ name: "community" });
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
          console.log(res.data)
          this.me=res.data.username
        })
        .catch((err) => {
          console.log(err)
        })
    },
      soojungstate:function(comment){
        if (this.soojung===false){
          this.soojung=true
        }
        this.soojung= !this.soojung
        console.log(comment)
        this.index=comment.id
      },
      updatestate:function(){
        this.update= !this.update
      },
      deletecomment:function(comment){
        axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/${this.communityDetail.id}/comment/${comment.id}/`,
        headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
      })
      .then(()=>{
        console.log("good")
      })
      },  
      soojungComment:function(comment){
        const commentsoojung={content:this.commentsoojung,}
        axios({
        method: "put",
        url: `http://127.0.0.1:8000/community/${this.communityDetail.id}/comment/${comment.id}/`,
        data:commentsoojung,
        headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
      })
      .then(()=>{
        this.soojung=true 
        console.log("good")
      })
      },  
      createComment:function(){
        const comment={content:this.comment,}
        if(comment){
          axios({
            method:"post",
            url:`http://127.0.0.1:8000/community/${this.communityDetail.id}/comment/`,
            data:comment,
            headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
          })
          .then(()=>{
            this.comment=null
          })
        }
      },
      getComment: function() {
        // this.communityDetail=this.$store.state.communityDetail
        this.communityDetail=this.$route.params.community
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/${this.communityDetail.id}/comment/`,

      })
        .then((res) => {
          this.commentList=res.data
          console.log(res)
        })
    },
    reload:function(){
      // this.$store.state.communityDetail=this.communityDetail
      this.$router.go()
      
    },
    },
    created(){
      // console.log(this.$store.state.communityDetail)
      this.getComment()
      this.getUserInfo()
      this.updatedata()
    }
}
</script>

<style>
.commutext{
  width:70%;
  text-align: left;
  position:absolute;
    top: 47%;
    left: 50%;
    transform: translate( -50%, -50% );
    color: white;
    height: 100%;
    margin-top: 100px;
}
.butt{
  width: 50px;
  height: 30px;
  border: none;
  /* color: rgb(220,53,69); */
  color: white;
  padding: 0;
  margin: 0;
  margin-right: 20px;
  border: 2px solid white;
}
.soojung{
  display: none;
}
</style>