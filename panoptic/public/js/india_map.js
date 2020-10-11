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
	geo = { "country_code": "IN", "country_name": "India" }

	// Default map
	var defaultMap = "usaAlbersLow";

	// calculate which map to be used
	var currentMap = defaultMap;
	var title = "";
	if (am4geodata_data_countries2[geo.country_code] !== undefined) {
		currentMap = am4geodata_data_countries2[geo.country_code]["maps"][0];

		// add country title
		if (am4geodata_data_countries2[geo.country_code]["country"]) {
			title = am4geodata_data_countries2[geo.country_code]["country"];
		}

	}

	// Create map instance
	var chart = am4core.create("chartdiv", am4maps.MapChart);

	// Set map definition
	chart.geodataSource.url = "https://www.amcharts.com/lib/4/geodata/json/" + currentMap + ".json";
	chart.geodataSource.events.on("parseended", function (ev) {
		var data = [];
		for (var i = 0; i < ev.target.data.features.length; i++) {
			let id = ev.target.data.features[i].id;
			data.push({
				id: id,
				value: window.state_wise_frt[id] || 0
			})
		}
		polygonSeries.data = data;
	})

	// Set projection
	chart.projection = new am4maps.projections.Mercator();
	chart.maxZoomLevel = 1;
	chart.seriesContainer.draggable = false;
	chart.seriesContainer.resizable = false;

	// Create map polygon series
	var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

	//Set min/max fill color for each area
	polygonSeries.heatRules.push({
		property: "fill",
		target: polygonSeries.mapPolygons.template,
		min: chart.colors.getIndex(15).brighten(0.5),
		max: chart.colors.getIndex(15).brighten(-0.3)
	});

	// Make map load polygon data (state shapes and names) from GeoJSON
	polygonSeries.useGeodata = true;

	// Configure series tooltip
	var polygonTemplate = polygonSeries.mapPolygons.template;
	polygonTemplate.tooltipText = "{name}: {value} FRT Systems";
	polygonTemplate.nonScalingStroke = true;
	polygonTemplate.strokeWidth = 0.3;

	// Create hover state and set alternative fill color
	var hs = polygonTemplate.states.create("hover");
	hs.properties.fill = 'white';
};