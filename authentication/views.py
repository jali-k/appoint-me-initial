from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.auth import login
from .models import User
import random, json


def phone_login_view(request):
    """Render the phone number input form."""
    return render(request, "authentication/login.html")


def send_verification_code(request):
    """Send a verification code to the provided phone number."""
    if request.method == "POST":
        data = json.loads(request.body)
        phone_number = data.get("phone_number")

        # Generate a random verification code
        verification_code = random.randint(100000, 999999)

        # Store the verification code in cache for 5 minutes
        cache.set(phone_number, verification_code, timeout=300)

        # Here you would integrate Twilio or other service to send the SMS
        print(f"Sending code {verification_code} to {phone_number}")

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


def verify_code(request):
    """Verify the entered code and log in the user."""
    if request.method == "POST":
        data = json.loads(request.body)
        phone_number = data.get("phone_number")
        entered_code = data.get("verification_code")

        # Retrieve the stored verification code
        stored_code = cache.get(phone_number)

        if stored_code and str(stored_code) == str(entered_code):
            # Code matches, log in the user
            try:
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                # If the user does not exist, create one
                user = User.objects.create_user(phone_number=phone_number)

            # Log the user in
            login(request, user)
            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "message": "Invalid code"})

    return JsonResponse({"success": False})
