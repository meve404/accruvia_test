<script>
  export default{
    name: 'App',
    data(){
      return{
        tweet: {
          'name': '',
          'tweeText': '',
        },
        APIData: []
      }
    },
    async created(){
      await this.getAPIData()
    },
    methods: {
      async getAPIData(){
        var response = await fetch('http://127.0.0.1:8000/accruvia-api/get-tweets/');
        this.APIData = await response.json();
      },
      async createTweet(){
        await fetch('http://127.0.0.1:8000/accruvia-api/make-tweet/'+ this.tweet.name + '/' + this.tweet.tweeText, {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          }
        });
        await this.getAPIData()
      }
    }
  }
</script>
<template>
<div class="section p-3">
  <div class="container">
    <div class="row">
      <div class="col-md-3">
      </div>
      <div class="col-md-6">
        <div class="card">
          <div class="body">

            <form @submit.prevent="createTweet">
              <div class="form-group">
                <div class="row p-2">
                  <div class="col-md-12">
                    <input type="text" class="form-control" placeholder="Full Name" v-model="tweet.name">
                  </div>
                  <div class="col-md-12 my-1">
                    <textarea type="text" class="form-control" placeholder="What's going on?" v-model="tweet.tweeText"></textarea>
                  </div>
                  <div class="col-md-6">
                    <button class="btn btn-success">Submit Tweet</button>
                  </div>
                </div>
              </div>
            </form>

          </div>
        </div>
        
        <div v-for="tweets in APIData" :key="tweets.id">
          <div class="card my-2">
            <div class="card-body">
              <h5 class="card-title text-success">{{ tweets.fullName }}</h5>
              <p class="card-text">
                {{ tweets.tweetText }}
              </p>
              <h6 class="card-subtitle mb-2 text-muted">{{ tweets.created }}</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style>

</style>
