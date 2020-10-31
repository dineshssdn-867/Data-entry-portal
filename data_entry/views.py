from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from twilio.rest import Client


@login_required
def home_view(request):
    value = Post.objects.count()
    value_male = Post.objects.filter(Gender='Male').count()
    value_female = Post.objects.filter(Gender='Female').count()
    context={'value':value,'value_male':value_male,'value_female':value_female}
    return render(request, "main/home.html",context)


@login_required(login_url='index')
def portal_view(request):
    return render(request, 'data_entry/dataentry.html')


@login_required(login_url='index')
def entry_view(request):
    if request.method == 'POST':
        post = Post()
        post.full_Name = request.POST['full_Name']
        if request.POST['spouse_Name']:
            post.spouse_Name = request.POST['spouse_Name']
        else:
            post.spouse_Name = ""
        post.father_Name = request.POST['father_Name']
        post.mother_Name = request.POST['mother_Name']
        post.Occupation = request.POST['Occupation']
        post.Gender = request.POST['Gender']
        post.blood_Group = request.POST['blood_Group']
        post.birth_date = request.POST['birth_date']
        post.phone = request.POST['phone']
        post.Darbar = request.POST['Darbar']
        post.Address = request.POST['Address']
        post.Pincode = request.POST['Pincode']
        post.image = request.FILES['myfile']
        post.user = request.user
        number=str(post.phone)
        value=str('Full_Name: '+post.full_Name+'\n Spouse_Name: '+post.spouse_Name+'\n Occupation: '+post.Occupation+'\n Gender: '+post.Gender+'\n Blood_Group: '+post.blood_Group+'\n Phone_Number: '+str(number)+'\n Darbar: '+post.Darbar+'\n Address: '+post.Address+'\n Pincode: '+post.Pincode)
        client =  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=value,
            from_='+13134374671',
            to=number
        )
        post.save()
        for full_Name in Post.objects.values_list('full_Name', flat=True).distinct():
            Post.objects.filter(pk__in=Post.objects.filter(full_Name=full_Name).values_list('id', flat=True)[1:]).delete()
        return redirect("main")
    else:
        return render(request, 'data_entry/dataentry.html')


@login_required(login_url='index')
def camera_view(request):
    return render(request, "data_entry/winner.html")


@login_required(login_url='index')
def view_entry(request):
    post_list=Post.objects.all().order_by("-id")
    query=request.GET.get('q')

    if query:
        post_list=post_list.filter(Q(full_Name__icontains=query))

    paginator=Paginator(post_list,3)
    page=request.GET.get('page')
    post_list=paginator.get_page(page)
    context={
        'posts':post_list
    }
    return render(request,'view_entry/view.html',context)

@login_required(login_url='index')
def delete_entry(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('view')

@login_required(login_url='index')
def logout_request(request):
    logout(request)
    return redirect("index")



@login_required(login_url='index')
def update_entry(request,id):
    post=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        post.save()
        return redirect('view')
    context={
        'form':form
    }
    return render(request,'view_entry/update.html',context)


