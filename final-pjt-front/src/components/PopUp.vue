<template>
        <div class="close-image">
        <iframe width="900px" height="600px" :src=movieVideo frameborder="0"></iframe>
      </div>
</template>

<script>
export default {
    name:'PopUp',
    methods:{
      closePopup: function(){
        this.$emit('close-popup')
      }
    },
    computed: {
        movieVideo() {
            console.log(`https://www.youtube.com/embed/${this.$store.state.movieVideo.key}?autoplay=1`)
            return `https://www.youtube.com/embed/${this.$store.state.movieVideo.key}?autoplay=1`
        },
    }

}
</script>

<style>
</style>