import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

def split_documents(source, text_splitter):
    all_docs = []

    for artigo in os.listdir(source):
        if artigo.endswith('.md'):
            try:
                caminho_completo = os.path.join(source, artigo)

                loader = UnstructuredMarkdownLoader(caminho_completo)
                loaded_documents = loader.load()

                docs = text_splitter.split_documents(loaded_documents)
                all_docs.extend(docs)

                print(f"✅ Artigo convertido: {caminho_completo}")
            
            except Exception as e:
                print(f"❌ Erro ao processar: {caminho_completo}: {e}")
                continue

    print("Número de documentos: ", len(all_docs))

    return all_docs

def generate_and_save_embeddings(all_docs):
    embeddings = OpenAIEmbeddings(model='text-embedding-3-large')

    qdrant_client = QdrantClient(url=os.getenv('QDRANT_URL'), api_key=os.getenv('QDRANT_KEY'))

    collection_exist = qdrant_client.collection_exists(collection_name="chat_proteomica")

    if collection_exist:
        qdrant_client.delete_collection(collection_name="chat_proteomica")

    QdrantVectorStore.from_documents(
        all_docs,
        embeddings,
        url=os.getenv('QDRANT_URL'),
        api_key=os.getenv('QDRANT_KEY'),
        prefer_grpc=True,
        collection_name="chat_proteomica"
    )

if __name__ == '__main__':
    load_dotenv()

    source = "./artigos_tratados_docling"
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2048, chunk_overlap=128)

    all_docs = split_documents(source, text_splitter)
    generate_and_save_embeddings(all_docs)