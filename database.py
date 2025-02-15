from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
uri = "mongodb+srv://leonie:<jNpBNJgyjJR6edW9>@database.prqcd.mongodb.net/?retryWrites=true&w=majority&appName=Database"

client = MongoClient(uri, server_api=ServerApi('1'), serverSelectionTimeoutMS=5000000)
db = client["countries"]
collection = db["regions"]
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

regions =[
    "Alaska", "North West Territory", "Alberta", "Ontario", "Quebec",
    "Western US", "Eastern US", "Central US", "Venezuela", "Peru",
    "Brazil", "Argentina", "Iceland", "Great Britain", "Scandinavia",
    "Ukraine", "Northern Europe", "Western Europe", "Southern Europe",
    "North Africa", "Egypt", "East Africa", "Congo", "South Africa",
    "Madagascar", "Middle East", "India", "South East Asia", "China",
    "Afghanistan", "Mongolia", "Japan", "Indonesia", "New Guinea",
    "Western Australia", "Eastern Australia"
]

co2_per_kwh = {
    "Alaska": 450, "North West Territory": 300, "Alberta": 650, "Ontario": 120, "Quebec": 30,
    "Western US": 400, "Eastern US": 350, "Central US": 500, "Venezuela": 600, "Peru": 200,
    "Brazil": 100, "Argentina": 250, "Iceland": 20, "Great Britain": 150, "Scandinavia": 50,
    "Ukraine": 700, "Northern Europe": 200, "Western Europe": 180, "Southern Europe": 300,
    "North Africa": 500, "Egypt": 550, "East Africa": 400, "Congo": 300, "South Africa": 700,
    "Madagascar": 450, "Middle East": 800, "India": 850, "South East Asia": 700, "China": 900,
    "Afghanistan": 650, "Mongolia": 750, "Japan": 100, "Indonesia": 500, "New Guinea": 200,
    "Western Australia": 600, "Eastern Australia": 500
}

gdp_multipliers = {
    "Alaska": "medium", "North West Territory": "low", "Alberta": "high", "Ontario": "medium", "Quebec": "low",
    "Western US": "high", "Eastern US": "high", "Central US": "high", "Venezuela": "low", "Peru": "low",
    "Brazil": "medium", "Argentina": "low", "Iceland": "low", "Great Britain": "high", "Scandinavia": "medium",
    "Ukraine": "low", "Northern Europe": "medium", "Western Europe": "high", "Southern Europe": "medium",
    "North Africa": "low", "Egypt": "low", "East Africa": "low", "Congo": "low", "South Africa": "medium",
    "Madagascar": "low", "Middle East": "high", "India": "high", "South East Asia": "high", "China": "high",
    "Afghanistan": "low", "Mongolia": "low", "Japan": "high", "Indonesia": "medium", "New Guinea": "low",
    "Western Australia": "medium", "Eastern Australia": "medium"
}
image = {
    "Alaska": "Alask.png", "North West Territory": "NorthWestTerritory.png", "Alberta": "Alberta.png", "Ontario": "Ontario.png", "Quebec": "Quebec.png",
    "Western US": "WesternUS.png", "Eastern US": "EasternUS.png", "Central US": "CentralUS.png", "Venezuela": "Venezuela.png", "Peru": "low",
    "Brazil": "Brazil.png", "Argentina": "Argentina.png", "Iceland": "Iceland.png", "Great Britain": "GreatBritain.png", "Scandinavia": "medium",
    "Ukraine": "Ukraine.png", "Northern Europe": "NorthernEurope.png", "Western Europe": "WesternEurope.png", "Southern Europe": "SouthernEurope.png",
    "North Africa": "NorthAfrica.png", "Egypt": "Egypt.png", "East Africa": "EastAfrica.png", "Congo": "Congo.png", "South Africa": "SouthAfrica.png",
    "Madagascar": "Madagascar.png", "Middle East": "MiddleEast.png", "India": "India.png", "South East Asia": "SouthEastAsia.png", "China": "China.png",
    "Afghanistan": "Afghanistan.png", "Mongolia": "Mongolia.png", "Japan": "Japan.png", "Indonesia": "Indonesia.png", "New Guinea": "NewGuinea.png",
    "Western Australia": "WesternAustralia.png", "Eastern Australia": "Eastern Australia.png"
}



def assign_multiplier(rating):
    """Assigns a random CO₂ multiplier based on GDP impact ('high', 'medium', 'low')."""
    if rating == "high":
        return round(random.uniform(2.1, 3.0), 2)
    elif rating == "medium":
        return round(random.uniform(1.1, 2.0), 2)
    elif rating == "low":
        return round(random.uniform(0.1, 1.0), 2)


data = []
for region in regions:
    gdp_rating = gdp_multipliers[region]
    new_multiplier = assign_multiplier(gdp_rating)  # Ensure the multiplier is correctly assigned

    data.append({
        "region": region,
        "co2_per_kwh": co2_per_kwh[region],
        "gdp_multiplier": gdp_rating,
        "new_multiplier": new_multiplier,
        "start_cost": round(1000 * new_multiplier)  # Correctly calculate start cost
        "image": image
    })

collection.insert_many(data)
