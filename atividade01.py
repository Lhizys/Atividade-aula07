import pandas as pd
import numpy as np

try:
    ENDERECO_DE_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencia = pd.read_csv(ENDERECO_DE_DADOS, sep=';', encoding='iso-8859-1')
    df_recuperacao_veiculos = df_ocorrencia [['cisp', 'recuperacao_veiculos']]
    df_recuperacao_veiculos = df_recuperacao_veiculos.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()
    #print(df_recuperacao_veiculos.head())
    #print('Dados obtidos com sucesso!')


except ImportError as e:
    print(f'Erro ao obter maiores e menores: {e}')
    exit()



try:
    array_recup_veiculo = np.array(df_recuperacao_veiculos['recuperacao_veiculos'])
    media = np.mean(array_recup_veiculo)
    mediana = np.median(array_recup_veiculo)
    distancia_media_mediana = (media - mediana) /mediana

    q1 = np.quantile(array_recup_veiculo, 0.25, method='weibull')
    q3 = np.quantile(array_recup_veiculo, 0.75, method='weibull')
    iqr =  q3 - q1
    minimo = np.min(array_recup_veiculo)
    limite_inferior = q1 - (1.5*iqr)
    limite_superior = q3 - (1,5*iqr)
    maximo = np.max(array_recup_veiculo)
    amplitude_total = maximo - minimo

    #print('\nMedidas de Posição e Disperção')
    #print(30*"=")
    #print(f'valor do q1: {q1}')
    #print(f'valor do q3: {q3}')
    #print(f'IQR: {iqr}')
    #print(f'Minimo: {minimo}')
    #print(f'Limite inferior: {limite_inferior}')
    #print(f'Maximo: {maximo}')
    #print(f'Limite superior: {limite_superior}')
    #print(f'Amplitude total é: {amplitude_total}')

    df_outliers_inf = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior]

    print('\nDPs com recuperção inferiores as demais:')
    print(30*"=")
    if len(df_outliers_inf) == 0:
        print('Não exitem DPs com valores discrepantes inferiores')
    else:
        print(df_outliers_inf.sort_values(by='recuperacao_veiculos', ascending=True))


except ImportError as e:
    print(f'Erro ao obter maiores e menores: {e}')
    exit()




