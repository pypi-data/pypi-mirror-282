


''''
	from verses.frontiers.trends.monetary.DB_verses_trends.connect import connect_to_verses_inventory
	[ driver, verses_inventory_DB ] = connect_to_verses_inventory ()
	collection_treasures = DB_verses_trends ["collection_treasures"]
	driver.close ()
"'''



#/
#
from verses.frontiers.trends.monetary.moves.URL.retrieve import retreive_monetary_URL
from verses._essence import retrieve_essence
#
#
import pymongo
#
#\

def connect_to_verses_inventory ():
	essence = retrieve_essence ()
	
	ingredients_DB_name = essence ["trends"] ["monetary"] ["databases"] ["DB_verses_trends"] ["alias"]
	monetary_URL = retreive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]