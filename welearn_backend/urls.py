
# # welearn_backend/urls.py
# from django.contrib import admin
# from django.urls import path
# from core import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # auth
#     path('api/register/', views.RegisterView.as_view()),
#     path('api/login/', views.login_view),
#     path('api/current-user/', views.current_user),

#     # users
#     path('api/users/', views.UserListView.as_view()),
#     path('api/users/<int:pk>/', views.UserDetailView.as_view()),

#     # courses
#     path('api/courses/', views.CourseListCreateView.as_view()),
#     path('api/all-courses/', views.CourseListView.as_view()),

#   # Offers endpoints
#     path('api/offers/', views.OfferListCreateView.as_view(), name='offer-list'),
#     path('api/offers/<int:pk>/', views.OfferRetrieveUpdateDeleteView.as_view(), name='offer-detail'),


#  # Purchases / Checkout
#     path('api/purchases/', views.PurchaseListView.as_view()),
#     path('api/checkout/', views.checkout, name='checkout'),
#      path('login/', views.login_view),
#     path('checkout/', views.checkout),

# ]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth
    path('api/login/', TokenObtainPairView.as_view(), name='login'),  # Alias for React login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Standard JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token

    # Registration & current user
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/current-user/', views.current_user, name='current_user'),

    # Users
    path('api/users/', views.UserListView.as_view(), name='user_list'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    # Courses
    path('api/courses/', views.CourseListCreateView.as_view(), name='course_list_create'),
    path('api/all-courses/', views.CourseListView.as_view(), name='all_courses'),

    # Offers
    path('api/offers/', views.OfferListCreateView.as_view(), name='offer_list'),
    path('api/offers/<int:pk>/', views.OfferRetrieveUpdateDeleteView.as_view(), name='offer_detail'),

    # Purchases / Checkout
    path('api/purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('api/checkout/', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
