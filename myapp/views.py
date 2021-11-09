
import pytz
from django.db.models.fields import EmailField
from django.http import request, response
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from myapp import models
from myapp.models import LmsUser

# Create your views here.

#出版社展示列表
def publisher_list(request):
    publisher = models.Publisher.objects.all()
    return render(request,'pub_list.html',{'pub_list' : publisher})

#添加出版社
def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        new_publisher_addr = request.POST.get('addr')
        models.Publisher.objects.create(name=new_publisher_name,addr=new_publisher_addr)
        return redirect('/pub_list/')
    return render(request,'pub_add.html')

#编辑出版社
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('edit_name')
        new_addr = request.POST.get('edit_addr')
        edit_obj.name = new_name
        edit_obj.addr = new_addr
        edit_obj.save()
        return redirect('/pub_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get (id=edit_id)
    return render(request,'pub_edit.html',{'publisher':edit_obj})

#删除出版社
def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    data = {'ret':True,'msg':'删除成功!'} 
    return redirect('/pub_list/')


#作者列表
def author_list(request):
    author = models.Author.objects.all()
    return render(request,'auth_list.html',{'auth_list':author})

#增加作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('name')
        new_author_sex = request.POST.get('sex')
        new_author_age = request.POST.get('age')
        new_author_tel = request.POST.get('tel')
        models.Author.objects.create(name=new_author_name,sex=new_author_sex,age=new_author_age,tel=new_author_tel)
        return redirect('/auth_list/')
    return render(request,'auth_add.html')

#修改作者
def edit_author(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Author.objects.get(id=edit_id)
        new_author_name = request.POST.get('edit_name')
        new_author_sex = request.POST.get('edit_sex')
        new_author_age = request.POST.get('edit_age')
        new_author_tel = request.POST.get('edit_tel')
        #new_book_id = request.POST.get('book_id')
        edit_obj.name = new_author_name
        edit_obj.sex = new_author_sex
        edit_obj.age = new_author_age
        edit_obj.tel = new_author_tel
        #edit_obj.book.set(new_book_id)
        edit_obj.save()
        return redirect('/auth_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Author.objects.get(id=edit_id)
    all_book = models.Book.objects.all()
    return render(request,'auth_edit.html',{
        'author':edit_obj,
        'book_list':all_book})
#删除作者
def drop_author(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Author.objects.get(id=drop_id)
    drop_obj.delete() 
    return redirect('/auth_list/')


#书籍列表
def book_list(request):
    book = models.Book.objects.all()
    return render(request,'book_list.html',{'book_list':book})

#添加书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_book_ISBN = request.POST.get('ISBN')
        new_book_translator = request.POST.get('translator')
        new_book_date = request.POST.get('date')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(name=new_book_name,publisher_id=publisher_id,ISBN=new_book_ISBN,translator=new_book_translator,date=new_book_date)
        return redirect('/book_list/')
    res = models.Publisher.objects.all()
    return render(request,'book_add.html',{'publisher_list':res})

#编辑书籍
def edit_book(request):
    if request.method =='POST':
        new_book_name = request.POST.get('name')
        new_book_ISBN = request.POST.get('ISBN')
        new_book_translator = request.POST.get('translator')
        new_book_date = request.POST.get('date')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id =request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.ISBN = new_book_ISBN
        edit_obj.translator = new_book_translator
        edit_obj.date = new_book_date
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect('/book_list/')
    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    all_publisher = models.Publisher.objects.all()
    return render(request,'book_edit.html',{'book':edit_obj,'publisher_list':all_publisher})

#删除书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')

#密码加密
def setPassword(password):
    """
    加密密码 算法单次md5
    ：parampassword:传入的密码
    ：return:加密后的密码
    """
    import hashlib
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)

#用户注册
def register(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        mobile = data.get('mobile')
        LmsUser.objects.create(
            username=username,
            email=email,
            password=setPassword(password),
            #password=password,
            mobile=mobile,
        )
        return HttpResponseRedirect('/login/')
    return render(request,'register.html')

#用户登录
def login(request):
    if request.method == 'POST' and request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        e = LmsUser.objects.filter(email= email).first()
        if e :
            now_password = setPassword(password)
            db_password = e.password 
            if now_password == db_password:
                #return render(request,'pub_list.html)
                response = HttpResponseRedirect('/pub_list/')
                response.set_cookie('username',e.username)
                return response
    return render(request,'login.html')
