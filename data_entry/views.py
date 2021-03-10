import csv
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Account
from .forms import PostForm
from .models import Post, Darbar


@login_required
def home_view(request):
    value = Post.objects.count()
    value_male = Post.objects.filter(Gender='Male').count()
    value_female = Post.objects.filter(Gender='Female').count()
    context = {'value': value, 'value_male': value_male, 'value_female': value_female}
    return render(request, "main/home.html", context)


@login_required(login_url='login:index')
def portal_view(request):
    users = Account.objects.filter(id=request.user.id).values('city')
    city = ''
    for user in users:
        city = str(user['city'])
    context = {'darbars': list(Darbar.objects.filter(darbar_city=city).values('darbar_name'))}
    return render(request, 'data_entry/dataentry.html', context)


@login_required(login_url='login:index')
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
        post.city = request.user.city
        post.save()
        #for full_Name, father_Name, mother_Name in Post.objects.values_list('full_Name','father_Name', 'mother_Name', flat=False).distinct():
        #    Post.objects.filter(
        #        pk__in=Post.objects.filter(full_Name=full_Name, father_Name=father_Name, mother_Name=mother_Name).values_list('id', flat=False)[1:]).delete()
        return redirect("data_entry:main")
    else:
        return render(request, 'data_entry/dataentry.html')


@login_required(login_url='login:index')
def camera_view(request):
    return render(request, "data_entry/winner.html")



@login_required(login_url='login:index')
def view_entry(request):
    users = Account.objects.filter(id=request.user.id).values('city')
    city = ''
    for user in users:
        city = str(user['city'])
    post_list = Post.objects.filter(city=city)
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'posts': post_list
    }
    return render(request, 'view_entry/view.html', context)


@login_required(login_url='login:index')
def delete_entry(request, id):
    post = get_object_or_404(Post, id=id)
    post.flag = 0
    post.save()
    return redirect('data_entry:view')


@login_required(login_url='login:index')
def logout_request(request):
    logout(request)
    return redirect("index")


@login_required(login_url='login:index')
def update_entry(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post.save()
        return redirect('data_entry:view')
    context = {
        'form': form
    }
    return render(request, 'view_entry/update.html', context)


@login_required(login_url='login:index')
def export_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['full_Name', 'spouse_Name', 'father_Name', 'mother_Name', 'Occupation', 'Gender', 'blood_Group',
                     'birth_date', 'phone', 'Darbar', 'Address', 'Pincode'])

    users = Post.objects.all().values_list('full_Name', 'spouse_Name', 'father_Name', 'mother_Name', 'Occupation',
                                           'Gender', 'blood_Group',
                                           'birth_date', 'phone', 'Darbar', 'Address', 'Pincode')
    for user in users:
        writer.writerow(user)

    return response
