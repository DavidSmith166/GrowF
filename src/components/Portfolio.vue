<!--<template>
    <div id ="dropdown">
        <b-dropdown id="ddown-buttons" text="Portfolios" class="m-2">
        <b-dropdown-item-button>Portfolio 1</b-dropdown-item-button>
        <b-dropdown-item-button>Portfolio 2</b-dropdown-item-button>
        <b-dropdown-item-button>Portfolio 3 </b-dropdown-item-button>
        <b-dropdown-item-button>Portfoio 4 </b-dropdown-item-button>
        </b-dropdown>
    </div>
</template>

<style>
#dropdown{
    display: flex;
    margin: left;
}
</style>
*/-->

<template>
<div>
<h1>Stocks ()</h1>
<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>#</th>
      <th>SKU</th>
      <th>Name</th>
      <th>Quantity</th>
      <th>Price</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr   v-for="stock in stocks" @click="selectStock(stock)">
      <th></th>
      <th></th>
      <td></td>
      <td> </td>
      <td></td>
      <td>
        <button class="btn btn-danger" @click="deleteStock(stock)"> X</button>
        <a class="btn btn-primary" v-bind:href="'/stock-update/' + stock.pk"> &#9998; </a>

      </td>
    </tr>
  </tbody>
</table>
<div>
<ul class="list-horizontal">
  <li><button class="btn btn-primary" @click="getPreviousPage()">Previous</button></li>
  <li v-for="page in pages">
    <a class="btn btn-primary" @click="getPage(page.link)"></a>
  </li>
  <li><button class="btn btn-primary" @click="getNextPage()">Next</button></li>
</ul>


</div>

<div class="card text-center" v-if="selectedStock">
  <div class="card-header">
    # -- 
  </div>
  <div class="card-block">
    <h4 class="card-title"></h4>
    <p class="card-text">

    </p>
    <a class="btn btn-primary" v-bind:href="'/stock-update/' + selectedStock.pk"> &#9998; </a>
    <button class="btn btn-danger" @click="deleteStock(selectedStock)"> X</button>

  </div>

</div>
</div>
</template>


<script>
import {APIService} from '../http/APIService';
import Loading from './Loading';
const API_URL = 'http://localhost:8000'; // change if necessary 
const apiService = new APIService();

export default {
  name: 'StockList',
  data() {
    return {
      selectedStock:null,
      stocks: [],
      numberOfPages:0,
      pages : [],
      numberOfSTOCKS:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  }, 
  methods: {
    getStocks(){

      this.loading = true;    
      apiService.getStocks().then((page) => {
        this.stocks = page.data;
        console.log(page);
        console.log(page.nextlink);
        this.numberOfStock
s = page.count;
        this.numberOfPages = page.numpages;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link = `/api/stocks/?page=${i}`;
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
      });
    },
    getPage(link){
      this.loading = true;  
      apiService.getStocksByURL(link).then((page) => {
        this.stocks = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });     
    },
    getNextPage(){
      console.log('next' + this.nextPageURL);
      this.loading = true;  
      apiService.getStocksByURL(this.nextPageURL).then((page) => {
        this.stocks = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });      

    },
    getPreviousPage(){
      this.loading = true;  
      apiService.getStocksByURL(this.previousPageURL).then((page) => {
        this.stocks = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });      

    },
    deleteStock(stock){
      console.log("deleting stock: " + JSON.stringify(stock))
      apiService.deleteStock(stock).then((r)=>{
        console.log(r);
        if(r.status === 204)
        {
          alert("Stock deleted");
          this.$router.go()

        }
      })
    },
    selectStock(stock){
      this.selectedStock= stock;
    }
  },
  mounted() {

    this.getStocks();

  },
}
</script>