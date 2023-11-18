# Importações
from concurrent.futures import ThreadPoolExecutor
from sklearn.metrics import confusion_matrix
from itertools import combinations
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import dask.dataframe as dd
from scipy import stats
import seaborn as sns
import pandas as pd
import numpy as np
import datetime


import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="seaborn")

# Leitura do arquivo CSV em partes (chunks) para otimização de uso de memória
csv_file_path = 'C:\Projetos\TCC\DrDoS_UDP.csv'
dados = []

# Carregue seus dados (substitua 'seus_dados.csv' pelo nome do seu arquivo)
dados = pd.read_csv(csv_file_path, low_memory=False)

dados = pd.DataFrame(dados)
chunk_size = 1000
len(dados)
amostra = dados.sample(n=chunk_size, random_state=42)
dados.columns = dados.columns.str.strip()
amostra2 = dados[dados['Label'].str.contains('BENIGN')]

# Concatenar amostra e amostra2
dados_tr = pd.concat([amostra, amostra2])

# Redefinir o índice do DataFrame concatenado
dados_tr.reset_index(drop=True, inplace=True)

# Lista das colunas a serem selecionadas
colunas_selecionadas = ['Fwd Packet Length Std', 'Packet Length Std', 'Fwd IAT Mean', 'min_seg_size_forward',
                        'Fwd IAT Max', 'Destination Port', 'Fwd Packet Length Max', 'Fwd Packet Length Mean',
                        'Fwd Packet Length Min', 'Protocol', 'Timestamp', 'Label']

# Remova espaços em branco dos nomes das colunas
dados_tr.columns = dados_tr.columns.str.strip()


# Verifique se todas as colunas selecionadas estão no DataFrame
if set(colunas_selecionadas).issubset(dados_tr.columns):
    # Selecionar apenas as colunas desejadas
    df_dados = dados_tr[colunas_selecionadas]
    # Remover colunas duplicadas
    df_dados = df_dados.loc[:,~df_dados.columns.duplicated()]

    # Mostrar todas as colunas disponíveis no novo DataFrame
    print("Colunas Selecionadas:")
    print(df_dados.columns)
    print("\n")
    print(df_dados[df_dados.columns[0]])
else:
    print(dados_tr.columns)
    print(dados_tr)
    print("Nomes das colunas selecionadas não correspondem às colunas no DataFrame.")

# Ordenando pelo tempo
df_dados.loc[:,'Timestamp'] = pd.to_datetime(df_dados['Timestamp'], errors='coerce')
df_dados = df_dados.sort_values(by='Timestamp')

# Função para criar gráfico de série temporal de uma coluna
def sns_x(coluna, maior, menor):
    output = f"histplot_Density_{coluna.replace(' ', '_')}.png"
    plot = sns.histplot(data=df_dados, x=coluna, hue="Label", kde=True, stat="density", kde_kws=dict(cut=3))
    fig = plot.get_figure()
    
    # Salvar o gráfico
    fig.savefig(output)
    

def criar_sns_densidade(coluna, maior, menor):
    sns_x(coluna, maior, menor)
    
print("criar_sns_densidade")
criar_sns_densidade(colunas_selecionadas[0], maior=0, menor=100)
criar_sns_densidade(colunas_selecionadas[1], maior=0, menor=50)
criar_sns_densidade(colunas_selecionadas[2], maior=0, menor=70000)
#criar_sns_densidade(colunas_selecionadas[3], maior=0, menor=500)
criar_sns_densidade(colunas_selecionadas[4], maior=0, menor=150000)
criar_sns_densidade(colunas_selecionadas[5], maior=0, menor=80000)
criar_sns_densidade(colunas_selecionadas[6], maior=200, menor=550)
criar_sns_densidade(colunas_selecionadas[7], maior=250, menor=500)
criar_sns_densidade(colunas_selecionadas[8], maior=250, menor=500)
criar_sns_densidade(colunas_selecionadas[9], maior=15, menor=19)

