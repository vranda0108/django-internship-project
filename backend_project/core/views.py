from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "Hello, this is a public endpoint!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}. This is a protected endpoint!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret_view(request):
    return Response({'message': f'Hello, {request.user.username}! This is a protected view.'})

class RegisterUserView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if email:
            send_welcome_email.delay(email)  # trigger background task
            return Response({"message": "User registered and email will be sent!"})
        return Response({"error": "Email is required."}, status=400)
    
@api_view(['POST'])
def trigger_email(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)
    
    send_welcome_email.delay(email)
    return Response({'message': f'Email sending scheduled for {email}'})

