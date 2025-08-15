
import chunker.BaseSplitter as bs
from typing import List
from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from langchain_experimental.text_splitter import SemanticChunker



class SemanticSplitter(bs.BaseSplitter):
    def get_chunks(self, texts:List[str])->List[Document]:
        embeddings = HuggingFaceEndpointEmbeddings(model="BAAI/bge-small-en-v1.5")
        text_splitter = SemanticChunker(embeddings)
        docs = text_splitter.create_documents(texts)
        return docs
    
