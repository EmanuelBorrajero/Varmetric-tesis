var $ = jQuery.noConflict();
// Create Measurement Criterion
function open_modal_create_measurement_criterion(url){
    $('#createMeasurementCriterion').load(url, function (){
        $(this).modal('show');
    });
}

function create_measurement_criterion(){
    activ_button_regist();
    $.ajax({
        data: $('#measurement_criterion_form_create').serialize(),
        url: $('#measurement_criterion_form_create').attr('action'),
        type: $('#measurement_criterion_form_create').attr('method'),
        success: function (response) {
            notificationSuccess(response.message);
            close_modal_regist();
            location.reload();
        },
        error: function (error) {
            notificationError(error.responseJSON.message);
            showErrorsRegist(error);
            activ_button_regist();
        }
    });
}

function activ_button_regist(){
	if($('#create_button_measurement_criterion').prop('disabled')){
		$('#create_button_measurement_criterion').prop('disabled',false);
	}else{
		$('#create_button_measurement_criterion').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createMeasurementCriterion').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateMeasurementCriterion').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateMeasurementCriterion').append(error);
}

//Update Measurement Criterion
function open_modal_update_measurement_criterion(url){
    $('#updateMeasurementCriterion').load(url, function (){
        $(this).modal('show');
    });
}

function update_measurement_criterion(){
    activ_button_update();
    var data = new FormData($('#measurement_criterion_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#measurement_criterion_form_update').attr('action'),
        type: $('#measurement_criterion_form_update').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            notificationSuccess(response.message);
            close_modal_update();
			location.reload();
        },
        error: function (error) {
            notificationError(error.responseJSON.message);
            showErrorsEdit(error);
            activ_button_update();
        }
    });
}

function activ_button_update(){
	if($('#update_button_measurement_criterion').prop('disabled')){
		$('#update_button_measurement_criterion').prop('disabled',false);
	}else{
		$('#update_button_measurement_criterion').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateMeasurementCriterion').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateMeasurementCriterion').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateMeasurementCriterion').append(error);
}

//Delete Measurement Criterion
function open_modal_measurement_criterion(url){
    $('#deleteMeasurementCriterion').load(url, function (){
        $(this).modal('show');
    });
}

function delete_measurement_criterion(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#measurement_criterion_form_delete').attr('action'),
        type: $('#measurement_criterion_form_delete').attr('method'),
        success: function (response) {
            notificationSuccess(response.message);
            close_modal_delete();
			location.reload();
        },
        error: function () {
            notificationError("Error al Eliminar");
            close_modal_delete();
        }
    });
}

function close_modal_delete() {
	$('#deleteMeasurementCriterion').modal('hide');
}

//SweetAlert2
function notificationError(mensaje){
	Swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}

function notificationSuccess(mensaje) {
	Swal.fire({
		title: 'Correcto!',
		text: mensaje,
		icon: 'success'
	})
}