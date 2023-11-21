function open_modal_value_answer_poll(url){
    $('#valueAnswerPoll').load(url, function (){
        $(this).modal('show');
    });
}

function value_answer_poll(){
    activ_button_value();
    var data = new FormData($('#value_answer_poll_form').get(0));
    $.ajax({
        data: data,
        url: $('#value_answer_poll_form').attr('action'),
        type: $('#value_answer_poll_form').attr('method'),
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            notificationSuccess(response.message);
            close_modal_value_answer_poll();
			location.reload();
        },
        error: function (error) {
            notificationError(error.responseJSON.message);
            showErrorsValue(error);
            activ_button_value();
        }
    });
}

function activ_button_value(){
	if($('#value_button_answer_poll').prop('disabled')){
		$('#value_button_answer_poll').prop('disabled',false);
	}else{
		$('#value_button_answer_poll').prop('disabled', true);
	}
}

function close_modal_value_answer_poll() {
	$('#valueAnswerPoll').modal('hide');
}

function showErrorsValue(errores) {
	$('#errorsValueAnswerPoll').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errorsValueAnswerPoll').append(error);
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