# Função para criar gráfico de série temporal de uma coluna
def criar_sns_histograma(df, coluna, timestamp):
    output = f"histplot_timestamp_{coluna.replace(' ', '_')}.png"
    
    # Converter a coluna de data (timestamp) para representar apenas a diferença entre as datas
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['Timestamp_diff'] = (df['Timestamp'] - df['Timestamp'].min()).dt.total_seconds()
    
    # Remover entradas com valores NaN (datas fora do intervalo)
    df = df.dropna(subset=['Timestamp_diff'])
    
    plot = sns.histplot(data=df, y=coluna, x='Timestamp_diff', kde_kws=dict(cut=3), hue="Label")
    fig = plot.get_figure()
    fig.savefig(output)

print("criar_sns_histograma")
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[0], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[1], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[2], timestamp=colunas_selecionadas[10])
#criar_sns_histograma(df_dados, coluna=colunas_selecionadas[3], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[4], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[5], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[6], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[7], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[8], timestamp=colunas_selecionadas[10])
criar_sns_histograma(df_dados, coluna=colunas_selecionadas[9], timestamp=colunas_selecionadas[10])


# Função para criar gráfico de série temporal de uma coluna
def criar_sns_boxplot_timestamp(coluna, maior, menor):
    output = f"boxplot_{coluna.replace(' ', '_')}.png"
    plot = sns.boxplot(data=df_dados, x=coluna, y="Label")
    fig = plot.get_figure()
    fig.savefig(output)

print("criar_sns_boxplot_timestamp")
criar_sns_boxplot_timestamp(colunas_selecionadas[0], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[1], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[2], maior=-1.0, menor=80000.0)
#criar_sns_boxplot_timestamp(colunas_selecionadas[3], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[4], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[5], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[6], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[7], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[8], maior=-1.0, menor=80000.0)
criar_sns_boxplot_timestamp(colunas_selecionadas[9], maior=-1.0, menor=80000.0)


def plot_boxplot(ps1, ps2):
    # Crie os DataFrames a partir das colunas fornecidas
    dfs = []
    
    # Crie os DataFrames a partir das colunas fornecidas
    for coluna in colunas_selecionadas[ps1:ps2]:
        df = pd.DataFrame({'group': coluna, 'value': df_dados[coluna]})
        dfs.append(df)
    
    # Concatene os DataFrames usando a função concat
    df_teste = pd.concat(dfs)
    
    output = f"boxplot_comparaty_{colunas_selecionadas[ps1].replace(' ', '_')}_E_{colunas_selecionadas[ps2].replace(' ', '_')}.png"
    
    # Usual boxplot
    plot = sns.boxplot(data=df_teste, x='group', y='value')
    fig = plot.get_figure()
    fig.savefig(output)

print("plot_boxplot")
plot_boxplot(0,1)
plot_boxplot(1,2)
#plot_boxplot(2,3)
#plot_boxplot(3,4)
plot_boxplot(4,5)
plot_boxplot(5,6)
plot_boxplot(6,7)
plot_boxplot(7,8)
plot_boxplot(8,9)
#plot_boxplot(9,10)

def plot_violinplot(df, ps1, ps2):
    # Obtenha as colunas selecionadas com base em ps1 e ps2
    colunas_selecionadas = df.columns[ps1:ps2]

    # Crie os DataFrames a partir das colunas fornecidas
    dfs = []
    for coluna in colunas_selecionadas:
        df_temp = pd.DataFrame({'group': coluna, 'value': df[coluna]})
        dfs.append(df_temp)
    
    # Concatene os DataFrames usando a função concat
    df_teste = pd.concat(dfs)
    
    # Adicione um sufixo aos nomes das colunas "group"
    df_teste['group'] = df_teste['group'] + f'_{ps1}_to_{ps2}'
    
    output = f"violinplot_comparaty_{df.columns[ps1].replace(' ', '_')}_E_{df.columns[ps2 - 1].replace(' ', '_')}.png"
    
    # Usual boxplot
    plot = sns.violinplot(x='group', y='value', data=df_teste)
    fig = plot.get_figure()
    fig.savefig(output)

print("plot_violinplot")
plot_violinplot(df_dados, 0,2)
plot_violinplot(df_dados, 2,4)
plot_violinplot(df_dados, 4,6)
plot_violinplot(df_dados, 6,8)
plot_violinplot(df_dados, 8,10)

def plot_violinplo2(coluna):
    output = f"violinplot_{coluna.replace(' ', '_')}.png"
    plot = sns.violinplot(data=df_dados, x='Label', y=coluna)
    fig = plot.get_figure()
    fig.savefig(output)

