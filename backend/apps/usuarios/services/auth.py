# login, troca de senha, etc.

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


def authenticate_user(username, password):
    """
    Authenticate a user with username and password.
    """
    user = authenticate(username=username, password=password)
    if user is not None:
        return user
    return None


def get_tokens_for_user(user):
    """
    Generate JWT tokens for a user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def change_password(user, old_password, new_password):
    """
    Change the password for a user.
    """
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return True
    return False
