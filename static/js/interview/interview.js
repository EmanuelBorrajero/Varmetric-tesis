var $ = jQuery.noConflict();

function open_modal_create_interview(url){
    $('#createInterview').load(url, function (){
        $(this).modal('show');
    });
}
//Create Variable
function create_interview(){
    activ_button_regist();
    $.ajax({
        data: $('#interview_form_create').serialize(),
        url: $('#interview_form_create').attr('action'),
        type: $('#interview_form_create').attr('method'),
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
	if($('#create_button_interview').prop('disabled')){
		$('#create_button_interview').prop('disabled',false);
	}else{
		$('#create_button_interview').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createInterview').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateInterview').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateInterview').append(error);
}

//Update Variable
function open_modal_update_interview(url){
    $('#updateInterview').load(url, function (){
        $(this).modal('show');
    });
}

function update_interview(){
    activ_button_update();
    var data = new FormData($('#interview_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#interview_form_update').attr('action'),
        type: $('#interview_form_update').attr('method'),
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
	if($('#update_button_interview').prop('disabled')){
		$('#update_button_interview').prop('disabled',false);
	}else{
		$('#update_button_interview').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateInterview').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateInterview').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateInterview').append(error);
}

//Delete Variable
function open_modal_delete_interview(url){
    $('#deleteInterview').load(url, function (){
        $(this).modal('show');
    });
}

function delete_interview(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#interview_form_delete').attr('action'),
        type: $('#interview_form_delete').attr('method'),
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
	$('#deleteInterview').modal('hide');
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