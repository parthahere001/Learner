


from email.policy import default
from multiprocessing import context
from re import X, template
from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect, HttpResponse
#from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import CreateUserForm, Createcourse, UFF
from django.template import loader
from django.shortcuts import redirect
from learner.forms import CreateUserForm
from .models import Course, Csource, Student, Teacher

# def index(request):
# 	return render(request, 'mainapp/index.html')


def add(request):
  myteachers = Teacher.objects.all()
  context = {
    'myteachers': myteachers,
  }
  template = loader.get_template('addcourse.html')
  return render(request, 'addcourse.html', context)


def addcourse(request):
  new_user=request.user 
  new_user= User.objects.get(id=new_user.id)
  nteacher = Teacher.objects.get(tid=new_user.id)
  x = request.POST['ctitle']
  y = request.POST['cdescription']
  
  a = request.POST['cenrollkey']
  
  c = request.POST.get('cfek',default=-1)
  if (c!=-1):
   ncourse = Course(title=x,description=y,teacher=nteacher,enrollkey=a,fek=a)
   ncourse.save()
  else:
    ncourse = Course(title=x,description=y,teacher=nteacher,enrollkey=a)
    ncourse.save()
  return HttpResponseRedirect(reverse('homet'))  

def delete(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  return HttpResponseRedirect(reverse('indext'))



  


def index(request):
  new_user=request.user 
  new_user= User.objects.get(id=new_user.id)
  new_s = Student.objects.get(sid=new_user.id)
  course = Course.objects.all().exclude(student = new_s)
  
#   template = loader.get_template('mainapp/index.html')
  context = {
    'course': course,
  }
  return render(request, 'index5.html', context)


def eindex(request):
  new_user=request.user 
  new_user= User.objects.get(id=new_user.id)
  new_s = Student.objects.get(sid=new_user.id)
  course = Course.objects.filter(student = new_s)
#   template = loader.get_template('mainapp/index.html')
  context = {
    'course': course,
  }
  return render(request, 'index4.html', context)




def indext(request):
  new_user=request.user 
  new_user= User.objects.get(id=new_user.id)
  new_t = Teacher.objects.get(tid=new_user)
  course = Course.objects.filter(teacher = new_t)
#   template = loader.get_template('mainapp/index.html')
  context = {
    'course': course,
  }
  return render(request, 'indext.html', context)



def resources(request, id):
  mycourse = Course.objects.get(id=id)
  mycresource = Csource.objects.filter(fid=id)
  template = loader.get_template('resources.html')
  context = {
    'mycourse' : mycourse, 
    'mycresource' : mycresource
  }
  return HttpResponse(template.render(context, request))

def rhome(request):
   return render(request, 'registerh.html')

def homes(request):
   return render(request, 'homes.html')
def homet(request):
   return render(request, 'homet.html')
def homepage(request):
   return render(request, 'newindex.html')

 

def succen(request):
  return render(request, 'succen.html')

def unsuccen(request):
  return render(request, 'unsuccen.html')

def enroll(request, id):
  mycourse = Course.objects.get(id=id)
  template = loader.get_template('enroll.html')
  context = {
    'mycourse' : mycourse, 
  }
  return HttpResponse(template.render(context, request))




def senroll(request, id):
  ekey = request.POST['userkey']
  course = Course.objects.get(id=id)
  if (ekey == course.enrollkey):
    new_user=request.user 
    new_user= User.objects.get(id=new_user.id)
    student= Student.objects.get(sid=new_user.id)
    student.edc.add(course)
    return redirect ("succen")
  else:
    return redirect ("unsuccen")







# def enrollkey(request, id):
#   x = request.POST['userkey']
#   course = Course.objects.get(id=id)
#   context = {
#     'course' : course, 
#   }
#   if x == course.enrollkey:
#     current_user = request.user
#     student= Student.objects.get(id=current_user.id)

#     student.enrolledcourses = course
#     return redirect ("succen")
#   else:
#     return redirect ("unsuccen")


def registers(request):
  form = CreateUserForm()


  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      messages.info(request, "Thanks for registering. You are now logged in.")
      new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
      login(request, new_user)
      

      new_user = User.objects.get(id=new_user.id)
         
      member = Student(sid=new_user)
      member.save()
      return render(request, 'homes.html')
     
  context = {'form':form}
  
  return render(request, 'registers.html',context)



def registert(request):
  form = CreateUserForm()


  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      messages.info(request, "Thanks for registering. You are now logged in.")
      new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
      login(request, new_user)
      

      new_user = User.objects.get(id=new_user.id)
      memberr = Student(sid=new_user,isteacher = 'y')
      memberr.save()
         
      member = Teacher(tid=new_user,name=new_user.username)
      member.save()
      return render(request, 'homet.html')
     
  context = {'form':form}
  
  return render(request, 'registert.html',context)





def userlogin(request):
  if request.method=="POST":
        # Get the post parameters
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']

      user=authenticate(username= loginusername, password= loginpassword)
      if user is not None:
          login(request, user)
          messages.success(request, "Successfully Logged In")
          new_user = request.user
          new_user = User.objects.get(id=new_user.id)
          ns = Student.objects.get(sid=new_user)
          if (ns.isteacher == 'y' ):
           return redirect("homet")
          else:
            return redirect("homes")
      else:
          messages.error(request, "Invalid credentials! Please try again")
          return redirect("userlogin")
  return render (request,'log.html')

  # return HttpResponse("404- Not found")
# def senroll(request):
#   course=Course.objects.get(id=id)
#   key=request.POST.get('userkey')
#   user=request.user
#   if (key==course.enrollkey):
#     user.Student.enrolledcourses.add(course)
#     return redirect('home')
	
	
def userlogout(request):
    logout(request)
    return redirect('userlogin')



def updatec(request, id):
  mycourse = Course.objects.get(id=id)
  template = loader.get_template('updatec.html')
  context = {
    'mycourse': mycourse,
  }
  return HttpResponse(template.render(context, request))
  
def updatecdata(request, id):
  ct = request.POST['ct']
  cd = request.POST['cd']
  ce = request.POST['ce']
  cf = request.POST['cf']
  course = Course.objects.get(id=id)
  course.title = ct
  course.description = cd
  course.enrollkey = ce
  course.fek = cf

  course.save()
  return HttpResponseRedirect(reverse('indext'))


def rfile(request, id):
  mycourse = Course.objects.get(id=id)
  template = loader.get_template('rfileupload.html')
  context = {
    'mycourse': mycourse,
  }
  return HttpResponse(template.render(context, request))
  


def rfileupload(request,id):
  form = UFF()
  c = Course.objects.get(id = id)
  if request.method == 'POST':
    form = UFF(request.POST, request.FILES)
    for f in request.FILES.getlist('file'):
      cs = Csource.objects.create(fid = c, file =  f, fname = str(f))
      cs.save()
      return render(request, 'homet.html')
  else:
    form = UFF()
  
  context = {
    'form':form,
    'id' : id
  }
  return render (request, 'rfileupload.html', context)


def cresource(request, id):
  mycresource = Csource.objects.filter(fid=id)
  course = Course.objects.get(id=id)
  template = loader.get_template('cresource.html')
  context = {
    'mycresource': mycresource,
    'course' : course
  }
  return HttpResponse(template.render(context, request))


def deletef(request, id):
  csourse = Csource.objects.get(id=id)
  csourse.delete()
  return HttpResponseRedirect(reverse('indext'))