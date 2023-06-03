var $ = jQuery.noConflict();

// Create Question Interview
function open_modal_create_question_interview(url){
    $('#createQuestionInterview').load(url, function (){
        $(this).modal('show');
    });
}

function create_question_interview(){
    activ_button_regist();
    $.ajax({
        data: $('#question_interview_form_create').serialize(),
        url: $('#question_interview_form_create').attr('action'),
        type: $('#question_interview_form_create').attr('method'),
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
	if($('#create_button_question_interview').prop('disabled')){
		$('#create_button_question_interview').prop('disabled',false);
	}else{
		$('#create_button_question_interview').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createQuestionInterview').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateQuestionOInterview').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateQuestionOInterview').append(error);
}

//Update Question Interview
function open_modal_update_question_interview(url){
    $('#updateQuestionInterview').load(url, function (){
        $(this).modal('show');
    });
}

function update_question_interview(){
    activ_button_update();
    var data = new FormData($('#question_interview_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#question_interview_form_update').attr('action'),
        type: $('#question_interview_form_update').attr('method'),
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
	if($('#update_button_question_interview').prop('disabled')){
		$('#update_button_question_interview').prop('disabled',false);
	}else{
		$('#update_button_question_interview').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateQuestionInterview').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateQuestionInterview').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateQuestionInterview').append(error);
}

//Delete Question Interview
function open_modal_delete_question_interview(url){
    $('#deleteQuestionInterview').load(url, function (){
        $(this).modal('show');
    });
}

function delete_question_interview(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#question_interview_form_delete').attr('action'),
        type: $('#question_interview_form_delete').attr('method'),
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
	$('#deleteQuestionInterview').modal('hide');
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