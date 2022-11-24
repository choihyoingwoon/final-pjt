<template>
  <div class="signup" style="background-color:black">
    <br>
    <h1 style="font-family: 'BMHANNAPro';">Community</h1>
    <div v-if="me">
      <hr>
      <div class="commucreate" :class="{'active1': active}" >
          <button style="font-family: 'BMHANNAAir';" class="btn btn-success"  @click="activeCreate"><h4>create</h4></button>
      </div>
      <hr>
    </div>
    <div style="font-family: 'BMHANNAPro';" class="commucreate" :class="{'active1': !active}">
        <div>
            <h4>Title</h4>
            <input placeholder="제목" type="text" v-model.trim="title" style="color:black;" />
        </div>
        <div>
          <hr>
            <h4>Content</h4>
            <textarea style="height:200px; width:100%; color:black;" type="text" v-model.trim="content"></textarea>
        </div>
    <button style="font-family: 'BMHANNAAir';" class="btn btn-danger" @click="[createCommunity(), reload()]"><h4>create</h4></button>
    </div>

    <table class="table table-hover" id="table" style="width:60%; margin: auto;">
      <thead>
        <tr style="font-family: 'BMHANNAPro'; background-color: rgb(50, 50, 50);">
          <th scope="col" style="width:100px; height: 70px;"><h3>번호</h3></th>
          <th scope="col"><h3>제목</h3></th>
          <th scope="col" style="width:15%;"><h3>작성일자</h3></th>
        </tr>
      </thead>
      <tbody style="font-family: 'BMHANNAPro'; background-color: rgb(70, 70, 70);">
        <tr v-for="(community,index) in communities" :key="community.id" @click="gocommunityDetail(community)" style="padding:0;">
          <th style="padding-top:30px !important;" scope="row"><h2>{{index+1}}</h2></th>
          <td><h4>{{community.title}}</h4><p>작성자 : {{community.user.username}}</p></td>
          <th style="padding-top:30px !important;"><h5>{{community.created_at | yyyyMMdd}}<br>{{community.created_at | hhMMss}}</h5></th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import VueJwtDecode from 'vue-jwt-decode'
export default {
    name:'communityList',
    data: function() {
    return {
      communities: null,
      title:null,
      content:null,
      active:false,
      me:null,
    };
  },
  filters:{  
    yyyyMMdd(value){
      if(value=='') return '';
      let js_date = new Date(value);
      return js_date.toLocaleDateString('kr');
    },
    hhMMss(value){
      if(value=='') return '';
      let js_date = new Date(value);
      return js_date.toLocaleTimeString('kr');
    },
},

    methods:{

      getUserInfo() {
      const token = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(token)
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
          this.me=res.data.username

        })
        .catch((err) => {
          console.log(err)
        })
    },
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
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `Bearer ${token}`,
      };
      return config;
    },
    createCommunity: function() {
      const communityItem = {
        title: this.title,
        content:this.content,
      };
      if (communityItem.title && communityItem.content) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/community/",
          data: communityItem,
          headers: {
            Authorization: "Bearer " + localStorage.getItem("jwt"),
          },
        })
          .then(() => {
            this.active =!this.active
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
      this.$router.push({ name: "communitydDetail", params: { community }});
    },


    },
    created:function(){
        this.getCommunity();
        this.getUserInfo()
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

