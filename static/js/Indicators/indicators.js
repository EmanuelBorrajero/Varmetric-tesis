var $ = jQuery.noConflict();
//Create Indicator
function open_modal_create_indicator(url){
    $('#createIndicator').load(url, function (){
        $(this).modal('show');
    });
}

function create_indicator(){
    activ_button_regist();
    $.ajax({
        data: $('#indicator_form_create').serialize(),
        url: $('#indicator_form_create').attr('action'),
        type: $('#indicator_form_create').attr('method'),
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
	if($('#create_button_indicator').prop('disabled')){
		$('#create_button_indicator').prop('disabled',false);
	}else{
		$('#create_button_indicator').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createIndicator').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateIndicator').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateIndicator').append(error);
}

//Update Indicator
function open_modal_update_indicator(url){
    $('#updateIndicator').load(url, function (){
        $(this).modal('show');
    });
}

function update_indicator(){
    activ_button_update();
    var data = new FormData($('#indicator_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#indicator_form_update').attr('action'),
        type: $('#indicator_form_update').attr('method'),
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
	if($('#update_button_indicator').prop('disabled')){
		$('#update_button_indicator').prop('disabled',false);
	}else{
		$('#update_button_indicator').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateIndicator').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateIndicator').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateIndicator').append(error);
}

//Delete Indicator
function open_modal_delete_indicator(url){
    $('#deleteIndicator').load(url, function (){
        $(this).modal('show');
    });
}

function delete_indicator(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#indicator_form_delete').attr('action'),
        type: $('#indicator_form_delete').attr('method'),
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
	$('#deleteIndicator').modal('hide');
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