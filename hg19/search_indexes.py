from haystack import indexes
from models import Sequence1, SequenceM

# TOO SLOW TO CREATE
#class Sequence1Index(indexes.SearchIndex, indexes.Indexable):
#    #text = indexes.CharField(document=True, model_attr='seq')
#    text = indexes.NgramField(document=True, model_attr='seq')
#    
#    def get_model(self):
#        return Sequence1
#
#    def index_queryset(self, using=None):
#        return self.get_model().objects.all()

class SequenceMIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, model_attr='seq')
    
    def get_model(self):
        return SequenceM

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
