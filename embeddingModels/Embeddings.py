from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    output_dimensionality=300
)

text = 'siddarooda samba sada shiva'

response = embedding.embed_query(text)
print(response)