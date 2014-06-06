from django.db import models
from django.db import connection
from fields import SequenceField
from django.db import connection

class SequenceManager(models.Manager):
    def get_db_where_ors(self, s):
        """Builds "where" statement to be used when searching between adjacent records
        """
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
        select s1.id, s1.seq || s2.seq as combined_seq, s1.position
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
    position = models.IntegerField(null=True)

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



class ChromosomeSequenceManager(models.Manager):
    def get_queryset(self):
        return super(ChromosomeSequenceManager, self).get_queryset().defer('sequence')

    def find_all_positions(self, chromosome, seq, limit=100):
        """ Returns an array with the positions of the occurrences of a substring in a chromosome
        """
        cursor = connection.cursor()
        search_length = 200000
        sql = """
            select strpos(substr(sequence, %s, %s), %s)
            from hg19_chromosomesequence
            where id = %s
            ;
        """
        chromosome_length = chromosome.get_length()
        positions = []
        pos = self.find_position(chromosome, seq)
        if pos is None or pos < 1:
            return positions
        pos += 1
        start_search = pos + 1
        positions.append(pos)
        while start_search < chromosome_length:
            cursor.execute(sql, (start_search, search_length, seq, chromosome.id))
            for row in cursor.fetchall():
                if row[0] > 0:
                    pos = start_search + row[0]
                    start_search += row[0]
                    positions.append(pos-1)
                # not found
                else:
                    start_search += search_length - len(seq)
        return positions

    def find_position(self, chromosome, seq):
        """ Returns the position of the first occurrence of a substring in a chromosome
        """
        cursor = connection.cursor()
        sql = """
            select strpos(sequence, %s)
            from hg19_chromosomesequence
            where id = %s
            ;
        """
        cursor.execute(sql, (seq, chromosome.id))
        for row in cursor.fetchall():
            return row[0] - 1
        return None

    def get_substring(self, chromosome, begin, length):
        cursor = connection.cursor()
        sql = """
            select substr(sequence, %s, %s)
            from hg19_chromosomesequence
            where id = %s
            ;
        """
        cursor.execute(sql, (begin, length, chromosome.id))
        for row in cursor.fetchall():
            return row[0]
        return None

    def get_length(self, chromosome):
        cursor = connection.cursor()
        sql = """
            select char_length(sequence)
            from hg19_chromosomesequence
            where id = %s
            ;
        """
        cursor.execute(sql, (chromosome.id,))
        for row in cursor.fetchall():
            return row[0]
        return None

# avoid south migration problem
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^hg19\.fields\.SequenceField"])
class ChromosomeSequence(models.Model):
    """
    One registry per chromosome in postBIS format
    """
    name = models.TextField()
    sequence = SequenceField()

    objects = ChromosomeSequenceManager()

    def get_substring(self, begin, length):
        return ChromosomeSequence.objects.get_substring(self, begin, length)

    def get_length(self):
        return ChromosomeSequence.objects.get_length(self)