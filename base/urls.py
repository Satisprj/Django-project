from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('reigster/',views.registerPage,name="register"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update_room/<str:pk>/',views.updateRoom,name="update_room"),
    path('delete_room/<str:pk>/',views.deleteRoom,name="delete_room"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    

]