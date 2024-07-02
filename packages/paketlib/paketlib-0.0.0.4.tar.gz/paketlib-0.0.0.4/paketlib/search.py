import requests
from bs4 import BeautifulSoup

class Telegram:
    def PrivateUrl(url: str):
        pass

def SearchLeak(Term, token):
    try:
        datar = {"token": token, "request": Term, "limit": 100, "lang": "ru"}
        url = 'https://server.leakosint.com/'
        response = requests.post(url, json=datar)
        data =  response.json()
        for source, items in data["List"].items():
            if source == "No results found":
                pass
            else:
                print("\n[data]")
                for item in items["Data"]:
                    for key, value in item.items():
                        print(f"├ {key}: {value}")
                print(f"╰ Data base: {source}")
    except:pass

def ipLookup(ip_address):
    api_url = f'http://ipinfo.io/{ip_address}/json'

    try:
        response = requests.get(api_url)
        data = response.json()

        return data
    except:
        return {}
    
def dbsearch(db, value):
    try:
        with open(db, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    if value in line:
                        print("\n[data]")
                        fdata = line.replace(",",";").replace("|",";").replace('"',"").replace('NULL',"").replace(":",";").strip().split(";")
                        sdata = f.readline(1).replace(",",";").replace("|",";").replace('"',"").replace('NULL',"").replace(":",";").strip().split(";")

                        for i in range(len(fdata)):
                            if len(fdata[i]) < 80 and fdata[i]:
                                betadata = f"├ {sdata[i].replace('_', ' ')}: {fdata[i]}"
                                print(f"{betadata}")
                        print("╰ Data base: "+db)
                except:print("╰ Data base: "+db)
    except BaseException as e: print('[ + ] Error: '+e)