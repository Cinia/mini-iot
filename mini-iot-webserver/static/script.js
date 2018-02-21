function update_chart_old() {
    console.log("requesting chart update")
    $.getJSON("/api/temperature", function (json) {
        //var data = [];
        var labels = [];
        var datasets = []

        lineChartData = {
            labels: labels,
            datasets: datasets
        };

        //var humidity = [];
        //console.log(json);
        json['tags'].forEach(tag => {
            labels = []; // hack to avoid duplicate labels
            temperature = [];
            console.log("get values for source=" + tag)
            $.getJSON("/api/temperature/" + tag, function (json_list) {
                console.log(json_list);
                json_list.forEach(list => {
                    if (list["value"] != null) {
                        labels.push(list["time"]);
                        value = list["value"];
                        //console.log("Adding value: " + value)
                        temperature.push(value);
                    }
                }
                )
                color = getRandomRgb();
                datasets.push({
                    label: tag,
                    borderColor: color,
                    backgroundColor: color,
                    fill: false,
                    data: temperature
                });
                lineChartData.labels = labels;
            });
            console.log(datasets);

            lineChartData.datasets = datasets;
    
            draw_chart(lineChartData);
        });

        
    });
}


function update_chart() {
    var tag = "red";
    $.getJSON("/api/temperature/" + tag, function (json_list) {
        var labels = [];
        var datasets = [];
        temperature = [];

        lineChartData = {
            labels: labels,
            datasets: datasets
        };
        console.log(json_list);
        json_list.forEach(list => {
            if (list["value"] != null) {
                labels.push(list["time"]);
                value = list["value"];
                //console.log("Adding value: " + value)
                temperature.push(value);
            }
        }
        )
        color = getRandomRgb();
        datasets.push({
            label: tag,
            borderColor: color,
            backgroundColor: color,
            fill: false,
            data: temperature
        });
        lineChartData.labels = labels;
        lineChartData.datasets = datasets;
    
        draw_chart(lineChartData);
});
}

function draw_chart(lineChartData) {
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = Chart.Line(ctx, {
        data: lineChartData,
        options: {
            responsive: true,
            hoverMode: 'index',
            stacked: false,
            title: {
                display: true,
                text: 'Chart.js Line Chart - Multi Axis'
            },
            scales: {
                yAxes: [{
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                }, {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",

                    // grid line settings
                    gridLines: {
                        drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
                }],
            }
        }
    });
}

function getRandomRgb() {
    var num = Math.round(0xffffff * Math.random());
    var r = num >> 16;
    var g = num >> 8 & 255;
    var b = num & 255;
    return 'rgb(' + r + ', ' + g + ', ' + b + ')';
}

