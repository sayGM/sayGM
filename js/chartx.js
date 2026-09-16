const ctx = document.getElementById('cryptoChart').getContext('2d');
new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['ETH', 'USDT', 'NEIRO', 'JUP', 'WCT', 'OTHERS'],
    datasets: [{
      data: [63.93, 13.59, 11.73, 6.40, 4.03, 0.32],
      backgroundColor: [
        '#ff6384', '#36a2eb', '#ffce56', '#8e44ad', '#00b894', '#636e72'
      ],
      borderColor: '#0d0d0d',
      borderWidth: 2,
      hoverOffset: 10
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const values = [754.75, 160.44, 138.52, 75.61, 47.52, 3.73];
            return `${context.label}: ${context.parsed}% – $${values[context.dataIndex]}`;
          }
        }
      }
    }
  }
});
