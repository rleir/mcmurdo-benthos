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
	      [ 915166800000,
      		946702800000,
      	//	978325200000,
      		1009861200000,
      	//	1041397200000,
      		1072933200000,
      	//	1104555600000,
      		1136091600000,
      	//	1167627600000,
      		1199163600000,
      	//	1230786000000,
      		1262322000000,
      	//	1293858000000,
      		1325394000000,
      	//	1357016400000,
      		1388552400000,
	//	1420088400000,
      		1451624400000 ]
	  )
          .tickFormat(function(d) {
              return d3.time.format('%Y')(new Date(d))
          });
      //    .tickValues([1078030800000,1122782400000,1167541200000,1251691200000])
      
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

