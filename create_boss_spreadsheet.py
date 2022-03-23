import pandas as pd
import datetime
import requests

# Get date
today = datetime.datetime.now()
date_time = today.strftime("%d%m%Y-%H%M%S")

# Files
xls_file = "elden-ring-bosses-" + str(date_time) + ".xlsx"

# List to use in DataFrame
rows = []

# Total 168 bosses, considering Fextralife page
page1 = "https://eldenring.fanapis.com/api/bosses?limit=50&page=1"
page2 = "https://eldenring.fanapis.com/api/bosses?limit=50&page=2"
page3 = "https://eldenring.fanapis.com/api/bosses?limit=50&page=3"
page4 = "https://eldenring.fanapis.com/api/bosses?limit=50&page=4"

def get_list(page):
    resp = requests.get(page)
    d = resp.json()
    return d.get('data')

l1 = get_list(page1)
l2 = get_list(page2)
l3 = get_list(page3)
l4 = get_list(page4)
l = [*l1, *l2, *l3, *l4]


for boss in l:
    # print("Boss: " + boss["name"] + " -- " + "Location: " + boss["location"])
    rows.append([boss["name"], boss["location"], "no"])

df1 = pd.DataFrame(rows, columns=["BOSS", "LOCATION", "KILLED"])
df1.to_excel(xls_file)