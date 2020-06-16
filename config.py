
import os
from dotenv import load_dotenv
load_dotenv()

dbhost = os.getenv("DBHOST", "127.0.0.1")
dbname = os.getenv("DBNAME", "abfriends")
dbuser = os.getenv("BUSER", "devuser")
dbpass = os.getenv("DBPASS", "devPW")

