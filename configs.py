# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22207976"))
    API_HASH = getenv("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")
    BOT_TOKEN = getenv("BOT_TOKEN", "6686752412:AAGX8tAgffjeSdbCltvPz_e8lT48wlJc7LA")
    FSUB = getenv("FSUB", "DKANIME47")
    CHID = int(getenv("CHID", "-100180202613"))
    SUDO = list(map(int, getenv("SUDO", "1598215463").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://devensh12:devensh1234@cluster0.x74masc.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
