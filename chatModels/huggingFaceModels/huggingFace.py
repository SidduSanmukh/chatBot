from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    temperature=0.7,
)
model = ChatHuggingFace(llm=llm)

while True:
    user = input("user: ")
    response = model.invoke(user)
    print('Bot: ', response.content)