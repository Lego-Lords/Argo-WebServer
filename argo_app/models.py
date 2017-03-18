from django.db import models

class Steps(models.Model):
        currentStep = models.IntegerField()
        maxSteps = models.IntegerField()
        modelName = models.CharField(max_length=45, unique=True)

        def __unicode__(self):
                return self.modelName