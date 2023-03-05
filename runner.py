from bible_prompt import bible_prompt
from query import generate_reply

history = [{"role": "system", "content": bible_prompt}]

while True:
    question = input("\nAsk a question >")
    answer = generate_reply(history, question)
    print("Holy Bible: ", answer)

    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})
