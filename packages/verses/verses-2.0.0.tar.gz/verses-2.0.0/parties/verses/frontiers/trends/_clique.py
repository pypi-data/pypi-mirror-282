





#/
#
from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures.document.insert import insert_document
from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures.document.search import search_treasures
from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures.document.count import count_treasures
#
#
import click
#
#
import ast
from pprint import pprint
#
#\

def trends_clique ():
	@click.group ("trends")
	def group ():
		pass
	
	''''
		verses trends insert-document --domain "wallet.1" --names "[ 'name_1', 'name_2' ]"
		verses_1 trends insert-document --domain "wallet.1" --names "[ 'name_1', 'name_2' ]"		
	"'''
	@group.command ("insert-document")
	@click.option ('--domain', required = True)
	@click.option ('--names', default = '[]')
	def command_insert_document (domain, names):
		insert_document ({
			"document": {
				"domain": domain,
				"names": ast.literal_eval (names)
			}
		})
	
	@group.command ("search")
	@click.option ('--domain', required = True)
	def command_search (domain):
		treasures = search_treasures ({
			"filter": {
				"domain": domain
			}
		})
		for treasure in treasures:
			pprint (treasure, indent = 4)
			
	@group.command ("count")
	def command_search ():
		count = count_treasures ()
		print ("count:", count)
		
	@group.command ("itemize")
	def on ():
		print ("on")
		

	return group




#



