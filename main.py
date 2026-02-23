import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

def main():
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    # 1. Initialize the LLM (Google Gemini)
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    # 2. Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers questions about software architecture."),
        ("user", "{input}")
    ])

    # 3. Create a chain using LCEL (LangChain Expression Language)
    # NOTE: This is the basic chain (Lab 1). 
    # In Lab 2 (RAG), this chain evolves to include a "retriever" 
    # that searches for context in Pinecone before querying the LLM.
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # 4. Invoke the chain
    print("--- LangChain LLM Chain Tutorial ---")
    user_input = "What is Retrieval-Augmented Generation (RAG)?"
    print(f"User Request: {user_input}")
    print("\nProcessing...")
    
    response = chain.invoke({"input": user_input})
    
    print("\nAI Response:")
    print(response)

if __name__ == "__main__":
    main()
