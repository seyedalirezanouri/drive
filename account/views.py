from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import RegistrationSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView

@extend_schema(
    tags=['User'],
    request=RegistrationSerializer,
    responses={
        201: OpenApiResponse(),
        400: OpenApiResponse(),
    }
)
class UserRegisterationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    authentication_classes = ()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):    
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response(status=status.HTTP_201_CREATED)
        
@extend_schema(
    tags=['User'],
    responses={
        201: OpenApiResponse(),
        400: OpenApiResponse(),
    }
)
class UserLoginView(TokenObtainPairView):
    pass