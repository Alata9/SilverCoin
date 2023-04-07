      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart_income);
      google.charts.setOnLoadCallback(drawChart_payments);

      function drawChart_income() {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Items');
        data.addColumn('number', 'Amount');
        data.addRows({{ data_income|safe }});

        var options = {
                       'width':350,
                       'height':200,
                       'is3D': true,
                       'legend': 'right'};

        var chart = new google.visualization.PieChart(document.getElementById('chart_div_1'));
        chart.draw(data, options);

        var chart = new google.visualization.BarChart(document.getElementById('chart_div_2'));
        chart.draw(data, options);

        var chart = new google.visualization.LineChart(document.getElementById('chart_div_3'));
        chart.draw(data, options);
      }


      function drawChart_payments() {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Items');
        data.addColumn('number', 'Amount');
        data.addRows({{ data_payments|safe }});

        var options = {
                       'width':350,
                       'height':200,
                       'is3D': true,
                       'legend': 'right'};

        var chart = new google.visualization.PieChart(document.getElementById('chart_div_4'));
        chart.draw(data, options);

        var chart = new google.visualization.BarChart(document.getElementById('chart_div_5'));
        chart.draw(data, options);

        var chart = new google.visualization.LineChart(document.getElementById('chart_div_6'));
        chart.draw(data, options);
      }