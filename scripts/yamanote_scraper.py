import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://simple.wikipedia.org/wiki/Yamanote_Line"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="wikitable")
if not table:
    print("❌ No table found with class 'wikitable'")
    exit()

rows = []
for tr in table.find_all("tr"):
    cells = tr.find_all(["td", "th"])
    row = [cell.get_text(strip=True) for cell in cells]
    if row:
        rows.append(row)

data_rows = rows[1:]
filtered_rows = [row for row in data_rows if len(row) >= 4]

def clean_distance(value):
    try:
        return float(value.replace("km", "").strip())
    except:
        return None

extracted_data = []
for row in filtered_rows:
    if len(row) < 4:
        continue
    station_eng = row[0]
    station_jpn = row[1]
    distance_between = clean_distance(row[2])
    distance_shinagawa = clean_distance(row[3])
    print(f"📦 Parsed: {station_jpn}, {station_eng}, Between={distance_between}, FromShinagawa={distance_shinagawa}")
    if distance_between is not None and distance_shinagawa is not None:
        extracted_data.append([station_jpn, station_eng, distance_between, distance_shinagawa])

df = pd.DataFrame(
    extracted_data,
    columns=["Station_Japanese", "Station_English", "Distance_between", "Distance_from_Shinagawa"]
)

# Optional rounding
df["Distance_between"] = df["Distance_between"].round(1)
df["Distance_from_Shinagawa"] = df["Distance_from_Shinagawa"].round(1)

os.makedirs("server/data", exist_ok=True)
df.to_csv("server/data/yamanote_stations.csv", index=False)

print(f"✅ Final CSV saved with {len(df)} stations.")