

''''
	from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures._indexes import prepare_collection_treasures_indexes
	prepare_collection_treasures_indexes ()
"'''

#/
#
from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures.document.insert import insert_document
from verses.frontiers.trends.monetary.DB_verses_trends.connect import connect_to_verses_inventory
#
#\

def prepare_collection_treasures_indexes ():
	print ("prepare_collection_treasures_indexes")

	[ driver, DB_verses_trends ] = connect_to_verses_inventory ()
	collection_treasures = DB_verses_trends ["collection_treasures"]
	
	collection_treasures.create_index([('domain', 1)], unique=True)
	
	driver.close ()