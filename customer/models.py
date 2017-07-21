from django.db import models

class customer_info(models.Model):
    GEND_CHOICES = (
        ("Male", ("Male")),
        ("Female", ("Female"))
    )

    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    add_city = models.CharField(max_length=50)
    add_dist = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GEND_CHOICES)

    def __str__(self):
        return '%s %s' % (self.fName, self.lName)


