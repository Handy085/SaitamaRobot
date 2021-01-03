from SaitamaRobot.sample_config import Config

class Development(Config):
    OWNER_ID =  1156597097 # your telegram ID
    OWNER_USERNAME = "Dani Bot"  # your telegram username
    API_KEY = "1479632590:AAE6PeEa4w2amR0JDaN3loy6GHqtvCRlLvY"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://danibot:dkkaj0123456@postgresql/postgres'  # sample db credentials
    JOIN_LOGGER = '-1001348440289' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [1156597097]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
