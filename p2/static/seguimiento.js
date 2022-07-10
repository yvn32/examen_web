$(document).ready(function(){

  const productos = [
    { codPedido: 00001,
	    codProducto: 10001,
	    url: "https://images.lider.cl/wmtcl?source=url[file:/productos/1126576a.jpg]&sink",
      descripcion: "Macetero cerámica con plato",
      precio: "$6.570",
      fechaCompra: "20/05/22",
      fechaDespacho: "22/05/22",
	    estado: "Entregado"},
    { codPedido: 00002,
	    codProducto: 10002,
	    url: "https://casaideas.cl/media/catalog/product/3/2/3222387000016_1_3.jpg?optimize=low&bg-color=255,255,255&fit=bounds&height=&width=&canvas=:",
      descripcion: "Maceta Fibra-Bambú 18x40 cm",
      precio: "$5.890",
      fechaCompra: "24/05/22",
      fechaDespacho: "Pendiente entrega",
	    estado: "En bodega"},
    { codPedido: 00001,
	    codProducto: 10003,
	    url: "https://sodimac.scene7.com/is/image/SodimacCL/461997?fmt=jpg&fit=fit,1&wid=420&hei=420",
      descripcion: "Tierra de hoja para jardín 80 lt",
      precio: "$8.790",
      fechaCompra: "20/05/22",
      fechaDespacho: "Pendiente entrega",
	    estado: "En camino"},
    { codPedido: 00002,
	    codProducto: 10004,
	    url: "https://www.vivamos.cl/wp-content/uploads/2022/03/photoroom_002_20220330_011345.png",
      descripcion: "Tierra de maceteros Roots 6 L",
      precio: "$2.390",
      fechaCompra: "24/05/22",
      fechaDespacho: "25/05/22",
	    estado: "Entregado"}
  ];

  $("#rastreado").hide();
  $("#vistaHistorial").hide();

  //*** SEGUIMIENTO DE PEDIDOS ***

  $("#rastrear").click(function(e){
    e.preventDefault();
    validarNum();
  });

  function validarNum(){
    let validar = $("#codigoRastreo").val();
    let exreg = /^[0-9]+$/;

    if(exreg.test(validar)){
      mostrarEstado();
    }
    else{
      alert("Por favor ingrese un código válido");
      $("#rastreado").hide();
    };
  };

  //Mostrar estado de entrega de productos a partir de código de pedido ingresado
  function mostrarEstado(){
    let codigo = parseInt($("#codigoRastreo").val());
    let texto = "";
    let contador = 0;

    productos.forEach((element) => {
      if(codigo == element.codPedido){
        contador += 1;
        var color = "";

        if(element.estado == "Entregado"){
          var color = "green";
        }
        else if(element.estado == "En bodega"){
          var color = "orange";
        }
        else{
          var color = "blue";
        };

        var textoSeguimiento =
        `<div class="col-12 col-md-6 col-lg-10 justify-content-center d-flex mt-3 mx-auto">
          <div class="d-flex flex-column flex-lg-row align-items-center p-3 shadow-lg rounded-3">
            <div style="background-image: url(${element.url});
            width: 100px;
            height: 100px;
            background-size: cover;
            background-position: center;
            border-radius: 100px;
            ">
            </div>
            <div class="ms-3">
              <h4>${element.descripcion}</h4>
            </div>
            <div class="ms-3 mx-2 d-flex align-items-center" style="border: ${color} solid 1px; border-radius: 15px;">
              <h5 class="p-0 m-0 px-3 py-2 fs-5" style="color: ${color};">${element.estado}</h5>
            </div>
          </div>
        </div>`;
  
        texto += textoSeguimiento;
      }
    });

    if(contador > 0){
      $("#prodSeguimiento").html(texto);
      $("#rastreado").show();
    }
    else{
      alert("El código ingresado no corresponde a ningún pedido");
      $("#rastreado").hide();
    };
  };

  //*** HISTORIAL DE COMPRAS ***

  //Mostrar historial
  $("#historial").click(function(e){
    e.preventDefault();
    mostrarHistorial();
  });

  //Ocultar historial
  $("#ocultar").click(function(e){
    e.preventDefault();
    $("#vistaHistorial").hide();
  }); 

  //Desplegar información de compras
  function mostrarHistorial(){
    let text = "";

    productos.forEach((element) => {
        var textoHistorial = 
        `<div class="col-12 col-md-6 col-lg-6 justify-content-center d-flex mt-3 mx-auto">
          <div class="d-flex flex-column flex-lg-row align-items-center p-3 shadow-lg rounded-3">
            <div style="background-image: url(${element.url});
            width: 100px;
            height: 100px;
            background-size: cover;
            background-position: center;
            border-radius: 100px;
            ">
            </div>
            <div class="ms-3">
              <h5>${element.descripcion}</h5>
              <p>Código de producto: ${element.codProducto}<br>
                Precio de compra: ${element.precio}<br>
                Fecha de compra: ${element.fechaCompra}<br>
                Código de pedido: ${element.codPedido}<br>
                Fecha de despacho: ${element.fechaDespacho}</p>
                <div class="ms-3 mx-2 d-flex align-items-center justify-content-center" style="border: #2A9D8F solid 1px; border-radius: 15px;">
                  <h5 class="p-0 m-0 px-3 py-2 fs-5" style="color:#2A9D8F;">${element.estado}</h5>
                </div>
            </div>
          </div>
        </div>`;
  
      text += textoHistorial;
    });
    $("#prodHistorial").html(text);
    $("#vistaHistorial").show();
  };

});