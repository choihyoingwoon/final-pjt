<template>
        <div class="close-image">
        <p>hi</p>
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
            console.log(this.$store.state.movieVideo)
            return this.$store.state.movieVideo
        }
    }

}
</script>

<style>

</style>