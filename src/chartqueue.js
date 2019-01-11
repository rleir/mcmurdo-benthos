// get all years which have data for all sites
queue()
//    .defer(d3.json, "chart_by_site_1988.json")
//    .defer(d3.json, "chart_by_site_2002.json")
//    .defer(d3.json, "chart_by_site_2003.json")
    .defer(d3.json, "chart_by_site_2004.json")
    .defer(d3.json, "chart_by_site_2007.json")
    .defer(d3.json, "chart_by_site_2008.json")
    .defer(d3.json, "chart_by_site_2009.json")
    .defer(d3.json, "chart_by_site_2010.json")
    .defer(d3.json, "chart_by_site_2011.json")
    .await(analyze);

function analyze(
    error,
    chart_by_site_2004,
    chart_by_site_2007,
    chart_by_site_2008,
    chart_by_site_2009,
    chart_by_site_2010,
    chart_by_site_2011) {
    if(error) { console.log(error); }

//    drawChart(chart_by_site_1988, '1988');
//    drawChart(chart_by_site_2002, '2002');
//    drawChart(chart_by_site_2003, '2003');
    drawChart(chart_by_site_2004, '2004');
    drawChart(chart_by_site_2007, '2007');
    drawChart(chart_by_site_2008, '2008');
    drawChart(chart_by_site_2009, '2009');
    drawChart(chart_by_site_2010, '2010');
    drawChart(chart_by_site_2011, '2011');
}


function drawChart (data,chartNum) {
    nv.addGraph(function() {
    var chart = nv.models.lineChart()
                  .x(function(d) { return d[0] })
                  .y(function(d) { return d[1]/100 }) //adjusting, 100% is 1.00, not 100 as it is in the data
                  .color(d3.scale.category10().range())
                  .useInteractiveGuideline(true)
                  ;

      chart.xAxis
          .tickValues( 
	      [ 1,
		2,
		3
	      ]
	  )
          .tickFormat(function(d) {
	      return d
	  });
      
    chart.yAxis
        .tickFormat(d3.format(',.1%'));

    d3.select('#chart' + chartNum + ' svg')
        .datum(data)
        .call(chart);

    //TODO: Figure out a good way to do this automatically
    nv.utils.windowResize(chart.update);

    return chart;
  });
};



