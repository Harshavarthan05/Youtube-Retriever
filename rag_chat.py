from retriever import retrieve_chunks
from llm import (build_prompt,
                 get_llm,
                 generate_answer,
                 validate
)

model = get_llm()

def chat(question, vector_db):
    if question is None:
        print("There is No question is Found")
        return None

    question = question.strip()

    if question == " ":
        print("Question is Empty")
        return None

    chunks = retrieve_chunks(question, vector_db)

    if chunks is None:
        print("No relavant value can be found")
        return None

    prompt = build_prompt(question, chunks)

    if prompt is None:
        print("Prompt not yet found in the process")
        return None

    model = get_llm()

    answer = generate_answer(model, prompt)

    answer = validate(answer)

    return answer


def display_answer(answer):
    if answer is None:
        return None

    print("\n***********AI Generator*************\n")
    print(answer)
    print("\n************************************\n")
