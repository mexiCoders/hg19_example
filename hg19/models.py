from django.db import models

class Sequence(models.Model):
    seq = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{seq}".format(seq=self.seq)

    class Meta:
        abstract = True


class Sequence1(Sequence):
    pass


class Sequence2(Sequence):
    pass


class Sequence3(Sequence):
    pass


class Sequence4(Sequence):
    pass


class Sequence5(Sequence):
    pass


class Sequence6(Sequence):
    pass


class Sequence7(Sequence):
    pass


class Sequence8(Sequence):
    pass


class Sequence9(Sequence):
    pass


class Sequence10(Sequence):
    pass


class Sequence11(Sequence):
    pass


class Sequence12(Sequence):
    pass


class Sequence13(Sequence):
    pass


class Sequence14(Sequence):
    pass


class Sequence15(Sequence):
    pass


class Sequence16(Sequence):
    pass


class Sequence17(Sequence):
    pass


class Sequence18(Sequence):
    pass


class Sequence19(Sequence):
    pass


class Sequence20(Sequence):
    pass


class Sequence21(Sequence):
    pass


class Sequence22(Sequence):
    pass


class SequenceX(Sequence):
    pass


class SequenceY(Sequence):
    pass
