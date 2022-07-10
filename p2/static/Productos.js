$(document).ready(function(){

  const productos = [
    { categoria: 00001,
	    codProducto: 10010,
	    url: "https://static.wixstatic.com/media/01c344_47f87077968a4af7b91806450bc6327b~mv2.jpg/v1/fill/w_500,h_667,al_c,q_85,usm_0.66_1.00_0.01/01c344_47f87077968a4af7b91806450bc6327b~mv2.webp",
      nombre: "Singonio Plateado",
      tamano: "14cm",
      precio: "$15.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una planta de interior trepadora, resistente y de fácil cuidado. Es originaria de Sudamérica y posee una hojas grandes con forma de flecha color verde claro jaspeado con nervios muy marcados."

    },
    { categoria: 00001,
	    codProducto: 10012,
	    url: "https://static.wixstatic.com/media/01c344_2807f74b85cd4773b31e67db62577845~mv2.jpg/v1/fill/w_500,h_500,al_c,q_85,usm_0.66_1.00_0.01/01c344_2807f74b85cd4773b31e67db62577845~mv2.webp",
      nombre: "Philodendro Cordatum Variegado",
      tamano: "30 cm",
      precio: "$32.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una planta trepadora (o colgante, dependiendo como la guíes) originaria de islas caribeñas. Famosa por sus hojas en forma de corazón, y con variegada en tonos amarillos, simboliza salud, abundancia y crecimiento."
    },
    { categoria: 00001,
	    codProducto: 10013,
	    url: "https://static.wixstatic.com/media/01c344_484469a6ddde42539024fef05e924ff1~mv2.jpg/v1/fill/w_500,h_667,al_c,q_85,usm_0.66_1.00_0.01/01c344_484469a6ddde42539024fef05e924ff1~mv2.webp",
      nombre: "Ficus Altíssima",
      tamano: "35 cm",
      precio: "$33.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una variante del reconocido Gomero, que al igual que este, en zonas tropicales crece como un gran árbol de exterior. Sus hojas son llamativas por su vibrante verde y además, es especial para principiantes, ya que requiere cuidados muy básicos."
    },
    { categoria: 00001,
	    codProducto: 10014,
	    url: "https://static.wixstatic.com/media/01c344_69c218c240fe470caad8e69b8e18d9bc~mv2.jpg/v1/fill/w_500,h_500,al_c,q_85,usm_0.66_1.00_0.01/01c344_69c218c240fe470caad8e69b8e18d9bc~mv2.webp",
      nombre: "Calathea Zebrina",
      tamano: "20 cm",
      precio: "$55.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Originaria de Brasil, esta calathea se caracteriza por sus hojas aterciopeladas en tonos verde oscuro y verde brillante. Es una hermosa planta que requiere mucha dedicación y cuidado."
    },
    { categoria: 00001,
	    codProducto: 10015,
	    url: "https://static.wixstatic.com/media/01c344_29ccc035772940e0ad996c1c2262244f~mv2.jpg/v1/fill/w_500,h_500,al_c,q_85,usm_0.66_1.00_0.01/01c344_29ccc035772940e0ad996c1c2262244f~mv2.webp",
      nombre: "Ficus Tineke",
      tamano: "22 cm",
      precio: "$31.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una variante del reconocido Gomero, que al igual que este, en zonas tropicales crece como un gran árbol de exterior. Sus hojas a veces pueden tener tonos rosados. Es especial para principiantes, ya que requiere cuidados muy básicos."
    },
    { categoria: 00001,
	    codProducto: 10016,
	    url: "https://static.wixstatic.com/media/01c344_b9cbf62c1ca54b00b973fb6979b7df89~mv2.jpg/v1/fill/w_500,h_500,al_c,q_85,usm_0.66_1.00_0.01/01c344_b9cbf62c1ca54b00b973fb6979b7df89~mv2.webp",
      nombre: "Aphelandra",
      tamano: "15 cm",
      precio: "$13.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una planta tropical muy atractiva por sus hojas de color verde oscuro brillante que contrastan con el blanco de los nervios. Las flores surgen de espigas terminales y suelen ser amarillas, rojas o naranjas. Florecen en primavera y en verano.  No es apta para principiantes."
    },
    { categoria: 00001,
	    codProducto: 10017,
	    url: "https://static.wixstatic.com/media/01c344_2d291f860667497e8594f26066bbb240~mv2.jpg/v1/fill/w_500,h_667,al_c,q_85,usm_0.66_1.00_0.01/01c344_2d291f860667497e8594f26066bbb240~mv2.webp",
      nombre: "Aphelandra",
      tamano: "19 cm",
      precio: "$15.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "General: Es una planta tropical originaria de Malasia. Es altamente atractiva por los colores de sus hojas que van desde el verde, amarillo, rojo, naranjo, rosado y combinación de todos ellos. No es apta para principiantes."
    },
    { categoria: 00001,
	    codProducto: 10018,
	    url: "https://static.wixstatic.com/media/01c344_b5f6c92a9c2c423f83d488c0734f1d7e~mv2.jpg/v1/fill/w_500,h_333,al_c,q_85,usm_0.66_1.00_0.01/01c344_b5f6c92a9c2c423f83d488c0734f1d7e~mv2.webp",
      nombre: "Monstera Deliciosa (Filodendro)",
      tamano: "15 cm",
      precio: "$24.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "La Monstera deliciosa es originalmente nativa de las regiones tropicales de America Central. También conocida como: Filodendro, Filodendron, Philodendro, Philodendron, Monstera, Costilla de Adán, Arpón, Hoja Rota, Mano de Tigre, Costilla de Vaca."
    },
    { categoria: 00001,
	    codProducto: 10019,
	    url: "https://static.wixstatic.com/media/01c344_cee5a7da290144f9abaf57955330f409~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/01c344_cee5a7da290144f9abaf57955330f409~mv2.webp",
      nombre: "Sansevieria",
      tamano: "45 cm",
      precio: "$17.990",
      diponibilidad:"Producto solo disponible en tienda.",
      descripcion: "Comúnmente llamada 'Lengua de Suegra', Susan es una planta muy fácil de cuidar, no requiere mucha agua, puede soportar lugares con escasa luz como también algunas horas de sol,  por lo que es perfecta para muchos espacios, además es una gran purificadora de aire!"
    }
   
  ];
  var texto_iterable=""
  productos.forEach((element) => {
    var cartaProducto = `<div class="card text-start bg-light text-black col-4 mt-4" >
        <img class="card-img-top rounded-3" src="${element.url}" alt="">
        <div class="card-body">
          <h4 class="card-title">${element.nombre}</h4>
          <p class="card-text">Tamaño: ${element.tamano}</p>
          <h3 class="card-text">Precio:</h3>
          <h3 class="card-text">${element.precio}</h3>
          <p class="card-text"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-shop" viewBox="0 0 16 16">
          <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"></path>
        </svg> ${element.diponibilidad} </p>
          <p class="card-text">${element.descripcion}</p>
          <button type="button" class="btn btn-success">
          Agregar al carrito
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart" viewBox="0 0 16 16">
          <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path>
          </svg>
              </button>
        </div>
      </div>`;
    texto_iterable+=cartaProducto;
    $("#DisplayProducto").html( texto_iterable )
  });
  
  
});