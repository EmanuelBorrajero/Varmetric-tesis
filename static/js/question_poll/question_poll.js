var $ = jQuery.noConflict();

// Create Question Poll
function open_modal_create_question_poll(url){
    $('#createQuestionPoll').load(url, function (){
        $(this).modal('show');
    });
}

function create_question_poll(){
    activ_button_regist();
    $.ajax({
        data: $('#question_poll_form_create').serialize(),
        url: $('#question_poll_form_create').attr('action'),
        type: $('#question_poll_form_create').attr('method'),
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
	if($('#create_button_question_poll').prop('disabled')){
		$('#create_button_question_poll').prop('disabled',false);
	}else{
		$('#create_button_question_poll').prop('disabled', true);
	}
}

function close_modal_regist() {
	$('#createQuestionPoll').modal('hide');
}

function showErrorsRegist(errores) {
	$('#errorsCreateQuestionPoll').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsCreateQuestionPoll').append(error);
}

//Update Dimension
function open_modal_update_question_poll(url){
    $('#updateQuestionPoll').load(url, function (){
        $(this).modal('show');
    });
}

function update_question_poll(){
    activ_button_update();
    var data = new FormData($('#question_poll_form_update').get(0));
    $.ajax({
        data: data,
        url: $('#question_poll_form_update').attr('action'),
        type: $('#question_poll_form_update').attr('method'),
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
	if($('#update_button_question_poll').prop('disabled')){
		$('#update_button_question_poll').prop('disabled',false);
	}else{
		$('#update_button_question_poll').prop('disabled', true);
	}
}

function close_modal_update() {
	$('#updateQuestionPoll').modal('hide');
}

function showErrorsEdit(errores) {
	$('#errorsUpdateQuestionPoll').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsUpdateQuestionPoll').append(error);
}

//Delete Dimension
function open_modal_delete_question_poll(url){
    $('#deleteQuestionPoll').load(url, function (){
        $(this).modal('show');
    });
}

function delete_question_poll(){
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#question_poll_form_delete').attr('action'),
        type: $('#question_poll_form_delete').attr('method'),
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
	$('#deleteQuestionPoll').modal('hide');
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