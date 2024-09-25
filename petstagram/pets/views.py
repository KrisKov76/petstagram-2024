from django.shortcuts import render


# Pet add view
def pet_add_page(request):
    return render(request, 'pets/pet-add-page.html')


# Pet delete view
def pet_delete_page(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-delete-page.html')


# Pet details view
def pet_details_page(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-details-page.html')


# Pet edit view
def pet_edit_page(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-edit-page.html')
