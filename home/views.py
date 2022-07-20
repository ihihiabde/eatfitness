from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):

    return render(request,'index.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def meal(request):

    return render(request,'./html/meal_plannig.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#---------------------------------------------------------- 
#-------------------------- meal ---------------------

def plan1(request):

    return render(request,'./html/meal/plan1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def plan2(request):

    return render(request,'./html/meal/plan2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def plan3(request):

    return render(request,'./html/meal/plan3.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def plan4(request):

    return render(request,'./html/meal/plan4.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#----------------------------------------------------------          
#-------------------------- end meal ----------------------

def arms(request):

    return render(request,'./html/ARMS.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#---------------------------------------------------------- 
#-------------------------- arms ---------------------

def arms_bicepsa(request):

    return render(request,'./html/arms/arms_bicepsA.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def arms_bicepsb(request):

    return render(request,'./html/arms/arms_bicepsB.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def arms_tricepsa(request):

    return render(request,'./html/arms/arms_tricepsA.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def arms_tricepsb(request):

    return render(request,'./html/arms/arms_tricepsB.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#----------------------------------------------------------          
#-------------------------- end arms ----------------------

def back(request):

    return render(request,'./html/BACK.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#---------------------------------------------------------- 
#-------------------------- back ---------------------

def back1(request):

    return render(request,'./html/BACK/back1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def back2(request):

    return render(request,'./html/BACK/back2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send


#----------------------------------------------------------          
#-------------------------- back ----------------------

def chest(request):

    return render(request,'./html/CHEST.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send
          # 
#---------------------------------------------------------- 
#-------------------------- chest ---------------------

def chest1(request):

    return render(request,'./html/CHEST/chest1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def chest2(request):

    return render(request,'./html/CHEST/chest2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send


#----------------------------------------------------------          
#-------------------------- END chest ----------------------

def courses(request):

    return render(request,'./html/COURSES.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def legs(request):

    return render(request,'./html/LEGS.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send
          
#----------------------------------------------------------          
#-------------------------- end legs ----------------------
def legs1(request):

    return render(request,'./html/legs/legs1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def legs2(request):

    return render(request,'./html/legs/legs2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def legs3(request):

    return render(request,'./html/legs/legs3.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#----------------------------------------------------------          
#-------------------------- end legs ----------------------

def shoulders(request):

    return render(request,'./html/SHOULDERS.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send    

#---------------------------------------------------------- 
#-------------------------- shoulders ---------------------

def shoulders1(request):

    return render(request,'./html/shoulders/shoulders1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def shoulders2(request):

    return render(request,'./html/shoulders/shoulders2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def shoulders3(request):

    return render(request,'./html/shoulders/shoulders3.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#----------------------------------------------------------          
#-------------------------- end arms ----------------------

def calories(request):

    return render(request,'./html/CALORIES.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def programs(request):

    return render(request,'./html/PROGRAMS.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#---------------------------------------------------------- 
#-------------------------- arms ---------------------

def program1(request):

    return render(request,'./html/program/program1.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def program2(request):

    return render(request,'./html/program/program2.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

def program3(request):

    return render(request,'./html/program/program3.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

#----------------------------------------------------------          
#-------------------------- end arms ----------------------

def contact_us(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message,email,
                  ["eat.fitness04@gmail.com"])
        
        return render(request, './html/CONTACT US.html', {'email': email})

                

    return render(request,'./html/CONTACT US.html',{})
          #       resquet,pagename,{send data with page}
          # {} mean we dont have data to send

