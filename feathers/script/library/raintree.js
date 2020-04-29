var raintree = angular.module('raintree', []);
const internal_failure_flag = {
	has_failed: true
};

raintree.service('responsevalidationservice', [function () {

	return ({
		is_success: function (json) {
			return json.success;
		},
		is_failure: function (json) {
			return !json.success;
		}
	});
}]);

raintree.service('errorcodeparserservice', [function () {

	return ({

		parse: function (errorcode) {

			if (typeof errorcode === 'object') {

				if (errorcode.hasOwnProperty('status')) {

					switch (errorcode.status) {
						case 404:
							GLOBAL_METHOD.failure_alert(GLOBAL_CONST.errormessage.error_404);
						case 401:
							GLOBAL_METHOD.failure_alert(GLOBAL_CONST.errormessage.error_401);
						case 501:
							GLOBAL_METHOD.failure_alert(GLOBAL_CONST.errormessage.error_501);
					}
				}
			}
		},

		parse_kaptein_error: function (errorcode) {

			var message;

			switch (errorcode) {

				case GLOBAL_CONST.errorcode.EC01:
					message = GLOBAL_CONST.errormessage.EC01;
					break;

				default:
					message = GLOBAL_CONST.errormessage.generic_error;
			}

			GLOBAL_METHOD.failure_alert(message);
		}
	});
}]);

raintree.service('communicationservice', ['$http', '$q', 'responsevalidationservice', 'errorcodeparserservice', function ($http, $q, responsevalidationservice, errorcodeparserservice) {

	return ({

		execute_get_request: function (url, responsekey, partial_decoding = false, excluded_fields = []) {

			return $http({
				method: 'GET',
				url: url,
				cache: false
			}).then(function success_callback(response) {

				if (responsevalidationservice.is_success(response.data)) {

					response_data = JSON.parse(JSON.stringify(response.data), function (key, value) {

						if (typeof value == "string") {

							if (!partial_decoding) return GLOBAL_METHOD.decode_html(value);
							else if (excluded_fields != null || excluded_fields.length > 0) return ($.inArray(key, excluded_key) == -1) ? GLOBAL_METHOD.decode_html(value) : value;
							else return GLOBAL_METHOD.decode_html(value);
						}

						return value;
					});

					if (response_data.hasOwnProperty(responsekey) && (response_data[responsekey] != null)) return response_data[responsekey];
					else return internal_failure_flag;
				} else return internal_failure_flag;


			}, function failure_callback(response) {
				return internal_failure_flag;
			});
		},

		execute_post_request: function (data, url, pre_post_callback, on_success_callback, on_failure_callback, on_complete_callback) {

			$.ajax({
				type: 'POST',
				url: url,
				dataType: "json",
				data: data,
				beforeSend: pre_post_callback,
				success: function (response) {

					if (responsevalidationservice.is_failure(response)) {

						errorcodeparserservice.parse_kaptein_error(response.message);
						on_failure_callback(response.message);
					} else if (responsevalidationservice.is_success(response)) on_success_callback(response);
				},
				error: function (errorThrown) {
					if (on_failure_callback != null) on_failure_callback(errorThrown);
				},
				complete: on_complete_callback,
				statusCode: {
					404: function () {
						errorcodeparserservice.parse({
							status: 404
						});
					},
					401: function () {
						errorcodeparserservice.parse({
							status: 401
						});
					},
					501: function () {
						errorcodeparserservice.parse({
							status: 501
						});
					}
				}
			});
		},

		execute_basic_request: function (url, on_success_callback, parse_errorcode) {

			return $http({
				method: 'GET',
				url: url,
				cache: false
			}).then(function success_callback(response) {

				if (responsevalidationservice.is_success(response.data)) on_success_callback();
				else {

					if (parse_errorcode) errorcodeparserservice.parse_kaptein_error(response.data.message);
					return internal_failure_flag;
				}

				return null;
			}, function failure_callback(response) {
				return internal_failure_flag;
			});
		}
	});
}]);