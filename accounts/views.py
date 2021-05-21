from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format= None):
        data                = self.request.data
        name                = data['name']
        email               = data['email']
        password1           = data['password1']
        password2           = data['password2']
        is_shop             = data['is_shop']
        is_delivery_person  = data['is_delivery_person']
        is_customer         = data['is_customer']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return Response( {'error': 'Email ID already exists.'} )
            else:
                if len(password1) < 8:
                    return Response( {'error': 'Password should be at least 8 characters'} )
                else:
                    user = User.objects.create_user(email=email, name=name, password=password1, is_shop=is_shop, is_delivery_person=is_delivery_person, is_customer=is_customer)
                    user.save()
                    return Response( {'success': 'User created successfully.'} )
        else:
            return Response( {'error': 'Passwords do not match'} )
