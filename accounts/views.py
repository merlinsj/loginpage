from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import redirect
import random, string

from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["POST"])
def signup(request):
    data = request.data
    print("Received data:", data)  # Debugging

    valid_codes = {'student': 'student123', 'teacher': 'teacher123'}
    
    role = data.get("role")
    security_code = data.get("security_code")
    
    if role not in valid_codes or security_code != valid_codes[role]:
        print("Invalid security code")  # Debugging
        return Response({"error": "Invalid security code"}, status=400)
    
    try:
        user = User.objects.create_user(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password")
        )
        user.role = role
        user.security_code = security_code
        user.save()
        print("User created successfully!")  # Debugging
        return Response({"message": "Signup successful! Redirecting to login..."}, status=201)
    except Exception as e:
        print("Signup error:", str(e))  # Debugging
        return Response({"error": "Signup failed. Please check your details."}, status=400)


@api_view(["POST"])
def login_view(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        role = "admin" if user.is_superuser else "user"
        return Response({"token": token.key, "role": role})
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")
    user = User.objects.filter(email=email).first()
    if user:
        new_password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        user.set_password(new_password)
        user.save()
        send_mail("Password Reset", f"Your new password is {new_password}", "admin@tracker.com", [email])
    return Response({"message": "If your email is registered, you’ll receive a reset link."})
