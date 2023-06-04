var $ = jQuery.noConflict();

// Create Observation Criterions
function open_modal_create_observation_criterions(url){
    $('#createObservationCriterions').load(url, function (){
        $(this).modal('show');
    });
}

function create_observation_criterions(){
    activ_button_regist();
    $.ajax({
        data: $('#observation_criterions_form_create').serialize(),
        url: $('#observation_criterions_form_create').attr('action'),
        type: $('#observation_criterions_form_create').attr('method'),
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
	if($('#create_button_observation_criterions').prop('disabled')){
		$('#create_button_observation_criterions').prop('disabled',false);
	}else{
		$('#create_button_observation_criterions').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createObservationCriterions').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateObservationCriterions').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateObservationCriterions').append(error);
}

//Update Observation Criterions
function open_modal_update_observation_criterions(url){
    $('#updateObservationCriterions').load(url, function (){
        $(this).modal('show');
    });
}

function update_observation_criterions(){
    activ_button_update();
    var data = new FormData($('#observation_criterions_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#observation_criterions_form_update').attr('action'),
        type: $('#observation_criterions_form_update').attr('method'),
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
	if($('#update_button_observation_criterions').prop('disabled')){
		$('#update_button_observation_criterions').prop('disabled',false);
	}else{
		$('#update_button_observation_criterions').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateObservationCriterions').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateObservationCriterions').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateObservationCriterions').append(error);
}

//Delete Observation Criterions
function open_modal_delete_observation_criterions(url){
    $('#deleteObservationCriterions').load(url, function (){
        $(this).modal('show');
    });
}

function delete_observation_criterions(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#observation_criterions_form_delete').attr('action'),
        type: $('#observation_criterions_form_delete').attr('method'),
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
	$('#deleteObservationCriterions').modal('hide');
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