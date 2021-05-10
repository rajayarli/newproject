from django.urls import path
from myapp import views
from  django.contrib.auth import views as v

urlpatterns=[

	path('home/',views.first),
	path('',views.cllg,name="home"),
	path('about',views.about,name="about"),
	path('contact',views.contact,name="contact"),
	path('register',views.register,name="register"),
	path('login/',v.LoginView.as_view
		(template_name='myapp/login.html'),name='login'),
	path('logout/',v.LogoutView.as_view
		(template_name='myapp/logout.html'),name='logout'),
	path('dashboard/',views.dashboard,name="dashboard"),
	path('mailsend/',views.mailsend,name="mailsend"),
	path('profile/',views.profile,name="profile"),
	path('update/',views.update,name="update"),
]