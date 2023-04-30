from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import FormularioRegistroUsuario

def autenticar_usuario(request, usuario, contrasena):
    # Función para autenticar y logear usuarios, creada para no repetir código.

    user = authenticate(request, username=usuario, password=contrasena)
    if user: login(request, user)
    return True if user is not None else False

def index(request):
    # Vista para renderizar la página inicial.

    if request.method == 'POST':
        # Si la resquest es con método POST se realiza el inicio de sesión.
        messages.success(request, "¡Has iniciado sesión!") if autenticar_usuario(request, request.POST['usuario'], request.POST['contrasena']) else messages.error(request, "¡Error al iniciar sesión!")
        return redirect('index')
    
    return render(request, 'index.html')

def cerrar_sesion(request):
    # Vista para realizar el cierre de sesión de usuario.

    logout(request)
    messages.success(request, "¡Has cerrado sesión!")
    return redirect('index')

def registro_usuario(request):
    # Vista para renderizar la página de registro de usuarios.

    if request.method == 'POST':
        # Si la request es con método POST se realiza el registro de usuario.
        form = FormularioRegistroUsuario(request.POST)

        if form.is_valid():
            # Se valida la información ingresada antes de registrar el usuario en la BD.
            form.save()
            autenticar_usuario(request, form.cleaned_data['username'], form.changed_data['password1'])
            messages.success(request, "¡Te has registrado correctamente!")
            return redirect('index')
        
    else:
        form = FormularioRegistroUsuario()
        return render(request, 'registro_usuario.html', {'form':form})
