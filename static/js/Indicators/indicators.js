var $ = jQuery.noConflict();

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