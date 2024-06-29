




'''
	from verses.frontiers.trends.monetary.DB_verses_trends.collection_treasures.document.count import count_treasures
	count_treasures ()
'''



#/
#
from verses._essence import retrieve_essence
from verses.frontiers.trends.monetary.DB_verses_trends.connect import connect_to_verses_inventory
#
#
import ships.modules.exceptions.parse as parse_exception
#
#
import pymongo
#
#
import time
#
#\



def count_treasures ():
	try:
		[ driver, DB_verses_trends ] = connect_to_verses_inventory ()
		collection_treasures = DB_verses_trends ["collection_treasures"]
	except Exception as E:
		print ("food collection connect:", E)
		
	count = "unknown"
	try:	
		essence = retrieve_essence ()
		
		print ("filter:", filter)
		
		count = collection_treasures.count_documents ({})
		
	except Exception as E:
		print (parse_exception.now (E))
	
		raise Exception (E)
		pass;
		
	try:
		driver.close ()
	except Exception as E:
		print (parse_exception.now (E))
		print ("food collection disconnect exception:", E)	
		
		
	return count;








