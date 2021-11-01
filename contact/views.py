from django.shortcuts import render


def contact(request):
    """View to return our contact page"""

    return render(request, 'contact/contact.html')


def sample_kit(request):
    """View to return our sample request page"""

    return render(request, 'contact/sample.html')


def quotation(request):
    """View to return our quotation page"""

    return render(request, 'contact/quotation.html')