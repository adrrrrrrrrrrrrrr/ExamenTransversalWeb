 // Definimos la parte fija de la Url
 var url_api= 'http://localhost:9020/ventas/'    
 //var lo_path = 'persona/'
 var lo_path = 'proveedores'


function limpiar() {
    //document.getElementById('txRut').value = ""
    document.getElementById('txIdProveedor').value = ""
    document.getElementById('txNombreProveedor').value = ""
    document.getElementById('txDireccionProveedor').value = ""
    document.getElementById('txTelefono').value = ""
    document.getElementById('txCorreo').value = ""
    
}




function ProveedoresAgregar() {
    var parametros = {
        "id_proveedor": document.getElementById('txIdProveedor').value,
        "nombre_proveedor": document.getElementById('txNombreProveedor').value,
        "direccion": document.getElementById('txDireccionProveedor').value,
        "telefono": document.getElementById('txTelefono').value,
        "correo": document.getElementById('txCorreo').value,
    };

    $.ajax({
        type: "POST",
        url: url_api + lo_path,
        data: JSON.stringify(parametros), // Convertimos el objeto a JSON
        contentType: "application/json", // Especificamos el tipo de contenido JSON
        dataType: "json",
        beforeSend: function () {
            console.log('Enviando datos...');
        },
        success: function (data) {
            console.log('Respuesta del servidor:', data);
            if (!data.OK) {
                alert(data.msg); // Mostrar mensaje de error si no es OK
            } else {
                alert("PROVEEDOR AGREGADO"); // Mostrar mensaje de éxito
                limpiar(); // Limpiar campos después de agregar
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log('Error en la solicitud:', textStatus, errorThrown);
            alert('Error al procesar la solicitud.');
        }
    });
}



function ProveedoresEliminar() {
    var id_proveedor = document.getElementById('txIdProveedor').value;

    // Confirmar eliminación
    if (!confirm('¿Estás seguro de que deseas eliminar el proveedor? ' + id_proveedor + '?')) {
        return;
    }

    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "DELETE",      // DELETE method
        async: false,        // Sincrónico
        url: url_api + lo_path + '/' + id_proveedor,  // Url de la API con ID del avión
        cache: false,
        dataType: "json",    // Formato de envio
        beforeSend: function (data) {
            // Método de ejecuta antes de enviar
            console.log('... eliminando...');
        },
        error: function (data) {
            // Si hay un error mostramos un mensaje
            console.log('Tenemos problemas  ' + data);
            alert('Error: ' + data.statusText);
        },
        success: function (data) {
            json = data;
            // Si no es Ok envia Mensaje
            if (!json.OK) {
                alert(JSON.stringify(json.msg));
                return;
            }
            alert(json.msg);
            limpiar();
        }
    });
}




function ProveedoresActualizar(){
    var parametros = {
        id_proveedor: document.getElementById('txIdProveedor').value,
        nombre_proveedor: document.getElementById('txNombreProveedor').value,
        direccion: document.getElementById('txDireccionProveedor').value,
        telefono: document.getElementById('txTelefono').value,
        correo: document.getElementById('txCorreo').value,
    };

    var id_proveedor = document.getElementById('txIdProveedor').value;

    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "PUT",      // GET, PUT, POST, DELETE
        data: JSON.stringify(parametros),  // Envío de Parámetros
        contentType: "application/json",   // Formato de envío
        async: false,      // Sincrónico
        url: url_api + lo_path + '/' + id_proveedor,  // Url de la API
        cache: false,
        dataType: "json",  // Formato de respuesta
        beforeSend: function () {
            // Método que se ejecuta antes de enviar
            console.log('... actualizando...');
        },
        error: function (data) {
            // Si hay un error mostramos un mensaje
            console.log('Tenemos problemas  ' + JSON.stringify(data));
            alert('Error: ' + data.statusText);
        },
        success: function (data) {
            var json = data;
            // Si no es Ok, envía un mensaje
            if (!json.OK) {
                alert(json.msg);
                return;
            }
            alert(json.msg);
            limpiar();
        }
    });
}


function ProveedoreslLeer() {
    var id_proveedor = document.getElementById('txIdProveedor').value;
    var pathUrl = url_api + lo_path + '/' + id_proveedor;

    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "GET",       // Método GET
        async: false,      // Sincrónico
        url: pathUrl,      // URL con el idAvion
        cache: false,
        dataType: "json",  // Formato de respuesta
        beforeSend: function () {
            // Método que se ejecuta antes de enviar
            console.log('... cargando...');
        },
        error: function (xhr, status, error) {
            // Manejo de error
            alert("Error: proveedor no registrado " + xhr.statusText);
            console.log('Tenemos problemas Houston ' + JSON.stringify(xhr));
            // Limpiar los campos en caso de error
            
            document.getElementById('txNombreProveedor').value = "";
            document.getElementById('txDireccionProveedor').value = "";
            document.getElementById('txTelefono').value = "";
            document.getElementById('txCorreo').value = "";

            habilitaLeer();

        },
        success: function (data) {
            // Manejo de éxito
            if (!data.OK) {
                alert(data.msg);
                return;
            }

            // Rellenar los campos con los datos obtenidos
            document.getElementById('txNombreProveedor').value = data.registro.nombre_proveedor;
            document.getElementById('txDireccionProveedor').value = data.registro.direccion;
            document.getElementById('txTelefono').value = data.registro.telefono;
            document.getElementById('txCorreo').value = data.registro.correo;
            habilitaLeer();

        }
    });
}

function habilitaLeer() {
    // Habilitar/Deshabilitar campos o botones según sea necesario
    console.log('habilitaLeer ejecutado');
}


