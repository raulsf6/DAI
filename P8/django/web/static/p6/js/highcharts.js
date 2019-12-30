document.addEventListener('DOMContentLoaded', function () {
    $.ajax({
        url: "/musicdb/get_chart/",
        data: {},
        type: 'get',                        
        success: function(data) {

            var Highchart = {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Musicians per group'
                },
                xAxis: {
                    title: {
                        text: 'Groups'
                    },
                    categories: []
                },
                yAxis: {
                    title: {
                        text: 'Musicians'
                    }
                },
            series: [{'data':[]}]
            }
            
            data['groups'].forEach(element => {
                Highchart['xAxis']['categories'].push(element.name)
                Highchart['series'][0]['data'].push(element.musicians)
            });
            
            
            var myChart = Highcharts.chart('container', Highchart);
        },
        failure: function(datos) {
                alert('esto no vá');
        }
    });
});

/*
{
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Musicians per group'
    },
    xAxis: {
        categories: ['Apples', 'Bananas', 'Oranges']
    },
    yAxis: {
        title: {
            text: 'Fruit eaten'
        }
    },
    series: [{
        name: 'Jane',
        data: [1, 0, 4]
    }, {
        name: 'John',
        data: [5, 7, 3]
    }]
}
*/