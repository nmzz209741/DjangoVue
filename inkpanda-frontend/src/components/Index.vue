<template>
  <div class="pt-5">
    <div v-if="poems && poems.length">
      <div class="card mb-3" v-for="poem of poems" v-bind:key="poem.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg
              class="bd-placeholder-img"
              width="200"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
              role="img"
              aria-label="Placeholder: Thumbnail"
            >
              <title>{{ poem.title }}</title>
              <rect width="100%" height="100%" fill="#55595c" />
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ poem.title.charAt(0) }}</text>
            </svg>
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ poem.title }}</h5>
              <p class="card-text">{{ poem.body }}</p>
              <router-link
                :to="{name: 'edit', params: { id: poem.id }}"
                class="btn btn-sm btn-primary"
              >Edit</router-link>
              <button class="btn btn-danger btn-sm ml-1" v-on:click="deletepoem(poem)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-if="poems.length == 0">No poems</p>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      poems: []
    };
  },
  created() {
    this.all();
  },
  methods: {
    deletepoem: function(poem) {
      if (confirm("Delete " + poem.title)) {
        axios
          .delete(`http://127.0.0.1:8000/api/poem/${poem.id}/`)
          .then(() => {
            this.all();
          });
      }
    },
    all: function() {
      axios.get("http://127.0.0.1:8000/api/poem/").then(response => {
        this.poems = response.data;
      });
    }
  }
};
</script>