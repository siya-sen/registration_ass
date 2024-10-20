from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Registration
from .forms import RegistrationForm

# Create (Insert) operation
def create_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registration created successfully'}, status=201)
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

# Read (Retrieve) operation
def get_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    data = {
        'ID': registration.id,
        'Name': registration.Name,
        'Email': registration.Email,
        'DateOfBirth': registration.DateOfBirth,
        'PhoneNumber': registration.PhoneNumber,
        'Gender': registration.Gender,
        'RegistrationDate': registration.RegistrationDate,
        'Status': registration.Status
    }
    return JsonResponse(data, status=200)

# Update operation
def update_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registration updated successfully'}, status=200)
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'registration_form.html', {'form': form})

# Delete operation
def delete_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    registration.delete()
    return JsonResponse({'message': 'Registration deleted successfully'}, status=200)

