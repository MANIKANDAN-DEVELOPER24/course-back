
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from .models import User, Course, Offer, Purchase
from .serializers import (
    UserSerializer, RegisterSerializer,
    CourseSerializer, OfferSerializer, PurchaseSerializer
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  permissions
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
# -------- AUTH --------
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Public


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])  # Public
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "username": user.username,
            "role": "admin" if user.is_superuser else "user",
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Private
def current_user(request):
    user = request.user
    data = UserSerializer(user).data
    data.update({
        "role": "admin" if user.is_superuser else "user",
        "is_superuser": user.is_superuser,
        "is_staff": user.is_staff
    })
    return Response(data)


# -------- USERS --------
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Private

    def get_queryset(self):
        return User.objects.filter(is_superuser=False, is_staff=False)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Private


# -------- COURSES --------
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]  # Public


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]   # 👈 anyone can access

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

# -------- OFFERS --------
class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [AllowAny]  # Public


class OfferRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [AllowAny]  # Public


# -------- PURCHASES --------
class PurchaseListView(generics.ListAPIView):
    queryset = Purchase.objects.all().order_by('-purchased_at')
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]  # Private


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Private
def checkout(request):
    course_ids = request.data.get('course_ids', [])
    if not course_ids:
        return Response({'error': 'No courses provided'}, status=status.HTTP_400_BAD_REQUEST)

    for course_id in course_ids:
        try:
            course = Course.objects.get(id=course_id)
            Purchase.objects.create(user=request.user, course=course)
        except Course.DoesNotExist:
            return Response({'error': f'Course {course_id} not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': 'Purchase successful'}, status=status.HTTP_200_OK)





# Only admins can edit/delete
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

# List + Create
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [permissions.AllowAny()]


# Update
class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete
class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


from rest_framework.generics import RetrieveAPIView
from core.models import Course
from core.serializers import CourseSerializer

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_serializer_context(self):
         context = super().get_serializer_context()
         context.update({"request": self.request})
         return context
