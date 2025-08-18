from BaseVecDB import BaseVecDB
from ChromaVecDB import ChromaVecDB
import data_collector.WikipediaDataCollector as wpdc
import data_collector.BaseDataCollector as bdc
import chunker.SemanticSplitter as ssplit

data_collector:bdc.BaseDataCollector = wpdc.WikipediaDataCollector()
result = data_collector.get_data()
text_result = [data.text for data in result]
splitter  =  ssplit.SemanticSplitter()
documents = splitter.get_chunks(text_result)

db_name = "chroma_wwi_semantic_chunks_default_embedding"

vecDB:BaseVecDB = ChromaVecDB(db_name)

vecDB.add_documents(documents)