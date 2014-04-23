from django.db import models
from django.db import connection

class SequenceManager(models.Manager):
    def get_db_where_ors(self, s):
        ors = []
        for i in range(1,len(s)):
            pre = '%' + s[:i].replace("'", "''")
            pos = s[i:].replace("'", "''") + '%'
            ors.append("(s1.seq like '{pre}' and s2.seq like '{pos}')".format(pre=pre, pos=pos))
        return ors

    def search_between(self, S, seq):
        """Search between adjacent records.
        param S is the Sequence class
        """

        seq = seq.replace("'", "''")
        query = """
        select s1.id, s1.seq || s2.seq as combined_seq 
        from {table_name} s1
            inner join {table_name} s2 on (s1.id + 1) = s2.id
        where s1.seq like {seq} 
        """.replace('{table_name}', S._meta.db_table).replace('{seq}', "'%"+seq+"%'")

        ors = self.get_db_where_ors(seq)
        str_ors = '\nor '.join(ors)
        query += "\nor " + str_ors

        cursor = connection.cursor()
        cursor.execute(query)
        rows = []
        for row in cursor.fetchall():
            rows.append(row)
        return rows

class Sequence(models.Model):
    seq = models.TextField()

    objects = SequenceManager()

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

class SequenceM(Sequence):
    "Mitocondrial"
    pass
