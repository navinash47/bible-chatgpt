from dotenv import load_dotenv

load_dotenv()


import os
import openai
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


openai.api_key = os.environ["OPENAI_API_KEY"]
pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],  # find at app.pinecone.io
    environment="us-east1-gcp",  # next to api key in console
)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])


docsearch = Pinecone.from_existing_index(index_name="bible", embedding=embeddings)


def generate_reply(history, prompt):
    docs = docsearch.similarity_search(query=prompt, k=2)
    context = []
    for doc in docs:
        context.append("Context:{}\n".format(doc))
    messages = history + [
        {
            "role": "user",
            "content": "Use the memory context below:\n${}\n\nMy question is:\n${}".format(
                context, prompt
            ),
        }
    ]
    # print(messages)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return completion.choices[0].message["content"]
