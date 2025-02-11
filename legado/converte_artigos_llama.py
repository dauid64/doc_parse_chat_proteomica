import os

from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

instruction = """The provided document is about Proteômica.
These documents provide details and topics related to Proteomics. Includes tests with tables on the subject.
Try to be precise while answering the questions"""

parser = LlamaParse(
    api_key=os.getenv("LLAMA_PARSE"),
    result_type="markdown",
    parsing_instruction=instruction,
    max_timeout=5000,
)

source = "./artigos_para_llama"

for artigo in os.listdir(source):
    if artigo.endswith('.pdf'):
        try:
            caminho_completo = os.path.join(source, artigo)

            destino_arquivo_md = f"./artigos_tratados_llama/{artigo.replace('.pdf', '.md')}"

            destino_arquivo_docling_md = f"./artigos_tratados_docling/{artigo.replace('.pdf', '.md')}"

            artigo_existe = os.path.exists(destino_arquivo_md)
            artigo_docling_existe = os.path.exists(destino_arquivo_docling_md)

            if not artigo_existe and not artigo_docling_existe:
                print("🔄 Convertendo artigo: ", caminho_completo)
                llama_parse_documents = parser.load_data(caminho_completo)
                parsed_doc = llama_parse_documents[0]

                with open(destino_arquivo_md, "w") as f:
                    f.write(parsed_doc.text)
                
                print(f"✅ Artigo convertido: {destino_arquivo_md}")
            else:
                print(f"⚠️ Artigo já convertido: {destino_arquivo_md}")
        
        except Exception as e:
            print(f"❌ Erro ao processar: {caminho_completo}: {e}")
            continue