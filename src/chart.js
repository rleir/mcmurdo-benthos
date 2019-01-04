d3.json('chart_by_year.json', function(data) {
  nv.addGraph(function() {
    var chart = nv.models.lineChart()
                  .x(function(d) { return d[0] })
                  .y(function(d) { return d[1]/100 }) //adjusting, 100% is 1.00, not 100 as it is in the data
                  .color(d3.scale.category10().range())
                  .useInteractiveGuideline(true)
                  ;

     chart.xAxis
          .tickValues( 
	      [ 1988,
		1990,
		1991,
		1992,
		1993,
		1997,
		1998,
		2002,
		2003,
		2004,
		2007,
		2008,
		2009,
		2010,
		2011,
		2012,
		2014
	      ]
	  )
          .tickFormat(function(d) {
	      return d
	  });
      
    chart.yAxis
        .tickFormat(d3.format(',.1%'));

    d3.select('#chart svg')
        .datum(data)
        .call(chart);

    //TODO: Figure out a good way to do this automatically
    nv.utils.windowResize(chart.update);

    return chart;
  });
});
