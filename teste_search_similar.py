import textwrap
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large')

vector_store = QdrantVectorStore.from_existing_collection(
    collection_name="chat_proteomica",
    embedding=embeddings,
    url="http://localhost:6333",
    prefer_grpc=True
)

query = "O que é proteômica?"

# similar_docs = vector_store.similarity_search_with_score(query)

# for doc, score in similar_docs:
#     print(f"text: {doc.page_content[:256]}\n")
#     print(f"score: {score}")
#     print("-" * 80)
#     print()

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
retrieved_docs = retriever.invoke(query)

compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2")
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

reranked_docs = compression_retriever.invoke(query)
len(reranked_docs)


for doc in reranked_docs:
    print(f"id: {doc.metadata['_id']}\n")
    print(f"text: {doc.page_content[:256]}\n")
    print(f"score: {doc.metadata['relevance_score']}")
    print("-" * 80)
    print()

# Chat Prompt
llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini-2024-07-18")

prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Answer the question and provide additional helpful information,
based on the pieces of information, if applicable. Be succinct.

Responses should be properly formatted to be easily read.
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=compression_retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt, "verbose": True},
)

response = qa.invoke("Quais as principais abordagens usadas em análise proteômica?")

print(response)

# def print_response(response):
#     response_txt = response["result"]
#     for chunk in response_txt.split("\n"):
#         if not chunk:
#             print()
#             continue
#         print("\n".join(textwrap.wrap(chunk, 100, break_long_words=False)))

# print_response(response)