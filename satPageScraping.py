
from lxml import html as lhtml
import requests

rootPage = 'http://www.sat.gob.mx/'

complementosPage = requests.get(rootPage + 'informacion_fiscal/factura_electronica/Paginas/complementos_factura_cfdi.aspx')
complementosPageTree = lhtml.fromstring(complementosPage.content)
complementosList = complementosPageTree.xpath('//*[@id="ctl00_PlaceHolderMain_Content__ControlWrapper_RichHtmlField"]/ul//a')

for complemento in complementosList:
	complementoName = complemento.xpath('text()')
	complementoLink = complemento.xpath('@href')
	complementoPage = requests.get(rootPage + complementoLink[0])
	complementoPageTree = lhtml.fromstring(complementoPage.content)
	complementoRecursosList = complementoPageTree.xpath('//*/a[contains(@href, ".xsd") or contains(@href, ".xslt")]/@href')
	print complementoName , ' --> ', complementoLink, ' ---> ', complementoRecursosList

