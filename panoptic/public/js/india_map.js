/**
 * ---------------------------------------
 * This demo was created using amCharts 4.
 *
 * For more information visit:
 * https://www.amcharts.com/
 *
 * Documentation is available at:
 * https://www.amcharts.com/docs/v4/
 * ---------------------------------------
 */

// Themes begin
am4core.useTheme(am4themes_material);
am4core.useTheme(am4themes_animated);
// Themes end

window.onload = function () {
	let chart = am4core.create("chartdiv", am4maps.MapChart);
	window.chart = chart;

	// Set map definition
	chart.geodataSource.url = "https://www.amcharts.com/lib/4/geodata/json/india2020High.json";
	chart.geodataSource.events.on("parseended", function (ev) {
		var data = [];

		for (var i = 0; i < ev.target.data.features.length; i++) {
			let id = ev.target.data.features[i].id;
			data.push({
				id: id,
				value: window.state_wise_frt[id] || 0
				// value: Math.floor(Math.random() * 40 )
			})
		}
		polygonSeries.data = data;
	})

	// Set projection
	chart.projection = new am4maps.projections.Mercator();
	chart.maxZoomLevel = 1;
	chart.seriesContainer.draggable = false;
	chart.seriesContainer.wheelable = false;
	chart.seriesContainer.resizable = false;
	chart.seriesContainer.events.disableType("doublehit");
	chart.chartContainer.background.events.disableType("doublehit");

	// Create map polygon series
	var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

	//Set min/max fill color for each area
	polygonSeries.heatRules.push({
		property: "fill",
		target: polygonSeries.mapPolygons.template,
		// min: chart.colors.getIndex(15).brighten(0.5),
		min: am4core.color('#174057'),
		max: am4core.color('#883D1A')
		// max: am4core.color('#2B6061')
	});

	// Make map load polygon data (state shapes and names) from GeoJSON
	polygonSeries.useGeodata = true;

	// Configure series tooltip
	var polygonTemplate = polygonSeries.mapPolygons.template;
	polygonTemplate.tooltipText = "{name}: {value} FRT Systems";
	polygonTemplate.nonScalingStroke = true;
	polygonTemplate.strokeWidth = 1;
	polygonTemplate.events.on("hit", function (ev) {
		let id = ev.target.dataItem.dataContext.id
		window.location = window.state_routes[id];
	});
	polygonTemplate.stroke = am4core.color("#E2652B");

	// Create hover state and set alternative fill color
	var hs = polygonTemplate.states.create("hover");
	hs.properties.fill = 'white';

	setTimeout(() => {
		console.log(polygonSeries.getPolygonById(current_state));
		if (current_state) {
			chart.maxZoomLevel = 32;
			chart.zoomToMapObject(polygonSeries.getPolygonById(current_state));
			chart.seriesContainer.draggable = false;
			chart.seriesContainer.wheelable = false;
			chart.seriesContainer.resizable = false;
		}
	}, 2000)
};