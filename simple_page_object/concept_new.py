from pybot.core.manager import Manager
from Pages.restinga import restingaPage


manager = Manager()

manager.go('http://www.restinga.ifrs.edu.br/site/')

page = restingaPage(manager)

page.preencherPesquisa('tcc')
page.clicarPesquisa()
page.clicarLink()
