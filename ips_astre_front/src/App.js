
import './App.css';
import DoughnutChart from './DoughnutChartComponent';
import BarChart from './BarChartComponent';
import { useState, useEffect } from "react";
import axios from 'axios';


function App() {

  var [hypothesis, setHypothesis] = useState([]);
  var [weightData, setweightData] = useState([]);
  var [studentArray, setStudentArray] = useState([]);
  var [weightArray, setWeightArray] = useState([]);

  // hypothesis
  function setResponseHypothesis(response) {
    console.log(response.data);
    setHypothesis(response.data.map((value)=>(value.hypothesis)));
    setweightData(response.data.map((value)=>(value.value))) ;
  }

  function fetchAPIHypothesis(endpoint) {
    axios.get(`http://127.0.0.1:8000/hypothesis/${endpoint}`).then(setResponseHypothesis);
  }


  useEffect(() => {
    fetchAPIHypothesis("astre");
  }, []);

  function selectOnclick(value) {
    switch(value.target.value){
      case "ips":
        fetchAPIHypothesis("ips");
        break;
      case "astre":
        fetchAPIHypothesis("astre");
        
        break;
      default:
        fetchAPIHypothesis("ips");
    }
  }

  // student
  function setResponseStudent(response) {
    console.log(response.data);
    setStudentArray(response.data.map((value)=>(value.student)));
    setWeightArray(response.data.map((value)=>(value.score))) ;
  }

  function fetchAPIStudent() {
    axios.get("http://127.0.0.1:8000/student").then(setResponseStudent);
  }

  useEffect(() => {
    fetchAPIStudent();
  }
  , []);

  // return (
  //   <div className="App">
  //     <h1>IPS ASTRE</h1>
  //     <select onChange={selectOnclick}>
  //       <option value="ips">IPS</option>
  //       <option value="astre">ASTRE</option>
  //     </select>
  //     <DoughnutChart hypothesis={hypothesis} weightData={weightData}/>
  //     <BarChart students={studentArray} weights={weightArray} />
  //   </div>
  // );

  return (
    <div className="App">
      <h1>IPS ASTRE</h1>
      <select onChange={selectOnclick}>
        <option value="ips">IPS</option>
        <option value="astre">ASTRE</option>
      </select>
      <div className="chart-container">
        <div className="chart">
          <DoughnutChart hypothesis={hypothesis} weightData={weightData} />
        </div>
        <div className="chart">
          <BarChart students={studentArray} weights={weightArray} />
        </div>
      </div>
    </div>
  );
}

export default App;
