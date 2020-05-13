const API_PRE_CONFIG = {

	base_address: "http://localhost",
	base_port: ":8097",
};

const API_CONFIG = {

	base_url: API_PRE_CONFIG.base_address + API_PRE_CONFIG.base_port,
	base_protocol: API_PRE_CONFIG.base_address + ":3005"
};

const API_PREFIX = {

	base_template_prefix: "../view/",
	base_directive_template_prefix: "../directive/"
};

const GLOBAL_API = {

	directive: {

	},

	route: {
		home: "/",
		map: "/map"
	},

	template: {
		dashboard: API_PREFIX.base_template_prefix + "dashboard.html",
		map: API_PREFIX.base_template_prefix + "map.html"
	},

	fetch: {

	},

	delegate_provider: {
		directive: API_PREFIX.base_directive_template_prefix + "**",
		view: API_PREFIX.base_template_prefix + "**"
	}
};

const GLOBAL_CONST = {

	version: {
		sterling: "0.0.1",
		feathers: "0.0.1",
		wings: "0.0.1"
	},

	controller: {
		home: "home_controller",
		dashboard: "dashboard_controller",
		map: "map_controller"
	},

	message: {

	},

	object: {
		dom_parser: new DOMParser(),
	},

	errorcode: {
		EC01: "STRECx001GENEX"
	},

	errormessage: {
		generic_error: "Something went wrong!",
		error_404: "(404) The requested operation could not be resolved.",
		error_401: "(401) An authentication failure has occured.",
		error_501: "(501) The server could not process your request.",
		EC01: "(001) &#x1F976; Something went wrong from our end. We are sorry for the inconvenience occured. Please try again!",
	},
};

const GLOBAL_METHOD = {

	decode_html: function (html) {
		return GLOBAL_CONST.object.dom_parser.parseFromString(html, "text/html").documentElement.textContent;
	},

	failure_alert: function (message) {
		swal({
			icon: "error",
			title: "Bummer",
			content: {
				element: 'span',
				attributes: {
					innerHTML: message
				}
			}
		});
	},

	success_alert: function (message) {
		swal({
			icon: "success",
			title: "Yay!",
			content: {
				element: 'span',
				attributes: {
					innerHTML: message
				}
			}
		});
	},

	convert_millis_to_date: function (timeinmillis) {
		return (new Date(timeinmillis).toLocaleDateString('en-IN'));
	},

	convert_millis_to_moment_date: function (timeinmillis) {
		return moment(new Date(timeinmillis)).format('LL');
	},

	convert_date_to_millis: function (date) {
		return date.getTime();
	},

	convert_millis_to_time: function (timeinmillis) {
		return (new Date(timeinmillis).toLocaleTimeString('en-IN'));
	},

	convert_to_comma_separated_number: function (number) {
		return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	},

	get_image_url: function (image) {
		return API_PREFIX.base_image_resource_prefix + image;
	},

	get_next_day_date: function (date) {
		return new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1);
	},

	get_previous_day_date: function (date) {
		return new Date(date.getFullYear(), date.getMonth(), date.getDate() - 1);
	}
};