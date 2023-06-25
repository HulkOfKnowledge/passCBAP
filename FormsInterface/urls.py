from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('sign-in',views.sign_in, name='sign-in'),
    path('',views.sign_in, name='sign-in'),
    path('sign-up',views.sign_up, name='sign-up'),
    path("sign-out", views.sign_out, name="sign-out"),

    # Password Reset URLs
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='FormsInterface/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='FormsInterface/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='FormsInterface/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='FormsInterface/password_reset_complete.html'), name='password_reset_complete'),
    
]