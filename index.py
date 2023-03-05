from dotenv import load_dotenv

load_dotenv()

import os
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader


source_dir_path = "bible"

data = []

print("Loading files...")

for filename in os.listdir(source_dir_path):
    f_path = os.path.join(source_dir_path, filename)
    loader = TextLoader(f_path)
    documents = loader.load()
    data.append(documents)


print("Splitting files...")
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = []

for d in data:
    docOutput = text_splitter.split_documents(d)
    docs = docs + docOutput


embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])


print("Connecting pinecone...")
pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],  # find at app.pinecone.io
    environment="us-east1-gcp",  # next to api key in console
)

index_name = "bible"

print("Creating index...")
pinecone.create_index(name=index_name, dimension=1536, pod_type="s1.x1")

print("Indexing vectors...")

docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

print("Indexing DONE!")
