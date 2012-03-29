from haystack import indexes
from issues.models import Issue

class IssueIndex(indexes.SearchIndex, indexes.Indexable):
	description = indexes.TextField(document=True, use_template=True)
	
	def get_model(self):
		return Issue
		
	def index_query(self):
		return self.get_model().all()
