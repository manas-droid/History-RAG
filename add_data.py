from vec_db.BaseVecDB import BaseVecDB
from vec_db.ChromaVecDB import ChromaVecDB
import data_collector.WikipediaDataCollector as wpdc
import data_collector.BaseDataCollector as bdc
import chunker.SemanticSplitter as ssplit
from data_collector.GutendexDataCollector import GutendexDataCollector

data_collector:bdc.BaseDataCollector = wpdc.WikipediaDataCollector()
result = data_collector.get_data()
text_result = [data.text for data in result]
splitter  =  ssplit.SemanticSplitter()
documents = splitter.get_chunks(text_result)

data_collector:bdc.BaseDataCollector = GutendexDataCollector()
gutendex_result = data_collector.get_data()
text_gutendex_result = [data.text for data in gutendex_result]
gutendex_documents = splitter.get_chunks(text_gutendex_result)
db_name = "chroma_wwi_semantic_chunks_default_embedding"


vecDB:BaseVecDB = ChromaVecDB(db_name)
vecDB.add_documents(gutendex_documents)
vecDB.add_documents(documents)

