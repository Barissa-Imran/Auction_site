from django.conf.urls import include,  url
from core.views import index, about, contact

urlpatterns = [
    url(r"^", include("users.urls")),
    url(r"", index, name='index'),
    url(r"^about/", about, name="about"),
    url(r"^contact/", contact, name="contact")
]
