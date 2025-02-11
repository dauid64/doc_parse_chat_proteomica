from docling.document_converter import DocumentConverter
import os

def convert_articles(source: str, converter: DocumentConverter):
    for artigo in os.listdir(source):
        if artigo.endswith('.pdf'):
            try:
                caminho_completo = os.path.join(source, artigo)

                destino_arquivo_md = f"./artigos_tratados_docling/{artigo.replace('.pdf', '.md')}"

                artigo_existe = os.path.exists(destino_arquivo_md)

                if not artigo_existe:
                    print("🔄 Convertendo artigo: ", caminho_completo)
                    result = converter.convert(caminho_completo)

                    with open(destino_arquivo_md, "w") as f:
                        f.write(result.document.export_to_markdown())
                    
                    print(f"✅ Artigo convertido: {destino_arquivo_md}")
                else:
                    print(f"⚠️ Artigo já convertido: {destino_arquivo_md}")
            
            except Exception as e:
                print(f"❌ Erro ao processar: {caminho_completo}: {e}")
                continue

if __name__ == '__main__':
    source = "./artigos_para_docling"
    converter = DocumentConverter()

    convert_articles(source, converter)