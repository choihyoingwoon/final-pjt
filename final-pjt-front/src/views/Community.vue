<template>
  <div class="signup bg-dark">
    <br>
    <h1>Community</h1>
    <hr>
    <div class="commucreate" :class="{'active': active}">
        <button class="btn btn-danger"  @click="activeCreate"><h4>create</h4></button>
    </div>
    <div class="commucreate" :class="{'active': !active}">
        <div>
            <h4>Title</h4>
            <input type="text" v-model.trim="title"/>
        </div>
        <div>
            <h4>Content</h4>
            <input type="text" v-model.trim="content"/>
        </div>
    <button class="btn btn-danger" @click="createCommunity"><h4>create</h4></button>
    </div>
    <hr>
    <ul>
        <li v-for="community in communities" :key="community.id">
            {{community.title}}
        </li>
    </ul>
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

    },
    created:function(){
        this.getCommunity();
    }
}
</script>

<style>
.commucreate{
    line-height: 30px;
    width: 50%;
    margin: auto;
    text-align: left;
}
.active{
    display:none;
}
</style>