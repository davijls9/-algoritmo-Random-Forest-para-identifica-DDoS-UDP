# DDoS Evaluation Dataset (CIC-DDoS2019)

Este repositório contém um conjunto de dados para avaliação de ataques de negação de serviço distribuídos (DDoS).

## Descrição

O conjunto de dados disponibilizado aqui contém informações sobre ataques DDoS e é utilizado para avaliar o desempenho de diferentes algoritmos de classificação.

## Informações da Base de Dados

Este conjunto de dados, CICDDoS2019, é referenciado no artigo "Developing Realistic Distributed Denial of Service (DDoS) Attack Dataset and Taxonomy" disponível [aqui](https://www.unb.ca/cic/datasets/ddos-2019.html).

### Resumo do Artigo

O artigo descreve a ameaça dos ataques de negação de serviço distribuídos (DDoS) à segurança de redes, enfatizando a busca por detectores em tempo real com baixo custo computacional. Destaca-se a importância de conjuntos de dados bem projetados para avaliar novos algoritmos e técnicas de detecção.

### Contribuição do Artigo

1. Revisão abrangente de conjuntos de dados existentes e proposta de uma nova taxonomia para ataques DDoS.
2. Geração do conjunto de dados CICDDoS2019, corrigindo lacunas presentes em conjuntos de dados anteriores.
3. Proposta de um novo método de detecção e classificação de famílias de ataques baseado em características de fluxo de rede.
4. Identificação dos conjuntos de características mais importantes para detectar diferentes tipos de ataques DDoS, com seus respectivos pesos.

### Nome do Artigo

"Developing Realistic Distributed Denial of Service (DDoS) Attack Dataset and Taxonomy.pdf"

## Pré-requisitos

Antes de usar este conjunto de dados e o código associado, certifique-se de ter instalado:

- Python (versão 3.11.1)
- Bibliotecas Python: pandas, scikit-learn, matplotlib, seaborn, etc.

## Uso

1. Faça o download ou clone este repositório.

2. Execute o arquivo `nome_do_arquivo.py` para começar a trabalhar com o conjunto de dados.

3. Certifique-se de definir o caminho correto para o arquivo CSV no código, alterando a variável `csv_file_path`.

4. Execute o código em um ambiente Python compatível.

5. Explore os dados, visualize, e treine modelos de classificação com os algoritmos disponíveis no código.

## Estrutura do Código

O código disponibilizado neste repositório contém:

- Importações de bibliotecas Python necessárias.
- Leitura do arquivo CSV e manipulação dos dados.
- Preparação e pré-processamento dos dados.
- Treinamento de modelos de classificação: Logistic Regression, Decision Tree, Random Forest.
- Avaliação dos modelos e métricas de desempenho.

## Resultados

Os resultados dos modelos de classificação são exibidos na saída do código. Métricas como precisão, recall, F1-score, e matrizes de confusão são mostradas para cada modelo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias no código, adição de novos algoritmos ou aprimoramento da documentação.

## Autores

- [Davi J Leite Santos](https://github.com/davijls9) - Desenvolvimento Completo.

## Licença

Este projeto é licenciado sob a licença [Nome da Licença] - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
