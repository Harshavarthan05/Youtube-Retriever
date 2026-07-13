# Youtube Retriever Model

## Project Overview:

The model is based on the youtube retriever process. The process how it works means.

1. You have to copy the url and paste through the UI system.
2. The url link video convert into audio using (whisper model) and extract through the text.
3. Next process can text process convert into small chunks like (500 tokens split the text).
4. Next we have to convert the small chunks into embedding vector like numeric value using (sentence Transfomer model).
5. And then we have to store the vector using Vector Database (model- faiss: it used to store the chunks of vector and search relevant value question given by the llm prompt).
6. next retriever process works to convert to identify correct model of question it would convert to chunks and then text to print in the prompt given the answer.
7. Next process LLM model given the prompt how it would answer how many sentence we need it give it like prompting process.
8. Finally we have to create the app model using (Streamlit app) it is more useful in the AI based project model.

## Problem Statement:

This Project mainly based on you have to learn any kind of study based topic youtube it given too many hours to watch to learn the concept 
and the video is too long so the user can struggle to study it takes time to learn it all but the youtube retrieve rescue the concept step by ste
and it loads the model and if you ask about any kind of question in that video model it will give the answer properly.

It is more useful for secondary, higher secondary and university students.

## Architecture:

Model architecture this tells how it works each step.

Url link
    |
Transcript(video->audio->text)
    |
Chunks(separate small chunks)
    |
Embedding(convert numeric value)
    |
Vector Database(store the vector data)
    |
Retriever(search relavent pattern of given question)
    |
LLM(prompt the process user ask question)
    |
Rag chat(Display the correct answer)
    |
App(User can clearly to access the app to use it)

## Library Usage:

1. Yt-Dlp - It is used for convert the url youtube video into Audio and download the audio save in mp3 file.

2. Whisper - Whisper is used for extract the audio into text format because machine can understand easily.

3. Sentence-Transformer - It is used for the chunks data convert into embedding(numeric vector value) because machine can understand numeric values.

4. Faiss - It store the vector data values.

5. Streamlit - It is UI framework built like a app.

## Model Usage:

1. mp3 - It is used to convert the video into audio file and save the model.

2. 'intfloat/e5-base-v2' - To perform semantic similarity and perform information retrieval.

3. 'TinyLlama/TinyLlama-1.1B-Chat-v1.0' - conversational text generation and instruction-following on devices with very limited memory and computational power.

## Model Structure:

Youtube_retriver
|
|
|----->transcript.py
|
|----->chunk.py
|
|----->embedding.py
|
|----->vector_db.py
|
|----->retriever.py
|
|----->rag_chat.py
|
|----->llm.py
|
|----->test_llm.py
|
|----->requirements.txt
|
|----->README.md

## Disadvantage of my Model:

1. Time latency it take long time to run the model.

2. Sometimes LLM get confuse to written the wrong answer and all.

3. UI framework not like familiar with all kind of user satisfaction and i will develop more efficient later.

4. If Video is 6-9 hrs it takes more time to chunks the model.

## Sample Output:

Url Pattern: https//youtube.com****//

User: What are the types of Machine learning?

Answer: 1.Supervised Learning
        2.Unsupervised Learning
        3.Reinforcement Learning


## Author:

Harshavarthan B