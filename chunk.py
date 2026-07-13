import re

def chunk_model(text, chunk_size=500):
    if text is None:
        return None

    text = text.strip()

    if text == "":
        return None

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence = sentence.strip()

        if current_length + len(sentence) <= chunk_size:
            current_chunk.append(sentence)
            current_length += len(sentence)

        else:
            chunks.append(" ".join(current_chunk))

            current_chunk = [sentence]
            current_length = len(sentence)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks