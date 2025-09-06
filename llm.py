import requests
from vec_db.BaseVecDB import BaseVecDB
from vec_db.ChromaVecDB import ChromaVecDB

def ask_ollama(prompt: str, model="mistral") -> str:
    url = "http://localhost:11434/api/generate"
    data = {"model": model, "prompt": prompt, "stream": False}
    r = requests.post(url, json=data)
    return r.json()['response']

def get_context(user_question:str)->str:
    db_name = "chroma_wwi_semantic_chunks_default_embedding"
    vecDB:BaseVecDB = ChromaVecDB(db_name)
    result = vecDB.get_related_data([user_question], 2)

    context_arr = result["documents"][0]

    context:str = ""
    point:int = 1
    for doc in context_arr:
        context += f"{point}. {doc}\n"
        point+=1
    
    return context
print(__name__)


if __name__ == "__main__":

    user_question = "What were the causes of World War 1 apart from Franz Ferdinand's murder?"

    context = get_context(user_question)

    full_prompt = f"""
    Act like you are a historian and answer the mentioned question by considering the below context:
    context: {context}
    question: 
    {user_question}
    """


    response = ask_ollama(prompt=full_prompt)

    print(f"response: {response}")