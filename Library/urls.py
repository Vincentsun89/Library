"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.publisher_list),
    #出版社列表
    url(r'^pub_list/',views.publisher_list),
    #新增出版社
    url(r'^pub_add/',views.add_publisher),
    #编辑出版社
    url(r'^pub_edit/',views.edit_publisher),
    #删除出版社
    url(r'^pub_drop/',views.drop_publisher),

    #作者列表
    url(r'^auth_list/',views.author_list),
    #新增作者
    url(r'^auth_add/',views.add_author),
    #编辑作者
    url(r'^auth_edit/',views.edit_author),
    #删除作者
    url(r'^auth_drop/',views.drop_author),

    #图书展示
    url(r'^book_list/',views.book_list),
    #新增图书
    url(r'^book_add/',views.add_book),
    #编辑图书
    url(r'^book_edit/',views.edit_book),
    #删除图书
    url(r'^book_drop/',views.drop_book),

    #用户注册
    url(r'^signup',views.register),
    url(r'^register/',views.register),
    #用户登录
    url(r'^login/',views.login),

]
