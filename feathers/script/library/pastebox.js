function pb_remove_class(parent_class, target_class) {
    $("." + parent_class).removeClass(target_class);
}

function pb_remove_class_by_parent_id(parent_id, target_class) {
    $("#" + parent_id).removeClass(target_class);
}

function pb_remove_class_by_expression(expression, target_class) {
    $(expression).removeClass(target_class);
}

function pb_add_class(parent_class, target_class) {
    $("." + parent_class).addClass(target_class);
}

function pb_add_class_by_parent_id(parent_id, target_class) {
    $("#" + parent_id).addClass(target_class);
}

function pb_add_class_by_expression(expression, target_class) {
    $(expression).addClass(target_class);
}

function pb_iterate_over_selector(selector_expression, iterator_method) {
    $(selector_expression).each(function (index, value) {
        iterator_method(index, value);
    });
}

/* https://stackoverflow.com/a/3239600/3640307 */
function pb_has_id(element_expression, id) {
    return ($(element_expression).attr('id') === id);
}

/* https://stackoverflow.com/a/1026087/3640307 */
function pb_capitalize_first_letter(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function pb_truncate_string(str, length) {

    str = str.trim();

    return (str.length <= length) ? str : (str.substring(0, length) + "...");
}

/* https://stackoverflow.com/a/2647967/3640307 */
function pb_variable_exists(variable) {
    return !(typeof variable === 'undefined' || variable === null);
}

function pb_array_not_empty(array) {
    return (pb_variable_exists(array) && !(array.length == 0));
}

function pb_array_empty(array) {
    return !(pb_array_not_empty(array));
}

function pb_is_empty_string(str) {
    return (str == null || str == undefined || str.trim() == "" || str.trim().length === 0);
}

function pb_update_value(id, value) {
    $('#' + id).val(value);
}

/* https://stackoverflow.com/a/46181/3640307 */
function pb_is_valid_email(email) {

    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return regex.test(String(email).toLowerCase());
}

function pb_is_valid_contact(contact) {

    var regex = /^[0-9]{3,20}$/;
    return regex.test(String(email).toLowerCase());
}

function pb_set_focus_by_id(target) {
    $('#' + target).focus();
}

function pb_register_return_key(target_id, callback) {

    $('#' + target_id).keypress(function (event) {

        var key = event.which;

        if (key == 13) callback();
    });
}

function pb_is_string_minimum_length(str, min_length) {
    return (str.length < min_length) ? false : true;
}

function pb_equal_strings(str1, str2, ignore_case = false) {

    if (!pb_variable_exists(str1) || !pb_variable_exists(str2)) return false;
    else if (ignore_case) return (str1.toLowerCase() === str2.toLowerCase());
    else return (str1 === str2);
}

function pb_is_empty_object(obj) {
    return $.isEmptyObject(obj);
}
/* https://stackoverflow.com/a/1353611/3640307 */
function pb_is_number(num) {
    return pb_variable_exists(num) && isFinite(String(num));
}

function pb_is_positive_number(num) {
    return pb_is_number(num) && (num >= 0);
}

/* https://stackoverflow.com/a/1353711/3640307 */
function pb_is_valid_date(date) {
    return date instanceof Date && !isNaN(date);
}

function pb_value_from_percent(percentage, amount, fixed_point = false, decimal_place = 2) {

    var result = (percentage / 100) * amount;

    return fixed_point ? +Number.parseFloat(result).toFixed(decimal_place) : result;
}

function pb_percent_from_value(value, amount, fixed_point = false, decimal_place = 2) {

    var result = (value / amount) * 100;

    return fixed_point ? +Number.parseFloat(result).toFixed(decimal_place) : result;
}

/* https://stackoverflow.com/a/8511350/3640307 */
function pb_is_object(obj) {
    return (typeof obj === 'object') && (obj !== null);
}

/* https://stackoverflow.com/a/175787/3640307 */
function pb_is_value_number(str) {
    return !isNaN(str);
}

function pb_get_element_value_from_form_object(form_object, element_name) {
    return form_object.find("[name=" + element_name + "]").val();
}

function pb_set_element_value_in_form_object(form_object, element_name, element_value) {
    form_object.find("[name=" + element_name + "]").val(element_value);
}