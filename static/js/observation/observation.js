var $ = jQuery.noConflict();

function open_modal_create_observation(url){
    $('#createObservation').load(url, function (){
        $(this).modal('show');
    });
}
//Create Variable
function create_observation(){
    activ_button_regist();
    $.ajax({
        data: $('#observation_form_create').serialize(),
        url: $('#observation_form_create').attr('action'),
        type: $('#observation_form_create').attr('method'),
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
	if($('#create_button_observation').prop('disabled')){
		$('#create_button_observation').prop('disabled',false);
	}else{
		$('#create_button_observation').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createObservation').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateObservation').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateObservation').append(error);
}

//Update Variable
function open_modal_update_observation(url){
    $('#updateObservation').load(url, function (){
        $(this).modal('show');
    });
}

function update_observation(){
    activ_button_update();
    var data = new FormData($('#observation_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#observation_form_update').attr('action'),
        type: $('#observation_form_update').attr('method'),
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
	if($('#update_button_observation').prop('disabled')){
		$('#update_button_observation').prop('disabled',false);
	}else{
		$('#update_button_observation').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateObservation').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateObservation').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateObservation').append(error);
}

//Delete Variable
function open_modal_delete_observation(url){
    $('#deleteObservation').load(url, function (){
        $(this).modal('show');
    });
}

function delete_observation(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#observation_form_delete').attr('action'),
        type: $('#observation_form_delete').attr('method'),
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
	$('#deleteObservation').modal('hide');
}

//Observation Details
function open_modal_detail_observation(url){
    $('#detailObservationCriterion').load(url, function (){
        $(this).modal('show');
    });
}

function close_modal_detail() {
	$('#detailObservationCriterion').modal('hide');
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

