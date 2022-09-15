
google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawTitleSubtitle);

function drawTitleSubtitle() {
var data = google.visualization.arrayToDataTable([
['Months', 'points'],
['Sept', 5],
['Oct', 3],
['Nov', 4],
['Dec', 2],
]);


var materialOptions = {
chart: {
title: 'Rewards Per Month',

},
hAxis: {
title: 'Months',
minValue: 0,
},
vAxis: {
title: 'Points'
},
bars: 'vertical'
};


var materialChart = new google.charts.Bar(document.getElementById('chart_div'));
document.getElementById('chart_div').style.height="410px";
document.getElementById('chart_div').style.width="420px";
materialChart.draw(data, materialOptions);
}



