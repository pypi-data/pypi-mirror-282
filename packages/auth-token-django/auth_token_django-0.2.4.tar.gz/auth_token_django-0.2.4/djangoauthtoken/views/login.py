from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings

from djangoauthtoken.models import TokenUser, Token
from djangoauthtoken.utils import get_or_create_csrf_token


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def login(request):
    """
    Login view
    It expects username and password.
    #TODO: Flag to switch to Email.
    """
    data = request.data
    password = data['password']
    try:
        if settings.USERNAME_LOGIN_METHOD:
            _user = data['username']
            _auth = auth.authenticate(username=_user, password=password)
        else:
            _user = data['email']
            _auth = auth.authenticate(username=_user, password=password)
        if _auth:
            user = TokenUser.objects.get(username=_user) if settings.USERNAME_LOGIN_METHOD else TokenUser.objects.get(
                email=_user)
            user_token = Token(user=user)
            user_token.save()
            _csrf = get_or_create_csrf_token(request)

            return Response({
                "id": user.id,
                "user": user.username if settings.USERNAME_LOGIN_METHOD else user.email,
                "token": user_token.token,
                "refresh_token": user_token.refresh_token,
                "expires_at": user_token.expiry_time
            },
                status=status.HTTP_200_OK,
                headers={
                    'X-CSRFToken': _csrf
                })
        else:
            # Create your own Exception layer.
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
