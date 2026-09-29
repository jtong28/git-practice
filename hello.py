from dotenv import load_dotenv
import os

load_dotenv()

secret = os.getenv("SECRET_MESSAGE")
print("Hello, world!")
print("The secret message is:", secret)