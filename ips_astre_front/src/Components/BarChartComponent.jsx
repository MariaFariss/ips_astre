import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);


export default function BarChart({ students, scores }) {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Bar Chart',
      },
    },
  };

  const data = {
    labels: students,
  
    datasets: [
      {
        label: 'astre',
        data: scores.map((weight) => (weight < 0 ? weight : 0)),
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
      {
        label: 'ips',
        data: scores.map((weight) => (weight >= 0 ? weight : 0)),
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
      },
    ],
  };

  return <Bar options={options} data={data} />;
}
