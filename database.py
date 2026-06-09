# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from langchain_community.utilities import SQLDatabase

# load_dotenv()

# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")
# db_host = os.getenv("DB_HOST")
# db_port = os.getenv("DB_PORT")
# db_name = os.getenv("DB_NAME")

# engine = create_engine(
#     f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# )

# db = SQLDatabase(engine)




import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from langchain_community.utilities import SQLDatabase

# Load .env file
load_dotenv()

# Read environment variables
db_user = os.getenv("DB_USER")
db_password = quote_plus(os.getenv("DB_PASSWORD"))  # Handles @, #, %, etc.
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Debug prints
print("DB_USER =", db_user)
print("DB_HOST =", db_host)
print("DB_PORT =", db_port)
print("DB_NAME =", db_name)

# Create connection URL
connection_url = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

print("Connection URL =", connection_url)

# Create SQLAlchemy engine
engine = create_engine(connection_url)

# Create LangChain SQL Database object
db = SQLDatabase(engine)