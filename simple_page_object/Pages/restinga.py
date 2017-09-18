from pybot.core.pageObject import PageObject
from pybot.core.pageElement import PageElement, PageElements


class restingaPage(PageObject):

    textPesq = PageElements(id_='palavras')
    buttomPesq = PageElement(css='.ok')
    linksPesq = PageElement(link_text='Superior')

    def preencherPesquisa(self, texto):
        self.textPesq = texto

    def clicarPesquisa(self):
        self.buttomPesq.click()

    def clicarLink(self):
        self.linksPesq.click()
