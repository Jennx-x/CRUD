(function ($) {
    "use strict";

    // Spinner
    // Función para ocultar un spinner (cargando) después de un breve tiempo
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show'); // Remueve la clase 'show' para ocultar el spinner
            }
        }, 1);
    };
    spinner(); // Llama a la función spinner para ejecutarla

    // Botón "Volver arriba"
    // Muestra el botón al hacer scroll más de 300px
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow'); // Muestra el botón
        } else {
            $('.back-to-top').fadeOut('slow'); // Oculta el botón
        }
    });
    // Acción al hacer clic en el botón "Volver arriba"
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo'); // Desplaza suavemente hacia arriba
        return false; // Previene el comportamiento predeterminado
    });

    // Toggler de la barra lateral
    // Cambia la clase "open" en la barra lateral y el contenido al hacer clic
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false; // Previene el comportamiento predeterminado
    });

    // Barra de progreso
    // Inicializa la barra de progreso al llegar a un cierto punto de desplazamiento
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%'); // Ajusta el ancho de la barra según su valor
        });
    }, {offset: '80%'}); // Se activa al llegar al 80% de la vista

    // Calendario
    // Inicializa un selector de fecha en línea
    $('#calender').datetimepicker({
        inline: true,
        format: 'L' // Formato de fecha
    });
})(jQuery);
    // BOTON DE EDITAR

    

    // Función para asignar los datos al formulario de eliminación
function setDeleteEventData(button) {
    var eventoId = button.getAttribute('data-id');  // Asumiendo que el id del evento es el atributo 'data-id'
    var form = document.getElementById('deleteEventForm');
    form.action = '/eliminarEvento/' + eventoId;  // Asegúrate de que esta URL esté correctamente configurada en tu URLconf
    // Muestra el modal de confirmación
    $('#deleteAppointmentModal').modal('show');
}

function openDeleteModal(eventoId) {
    // Obtén el formulario dentro del modal
    const deleteForm = document.getElementById('deleteEventForm');
    if (deleteForm) {
        // Actualiza la acción del formulario con la URL dinámica
        deleteForm.action = `/eliminarEvento/${eventoId}/`; // Ajusta la URL según tu vista en Django
    } else {
        console.error("Formulario de eliminación no encontrado.");
    }

    // Muestra el modal
    const modalElement = document.getElementById('deleteAppointmentModal');
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    } else {
        console.error("Modal de eliminación no encontrado.");
    }
}


function openEditModal(evento) {
    // Asigna los valores al formulario
    document.getElementById('editId').value = evento.id;
    document.getElementById('editNombre').value = evento.nombre;
    document.getElementById('editFecha').value = evento.fecha;
    document.getElementById('editHora').value = evento.hora;
    document.getElementById('editLugar').value = evento.lugar;
    document.getElementById('editArtista').value = evento.artista || ''; // Si no hay artista, poner cadena vacía
    document.getElementById('editDuracion').value = evento.duracion || ''; // Si no hay duración, poner cadena vacía
    document.getElementById('editTema').value = evento.tema || ''; // Si no hay tema, poner cadena vacía
    document.getElementById('editOrador').value = evento.orador || ''; // Si no hay orador, poner cadena vacía

    // Muestra el modal
    new bootstrap.Modal(document.getElementById('editAppointmentModal')).show();
}


// AJAX para Guardar los Cambios sin Recargar la Página
// javascript
document.getElementById('editEventForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);  // Toma los datos del formulario
    fetch('{% url "editar_evento" %}', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),  // CSRF Token para Django
        },
    })
    .then(response => response.json())  // Espera una respuesta en formato JSON
    .then(data => {
        if (data.success) {
            alert(data.message);
            location.reload();  // Recarga la tabla de eventos
        } else {
            alert('Error al guardar cambios');
        }
    })
    .catch(error => console.error('Error:', error));  // Captura errores
});


