from django.db import transaction

from apps.usuarios.models import Usuario


@transaction.atomic
def criar_usuario(username, password, email=None, first_name=None, last_name=None):
    """
    Cria um novo usuário no sistema.
    """
    usuario = Usuario(
        username=username,
        password=password,
        email=email.strip().lower() if email else None,
        first_name=first_name,
        last_name=last_name,
    )
    usuario.save()
    return usuario
