sterling.service('transmissionservice', ['communicationservice', function (communicationservice) {

	return ({

		get_entity: function (url, responsekey, partial_decoding = false, excluded_fields = [], success_callback, failure_callback = null, on_complete_callback = null) {

			communicationservice.execute_get_request(url, responsekey, partial_decoding, excluded_fields).then(function (response) {

				if (response.hasOwnProperty('has_failed') && (failure_callback != null)) failure_callback();
				else success_callback(response);

				if (on_complete_callback != null) on_complete_callback();
			});
		},

		post_entity_form: function (data, url, pre_post_callback, success_callback, failure_callback, on_complete_callback) {

			console.log(data);

			communicationservice.execute_post_request(data, url, pre_post_callback, success_callback, failure_callback, on_complete_callback);
		},

		basic_request: function (url, pre_request_callback, success_callback, failure_callback, on_complete_callback, parse_errorcode = false) {

			if (pre_request_callback !== null) pre_request_callback();

			communicationservice.execute_basic_request(url, success_callback, parse_errorcode).then(function (response) {

				if ((response !== null) && response.hasOwnProperty('has_failed') && (failure_callback !== null)) failure_callback();
				if (on_complete_callback != null) on_complete_callback();
			});
		}
	});
}]);