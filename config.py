
import os
from dotenv import load_dotenv
load_dotenv()


dbhost = os.getenv("DB_HOST", "127.0.0.1")
dbname = os.getenv("DB_DATABASE", "abfriends")
dbuser = os.getenv("DB_USERNAME", "devuser")
dbpass = os.getenv("DB_PASSWORD", "devPW")
