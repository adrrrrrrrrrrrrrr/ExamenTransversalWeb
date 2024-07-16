//alert(33)
var url_api_login= url_host +'/api/token/'
//var url_api= 'http://localhost:9020/api/token/'     
//var lo_path = 'persona/'

function segurLogin() {
    //alert("Login Segur" + url_api_login)
    // Creo Texto con los datos en formato json
    
    // let parametros = `username=${document.getElementById('txEmail').value}
    //     &password=${document.getElementById('txPassword').value}`
    var formData = new FormData();
    formData.append('username', document.getElementById('txUser').value);
    formData.append('password', document.getElementById('txPassword').value);
    //alert("hola" + parametros)
    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "POST",      // GET, PUT, POST, DELETE
        data: formData,  // Envio deParámetro
        async: false,      // Sincrónico
        url: url_api_login ,  // Url de la API
        contentType: false,
        processData: false,
        cache: false,
        beforeSend: function (data){
            // Método de ejecuta antes de enviar
            console.log('... cargando...');
        }
        , error: function (data) {
            msgHarrys.mensaje("Empleado","Usuario y/o Contraseña incorrectos")
            //alert("Error " + data)
            //si hay un error mostramos un mensaje
            console.log('Tenemos problemas Houston ' + JSON.stringify(data));
        },
        success: function (data) {
            console.log("Login=>",data)
            //alert("Success" + JSON.stringify(data))
            if (data.access){
                // Gurdamos amobos token's
                // No Sirve ya que la página se recarga
                // por lo cual hay que grabar en localStorage
                url_token_access =  data.access    // Error
                url_token_refresh =  data.refresh  // Error

                // Grabamos en LocalStorage
                localStorage.removeItem("url_token_access");
                localStorage.removeItem("url_token_refresh");

                localStorage.setItem("url_token_access", data.access);
                localStorage.setItem("url_token_refresh", data.refresh);
                
                msgHarrys.mensaje("Empleado","Usuario y Contraseña Correctos : " + data.access)
                // Redirección a la página de productos de la misma url
                document.location.href = "/catalogo_login";
                return
//                alert(data.refresh)
//                alert(data.access)
                }
        }
    });
}