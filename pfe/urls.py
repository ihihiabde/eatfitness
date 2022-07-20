"""pfe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import index,arms,back,calories,chest,contact_us,courses,legs,programs,shoulders,arms_tricepsb,arms_tricepsa,arms_bicepsa,arms_bicepsb,meal,plan1,plan2,plan3,plan4,program1,program2,program3,chest1,chest2,back1,back2,legs1,legs2,legs3,shoulders1,shoulders2,shoulders3
urlpatterns = [ 
    path('',index,name='home'),

    path('meal',meal,name='meal'),
        path('plan1',plan1,name='plan1'),
        path('plan2',plan2,name='plan2'),
        path('plan3',plan3,name='plan3'),
        path('plan4',plan4,name='plan4'),
    path('arms',arms,name='arms'),
        path('arms_bicepsa',arms_bicepsa,name='arms_bicepsa'),
        path('arms_bicepsb',arms_bicepsb,name='arms_bicepsb'),
        path('arms_tricepsa',arms_tricepsa,name='arms_tricepsa'),
        path('arms_tricepsb',arms_tricepsb,name='arms_tricepsb'),
    path('back',back,name='back'),
        path('back1',back1,name='back1'),
        path('back2',back2,name='back2'),
    path('calories',calories,name='calories'),
    path('chest',chest,name='chest'),
        path('chest1',chest1,name='chest1'),
        path('chest2',chest2,name='chest2'),
    path('contact_us',contact_us,name='contact_us'),
    path('courses',courses,name='courses'),
    path('legs',legs,name='legs'),
        path('legs1',legs1,name='legs1'),
        path('legs2',legs2,name='legs2'),
        path('legs3',legs3,name='legs3'),
    path('programs',programs,name='programs'),
        path('program1',program1,name='program1'),
        path('program2',program2,name='program2'),
        path('program3',program3,name='program3'),
    path('shoulders',shoulders,name='shoulders'),
        path('shoulders1',shoulders1,name='shoulders1'),
        path('shoulders2',shoulders2,name='shoulders2'),
        path('shoulders3',shoulders3,name='shoulders3'),
   
]
