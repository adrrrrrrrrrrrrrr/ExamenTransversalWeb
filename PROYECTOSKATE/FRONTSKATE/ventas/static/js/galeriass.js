//alert("hola0")


function galeriaLogin(swLogin){
    let url_host = 'http://localhost:9020';  // Asegúrate de que url_host apunte al puerto correcto

    let url_gal = url_host + '/ventas/backend/productos/'
    // Si es con Login llama a otra url
    if (swLogin)
        url_gal = url_host + '/ventas/backend/productos_login/'
    $.ajax({
        type: "GET",      // GET, PUT, POST, DELETE
        async: false,      // Sincrónico
        url: url_gal ,  // Url de la API
        cache: false,
        dataType: "json",             // Formato de envio
        beforeSend: function (xhr) {
            // Si es con Login rescata el token del LocalStorage
            // y Lo Envía
            if (swLogin){
                url_token_access = localStorage.getItem("url_token_access");
                xhr.setRequestHeader('Authorization','Bearer '+url_token_access );
            }
            // Método de ejecuta antes de enviar
            console.log('... cargando...');
        }
        , error: function (data) {
            alert("Error " +   JSON.stringify(data))
            console.log('Tenemos problemas Houston ' +  JSON.stringify(data));
        },
        success: function (data) {
            //alert("Success" + data)
            if (!data.OK){
                alert(data.msg)
                return
            }
            renderizaHtml(data)
        }
    });
}


let carrito = []; // Arreglo para almacenar los productos del carrito

function renderizaHtml(data) {
    let strProd = "";
    for (let x = 0; x < data.registro.length; x++) {
        let reg = data.registro[x];
        let unProd = `
        <div class="col-sm-6 col-lg-4">
            <div class="card card-sm">
                <a href="#" class="d-block">
                    <img src="/static/img/tablas/${reg.imagen}" class="card-img-top"></a>
                <div class="card-body">
                    <div class="d-flex align-items-center">
                        <div>
                            <div>${reg.nombre}</div>
                            <div class="text-secondary">${reg.desc_corta}</div>
                        </div>
                        <div class="ms-auto">   
                            <!-- Download SVG icon from http://tabler-icons.io/i/eye -->
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10 12a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" /><path d="M21 12c-2.4 4 -5.4 6 -9 6c-3.6 0 -6.6 -2 -9 -6c2.4 -4 5.4 -6 9 -6c3.6 0 6.6 2 9 6" /></svg>
                            ${reg.cant_favoritos}
                            <!-- Download SVG icon from http://tabler-icons.io/i/heart -->
                             <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M19.5 12.572l-7.5 7.428l-7.5 -7.428a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.572" /></svg>
                            ${reg.cant_vistos}
                            <!-- Download SVG icon from http://tabler-icons.io/i/brand-cashapp -->
                             <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-brand-cashapp"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M17.1 8.648a.568 .568 0 0 1 -.761 .011a5.682 5.682 0 0 0 -3.659 -1.34c-1.102 0 -2.205 .363 -2.205 1.374c0 1.023 1.182 1.364 2.546 1.875c2.386 .796 4.363 1.796 4.363 4.137c0 2.545 -1.977 4.295 -5.204 4.488l-.295 1.364a.557 .557 0 0 1 -.546 .443h-2.034l-.102 -.011a.568 .568 0 0 1 -.432 -.67l.318 -1.444a7.432 7.432 0 0 1 -3.273 -1.784v-.011a.545 .545 0 0 1 0 -.773l1.137 -1.102c.214 -.2 .547 -.2 .761 0a5.495 5.495 0 0 0 3.852 1.5c1.478 0 2.466 -.625 2.466 -1.614c0 -.989 -1 -1.25 -2.886 -1.954c-2 -.716 -3.898 -1.728 -3.898 -4.091c0 -2.75 2.284 -4.091 4.989 -4.216l.284 -1.398a.545 .545 0 0 1 .545 -.432h2.023l.114 .012a.544 .544 0 0 1 .42 .647l-.307 1.557a8.528 8.528 0 0 1 2.818 1.58l.023 .022c.216 .228 .216 .569 0 .773l-1.057 1.057z" /></svg>             
                             ${reg.precio}
                        </div>
                    </div>
                </div>
                <button class="boton-item" onclick="agregarAlCarrito('${reg.nombre}', ${parseFloat(reg.precio)})">Agregar al Carrito</button>
            </div>
        </div>
        `;
        strProd += unProd;
    }
    document.getElementById("objDiv").innerHTML = strProd;
}

function agregarAlCarrito(nombre, precio) {
    const index = carrito.findIndex(item => item.nombre === nombre);
    if (index > -1) {
        carrito[index].cantidad++;
    } else {
        carrito.push({ nombre, precio, cantidad: 1 });
    }
    mostrarCarrito();
}

function mostrarCarrito() {
  let strCarrito = "<h2>Carrito:</h2>";
  let total = 0;

  carrito.forEach((item, index) => {
      total += item.precio * item.cantidad;
      strCarrito += `
          <div class="carrito-item">
              ${item.nombre} - $${item.precio.toFixed(2)} x ${item.cantidad} 
              <button onclick="actualizarCantidad(${index}, 1)">+</button>
              <button onclick="actualizarCantidad(${index}, -1)">-</button>
              <button onclick="eliminarDelCarrito(${index})">Eliminar</button>
          </div>`;
  });

  strCarrito += `<div class="total"><strong>Total: $${total.toFixed(2)}</strong></div>`;
  strCarrito += `<button class="btn-pagar" onclick="pagar()">Pagar</button>`;
  
  document.getElementById("carritoDiv").innerHTML = strCarrito;
  
  // Mostrar el carrito si hay productos
  if (carrito.length > 0) {
      document.getElementById("carritoDiv").classList.add("active");
  } else {
      document.getElementById("carritoDiv").classList.remove("active");
  }
}


function actualizarCantidad(index, cambio) {
    if (carrito[index].cantidad + cambio > 0) {
        carrito[index].cantidad += cambio;
    } else {
        eliminarDelCarrito(index);
    }
    mostrarCarrito();
}

function eliminarDelCarrito(index) {
    carrito.splice(index, 1);
    mostrarCarrito();
}

function pagar() {
  alert("Proceso de pago iniciado. Total a pagar: $" + calcularTotal().toFixed(2));
  carrito = []; // Vaciar el carrito
  document.getElementById("carritoDiv").innerHTML = ""; // Limpiar el contenido del carrito
  document.getElementById("carritoDiv").classList.remove("active"); // Asegúrate de quitar la clase 'active'
}


function calcularTotal() {
    return carrito.reduce((total, item) => total + (item.precio * item.cantidad), 0);
}
