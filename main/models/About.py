from django.db import models


class About(models.Model):

    content = models.TextField(default="Cette page n'est pas encore remplie.")

    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date =  models.DateTimeField(auto_now=True)

    def ___str__(self):
        return self.update_date
