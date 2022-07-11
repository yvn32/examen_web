from distutils.command.upload import upload
import http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from basedatos import models
from basedatos.models import producto, pedido, detallePedido, tipoPedido, estadoPedido, estadoEntrega, cliente, giro, proveedor, usuario
from django.contrib import messages
from p2.forms import productoForm

# PÁGINA DE INICIO
def inicio(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "index.html",contexto)

# REGISTRO DE USUARIO
def registro(request):
    user = ""
    pwd = ""
    espacios = 0
    msje = ""
    usuarios = []
    existe = 0
    usuarioLogueado = ""
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
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "registro.html",contexto)

# LOGIN DE USUARIO
def login(request):
    user = ""
    pwd = ""
    mensaje = ""
    usuarios = []
    loguear = False
    usuarioLogueado = ""
    usuarioLoguear = []

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
            request.session['usuarioLogueado'] = user
            usuarioLoguear = usuario.objects.get(nombreUsuario=user)
            usuarioLoguear.logueado = 1
            usuarioLoguear.save()
            contexto = {"usuarioLogueado":usuarioLogueado}
            return redirect('/',contexto)
        else:
            messages.success(request, 'Los datos ingresados son inválidos, por favor intente nuevamente')

    except:
        mensaje = f'Los datos ingresados son inválidos, por favor intente nuevamente'      
    
    contexto = {"mensaje":mensaje,
                "user":user,
                "usuarioLogueado":usuarioLogueado}
    return render(request, "login.html", contexto)

# DESLOGUEAR USUARIO
def salir(request):
    usuarioLogueado = request.session['usuarioLogueado']
    usuarioDesloguear = usuario.objects.get(nombreUsuario=usuarioLogueado)
    usuarioDesloguear.logueado = 0
    usuarioDesloguear.save()
    usuarioLogueado = ""
    request.session['usuarioLogueado'] = ""
    contexto = {"usuarioLogueado":usuarioLogueado}
    return redirect('/login',contexto)

# MANTENEDOR GENERAL
def mantenedor(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "mantenedor.html",contexto)

# MANTENEDOR DE USUARIO
def mantenedorUsuarios(request):
    usuarios = usuario.objects.all()
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado,
                "usuarios": usuarios}
    return render(request, "mantenedorUsuarios.html", contexto)

# ELIMINAR USUARIO
def eliminarUsuario(request, id):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    usuarioEliminar = usuario.objects.get(id=id)
    if usuarioEliminar.nombreUsuario == usuarioLogueado:
        messages.success(request, f'No es posible eliminar al usuario {usuarioEliminar.nombreUsuario} porque se encuentra logueado. Por favor cierre la sesión e intente la eliminación nuevamente.')
    else:
        usuarioEliminar.delete()
    return redirect('/mantenedorUsuarios')

# EDITAR USUARIO
def editarUsuario(request, id):
    espacios = 0
    usuarioEditar = usuario.objects.get(id=id)
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    try:
        pwd = request.GET["e_password"]
        print(pwd)
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
            messages.success(request, f'{usuarioEditar.nombreUsuario} modificado')
            usuarioEditar = []
    except:
        print("Error pwd")
    
    try:
        suscripcion = str(request.GET["e_suscripcion"])
        print(suscripcion)
        usuarioEditar.suscripcion = suscripcion
        usuarioEditar.save()
        messages.success(request, f'{usuarioEditar.nombreUsuario} modificado')
        usuarioEditar = []
    except:
        print("Error suscripción")
  
    contexto = {"usuarioEditar":usuarioEditar,
                "usuarioLogueado":usuarioLogueado}
    return render(request, "editarUsuario.html", contexto)

# MANTENEDOR DE PRODUCTO
def mantenedorProductos(request):
    productos = producto.objects.all()
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {'productos': productos,
                "usuarioLogueado":usuarioLogueado}
    return render(request, "mantenedorProductos.html", contexto)

# ELIMINAR PRODUCTO
def eliminarProducto(request, id):
    productoEliminar = producto.objects.get(id=id)
    productoEliminar.delete()
    return redirect('/mantenedorProductos')

# AGREGAR PRODUCTO
def ingresarProductos (request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    submitted = False
    form = productoForm
    if request.method == "POST":
        form = productoForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mantenedorProductos?submitted=True')
        else:
            print("Formulario inválido")
    return render(request, "ingresarProductos.html", {'form': form, 'submitted': submitted, 'usuarioLogueado':usuarioLogueado})

# EDITAR PRODUCTO
def editarProductos(request, pk):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    producto_id = producto.objects.get(id=pk)
    form = productoForm(instance=producto_id)

    if request.method == "POST":
        form = productoForm(request.POST, instance=producto_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mantenedorProductos')
    context = {'form':form,
                'usuarioLogueado':usuarioLogueado}
    return render(request, 'editarProductos.html', context)

# PÁGINA DE PRODUCTOS
def productos(request):
    usuarioLogueado = ""
    llamadabd = []
    productos = producto.objects.all()
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        if usuarioLogueado != "":
            print(usuarioLogueado)
            llamadabd = usuario.objects.get(nombreUsuario=usuarioLogueado) 
    except:
        request.session['usuarioLogueado'] = ""
        usuarioLogueado = ""
        print('No pasa nada')

    contexto = {'productos': productos,
                'llamadabd':llamadabd,
                'usuarioLogueado':usuarioLogueado}
    return render(request, "productos.html", contexto)

# PÁGINA DE SEGUIMIENTO
def seguimiento(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "seguimiento.html",contexto)

# PÁGINA DE DONACIONES
def donacion(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "donacion.html",contexto)

# PÁGINA DE CARRITO DE COMPRA
def carritoCompra(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "carritoCompra.html",contexto)

# PLANTILLA CON NAVBAR Y FOOTER
def plantilla(request):
    usuarioLogueado = ""
    try:
        usuarioLogueado = request.session['usuarioLogueado']
        print(usuarioLogueado)
    except:
        print('No se ha logueado ningún usuario')
    contexto = {"usuarioLogueado":usuarioLogueado}
    return render(request, "plantilla.html",contexto)

