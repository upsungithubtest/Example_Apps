
import os
from dotenv import load_dotenv
load_dotenv()

dbhost = os.getenv("DBHOST", "mariadb-srv")
dbname = os.getenv("DBNAME", "abfriends")
dbuser = os.getenv("BUSER", "root")
dbpass = os.getenv("DBPASS", "VeF86#uU@*Lb")

