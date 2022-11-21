<template>
  <div class="user-wrap bg-dark" style="height:100vh;">
    <div class="commutext">
      <div class="d-flex justify-content-between" style="display:flex;">
        <h1>제목 : {{communityDetail.title}}</h1>
        <span style="text-align:right">
          <h6>작성자 : {{communityDetail.user.username}}</h6>
          <h6>작성일자 : {{communityDetail.created_at}}</h6>
          <h6>수정일자 : {{communityDetail.updated_at}}</h6>
        </span>
      </div>
      <hr>
      <h3>{{communityDetail.content}}</h3>
      <hr>
      <h1>댓글</h1>
      <input placeholder="댓글(악플은 안돼용)" @keyup.enter ="createComment" type="text" v-model.trim="comment">
      <button @click="createComment">입력</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'communityDetail',
  data:function(){
    return{
      comment:null
    }
  },
  computed: {
      communityDetail() {
          return this.$store.state.communityDetail
      },
    },
    methods:{
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
            console.log(comment)
          })
          .catch((err)=>{
            console.log(err)
          })
        }
      }
    }
}
</script>

<style>
.commutext{
  width:70%;
  text-align: left;
  position:absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50% );
    color: white;
    height: 100%;
    margin-top: 100px;
}
</style>