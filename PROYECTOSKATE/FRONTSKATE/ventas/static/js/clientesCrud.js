 // Definimos la parte fija de la Url
 var url_api= 'http://localhost:9020/ventas/'    
 //var lo_path = 'persona/'
 var lo_path = 'cliente'


function limpiar() {
    //document.getElementById('txRut').value = ""
    document.getElementById('txIdCliente').value = ""
    document.getElementById('txRut').value = ""
    document.getElementById('txNombre').value = ""
    document.getElementById('txApaterno').value = ""
    document.getElementById('txAmaterno').value = ""
    document.getElementById('txCorreo').value = ""
    document.getElementById('txTelefono').value = ""
    document.getElementById('txSexo').value = ""
    document.getElementById('txFnacimiento').value = ""
    document.getElementById('txEdad').value = ""
    document.getElementById('txDireccion').value = ""

    
}




function ClienteAgregar() {
    var parametros = {
        "id_cliente": document.getElementById('txIdCliente').value,
        "rut": document.getElementById('txRut').value,
        "nombre": document.getElementById('txNombre').value,
        "apaterno": document.getElementById('txApaterno').value,
        "amaterno": document.getElementById('txAmaterno').value,
        "correo": document.getElementById('txCorreo').value,
        "numero_telefono": document.getElementById('txTelefono').value,
        "sexo": document.getElementById('txSexo').value,
        "Fec_nacimiento": document.getElementById('txFnacimiento').value,
        "edad": document.getElementById('txEdad').value,
        "direccion": document.getElementById('txDireccion').value
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
                alert("Cliente agregado"); // Mostrar mensaje de éxito
                limpiar(); // Limpiar campos después de agregar
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log('Error en la solicitud:', textStatus, errorThrown);
            alert('Error al procesar la solicitud.');
        }
    });
}



function ClienteEliminar() {
    var id_cliente = document.getElementById('txIdCliente').value;

    // Confirmar eliminación
    if (!confirm('¿Estás seguro de que deseas eliminar el cliente con ID ' + id_cliente + '?')) {
        return;
    }

    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "DELETE",      // DELETE method
        async: false,        // Sincrónico
        url: url_api + lo_path + '/' + id_cliente,  // Url de la API con ID del avión
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




function ClienteActualizar(){
    var parametros = {
        id_cliente: document.getElementById('txIdCliente').value,
        rut: document.getElementById('txRut').value,
        nombre: document.getElementById('txNombre').value,
        apaterno: document.getElementById('txApaterno').value,
        amaterno: document.getElementById('txAmaterno').value,
        correo: document.getElementById('txCorreo').value,
        numero_telefono: document.getElementById('txTelefono').value,
        sexo: document.getElementById('txSexo').value,
        Fec_nacimiento: document.getElementById('txFnacimiento').value,
        edad: document.getElementById('txEdad').value,
        direccion: document.getElementById('txDireccion').value

    };

    var id_cliente = document.getElementById('txIdCliente').value;

    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "PUT",      // GET, PUT, POST, DELETE
        data: JSON.stringify(parametros),  // Envío de Parámetros
        contentType: "application/json",   // Formato de envío
        async: false,      // Sincrónico
        url: url_api + lo_path + '/' + id_cliente,  // Url de la API
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


function ClienteLeer() {
    var id_cliente = document.getElementById('txIdCliente').value;
    var pathUrl = url_api + lo_path + '/' + id_cliente;

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
            alert("Error: ID DE CLIENTE NO REGISTRADO " + xhr.statusText);
            console.log('Tenemos problemas Houston ' + JSON.stringify(xhr));
            // Limpiar los campos en caso de error
            document.getElementById('txRut').value = "";
            document.getElementById('txNombre').value = "";
            document.getElementById('txApaterno').value = "";
            document.getElementById('txAmaterno').value = "";
            document.getElementById('txCorreo').value = "";
            document.getElementById('txTelefono').value = "";
            document.getElementById('txSexo').value = "";
            document.getElementById('txFnacimiento').value = "";
            document.getElementById('txEdad').value = "";
            document.getElementById('txDireccion').value = "";
            habilitaLeer();

        },
        success: function (data) {
            // Manejo de éxito
            if (!data.OK) {
                alert(data.msg);
                return;
            }

            // Rellenar los campos con los datos obtenidos
            document.getElementById('txRut').value = data.registro.rut;
            document.getElementById('txNombre').value = data.registro.nombre;
            document.getElementById('txApaterno').value = data.registro.apaterno;
            document.getElementById('txAmaterno').value = data.registro.amaterno;
            document.getElementById('txCorreo').value = data.registro.correo;
            document.getElementById('txTelefono').value = data.registro.numero_telefono;
            document.getElementById('txSexo').value = data.registro.sexo;
            document.getElementById('txFnacimiento').value = data.registro.Fec_nacimiento;
            document.getElementById('txEdad').value = data.registro.edad;
            document.getElementById('txDireccion').value = data.registro.direccion;
            habilitaLeer();

       
        }
    });
}

function habilitaLeer() {
    // Habilitar/Deshabilitar campos o botones según sea necesario
    console.log('habilitaLeer ejecutado');
}


