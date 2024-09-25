from django.shortcuts import render


# Photo add view
def photo_add_page(request):
    return render(request, 'photos/photo-add-page.html')


# Photo details view
def photo_details_page(request, pk:int):
    return render(request, 'photos/photo-details-page.html')


# Photo edit view
def photo_edit_page(request, pk:int):
    return render(request, 'photos/photo-edit-page.html')
