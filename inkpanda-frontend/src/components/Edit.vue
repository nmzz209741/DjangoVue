<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="title">Title</label>
                <input
                    type="text"
                    class="form-control"
                    id="title"
                    v-model="poem.title"
                    v-validate="'required'"
                    name="title"
                    placeholder="Enter title"
                    :class="{'is-invalid': errors.has('poem.title') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid title.
                </div>
            </div>
            <div class="form-group">
                <label for="body">body</label>
                <textarea
                    name="body"
                    class="form-control"
                    id="body"
                    v-validate="'required'"
                    v-model="poem.body"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('poem.body') && submitted}"></textarea>
                <div class="invalid-feedback">
                    Please provide a valid body.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            poem: {
                title: '',
                description: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get(`http://127.0.0.1:8000/api/poem/${ this.$route.params.id }/`)
            .then( response => {
                console.log(response.data)
                this.poem = response.data
            });
    },
    methods: {
        update: function () {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/poem/${this.poem.id}/`,
                        this.poem
                    )
                    .then(() => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>