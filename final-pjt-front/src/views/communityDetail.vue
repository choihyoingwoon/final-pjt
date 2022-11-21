<template>
  <div class="signup bg-dark" style="height:100vh; font-family: 'BMHANNAAir';">
    <div class="commutext">
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
      <hr>
      <h1>댓글</h1>
      <input style="width:100%;" placeholder="댓글(악플은 안돼용)" @keyup.enter ="createComment" type="text" v-model.trim="comment">
      <div v-for="comment in commentList"
      :key="comment.id">
        <p>{{comment.content}}</p>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'communityDetail',
  data:function(){
    return{
      comment:null,
      changecontent:null,
      commentList:[]
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
      },
      getComment: function() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/${this.communityDetail.id}/comment/`,
      })
        .then((res) => {
          this.commentList=res.data
        })
        .catch((err) => {
          console.log(err);
        });
    },
    },
    created(){
      this.getComment()
    }
}
</script>

<style>
.commutext{
  width:70%;
  text-align: left;
  position:absolute;
    top: 45%;
    left: 50%;
    transform: translate( -50%, -50% );
    color: white;
    height: 100%;
    margin-top: 100px;
}
</style>