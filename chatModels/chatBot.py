from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import sys
load_dotenv()

sys.stdout.reconfigure(line_buffering=False) 
sys.stdout.reconfigure(write_through=True)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

while True:
    user = input('user: ')
    for chunk in model.stream(user):
        print(chunk.content, end="", flush=True)
    print()
# full = None
# while True:
#     user = input("user : ")
#     for chunk in model.stream(user):
#         full = chunk if full is None else full + chunk
#         print(full.text)