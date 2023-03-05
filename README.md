
# Chat with the Holy Bible

Using OpenAI's embedding & turbo model


## Installation

Install the project with 

```bash
  git clone https://github.com/your-username/your-project.git
  cd my-project
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

To get these API Keys, sign up for an account on [OpenAI](https://platform.openai.com/account/api-keys) and [Pinecone](https://www.pinecone.io/) and get the keys.


```bash
  OPENAI_API_KEY=sk-xxxx
  PINECONE_API_KEY=xxxxx
```
## Vector Store

Create a vector store of the Bible. This can take anywhere from 5 to 20 minutes.

```bash
  python index.py
```

Once you create a vector store, you don't have to run `index.py` again.
## Ask Questions.

```bash
  python runner.py
```
