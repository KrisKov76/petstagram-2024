from django.shortcuts import render


# Login view
def login(request):
    return render(request, 'accounts/login-page.html')


# Register view
def register(request):
    return render(request, 'accounts/register-page.html')


# Profile details view
def profile_details(request, pk: int):
    return render(request, 'accounts/profile-details-page.html')


# Profile edit view
def profile_edit(request, pk: int):
    return render(request, 'accounts/profile-edit-page.html')


# Profile delete view
def profile_delete(request, pk: int):
    return render(request, 'accounts/profile-delete-page.html')
