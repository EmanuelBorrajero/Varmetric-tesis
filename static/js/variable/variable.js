var $ = jQuery.noConflict();

function open_modal_create_variable(url){
    $('#createVariable').load(url, function (){
        $(this).modal('show');
    });
}
//Create Variable
function create_variable(){
    activ_button_regist();
    $.ajax({
        data: $('#variable_form_create').serialize(),
        url: $('#variable_form_create').attr('action'),
        type: $('#variable_form_create').attr('method'),
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
	if($('#create_button_variable').prop('disabled')){
		$('#create_button_variable').prop('disabled',false);
	}else{
		$('#create_button_variable').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createVariable').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateVariable').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateVariable').append(error);
}

//Update Variable
function open_modal_update_variable(url){
    $('#updateVariable').load(url, function (){
        $(this).modal('show');
    });
}

function update_variable(){
    activ_button_update();
    var data = new FormData($('#variable_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#variable_form_update').attr('action'),
        type: $('#variable_form_update').attr('method'),
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
	if($('#update_button_variable').prop('disabled')){
		$('#update_button_variable').prop('disabled',false);
	}else{
		$('#update_button_variable').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateVariable').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateVariable').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateVariable').append(error);
}

//Delete Variable
function open_modal_delete_variable(url){
    $('#deleteVariable').load(url, function (){
        $(this).modal('show');
    });
}

function delete_variable(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#variable_form_delete').attr('action'),
        type: $('#variable_form_delete').attr('method'),
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
	$('#deleteVariable').modal('hide');
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