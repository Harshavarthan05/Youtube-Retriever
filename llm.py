from transformers import pipeline

model = None

def receive_context(context):
    if context is None:
        print("No context found")
        return None

    if len(context) == 0:
        print("The length of context is empty")
        return None

    return context

def receive_question(question):
    if question is None:
        print("Question is not found in context")
        return None

    question = question.strip()

    if question == " ":
        print("Question of the value is Empty")
        return None

    return question

def build_prompt(question, context):
    question = receive_question(question)
    context = receive_context(context)

    if question is None or context is None:
        return None

    prompt = f"""

    You are a question-answering assistant.

Answer ONLY using the provided context.

Do not add information that is not present in the context.

If the answer cannot be found in the context, reply:
"I could not find the answer in the video transcript."

Keep the answer between 2 and 5 sentences.

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt

def llm_model():
    print("Entering llm_model()")

    try:
        print("Loading TinyLlama...")

        model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        )

        print("Model loaded successfully.")

        return model

    except Exception as e:
        print("ERROR OCCURRED:")
        print(type(e))
        print(e)

        return None

def get_llm():
    global model

    if model is None:
        model = llm_model()

    return model
    
def generate_answer(model, prompt):
    if model is None:
        print("The model is not present")
        return None

    if prompt is None:
        print("The prompt not found in process")
        return None

    outputs = model(
        prompt, 
        max_new_tokens = 40, 
        do_sample = False,
        return_full_text = False
    )

    return outputs[0]["generated_text"]

def validate(answer):
    if answer is None:
        print("The answer not found yet")
        return None

    answer = answer.strip()

    if answer == " ":
        print("The answer is Empty No prompt found")
        return None

    return answer
