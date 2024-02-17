from django.urls import path
from apps.users.views import SignUpView, UpdateUserView, UserDetailView, UpdateAvatarView, DeleteAvatarView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('update-avatar/', UpdateAvatarView.as_view(), name='update_avatar'),
    path('delete-avatar/<int:pk>/', DeleteAvatarView.as_view(), name='delete_avatar'),
]
