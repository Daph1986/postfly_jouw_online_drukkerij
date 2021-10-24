from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
	""" Displays the user's profile """
	profile = get_object_or_404(UserProfile, user=request.user)

	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your profile is updated successfully')

	form = UserProfileForm(instance=profile)

	template = 'profiles/profile.html'
	context = {
		'form': form,
	}

	return render(request, template, context)


def dashboard(request):
    """View to return files specifications page"""

    return render(request, 'profiles/dashboard.html')

