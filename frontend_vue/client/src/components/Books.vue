<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>ToDo Items</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">Date</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in list" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.description }}</td>
              <td>{{ book.date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      list: [],
    };
  },
  methods: {
    getList() {
      const path = 'http://localhost:5000/api/v1/lists/get?id=0';
      axios.get(path)
        .then((res) => {
          this.list = res.data.entries;
          console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getList();
  },
};
</script>
