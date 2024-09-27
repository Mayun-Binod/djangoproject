from django.urls import path
from .views import *

urlpatterns = [
    path("home/", emp_home, name='emp_home'),
    path("add-emp/", add_emp, name='add_emp'),
    path("delete-emp/<int:emp_id>/", delete_emp, name='delete_emp'),
    path("update-emp/<int:emp_id>/", update_emp, name='update_emp'),
    path("do-update-emp/<int:emp_id>/", do_update_emp, name='do_update_emp'),
]
