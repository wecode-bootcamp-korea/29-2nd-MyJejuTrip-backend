import json
import re

from json.decoder           import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.conf            import settings
from django.core.exceptions import ValidationError

import jwt
import bcrypt

from users.models           import User
from my_settings            import SECRET_KEY, ALGORITHMS
from .validate              import validate_email, validate_password



class SignUpView(View):
  def post(self,request):
    data = json.loads(request.body)
    try:
      name            = data['name']
      email           = data['email']
      password        = data['password']
      has_agreed      = data['has_agreed']
      hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

      validate_email(email)
      validate_password(password)

      if User.objects.filter(email= email):
        return JsonResponse({'message': 'EMAIL_ALREADY_EXISTS'}, status=400)
      
      user = User(
        name       = name,
        email      = email,
        password   = hashed_password,
        has_agreed = has_agreed,
      )

      user.save()
    
      return JsonResponse({'message':'success'}, status=200)

    except KeyError:
      return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    except ValidationError:
      return JsonResponse({'message': 'INVALID_KEY'}, status=400)