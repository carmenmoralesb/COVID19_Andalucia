const tableContainer = document.getElementById("container");

const chartData = {
    type: "line",
    data: {
        labels: [
            "Almería",
            "Cádiz",
            "Córdoba",
            "Granada",
            "Huelva",
            "Jaén",
            "Málaga",
            "Sevilla",
        ],
        datasets: [{
                label: "PCR 14 días",
                data: {
                    pcr14days
                },
                borderWidth: 1,
            },
            {
                label: "UCI",
                data: {
                    UCI
                },
                borderWidth: 1,
            },
            {
                label: "Fallecidos",
                data: {
                    deceased
                },
                borderWidth: 1,
            },
            {
                label: "Curados",
                data: {
                    recovered
                },
                borderWidth: 1,
            },
        ],
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    reverse: false,
                },
            }, ],
        },
    },
};

const xAxis = chartData.data.labels;
const yAxis = chartData.data.datasets;

const tableHeader = `<tr>${xAxis.reduce((memo, entry) => {
  memo += `<th>${entry}</th>`;
  return memo;
}, "<th></th>")}</tr>`;

const tableBody = yAxis.reduce((memo, entry) => {
  const rows = entry.data.reduce((memo, entry) => {
    memo += `<td>${entry}</td>`;
    return memo;
  }, "");

  memo += `<tr><td>${entry.label}</td>${rows}</tr>`;

  return memo;
}, "");

const table = `<table class="fl-table">${tableHeader}${tableBody}</table>`;

tableContainer.innerHTML = table;