print("plot_violinplo2")
plot_violinplo2(colunas_selecionadas[0])
plot_violinplo2(colunas_selecionadas[1])
plot_violinplo2(colunas_selecionadas[2])
#plot_violinplo2(colunas_selecionadas[3])
plot_violinplo2(colunas_selecionadas[4])
plot_violinplo2(colunas_selecionadas[5])
plot_violinplo2(colunas_selecionadas[6])
plot_violinplo2(colunas_selecionadas[7])
plot_violinplo2(colunas_selecionadas[8])
plot_violinplo2(colunas_selecionadas[9])


def criar_sns_marginal_distribution(df, coluna, coluna2):
    output = f"jointplot_{coluna.replace(' ', '_')}.png"
    plot = sns.jointplot(data=df, x=coluna, y=coluna2, kind="hist", hue="Label")
    fig = plot.get_figure()
    fig.savefig(output)

print("criar_sns_marginal_distribution")
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[0], 
                                coluna2=colunas_selecionadas[1])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[1], 
                                coluna2=colunas_selecionadas[2])
#criar_sns_marginal_distribution(df_dados,
#                                coluna=colunas_selecionadas[2], 
#                                coluna2=colunas_selecionadas[3])
#criar_sns_marginal_distribution(df_dados,
#                                coluna=colunas_selecionadas[3], 
#                                coluna2=colunas_selecionadas[4])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[4], 
                                coluna2=colunas_selecionadas[5])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[5], 
                                coluna2=colunas_selecionadas[6])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[6], 
                                coluna2=colunas_selecionadas[7])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[7], 
                                coluna2=colunas_selecionadas[8])
criar_sns_marginal_distribution(df_dados,
                                coluna=colunas_selecionadas[8], 
                                coluna2=colunas_selecionadas[9])

def criar_sns_pairplot(df, numero):
    output = f"pairplot_{numero}.png"
    plot = sns.pairplot(df, hue="Label", size=2.0)
    fig = plot.get_figure()
    fig.savefig(output)

# Lista das colunas a serem selecionadas 1
colunas_selecionadas1 = ['Fwd Packet Length Std', 'Packet Length Std', 'Fwd IAT Mean','min_seg_size_forward', 
                         'Fwd IAT Max','Timestamp','Label']

# Lista das colunas a serem selecionadas 2
colunas_selecionadas2 = ['Fwd Packet Length Std', 'Packet Length Std', 'Fwd IAT Mean','Destination Port',
                         'Fwd Packet Length Max', 'Fwd Packet Length Mean','Timestamp', 'Label']

# Lista das colunas a serem selecionadas 3
colunas_selecionadas3 = ['Fwd Packet Length Std', 'Packet Length Std', 'Fwd IAT Mean','Fwd Packet Length Min',
                         'Protocol','Timestamp', 'Label' ]

# Lista das colunas a serem selecionadas 4
colunas_selecionadas4 = ['min_seg_size_forward', 'Fwd IAT Max','Destination Port','Fwd Packet Length Max', 
                         'Fwd Packet Length Mean','Timestamp', 'Label']

# Lista das colunas a serem selecionadas 5
colunas_selecionadas5 = ['min_seg_size_forward','Fwd IAT Max', 'Fwd Packet Length Min','Protocol','Timestamp', 
                         'Label' ]

# Lista das colunas a serem selecionadas 6
colunas_selecionadas6 = ['Fwd Packet Length Min','Protocol','Destination Port','Fwd Packet Length Max', 
                         'Fwd Packet Length Mean','Timestamp', 'Label']

# Selecionar apenas as colunas desejadas
df_dados1 = df_dados[colunas_selecionadas1]
df_dados2 = df_dados[colunas_selecionadas2]
df_dados3 = df_dados[colunas_selecionadas3]
df_dados4 = df_dados[colunas_selecionadas4]
df_dados5 = df_dados[colunas_selecionadas5]
df_dados6 = df_dados[colunas_selecionadas6]

print("criar_sns_pairplot")
criar_sns_pairplot(df_dados1, 1)
criar_sns_pairplot(df_dados2, 2)
criar_sns_pairplot(df_dados3, 3)
criar_sns_pairplot(df_dados4, 4)
criar_sns_pairplot(df_dados5, 5)
criar_sns_pairplot(df_dados6, 6)