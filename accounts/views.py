from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# In views.py, instead of importing Profile at the top, import it inside the function that needs it
def some_view(request):
    from .models import Profile
    # Now you can use Profile here without circular import

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CustomUser, Profile
from decouple import config

# Security codes for students and teachers (now from environment variables)
STUDENT_SECURITY_CODE = config('STUDENT_SECURITY_CODE', default="student123")
TEACHER_SECURITY_CODE = config('TEACHER_SECURITY_CODE', default="teacher123")

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')
            security_code = data.get('securityCode')

            # Validate required fields
            if not all([username, email, password, role]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already taken'}, status=400)

            # Validate security code for students and teachers
            if role == 'student' and security_code != STUDENT_SECURITY_CODE:
                return JsonResponse({'error': 'Invalid student security code'}, status=400)
            elif role == 'teacher' and security_code != TEACHER_SECURITY_CODE:
                return JsonResponse({'error': 'Invalid teacher security code'}, status=400)

            # Create custom user
            user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role)
            user.save()

            # Create profile for the user if needed (for student/teacher)
            if role in ['student', 'teacher']:
                Profile.objects.create(user=user, role=role)

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=400)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not all([username, password]):
                return JsonResponse({'error': 'Missing username or password'}, status=400)

            user = authenticate(username=username, password=password)
            if user:
                # Check if admin user is a superuser
                if user.role == 'admin' and not user.is_superuser:
                    return JsonResponse({'error': 'Only superusers can login as admin'}, status=403)

                login(request, user)
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=400)
