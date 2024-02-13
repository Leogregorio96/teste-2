from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/leo-gregorio', methods=['POST'])
def meu_endpoint():
    # Verifica se o corpo da solicitação contém JSON
    if request.is_json:
        # Obtém o JSON enviado na solicitação
        dados_recebidos = request.get_json()
        
        # Aqui você pode trabalhar com os dados_recebidos, que é um dicionário Python
        print(dados_recebidos)  # Isso imprimirá os dados no console

        # Você pode acessar valores específicos usando a chave correspondente
        valor1 = dados_recebidos.get('chave1', 'padrão se chave1 não existir')
        print(valor1)  # Isso imprimirá o valor associado à 'chave1' no console

        # Aqui você pode processar os dados como necessário
        # ...

        # E depois você pode retornar uma resposta
        resposta = {"mensagem": "Dados recebidos com sucesso!", "seusDados": dados_recebidos}
        return jsonify(resposta), 200
    else:
        return jsonify({"erro": "Corpo da solicitação não é JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)


