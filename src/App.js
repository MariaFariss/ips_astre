
import './App.css';
import DoughnutChart from './Components/DoughnutChartComponent';
import BarChart from './Components/BarChartComponent';
import CircularLiner from './Components/CircularLinerComponent';
import { useState, useEffect } from "react";
import axios from 'axios';


function App() {

  var [hypothesis, setHypothesis] = useState([]);
  var [weightData, setweightData] = useState([]);
  var [studentArray, setStudentArray] = useState([]);
  var [studentScore, setStudentScore] = useState([]);

  // hypothesis
  function setResponseHypothesis(response) {
    // console.log(response.data);
    setHypothesis(response.data.map((value)=>(value.hypothesis)));
    setweightData(response.data.map((value)=>(value.value))) ;
  }

  function fetchAPIHypothesis(endpoint) {
    axios.get(`http://127.0.0.1:8000/hypothesis/${endpoint}`).then(setResponseHypothesis);
  }


  useEffect(() => {
    fetchAPIHypothesis("ips");
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

  const updateValue = (e, hypothesisArray) => {
    let newWeightData = [...weightData];
    let index = hypothesis.indexOf(hypothesisArray);
    if(weightData[index]<0){
      e = -e/20
    }
    else{
      e = e/20
    }
    newWeightData[index] = e;
    setweightData(newWeightData)
    console.log(hypothesisArray);
    console.log(newWeightData)
    UpdateAPIStudent(newWeightData)

  }

  // student
  function setResponseStudent(response) {
    console.log(response.data);
    setStudentArray(response.data.map((value)=>(value.student)));
    setStudentScore(response.data.map((value)=>(value.score))) ;
  }

  function fetchAPIStudent() {
    axios.get("http://127.0.0.1:8000/student").then(setResponseStudent);
  }

  function UpdateAPIStudent(weights) {
    let body = {
      hypothesis: hypothesis,
      weight: weights
    }
    console.log(body);
    axios.post('http://127.0.0.1:8000/studentUpdate', body).then(setResponseStudent);
  }

  useEffect(() => {
    fetchAPIStudent();
  }
  , []);
  
return (
  <div className="App">
    <h1>IPS ASTRE</h1>

    <select onChange={selectOnclick}>
      <option value="ips">IPS</option>
      <option value="astre">ASTRE</option>
    </select>

    <div className="chart-container">
      {hypothesis.map((hypo, index) => (
        <div key={index} className="chartUpper">
          <CircularLiner hypothesis={hypo} weightData={weightData[index]} onChange={updateValue} />
        </div>
      ))}
    </div>

    <div className="chart-container">
      <div className="chart test">
        <DoughnutChart hypothesis={hypothesis} weightData={weightData} className="child" />
      </div>
      <div className="chart">
        <BarChart students={studentArray} scores={studentScore} />
      </div>
    </div>
  </div>
);
}
export default App;
