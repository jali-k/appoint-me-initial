from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PhoneNumberForm
from django.core.cache import cache
from .models import User


# Create your views here.
def phone_number_input_view(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            # Save the phone number or send SMS verification
            phone_number = form.cleaned_data["phone_number"]
            # Logic to send SMS via Twilio or another service
            return redirect("verify_code")
    else:
        form = PhoneNumberForm()
    return render(request, "authentication/phone_input.html", {"form": form})


@csrf_exempt
def send_verification_code(request):
    if request.method == "POST":
        data = json.loads(request.body)
        phone_number = data.get("phone_number")

        # Generate a random 6-digit verification code
        verification_code = random.randint(100000, 999999)

        # Save the verification code in cache with phone_number as the key
        cache.set(
            phone_number, verification_code, timeout=300
        )  # Code expires in 5 minutes

        # Send the code via SMS (using Twilio or any other service)
        send_sms(phone_number, verification_code)

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


def send_sms(phone_number, code):
    # Example of sending SMS via Twilio
    # from twilio.rest import Client
    # client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # client.messages.create(to=phone_number, from_="+1234567890", body=f"Your code is {code}")
    print(f"Sending SMS to {phone_number}: Your code is {code}")


@csrf_exempt
def verify_code(request):
    if request.method == "POST":
        data = json.loads(request.body)
        phone_number = data.get("phone_number")
        code_entered = data.get("verification_code")

        # Retrieve the code from cache
        code_stored = cache.get(phone_number)

        if code_stored and str(code_stored) == str(code_entered):
            # Successful verification
            # Log in the user or create a session here
            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "message": "Invalid code"})

    return JsonResponse({"success": False})
