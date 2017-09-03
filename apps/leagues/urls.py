from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index_new, name="index_new"),
	url(r"^index_old$", views.index_old, name="index_old"),
	url(r"^index_new$", views.index_new, name="index_new"),

	url(r"^make_data/", views.make_data, name="make_data"),
]
