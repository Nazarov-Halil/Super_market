from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import get_user_model, logout
from apps.users.forms import UserFrom, UserUpdateForm, AvatarForm
from django.urls import reverse_lazy

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = UserFrom
    success_url = reverse_lazy('login')
    template_name = 'User/update-profile.html'


class UpdateUserView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('product_list')
    template_name = 'User/update-profile.html'

    # def get_context_data(self, **kwargs):
    #     return f"{}"


def logout_logics(request):
    logout(request)
    return redirect('product_list')


class UserDetailView(DetailView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('detail')
    template_name = 'User/detail.html'


class UpdateAvatarView(UpdateView):
    model = User
    form_class = AvatarForm
    template_name = 'User/detail.html'
    success_url = reverse_lazy('detail')

    def get_object(self, **kwargs):
        return self.request.user


class DeleteAvatarView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        user.avatar = None
        user.save()
        return redirect('update', user.id)
