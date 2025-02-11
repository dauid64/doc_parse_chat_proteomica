# RAG Avançado Chat Proteômica

Esse é o projeto responsável por alimentar o banco vetórial do [chat_proteomica](https://github.com/dauid64/chat_proteomica).

## Estrutura

- 📂 artigos_para_docling

    Nesta pasta fica os artigos coletado pelos pesquisadores do Laboratório de Proteômica, disponível no [drive](https://drive.google.com/drive/folders/1EhdFNfqo6X9Gi9jkbah8F7iEX39Ytg9L?usp=drive_link).

    obs: nem todos os arquivos foram possíveis de ser convertidos e teve que ser retirado, porém grande quantidade foi possível como pode ver no arquivo `artigos_tratados_docling` com suas conversões em markdown.

- 📄 converte_artigos.py

    Esse script é responsável por pegar todos os pdfs que estão na pasta `artigos_para_docling` e converte-los para o formato markdown para melhor interpretação da IA utilizando a biblioteca Docling, utilizei essa biblioteca por ter um melhor resultado do que por exemplo LlamaParse.

- 📄 geracao_embeddings.py

    Neste arquivo é feito o split do texto dos documentos já convertidos para merkdown, gerar os embeddings utilizando o modelo da Open AI e armazena-los no banco vetorial Qdrant.

- 📂 legado

    Pasta com testes feitos utilizando o LlamaParse.

