sterling.controller(GLOBAL_CONST.controller.home, ['$scope', '$mdSidenav', '$mdDialog', '$location', function($scope, $mdSidenav, $mdDialog, $location) {

	$scope.year = new Date().getFullYear();
	$scope.version = GLOBAL_CONST.version.sterling;
	$scope.enview_sidenav = ENVIEW_SIDENAV;

	$scope.show_menu = function ($mdMenu, event) {
		$mdMenu.open(event);
	};

	$scope.view_software_info_dialog = function (event) {

		$mdDialog.show({
			contentElement: '#st-software-info',
			parent: angular.element(document.body),
			targetEvent: event,
			clickOutsideToClose: true
		});
	};

	$scope.direct_to_location = function(route) {
		$location.path(route);
	}
}]);