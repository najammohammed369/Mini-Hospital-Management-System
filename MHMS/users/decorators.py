from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def doctor_required(view):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role != "doctor":
            return redirect("home")
        return view(request, *args, **kwargs)
    return wrapper
