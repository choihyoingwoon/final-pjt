<template>
  <div class="signup bg-dark">
    <br>
    <h1 style="font-family: 'BMHANNAPro';">Community</h1>
    <hr>
    <div class="commucreate" :class="{'active1': active}">
        <button style="font-family: 'BMHANNAAir';" class="btn btn-danger"  @click="activeCreate"><h4>create</h4></button>
    </div>
    <div style="font-family: 'BMHANNAPro';" class="commucreate" :class="{'active1': !active}">
        <div>
            <h4>Title</h4>
            <input placeholder="제목" type="text" v-model.trim="title"/>
        </div>
        <div>
          <hr>
            <h4>Content</h4>
            <textarea style="height:200px; width:100%" type="text" v-model.trim="content"></textarea>
        </div>
    <button style="font-family: 'BMHANNAAir';" class="btn btn-danger" @click="[createCommunity(), reload()]"><h4>create</h4></button>
    </div>
    <hr>
    <!-- <div class="flex" id="article">
      <h4>번호</h4>
      <h4>제목</h4>
      <h4>작성자</h4>
    </div>
    <ul>
        <div id= "articlelist" v-for="community in communities" :key="community.id">
          <h5>{{community.id}}</h5>  
          <h5>{{community.title}}</h5>
          <h5>{{community.user.username}}</h5>
        </div>
    </ul> -->
    <table class="table table-dark table-bordered table-striped" id="table" style="width:60%; margin: auto;">
      <thead>
        <tr style="font-family: 'BMHANNAPro';">
          <th scope="col" style="width:100px; height: 70px;"><h3>번호</h3></th>
          <th scope="col"><h3>제목</h3></th>
          <th scope="col" style="width:15%;"><h3>작성일자</h3></th>
        </tr>
      </thead>
      <tbody style="font-family: 'BMHANNAAir';">
        <tr v-for="community in communities" :key="community.id" @click="gocommunityDetail(community)" >
          <th style="padding-top:30px !important;" scope="row"><h1>{{community.id}}</h1></th>
          <td><h3>{{community.title}}</h3><p>작성자 : {{community.user.username}}</p></td>
          <th style="padding-top:25px !important;"><h4>{{community.created_at}}</h4></th>
          <!-- <button @click="gocommunityDetail(community)">자세히</button> -->
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
    name:'communityList',
    data: function() {
    return {
      communities: null,
      title:null,
      content:null,
      active:false,
    };
  },
//   computed:{
//     getUser(){
//         return this.$store.state.user
//     }
//   },

    methods:{
        getCommunity: function() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/community/",
      })
        .then((res) => {
          this.communities = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setToken: function() {
      // 1. LocalStorage에서 jwt 토큰을 가져옴
      const token = localStorage.getItem("jwt");
      // 2. header에 token을 넣기 위한 준비
      const config = {
        // Bearer 뒤에 공백 필수
        Authorization: `Bearer ${token}`,
      };
      // 3. 응답
      return config;
    },
    createCommunity: function() {
      const communityItem = {
        title: this.title,
        content:this.content,
      };
      console.log(communityItem)
      if (communityItem.title && communityItem.content) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/community/",
          data: communityItem,
          // 로컬스토리지에 저장한 토큰을 꺼내와서 요청의 헤더정보에 포함시킨다.
          headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
        })
          .then(() => {
            this.active =!this.active
            console.log(this.communities)
          })
          .catch((err) => {
            console.error(err);
            this.active =!this.active
          });
      }else{
        alert("title과 content를 입력하세요")
      }
    },
    activeCreate : function(){
        this.active =!this.active
    },
    reload:function(){
      this.$router.go()
    },
    gocommunityDetail : function(community){
      this.$store.state.communityDetail=community
      this.$router.push({ name: "communitydDetail"});
    },


    },
    created:function(){
        this.getCommunity();
    },

}
</script>

<style>
.commucreate{
    line-height: 30px;
    width: 50%;
    margin: auto;
    text-align: left;
}
.active1{
    display:none;
}

#article {
  display: flex;
  justify-content: space-around;
  padding-top: 30px;
}

#articlelist {
  display: flex;
  justify-content: space-around;
  padding-top: 30px;
}

#table{
  color: white;
}
td{
  text-align: left;
  padding-top:20px !important;
  padding-left:50px !important;
}
</style>

