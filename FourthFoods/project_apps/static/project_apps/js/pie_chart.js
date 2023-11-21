    //Basic Values for the chart 
    var data = [{
      type: "pie",
      values: [2],
      labels: ["."],
      textinfo: "label+percent",
      automargin: true
  }]

  var layout = {
  height: 630,
  width: 700,
  margin: {"t": 10, "b": 0, "l": 0, "r": 0},
  showlegend: false
  }




  function updateGraph() {
      let arrayTotal = [];

      if (document.getElementById('product1').value == '' || document.getElementById('product2').value == '' || document.getElementById('product3').value == '') {
          alert("Make sure all fields are filled out. If a category has no needed inputs, please insert '0' (zero) in its respective place. Thank you!")
      } else {
          for (let i = 0; i < 3; i++) {
              arrayTotal[i] = document.getElementById('product' + (i+1)).value;
          }
      

          data = [{
              type: "pie",
              values: arrayTotal,
              labels: ["Produce", "Meat", "Miscellaneous"],
              textinfo: "label+percent",
              textposition: "outside",
              automargin: true
          }]
          
          Plotly.newPlot('myDiv', data, layout)
          alert("Graph has been created, please head to the home tab to view the graph.")
      }
                 
  }
  
Plotly.newPlot('myDiv', data, layout)