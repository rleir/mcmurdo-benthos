d3.json('chart.json', function(data) {
  nv.addGraph(function() {
    var chart = nv.models.lineChart()
                  .x(function(d) { return d[0] })
                  .y(function(d) { return d[1]/100 }) //adjusting, 100% is 1.00, not 100 as it is in the data
                  .color(d3.scale.category10().range())
                  .useInteractiveGuideline(true)
                  ;

     chart.xAxis
          .tickValues( 
	      [ 567993600, 
		852076800, 
		883612800, 
		1009843200, 
		1041379200, 
		1072915200, 
		1167609600, 
		1199145600, 
		1230768000, 
		1262304000, 
		1293840000, 
		1325376000, 
		1388534400
	      ]
	  )
          .tickFormat(function(d) {
	      return d3.time.format('%Y')(new Date(d*1000))
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
