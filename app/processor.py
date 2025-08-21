import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import os
nltk.download('vader_lexicon', quiet=True)


class SentimentProcessor:
    def _init_(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('vader_lexicon', download_dir=nltk_dir, quiet=True)
        self.analyzer = SentimentIntensityAnalyzer()

class Processor:

    def __init__(self):
        self.dataframe = None
        self.weapons = None
        self.a = SentimentProcessor()

    def create_dataframe(self, data):
        self.dataframe = pd.DataFrame(data)
        self.dataframe = self.dataframe.set_index("_id")


    def return_data(self):
        return self.dataframe

    def create_the_columns_sentiment_and_rarest_word(self):
        list_of_min_word = []
        list_of_calculating_emotion = []
        list_of_weapons = []
        for tweet in self.dataframe.Text.values:
            list_of_min_word.append(self.find_rare_word(tweet))
            list_of_calculating_emotion.append(self.find_text_sentiment(tweet))
            list_of_weapons.append(self.check_if_weapons_exists(tweet))
        self.dataframe.insert(2,"rarest_word",list_of_min_word)
        self.dataframe.insert(3,"sentiment",list_of_calculating_emotion)
        self.dataframe.insert(4,"weapons_detected",list_of_weapons)




    def find_rare_word(self, text):
        counter = Counter(text.split())
        return counter.most_common()[-1][0]


    def find_text_sentiment(self, text):
            score = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
            if score > .5:
                return "positive"
            elif score > -.5:
                return "neutral"
            else:
                return "negative"

    def check_if_weapons_exists(self, text):
        if not self.weapons:
            self.get_weapons()
        for weapon in self.weapons:
            if weapon in text:
                return weapon
        return -1



    def get_weapons(self):
        self.weapons = ["A-bomb",
"ammo",
"ammunition",
"armaments",
"arms",
"arrow",
"assault rifle",
"atom bomb",
"atomic bomb",
"autocannon",
"automatic rifle",
"axe",
"ballista",
"ballistic missile",
"bat",
"baton",
"battle axe",
"bayonet",
"bazooka",
"billy club",
"biological weapon",
"blackjack",
"blade",
"blaster",
"blowgun",
"blowpipe",
"bludgeon",
"bomb",
"boobytrap",
"boomerang",
"bow and arrow",
"Bowie knife",
"brass knuckles",
"bullet",
"bullwhip",
"cannon",
"carbine",
"cat o'nine tails",
"catapult",
"cleaver",
"club",
"crossbow",
"cudgel",
"cutlass",
"dagger",
"dart",
"depth charge",
"epee",
"explosives",
"firearm",
"flail",
"flamethrower",
"flintlock",
"foil",
"Gatling gun",
"grenade",
"grenade launcher",
"guided missile",
"gun",
"gunpowder",
"halberd",
"hand grenade",
"handgun",
"harpoon",
"hatchet",
"howitzer",
"hunting knife",
"javelin",
"katana",
"knife",
"knout",
"kris",
"lance",
"landmine",
"longbow",
"longsword",
"mace",
"machete",
"machine gun",
"magnum",
"maul",
"mine",
"missile",
"morning star",
"mortar",
"munitions",
"musket",
"mustard gas",
"muzzleloader",
"nerve gas",
"night stick",
"nuclear bomb",
"nunchaku (nunchucks)",
"onager",
"ordnance",
"peashooter",
"pepper spray",
"pickaxe",
"pike",
"pistol",
"pommel",
"quarterstaff",
"rapier",
"revolver",
"rifle",
"rocket",
"rocket launcher",
"saber",
"scimitar",
"scythe",
"semiautomatic",
"shell",
"shillelagh",
"shooter",
"shotgun",
"sickle",
"slingshot",
"spear",
"spiked mace",
"stiletto",
"stun gun",
"submachine gun",
"switchblade",
"sword",
"tank",
"tank gun",
"taser",
"tear gas",
"tomahawk",
"torpedo",
"trebuchet",
"trident",
"tripwire",
"truncheon",
"uzi",
"weapon",
"weapon of mass destruction",
"weaponry",
"whip"]
        return self.weapons
