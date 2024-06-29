from app import app

# import
# from langchain_google_genai import ChatGoogleGenerativeAI

# google_api_key = os.getenv("GOOGLE_GENAI_APIKEY")

# llm = ChatGoogleGenerativeAI(model="gemini-pro-vision", google_api_key=google_api_key)
# result = llm.invoke("Write a ballad about LangChain")

if __name__ == '__main__':
    app.run(debug=True)
