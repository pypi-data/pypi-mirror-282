
#/
#
from ._quests.itemize import itemize_treasures
from ._quests.pass_treasure import pass_treasure
#
#
import click
#
#\

def treasures_clique ():
	@click.group ("treasures")
	def group ():
		pass
		
		
	@group.command ("itemize")
	def command_itemize ():		
		itemize_treasures ({
			"print_to_shell": "yes"
		})
		
		
		
	@group.command ("pass", help = """
		
		This is for passing a treasure to the trends.
		
	""")
	@click.option ('--domain', required = True)
	def command_pass_treasure (domain):		
		pass_treasure ({
			"domain": domain
		})

	return group




#



