import requests
import json
import csv
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from decouple import config

def send_email(reciever_email, message):
    sender_email = "rebelbean@seznam.cz"
    receiver_email = [reciever_email] #recipients
    password = "passwordtest"
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Preklad'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP_SSL('smtp.seznam.cz', 465) #choose your provider server
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    return "Email sent!"

response = requests.get("https://www.imdb.com/chart/top/")
# print(response.text)

regiojet_lokace_z_api = requests.get("https://brn-ybus-pubapi.sa.cz/restapi/consts/locations")
regiojet_lokace = regiojet_lokace_z_api.json()
# for country in regiojet_lokace:
#     print(country["country"])


# deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
# deepl_url = "https://api-free.deepl.com/v2/translate"
#
# text = "Ahoj, jmenuji se Miro"
# parametry = {
#     "auth_key":deepl_api_key,
#     "text": text,
#     "target_lang": "EN"
# }

# preklad = requests.get(url=deepl_url, params=parametry).json()
# print(preklad)
# print(preklad["translations"][0]["text"])

def translate(text, target_lang, source_lang=None):
    deepl_url = "https://api-free.deepl.com/v2/translate"
    parametry = {
        "auth_key": "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx",
        "text": text,
        "target_lang": target_lang
    }
    if source_lang:
        parametry.update({"source_lang": source_lang})
    preklad = requests.get(url=deepl_url, params=parametry).json()
    return preklad["translations"][0]["text"]


def translator():
    text = input("Zadaj text na prelozenie: ")
    tar_language = input("Do jakeho jazyka to chcete prelozit: ")
    preklad = translate(text, tar_language)
    na_mail = input("chcete poslat preklad na mail? yes/no: ")
    if na_mail == "yes":
        poslat_na_mail = input("zadejte email: ")
        send_email(poslat_na_mail, preklad)
    return preklad

# print(translator())


filmy_list = []
r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.text, "html.parser")
filmy = soup.find_all("td", class_="titleColumn")

for film in filmy:
    name = film.find("a").text
    year = film.find("span").text
    year_int = int(year.strip("()"))
    reziser_a_herci = [film.find("a").get("title").split(",")[0].strip(" (dir.)")]+[film.find("a").get("title").split(",")[1:]]
    print(reziser_a_herci)
    jmeno_rok = [name, year_int]
    filmy_list.append(jmeno_rok)
    sorted_filmy = sorted(filmy_list, reverse=True, key=lambda x: x[1])

# for film in sorted_filmy:
#     print(film)

headers = ["jmeno_filmu", "rok", "reziser", "herci"]
