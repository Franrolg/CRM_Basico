from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        user = authenticate(request, username=usuario, password=contrasena)

        if user: 
            login(request, user)
            messages.success(request, "¡Has iniciado sesión!")
        else: 
            messages.error(request, "¡Error al iniciar sesión!")
        
        return redirect('index')

    return render(request, 'index.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "¡Has cerrado sesión!")
    return redirect('index')

def registro_usuario(request):
    return render(request, 'registro_usuario.html')
