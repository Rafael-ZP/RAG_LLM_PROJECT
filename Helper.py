# Import Necessary Modules

from dotenv import load_dotenv
import os
from langchain_community.llms import GooglePalm
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Load environment variables from .env
load_dotenv()
api_key='AIzaSyBBUBI8fwPKVey1BGRn5UtIoRKkduFOirA'
# Create Google Palm LLM model with the desired temperature
temperature_value = 1  # Adjust the temperature as needed
llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=temperature_value)

# Initialize instructor embeddings using the Hugging Face model
embeddings = HuggingFaceInstructEmbeddings()
Vector_Path = "New_Faiss_Index"
filename = "rules.txt"  # Update with your actual file path


def create_vector():
    try:
        # Load data from text file
        loader = TextLoader(file_path=filename)
        data = loader.load()

        # Create a FAISS instance for the vector database from 'data'
        Vector_db = FAISS.from_documents(documents=data, embedding=embeddings)

        # Save the vector database locally
        Vector_db.save_local(Vector_Path)
        print("Vector database created and saved successfully.")
    except Exception as e:
        print(f"An error occurred while creating the vector database: {e}")


def get_qa_chain():
    try:
        # Load the vector database from the local folder
        Vector_db = FAISS.load_local(Vector_Path, embeddings,allow_dangerous_deserialization=True)

        # Create a retriever for querying the vector database
        retriever = Vector_db.as_retriever()

        prompt_template = """Given the following context and a question, generate an answer based on this context only.
                            In the answer try to provide as much text as possible from "response" section in the source 
                            document context without making much changes. If the answer is not found in the context, 
                            kindly state "I don't know." Don't try to make up an answer.
                            CONTEXT: {context}
                            QUESTION: {question}"""
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain_type_kwargs = {"prompt": PROMPT}
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            input_key="query",
            return_source_documents=True,
            chain_type_kwargs=chain_type_kwargs
        )
        print("QA chain created successfully.")
        return chain
    except Exception as e:
        print(f"An error occurred while getting the QA chain: {e}")


if __name__ == "__main__":
    create_vector()
    chain = get_qa_chain()
    if chain:
        query = "How to behave in a park?"
        response = chain({"query": query})
        print(response)
