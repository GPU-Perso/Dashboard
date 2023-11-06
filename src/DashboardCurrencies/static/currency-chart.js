var ctx = document.getElementById("chart");
new Chart(ctx, {
    type: 'line',
    data: {
        labels: [1, 2, 3, 4, 5],
        datasets: [{
            label: 'USD',
            data: [5, 8, 3, 10, 8],
            fill: false,
            borderColor: 'rgb(255, 128, 128)'
        }]
    }

})