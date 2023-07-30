arquivo = float(input("Digite o tamanho do arquivo: "))

internet = float(input("Digite a velocidade de Internet: "))

megabytes = internet / 8

tempo_download = arquivo / megabytes / 60

print(f"Download: {tempo_download} minutos")