sterling.controller(GLOBAL_CONST.controller.map, ['$scope', function($scope) {

	var covid_map = null;
	var tiles = null;

	const prepare_map = function() {

		covid_map = L.map('covid-map').setView([20.5937, 78.9629], 5);
		tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			maxZoom: 6,
			attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
		});

		tiles.addTo(covid_map);
	};

	angular.element(document).ready(function() {
		prepare_map();
	});
}]);