google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);



function drawChart() {



var data = google.visualization.arrayToDataTable([
['Task', 'Hours per Day'],
['Training', 10],
['Rewards', 8],
['Exit Interviews ', 7],
['Attendance Tracking', 5]
]);



var options = {
title: 'Features Priority',
is3D: true,
};



var chart = new google.visualization.PieChart(document.getElementById('piechart'));

document.getElementById('piechart').style.width = "600px"

chart.draw(data, options);
}