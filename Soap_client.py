from suds.client import Client
url = "http://DESKTOP-FNJE4AO:8088/mockApiPortSoap11?wsdl"
client = Client(url)
register_call = client.service.registerCall("Kuba")
results = client.service.results("Kuba")
print(register_call,results,sep="\n")


