from .models import MenuItem, ContactInformation

#custom context processor to pass menu items to base.html
def list_menu(request):
    menu_items = MenuItem.objects.all()
    phone = ContactInformation.objects.all()[0].phone
    fax = ContactInformation.objects.all()[0].fax
    email = ContactInformation.objects.all()[0].email
    address = ContactInformation.objects.all()[0].address
    print(phone)
    return {'menu_items': menu_items,
            'phone': phone,
            'fax': fax,
            'email': email,
            'address': address,}
