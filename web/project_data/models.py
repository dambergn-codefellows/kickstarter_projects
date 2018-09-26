from django.db import models


class Project(models.Model):
    """
    """
    ID = models.IntegerField()
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.FloatField()
    launched = models.CharField(max_length=1024)
    pledged = models.FloatField()
    state = models.CharField(max_length=1024)
    backers = models.IntegerField()
    country = models.CharField(max_length=1024)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()
    

    def __str__(self):
        return '{}'.format(self.name)
