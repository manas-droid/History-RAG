import requests

def ask_ollama(prompt: str, model="mistral") -> str:
    url = "http://localhost:11434/api/generate"
    data = {"model": model, "prompt": prompt, "stream": False}
    r = requests.post(url, json=data)
    return r.json()['response']

context = "1. The other assassins were also unsuccessful. An hour later, as Ferdinand was returning from visiting the injured officers in hospital, his car took a wrong turn into a street where Gavrilo Princip was standing. He fired two pistol shots, fatally wounding Ferdinand and his wife Sophie. " \
"2. James W. Gerard, of Berlin, who had\r\nmotored to Kiel the day before. Mrs. Gerard's sister, Countess Sigray,\r\nis the wife of a Hungarian nobleman, and the Ambassador's wife, if my\r\nmemory serves me correctly, once told me of her sister's acquaintance\r\nwith both of the assassinated Royalties. We Americans discussed the\r\nimmediate consequences of the day's event--how the Kaiser would take it,\r\nhow it would affect poor old Emperor Francis Joseph. William II and\r\nAdmiral von Tirpitz had been the Archduke's guests at Konopischt in\r\nBohemia only a few weeks before. The Kaiser and the future ruler of\r\nAustria-Hungary had become great friends. They were not always that. There had been a good deal of the William II in Franz Ferdinand himself. People often said it was a case of Greek meet Greek, and that two such\r\ninsistent personalities were inevitably bound to clash. Others said that\r\nthe Archduke, inspired by his brilliantly clever consort, always\r\ninsisted that German overlordship in Vienna would cease when he came to\r\nthe throne. Still others knew that despite antipathies and antagonisms,\r\nthe two men had at length come to be genuinely fond of each other, and\r\nthat their ideas and ideals for the greater glory of Germanic Europe\r\ncoincided. These things we chatted and canvassed, irresponsibly, on _Utowana's_\r\nimmaculate deck. All of us were persuaded of the imminency of a crisis\r\nin Austrian-Serbian relations in consequence of Princip's crime. But I\r\nam quite sure not a soul of us held himself capable of imagining that,\r\nbecause of that remote felony, Great Britain and Germany would be at war\r\nfive weeks later. Beyond us spread the peaceful panorama of British and\r\nGerman war-craft, anchored side by side, and the thought would have\r\nperished at birth. Returned to the terrace of the Seebade-Anstalt, one found the atmosphere\r\nheavily charged with suppressed excitement. Immaculately-groomed young\r\ndiplomats, down from Berlin for the Sunday, were twirling their\r\nwalking-sticks and yellow gloves which were not, after all, to accompany\r\nthem to Grand-Admiral Prince Henry of Prussia's garden-party. That,\r\nlike everything else connected with Kiel Week, had suddenly been called\r\noff. A party of Americans flocked together at the entrance to the hotel to\r\nexchange low-spoken views on the all-pervading topic. There was big\r\nLieutenant-Commander Walter R."

user_question = "What part of history don't you have enough knowledge of? I want to create a RAG about history and I looking for some help from you! Please be a good lad and tell me"

full_prompt = f"""
Act like you are a historian and answer the mentioned question:

question: 
{user_question}
"""


response = ask_ollama(prompt=full_prompt)

print(f"response: {response}")






