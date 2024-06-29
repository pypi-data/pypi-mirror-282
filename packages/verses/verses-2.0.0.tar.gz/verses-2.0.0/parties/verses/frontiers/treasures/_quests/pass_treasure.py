




''''
	verses treasures send --name "treasure.1" --version 1.0.0
"'''

''''
	objective:
		stow_treasure ({
			"domain": "treasure.1",
			"version": "1.0.0"
		})
	
		the procedure:
			[ ] search the treasures
"'''

''''
	DB: verses_trends_DB
		collection: treasures_collection
"'''


#/
#
from verses.frontiers.treasures._quests.itemize import itemize_treasures
from verses.frontiers.treasures.check.domain_fiber import check_domain_fiber
#
#
from verses._essence import retrieve_essence
#
#\

def pass_treasure (packet):
	essence = retrieve_essence ()

	domain = packet ["domain"]
	#name = treasure ["name"] 
	#version = treasure ["version"] 
	
	treasures = itemize_treasures ()
	print (treasures)
	
	check_domain_fiber ({
		"domain_fiber": domain
	})
	
	return;