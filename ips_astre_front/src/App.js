
import './App.css';
import DoughnutChart from './DoughnutChartComponent';
import { useState, useEffect } from "react";
import axios from 'axios';


function App() {

  const [data, setData] = useState([]);
  var [hypothesis, setHypothesis] = useState([]);
  var [weightData, setweightData] = useState([]);

  function setResponse(response) {
    console.log(response.data);
    setHypothesis(response.data.map((value)=>(value.hypothesis)));
    setweightData(response.data.map((value)=>(value.value))) ;
    setData(response.data);
  }

  function fetchAPI(endpoint) {
    axios.get(`http://127.0.0.1:8000/hypothesis/${endpoint}`).then(setResponse);
  }


  useEffect(() => {
    fetchAPI("astre");
  }, []);

  function selectOnclick(value) {
    switch(value.target.value){
      case "ips":
        fetchAPI("ips");
        break;
      case "astre":
        fetchAPI("astre");
        
        break;
      default:
        fetchAPI("ips");
    }
  }
 

  return (
    <div className="App">
      <h1>IPS ASTRE</h1>
      <select onChange={selectOnclick}>
        <option value="ips">IPS</option>
        <option value="astre">ASTRE</option>
      </select>
      <DoughnutChart hypothesis={hypothesis} weightData={weightData}/>
    </div>
  );
}

export default App;
