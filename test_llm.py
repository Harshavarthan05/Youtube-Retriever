from transformers import pipeline

print("Loading model...")

model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

print("Model loaded!")

result = model(
    "What is Artificial Intelligence?",
    max_new_tokens=50
)

print(result[0]["generated_text"])