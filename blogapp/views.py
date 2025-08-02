from django.shortcuts import render,redirect

from django.views.generic import View

from blogapp.forms import RegistrationForm,SignInForm,BlogForm

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from blogapp.models import Blog



# Create your views here.




class SignUpView(View):

    template_name="register.html"

    form_class = RegistrationForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            messages.success(request,"your account has been created")

            return redirect("signin")
        
        else:

            messages.error(request," sorry.....field to created your account")

            return render(request,self.template_name,{"form":form_instance})
        
class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            validated_data=form_instance.cleaned_data

            uname=validated_data.get("username")

            pword=validated_data.get("password")

            user_object= authenticate(request,username=uname,password=pword)

            if user_object:

                login(request,user_object)

                messages.success(request,"success")

                return redirect("blog-list")
            
        messages.error(request,"invalid credentials")

        return render(request,self.template_name,{"form":form_instance})

class BlogListView(View):

    template_name="blog-list.html"

    def get(self,request,*args,**kwargs):

        qs=Blog.objects.all()

        return request(request,self.template_name,{"data":qs})

class BlogCreateView(View):

     template_name="blog-add.html"

     form_class=BlogForm

     def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
     def post(self,request,*args,**kwargs):

        form_data = request.POST

        media_files=request.FILES

        form_instance=self.form_class(form_data,files=media_files)

        if form_instance.is_valid():

            validated_data=form_instance.cleaned_data

            Blog.objects.create(**validated_data,owner=request.user)

            form_instance.save()

            messages.success(request,"blog has been added")

            return redirect("blog-list")
        
        else:
            
         messages.error(request,"filed to add blog")

        return render(request,self.form_class,{"form":form_instance})



