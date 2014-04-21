from django.db import models

class Sequence(models.Model):
    seq = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{seq}".format(seq=self.seq)

    class Meta:
        abstract = True

class Sequence1(Sequence):
    pass
