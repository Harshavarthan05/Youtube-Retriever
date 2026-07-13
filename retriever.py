from embedding import create_embedded

def receive_question(question):
    if question is None:
        print("The question not found it..")
        return None

    question = question.strip()

    if question == " ":
        print("If question is empty")
        return None

    return question

def validate_question(question):
    question = receive_question(question)

    if question is None:
        print("Invalid question not found")
        return None

    return question

def create_embedding(question):
    question = validate_question(question)

    query_embedding = create_embedded(question)

    if query_embedding is None:
        print("No vector cannot be found ")
        return None

    return query_embedding

def retrieve_chunks(question, vector_db, k=3):
    query_embedding = create_embedding(question)

    if query_embedding is None:
        print("Retrieve chunks cannot be found")
        return None

    res = vector_db.search_vector(query_embedding, k)

    if not res:
        print("Result not found in the system")
        return None

    return res

def prepare_context(question, vector_db):

    chunks = retrieve_chunks(question, vector_db)

    if chunks is None:
        return None

    context = "\n\n".join(chunks)

    print("Context have successfully found")

    return context