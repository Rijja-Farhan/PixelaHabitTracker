import requests
from datetime import *
TOKEN = "12345abc"
USERNAME ="name"
GRAPH_ID = 'graph1'
pixela_endpoint="https://pixe.la/v1/users"
pixela_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# response = requests.post(url=pixela_endpoint,json=pixela_params)
# print(response.text)

#user account creation
#new user account is created, now commenting it because this step is not required again
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id" : "graph1",
    "name" :"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"

}
headers={
    "X-USER-TOKEN": TOKEN
}
#graph creation
#commenting this out because the graph is created
# response = requests.post(url=graph_endpoint,json=graph_config,headers =headers)
# print(response.text)

#http post request. posting a pixel
today = datetime.today()
entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
entry_param={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how much cycling have you done today?")
}
response = requests.post(url=entry_endpoint,json=entry_param,headers=headers)
print(response.text)

# #updating a pixel
# today = datetime(year=2023,month=8,day=17)
# update_endpoint = f" {pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# update_data = {
#
#
#     "quantity":"10.23"
#
# }
# response = requests.put(url=update_endpoint,json=update_data,headers=headers)
# print(response.text)
