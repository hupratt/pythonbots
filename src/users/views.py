from django.shortcuts import render
# from django.contrib.auth.views import logout
# from django.urls import reverse_lazy
# from django.views import generic
from .forms import SubForm, ProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
# from django.conf import settings
from .models import CustomUser
# from django.core.files.base import ContentFile
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    
def login_signup_page(request):
    """
    Login/signup method
    
    """
    # cur_user = request.user.username
    # if len(cur_user) == 0:
    #     print("Anonymous")
    # if len(cur_user) != 0:
    #     User = get_user_model()
    #     user, created = User.objects.get_or_create(username=cur_user)
    #     print('connected user', user.username)

    signupform = SubForm(request.POST or None, request.FILES or None) # write to database form, can't be used for logi
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    if signupform.is_valid() and request.method == 'POST':
        print("signupform is valid")
        print("signupform", request.POST['username'], request.POST['password'])

        # signupform.save(commit=False)
        User = get_user_model()
        user, created = User.objects.get_or_create(username=signupform.cleaned_data.get("username"), 
            email=signupform.cleaned_data.get("email"), first_name=signupform.cleaned_data.get("first_name"),
            last_name=signupform.cleaned_data.get("last_name"), profile_pic=request.FILES['profile_pic'])
        user.set_password(signupform.cleaned_data.get("password"))
        user.save()
        messages.success(request,"Thank you for subscribing")
        return redirect('../login')

    elif signupform.errors:
        messages.error(request,"There was an error handling your request")
    else:
        signupform = SubForm()
    context = { 
        "user_form":signupform,
        # "uname":cur_user,
        # "email":user.email,
        # "first_name":user.first_name,
        # "last_name":user.last_name,
        # "profile_pic":user.profile.profile_pic,
    }
    return render(request, "login_signup_page.html", context) #queryset

def profile(request):
    if request.user.is_authenticated is False:
        raise Http404
    pform = ProfileForm(request.POST or None, request.FILES or None)
    if pform.is_valid() and request.method == 'POST':
        # pform.save(commit=False)
        profile, created = CustomUser.objects.get_or_create(id=request.user.id)
        if 'profile_pic' in request.FILES.keys():
            profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            messages.success(request,"Picture saved")
        else:
            profile.first_name=pform.cleaned_data.get("first_name")
            profile.last_name=pform.cleaned_data.get("last_name")
            profile.email=pform.cleaned_data.get("email")
            # profile.password=pform.cleaned_data.get("password")
            # profile.username=pform.cleaned_data.get("username")
            profile.save()

            messages.success(request,"Profile info successfully changed")
    else:
        pform = ProfileForm()
    context = { 
        "profile_form":pform,
        "user":request.user,
        # "email":request.user.email,
        # "first_name":request.user.first_name,
        # "last_name":request.user.last_name,
        # "profile_pic":request.user.profile_pic,
    }
    return render(request, "profile.html", context) #queryset

# def handle_uploaded_file(f):
#     with open(os.path.join(settings.MEDIA_ROOT,"h.png"), 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

