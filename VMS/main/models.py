from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=5, choices=[("IN", "IN"), ("OUT", "OUT")], null=True, blank=True)
    img = models.ImageField(upload_to='vistor_imgs/', null=True, blank=True)

    def __str__(self):
        return self.name
