var $ = jQuery.noConflict();

  function open_modal_create_scale(var_id) {
	$('#myModal').modal('show');
    var newField = document.createElement("div");
    newField.classList.add("mb-3");
    newField.innerHTML = `
      <input type="hidden" class="form-control" id="var_id" name="var_id" value="`+var_id+`">
    `;
    // Agregar el nuevo campo al formulario
    var form = document.querySelector("form");
    form.appendChild(newField);
}


  function sendDates() {
        var countValue = document.getElementById('count').value;
        if (countValue === '') {
          notificationError();
        } else {
          var formData = $('#miFormulario').serialize();
          // Enviar los datos mediante AJAX
          console.log(formData);
        $.ajax({
          data: formData,
          url: $('#miFormulario').attr('action'),
          type: $('#miFormulario').attr('method'), 
          success: function(response) {
            waitalert(); // Mostrar una alerta de espera
            window.location.href = response.url + response.var_id
          }
        });
        }
      }

  function close_modal_scale() {
	$('#myModal').modal('hide');
    location.reload();
}

function close_modal_and_wait() {
	$('#myModal').modal('hide');
}

//Crear Etiqueta
function open_modal_create(url){
  $('#createEscale').load(url, function (){
      $(this).modal('show');
  });
}

function create_label(){
  var scaleLabel = $('#id_scale_label').val();
  if (scaleLabel === '') {
    notificationErrorCreate('La etiqueta de escala no puede estar vacía');
    return;
  }else{
  activ_button_create();
  var data = new FormData($('#create_scale').get(0));
  $.ajax({
      data: data,
      url: $('#create_scale').attr('action'),
      type: $('#create_scale').attr('method'),
      cache: false,
      contentType: false,
      processData: false,
      success: function (response) {
          notificationSuccessCreate(response.message);
          close_modal_create();
          location.reload();
      },
      error: function (error) {
          notificationErrorCreate(error.responseJSON.message);
          showErrorsCreate(error);
          activ_button_create();
      }
  });
}
}

function activ_button_create(){
	if($('#create_button').prop('disabled')){
		$('#create_button').prop('disabled',false);
	}else{
		$('#create_button').prop('disabled', true);
	}
}

function close_modal_create() {
	$('#createEscale').modal('hide');
}

function showErrorsCreate(errores) {
	$('#errors').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errors').append(error);
}

//SweetAlert2
function waitalert(){
    close_modal_and_wait();
    Swal.fire({
        title: 'Procesando',
        text: 'Espere un momento...',
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false
      });
      Swal.showLoading();
    }

function notificationError(){
	Swal.fire({
		title: 'Error!',
		text: 'El campo de cantidad de intervalos no puede estar vacío',
		icon: 'error'
	})
}

function notificationErrorCreate(mensaje){
	Swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}

function notificationSuccessCreate(mensaje) {
	Swal.fire({
		title: 'Correcto!',
		text: mensaje,
		icon: 'success'
	})
}


