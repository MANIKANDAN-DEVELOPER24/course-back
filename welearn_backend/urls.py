# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


# from core import views
# from core.views import (
#     CourseListCreateView,
#     CourseUpdateView,
#     CourseDeleteView,
# )
# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # JWT auth
#     path('api/login/', TokenObtainPairView.as_view(), name='login'),  # Alias for React login
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Registration & current user
#     path('api/register/', views.RegisterView.as_view(), name='register'),
#     path('api/current-user/', views.current_user, name='current_user'),

#     # Users
#     path('api/users/', views.UserListView.as_view(), name='user_list'),
#     path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

#     # Courses
#     path('api/courses/', views.CourseListCreateView.as_view(), name='course_list_create'),
#     path('api/all-courses/', views.CourseListView.as_view(), name='all_courses'),

#     # Offers
#     path('api/offers/', views.OfferListCreateView.as_view(), name='offer_list'),
#     path('api/offers/<int:pk>/', views.OfferRetrieveUpdateDeleteView.as_view(), name='offer_detail'),

#     # Purchases / Checkout
#     path('api/purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
#     path('api/checkout/', views.checkout, name='checkout'),

#     path("courses/", CourseListCreateView.as_view(), name="course-list-create"),
#     path("courses/<int:pk>/update/", CourseUpdateView.as_view(), name="course-update"),
#     path("courses/<int:pk>/delete/", CourseDeleteView.as_view(), name="course-delete"),
# ]

# # ✅ Always serve media in local AND production (for Render)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views
from core.views import (
    CourseListCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration & current user
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/current-user/', views.current_user, name='current_user'),

    # Users
    path('api/users/', views.UserListView.as_view(), name='user_list'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    # Courses
    path('api/courses/', views.CourseListCreateView.as_view(), name='course_list_create'),
    path('api/courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('api/courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('api/all-courses/', views.CourseListView.as_view(), name='all_courses'),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),


    # Offers
    path('api/offers/', views.OfferListCreateView.as_view(), name='offer_list'),
    path('api/offers/<int:pk>/', views.OfferRetrieveUpdateDeleteView.as_view(), name='offer_detail'),

    # Purchases / Checkout
    path('api/purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('api/checkout/', views.checkout, name='checkout'),
]

# ✅ Always serve media in local AND production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# from core import views
# from core.views import (
#     CourseListCreateView,
#     CourseUpdateView,
#     CourseDeleteView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # JWT auth
#     path('api/login/', TokenObtainPairView.as_view(), name='login'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Registration & current user
#     path('api/register/', views.RegisterView.as_view(), name='register'),
#     path('api/current-user/', views.current_user, name='current_user'),

#     # Users
#     path('api/users/', views.UserListView.as_view(), name='user_list'),
#     path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

#     # Courses
#     path('api/courses/', views.CourseListCreateView.as_view(), name='course_list_create'),
#     path('api/courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
#     path('api/courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
#     path('api/all-courses/', views.CourseListView.as_view(), name='all_courses'),
#     path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),

#     # Offers
#     path('api/offers/', views.OfferListCreateView.as_view(), name='offer_list'),
#     path('api/offers/<int:pk>/', views.OfferRetrieveUpdateDeleteView.as_view(), name='offer_detail'),

#     # Purchases / Checkout
#     path('api/purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
#     path('api/checkout/preview/', views.checkout_preview, name='checkout_preview'),
#     path('api/checkout/confirm/', views.checkout_confirm, name='checkout_confirm'),
# ]

# # ✅ Always serve media in local AND production
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
