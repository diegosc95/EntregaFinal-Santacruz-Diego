from .models import Avatar

def avatar_context(request):
    imagen_url = None
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario=request.user).last()
        if avatar:
            imagen_url = avatar.imagen.url
    return {'imagen_url': imagen_url}