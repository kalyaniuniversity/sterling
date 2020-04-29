var sterling = angular.module('sterling', ['ngRoute', 'ngMaterial', 'ngAnimate', 'ngMessages', 'ngSanitize', 'raintree']);

sterling.config(['$sceDelegateProvider', function ($sceDelegateProvider) {

	$sceDelegateProvider.resourceUrlWhitelist([
		'self',
		GLOBAL_API.delegate_provider.directive,
		GLOBAL_API.delegate_provider.view
	]);
}]);

sterling.config(function ($mdDateLocaleProvider) {

	$mdDateLocaleProvider.formatDate = function (date) {
		return date ? moment(date).format('LL') : '';
	};
});

sterling.config(['$mdThemingProvider', function ($mdThemingProvider) {

	$mdThemingProvider
		.theme('default')
		.primaryPalette('grey');
}]);

sterling.config(['$routeProvider', '$locationProvider', function ($routeProvider) {

	$routeProvider.caseInsensitiveMatch = true;

	$routeProvider

		.when(GLOBAL_API.route.home, {
			templateUrl: GLOBAL_API.template.dashboard,
			controller: GLOBAL_CONST.controller.dashboard
		})

		.otherwise({
			redirectTo: GLOBAL_API.route.home
		});
}]);

sterling.run(function () {

});

swal.setDefaults({
	closeOnClickOutside: false
});