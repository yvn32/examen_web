from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from basedatos.models import producto, pedido, detallePedido, tipoPedido, estadoPedido, estadoEntrega, cliente, giro, proveedor, usuario
from django.contrib import messages

# PÁGINA DE INICIO
def inicio(request):
    msje = ""
    contexto = {"msje":msje}
    return render(request, "index.html",contexto)

# REGISTRO DE USUARIO
def registro(request):
    user = ""
    pwd = ""
    espacios = 0
    msje = ""
    usuarios = []
    existe = 0
    try:
        user = request.GET["r_correo"]
        pwd = request.GET["r_password"]
        usuarios = usuario.objects.all()       
        for u in usuarios:
            if u.nombreUsuario == user:
                existe += 1
        for i in user:
            if i == " ":
                espacios += 1
        for i in pwd:
            if i == " ":
                espacios += 1
        if user == "" or pwd == "":
            messages.success(request, 'Por favor ingrese los datos solicitados')
        elif existe > 0:
            messages.success(request, 'El usuario ya se encuentra registrado, por favor inicie sesión')
        elif espacios > 0:
            messages.success(request, 'Usuario y password no pueden contener espacios')
        else:
            usuario.objects.create(
                nombreUsuario = user,
                password = pwd,
                suscripcion = 0,
                logueado = 0)
            messages.success(request, f'Se ha registrado al usuario {user}')
    except:
        msje = f'Los datos ingresados son inválidos, por favor intente nuevamente'
        print(msje)
    return render(request, "registro.html")

# LOGIN DE USUARIO
def login(request):
    user = ""
    pwd = ""
    mensaje = ""
    usuarios = []
    loguear = False
    try:
        user = request.GET["correo"]
        pwd = request.GET["password"]
        usuarios = usuario.objects.all()
        for u in usuarios:
            if u.nombreUsuario == user:
                for p in usuarios:
                    if p.password == pwd:
                        loguear = True
        if loguear == True:
            messages.success(request, f'Ha iniciado sesión el usuario {user}')
            request.session['usuarioLogueado'] = user
        else:
            messages.success(request, 'Los datos ingresados son inválidos, por favor intente nuevamente')
    except:
        mensaje = f'Los datos ingresados son inválidos, por favor intente nuevamente'      
    contexto = {'mensaje':mensaje,
                'user':user}
    return render(request, "login.html", contexto)

# MANTENEDOR GENERAL
def mantenedor(request):
    return render(request, "mantenedor.html")

# MANTENEDOR DE USUARIO
def mantenedorUsuarios(request):
    usuarios = usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, "mantenedorUsuarios.html", contexto)

# ELIMINAR USUARIO
def eliminarUsuario(request, id):
    usuarioEliminar = usuario.objects.get(id=id)
    usuarioEliminar.delete()
    return redirect('/mantenedorUsuarios')

# EDITAR USUARIO
def editarUsuario(request, id):
    espacios = 0
    usuarioEditar = usuario.objects.get(id=id)
    try:
        pwd = request.GET["e_password"]
        for i in pwd:
            if i == " ":
                espacios += 1
        if pwd == "":
            messages.success(request, 'No se han ingresado datos')
        elif espacios > 0:
            messages.success(request, 'Por favor elimine los espacios')
        else:
            usuarioEditar.password = pwd
            usuarioEditar.save()
            messages.success(request, 'Usuario modificado')
    except:
        print("Error")
    contexto = {"usuarioEditar":usuarioEditar}
    return render(request, "editarUsuario.html", contexto)

# MANTENEDOR DE PRODUCTO
def mantenedorProductos(request):
    productos = producto.objects.all()
    contexto = {'productos': productos}
    return render(request, "mantenedorProductos.html", contexto)

# ELIMINAR PRODUCTO
def eliminarProducto(request, id):
    productoEliminar = producto.objects.get(id=id)
    productoEliminar.delete()
    return redirect('/mantenedorProductos')

# PÁGINA DE PRODUCTOS
def productos(request):
    usuarioLogueado = request.session['usuarioLogueado']
    print(usuarioLogueado)
    mensaje = ""
    llamadabd = []
    try:
        llamadabd = usuario.objects.get(nombreUsuario=usuarioLogueado)
        print(llamadabd.nombreUsuario)
        print(llamadabd.password)
        print(llamadabd.suscripcion)
    except:
        print('Caí en el except de página de productos') 
    productos = producto.objects.all()
    contexto = {'datos': productos,
                'llamadabd':llamadabd,
                'mensaje':mensaje,
                'usuarioLogueado':usuarioLogueado}
    return render(request, "productos.html", contexto)

# PÁGINA DE SEGUIMIENTO
def seguimiento(request):
    return render(request, "seguimiento.html")

# PÁGINA DE DONACIONES
def donacion(request):
    return render(request, "donacion.html")

# PÁGINA DE CARRITO DE COMPRA
def carritoCompra(request):
    return render(request, "carritoCompra.html")

# PLANTILLA CON NAVBAR Y FOOTER
def plantilla(request):
    return render(request, "plantilla.html")

