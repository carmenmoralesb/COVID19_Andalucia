function setData(provincesIncidence) {
    var ctx = document.getElementById("pie-chart2").getContext("2d");

    var data_1 = {
        datasets: [{
            fill: true,
            backgroundColor: [
                "#488f31",
                "#75a760",
                "#9fc08f",
                "#c8d8bf",
                "#f1f1f1",
                "#f1c6c6",
                "#ec9c9d",
            ],
            label: "Contagios en un día",
            data: {
                provincesIncidence
            },
        }, ],
        labels: {
            labels
        },
    };
    var chart1 = new Chart(ctx, {
        type: "pie",
        data: data_1,
        options: {
            scales: {
                y: {
                    min: 0,
                },
            },
            responsive: true,
        },
    });
}