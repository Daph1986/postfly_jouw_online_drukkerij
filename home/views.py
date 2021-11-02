from django.shortcuts import render

# Create your views here.

def index(request):
    """View to return index page"""

    return render(request, 'home/index.html')


def specs(request):
    """View to return files specifications page"""

    return render(request, 'home/specs.html')


def bleed(request):
    """View to return files bleed page"""

    return render(request, 'home/bleed.html')


def file_type(request):
    """View to return files file type page"""

    return render(request, 'home/file.html')


def deep_black(request):
    """View to return files deep black page"""

    return render(request, 'home/black.html')


def ink_coverage(request):
    """View to return files ink coverage page"""

    return render(request, 'home/ink.html')


def job_options(request):
    """View to return files job options page"""

    return render(request, 'home/joboptions.html')


def color(request):
    """View to return files color page"""

    return render(request, 'home/color.html')


def outlines(request):
    """View to return files outlines page"""

    return render(request, 'home/outlines.html')


def foil(request):
    """View to return files cold foil page"""

    return render(request, 'home/foil.html')


def overprint(request):
    """View to return files overprint page"""

    return render(request, 'home/overprint.html')


def resolution(request):
    """View to return files resolution page"""

    return render(request, 'home/resolution.html')


def templates(request):
    """View to return files templates page"""

    return render(request, 'home/templates.html')


def faq(request):
    """View to return FAQ page"""

    return render(request, 'home/faq.html')

def team(request):
    """View to return team page"""

    return render(request, 'home/team.html')


def printing_house(request):
    """View to return printing house page"""

    return render(request, 'home/printing.html')


def our_concept(request):
    """View to return our concept page"""

    return render(request, 'home/concept.html')