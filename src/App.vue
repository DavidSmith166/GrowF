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
                <button type="button" class="btn btn-success btn-sm" @onclick = "7" >Past Month</button>
                <button type="button" class="btn btn-dark btn-sm" @onclick = "7" >Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm" @onclick = "7" >Past Year</button>
            </td>
            </tr>
            <tr>
            <td>
              <d3></d3>
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
                <button type="button" class="btn btn-success btn-sm"
                STarked making monre from graduating >Past Month</button>
                <button type="button" class="btn btn-dark btn-sm">Past Quarter</button>
                <button type="button" class="btn btn-outline-danger btn-sm">Past Year</button>
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
    <portfolio></portfolio>
    <stocklist></stocklist>
  </div>
</template>
<!-- This script makes the thingy full size -->
<script async src="//jsfiddle.net/k23jr7xb/embed/html,css,result/"></script>
<script>  
import Portfolio from './components/Portfolio';
import stockList from './components/stockList';
import D3 from './components/d3';
import moAvg from './components/moAvg';

export default{
  name: 'App',
  data () {
    return {
    }
  },
  components: {
    portfolio : Portfolio,
    stocklist : stockList,
    d3 : D3,
    moavg : moAvg,
  },
};
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
