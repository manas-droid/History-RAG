from vec_db.BaseVecDB import BaseVecDB
from vec_db.ChromaVecDB import ChromaVecDB
import json


db_name = "chroma_wwi_semantic_chunks_default_embedding"

vecDB:BaseVecDB = ChromaVecDB(db_name)

result = vecDB.get_related_data(["Who murdered Franz Ferdinand?"], 2)

json_string = json.dumps(result, indent=4)

file_name = "query_result.json"
with open(file_name, "w") as json_file:
    json_file.write(json_string)

print(f"Document saved to {file_name}")
