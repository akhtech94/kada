from django.db import models

class Shops(models.Model):
    name            = models.CharField(max_length=100, blank=False, null=False)
    landmark        = models.CharField(max_length=50, blank=True, null=True)
    streetAddress   = models.CharField(max_length=255, blank=False, null=False)
    district        = models.CharField(max_length=50, blank=False, null=False)
    State           = models.CharField(max_length=50, blank=False, null=False)
    country         = models.CharField(max_length=50, blank=False, null=False)
    pincode         = models.IntegerField(blank=False, null=False)
    phoneNumber1    = models.CharField(max_length=20, blank=False, null=False)
    phoneNumber2    = models.CharField(max_length=20, blank=True, null=True)
    dateJoined      = models.DateTimeField(auto_now_add=True)
    category        = models.CharField(max_length=25, blank=True, null=True)
    gst             = models.CharField(max_length=30, blank=True, null=True)
    licenseno       = models.CharField(max_length=30, blank=True, null=True)
    is_active       = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name
