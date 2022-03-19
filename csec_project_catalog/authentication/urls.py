
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    # Registartion
     path('register/',views.registeration, name='register'),

    # Profile Page / Dashboard
     path('profile/',views.profile, name='profile'),

    # path('', include('django.contrib.auth.urls')),

    # Login / Log Out
     path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        next_page='profile'
        ),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(
          next_page='login'
        ),
        name='logout'
    ),

    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change_password.html',
            success_url='/auth/change-password/done'
        ),
        name='change-password'
    ),

    path(
        'change-password/done',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change_password_done.html',
        ),
        name='change-password-done'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password-reset/password_reset_form.html',
             subject_template_name='registration/password-reset/password_reset_subject.txt',
             email_template_name='registration/password-reset/password_reset_email.html',
             success_url='/auth/password-reset/done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]