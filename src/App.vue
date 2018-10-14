<template>
  <div id="app">
    <head>
      <script src="https://d3js.org/d3.v4.min.js"></script>
    </head>
    <h1>GrowF</h1>
    <div id = "Graphs">
      <div id = "Marquee">
        <h2>Marquee</h2>
        <table align="center" class="table table-hover">
          <tbody>
            <tr>
            <td>
                <button type="button" class="btn btn-success btn-sm" @click = "Mar1()" >Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" @click = "Mar2()" >Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm" @click = "Mar3()" >Past Year</button>
            </td>
            </tr>
            <tr>
            <td>
              <d3 :result="result"></d3>
            </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div id = "Current">
        <h2> Current </h2>
        <table align = "center" class="table table-hover">
          <tbody>
            <tr>
            <td>
        <button type="button" class="btn btn-success btn-sm" @click = "Cur1()">>Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" @click = "Cur2()">Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm" @click = "Cur3()">Past Year</button>
            </td>
            </tr>
            <tr>
              <td padding="0px">
                <!---<moavg></moavg>-->
                <div class='issuu-embed-container'>
                  <iframe src='d3.html' frameborder='0' allowfullscreen></iframe>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- Stuff makes thing full size praise be -->
                
      </div>
    </div>
<<<<<<< HEAD
=======
    <!--<portfolio></portfolio>-->
>>>>>>> a3a638dcba37dae1c5c1f0bcd3e7b5bd9eec13fa
    <stocklist></stocklist>
  </div>
</template>
<!-- This script makes the thingy full size -->
<script async src="//jsfiddle.net/k23jr7xb/embed/html,css,result/"></script>
<script>  
import stockList from './components/stockList';
import D3 from './components/d3';
import moAvg from './components/moAvg';
import axios from 'axios';

export default{
  name: 'App',
  data () {
    return {
      yourStock: [],
      result : [],
    }
  },
  components: {
<<<<<<< HEAD
=======
    //portfolio : Portfolio,
>>>>>>> a3a638dcba37dae1c5c1f0bcd3e7b5bd9eec13fa
    stocklist : stockList,
    d3 : D3,
    moavg : moAvg,
  },
  methods: {
    getStock() {
      const path = 'http://localhost:8000/api/stock';
      axios.get(path)
        .then((res) => {
          this.yourStock = res.data.yourStock;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    Mar1() {
      const path = 'http://localhost:8000/yahoo';
      const payload = {
        function : 'get_fixed_stock_value_list',
        args : ['AAPL',30]
      }
      axios.get(path,payload)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
    });
    },
    Mar2() {
      const path = 'http://localhost:8000/yahoo';
      const payload = {
        function : 'get_fixed_stock_value_list',
        args : ['AAPL',90]
      }      
      axios.get(path,payload)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
    });
    },
    Mar3() {
      const path = 'http://localhost:8000/yahoo';
      const payload = {
        function : 'get_fixed_stock_value_list',
        args : ['AAPL',365]
      }
      axios.get(path,payload)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
    });
    }
  },
    created() {
      this.getStock();
    },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height:auto;
  width:auto;
  padding: 0%;
}
h1, h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}

#Graphs{
  display: inline-block;
 
}
#Marquee {
 width:50%;
}
embed{
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}

.issuu-embed-container {

  position: relative;

  padding-bottom: 75%; /* set the aspect ratio here as (height / width) * 100% */

  height: 0;

  overflow: hidden;

  max-width: 100%;

}

.issuu-embed-container iframe {

  position: absolute;

  top: 0;

  left: 0;

  width: 100%;

  height: 100%;

}

</style>
