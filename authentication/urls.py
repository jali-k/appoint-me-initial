from django.urls import path
from .views import phone_login_view, send_verification_code, verify_code

urlpatterns = [
    path("login/", phone_login_view, name="phone_login"),
    path(
        "send-verification-code/", send_verification_code, name="send_verification_code"
    ),
    path("verify-code/", verify_code, name="verify_code"),
]
