<template>

        <div id="container" class="container">

            <div class="row">

                <div class="col-sm-8 offset-sm-2">
                <div class="alert alert-warning" v-show="showCreateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Stock successfully created!</strong>
                </div>
                <div class="alert alert-warning" v-show="showUpdateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Stock successfully updated!</strong>
                </div>

                <div class="alert alert-warning" v-show="showError"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Error!</strong>
                </div>                
                    <h1>Create a Stock</h1>
                    <div class="info-form">
                      <form>
                        <div class="form-group">
                          <label for="sku">Stock SKU</label>
                          <input v-model="stock.sku" type="text" class="form-control" id="sku" aria-describedby="skuHelp" placeholder="Enter SKU">
                          <small id="skuHelp" class="form-text text-muted">Enter your stock's SKU</small>
                          <label for="name">Stock Name</label>
                          <input v-model="stock.name" type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Enter name">
                          <small id="nameHelp" class="form-text text-muted">Enter your stock's name</small>

                          <label for="description">Stock Description</label>
                          <textarea v-model="stock.description" class="form-control" id="description" aria-describedby="descHelp" placeholder="Enter description"></textarea>
                          <small id="descHelp" class="form-text text-muted">Enter your stock's description</small>

                          <label for="buyPrice">Stock Cost</label>
                          <input v-model="stock.buyPrice" type="text" class="form-control" id="buyPrice" aria-describedby="buyPriceHelp" placeholder="Enter the buying price">
                          <small id="buyPriceHelp" class="form-text text-muted">Enter your stock's cost</small>

                          <label for="sellPrice">Stock Price</label>
                          <input v-model="stock.sellPrice" type="text" class="form-control" id="sellPrice" aria-describedby="sellPriceHelp" placeholder="Enter name">
                          <small id="sellPriceHelp" class="form-text text-muted">Enter your stock's selling price</small>

                          <label for="unit">Stock Unit</label>
                          <input v-model="stock.unit" type="text" class="form-control" id="unit" aria-describedby="unitHelp" placeholder="Enter unit">
                          <small id="unitHelp" class="form-text text-muted">Enter your stock's unit</small>

                          <label for="quantity">Stock Quantity</label>
                          <input v-model="stock.quantity" type="text" class="form-control" id="quantity" aria-describedby="quantityHelp" placeholder="Enter quantity">
                          <small id="quantityHelp" class="form-text text-muted">Enter your stock's quantity</small>

                        </div>
                      </form>
                       <button class="btn btn-primary" v-if="!this.stock.pk" @click="createStock()" ><span v-if="!creating">Create</span><span v-if="creating">Creating... Please wait </span></button>
                       <button class="btn btn-primary" v-if="this.stock.pk" @click="updateStock()" ><span v-if="!updating">Update</span><span v-if="updating">Updating... Please wait </span></button>
                       <button class="btn btn-primary"  @click="newStock()" >New..</button>

                    </div>
                </div>
            </div>
        </div>

</template>

<script>
import {APIService} from '../http/APIService';

const apiService = new APIService();

export default {
  name: 'StockCreate',
  components: {
  },
  data() {
    return {
      showCreateMessage: false,
      showUpdateMessage: false,
      showError: false,
      stock: {},
      stocks: '',
      creating: false,
      updating: false
    };
  }, 
  methods: {
    hideMessage(){
      this.showCreateMessage = false;
      this.showUpdateMessage = false;
      this.showError = false;
    },
    createStock(){
      this.creating = true;
      apiService.createStock(this.stock).then((result)=>{
          if(result.status === 201){
            this.stock = result.data;
            this.showCreateMessage = true;
          }
          this.creating = false;          
      },(error)=>{
        this.showError = true;
        this.creating = false;
      });
    },
    updateStock(){
      this.updating = true;
     apiService.updateStock(this.stock).then((result)=>{
          if(result.status === 200){
            this.showUpdateMessage = true;
          }

      },(error)=>{
        this.showError = true;
        this.updating = false;
      });
    },
    newStock(){
      this.stock = {};
    }

  },
  mounted() {

    if(this.$route.params.pk){
        apiService.getStock(this.$route.params.pk).then((stock)=>{
        this.stock = stock;
      })
    }
  },
}
</script>




