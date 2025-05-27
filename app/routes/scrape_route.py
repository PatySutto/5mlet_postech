from flask import Flask, jsonify, request, redirect, render_template_string, url_for
from app.services.GetEmbrapaData import GetEmbrapaData
from app import app


@app.route('/get_production_data', methods=['GET'])
def get_production_data():
    """
    Obtém dados de produção de uva da Embrapa.
    ---
    parameters:
      - name: ano
        in: query
        type: number
        required: true
    
    responses:
      200:
        description: Dados de produção de uva
        schema:
          type: object
          properties:
            categoria:
              type: object
              description: Dicionário com os dados da categoria e seus subitens
            total:
              type: number
              description: Total da categoria
            ano:
              type: number
              description: Ano da coleta dos dados
      500:
        description: Internal Server Error. Erro inesperado 

      502:
        description: 502 Bad Gateway. Falhas na comunicação com serviços.
    """
    ano = float(request.args.get("ano", 0))

    # Chamada da função que obtém os dados da Embrapa
    dados = GetEmbrapaData().get_production_data(ano)

    if 'erro' in dados:
        if dados['erro'] == "Erro na requisição HTTP: 502 Bad Gateway":
            return jsonify({"erro": "502 Bad Gateway. Falhas na comunicação com serviços."}), 502
        else:
            return jsonify({"erro": "Erro inesperado"}), 500
      
    return jsonify(dados)

@app.route('/get_processing_data', methods=['GET'])
def get_processing_data():
    """
    Obtém dados de processamento de uva da Embrapa.
    ---
    parameters:
      - name: ano
        in: query
        type: number
        required: true
      - name: opcao
        in: query
        type: string
        required: true
        enum: ['Viníferas', 'Americanas e híbridas', 'Uvas de mesa', 'Sem classificação']
    
    responses:
        200:
          description: Dados de processamento de uva
          schema:
            type: object
            properties:
              categoria:
                type: object
                description: Dicionário com os dados da categoria e seus subitens
              total:
                type: number
                description: Total da categoria
              ano:
                type: number
                description: Ano da coleta dos dados
        500:
          description: Internal Server Error. Erro inesperado 

        502:
          description: 502 Bad Gateway. Falhas na comunicação com serviços.
    """
    ano = float(request.args.get("ano", 0))
    opcao = request.args.get("opcao", "")

    # Chamada da função que obtém os dados da Embrapa
    dados = GetEmbrapaData().get_processing_data(ano, opcao)

    if 'erro' in dados:
        if dados['erro'] == "Erro na requisição HTTP: 502 Bad Gateway":
            return jsonify({"erro": "502 Bad Gateway. Falhas na comunicação com serviços."}), 502
        else:
            return jsonify({"erro": "Erro inesperado"}), 500
      
    return jsonify(dados)
   
@app.route('/get_commercialization_data', methods=['GET'])
def get_commercialization_data():
    """
    Obtém dados de comercialização de uva da Embrapa.
    ---
    parameters:
      - name: ano
        in: query
        type: number
        required: true
    
    responses:
      200:
        description: Dados de comercialização de uva
        schema:
          type: object
          properties:
            categoria:
              type: object
              description: Dicionário com os dados da categoria e seus subitens
            total:
              type: number
              description: Total da categoria
            ano:
              type: number
              description: Ano da coleta dos dados
      500:
        description: Internal Server Error. Erro inesperado 

      502:
        description: 502 Bad Gateway. Falhas na comunicação com serviços.
    """
    ano = float(request.args.get("ano", 0))

    # Chamada da função que obtém os dados da Embrapa
    dados = GetEmbrapaData().get_commercialization_data(ano)

    if 'erro' in dados:
        if dados['erro'] == "Erro na requisição HTTP: 502 Bad Gateway":
            return jsonify({"erro": "502 Bad Gateway. Falhas na comunicação com serviços."}), 502
        else:
            return jsonify({"erro": f"Erro inesperado {dados}"}), 500
      
    return jsonify(dados)

@app.route('/get_importation_data', methods=['GET'])
def get_importation_data():
    """
    Obtém dados de importação de uva da Embrapa.
    ---
    parameters:
      - name: ano
        in: query
        type: number
        required: true
      - name: opcao
        in: query
        type: string
        required: true
        enum: ['Vinhos de mesa', 'Espumantes', 'Uvas frescas', 'Uvas passas', 'Suco de uva']
    
    responses:
        200:
          description: Dados de importação de uva
          schema:
            type: array
            items:
              type: object
            example:
              - pais: "Argentina"
                quantidade: 123
                ano: 2023
             
        500:
          description: Internal Server Error. Erro inesperado 

        502:
          description: 502 Bad Gateway. Falhas na comunicação com serviços.
    """
    ano = float(request.args.get("ano", 0))
    opcao = request.args.get("opcao", "")

    # Chamada da função que obtém os dados da Embrapa
    dados = GetEmbrapaData().get_importation_data(ano, opcao)

    if 'erro' in dados:
        if dados['erro'] == "Erro na requisição HTTP: 502 Bad Gateway":
            return jsonify({"erro": "502 Bad Gateway. Falhas na comunicação com serviços."}), 502
        else:
            return jsonify({"erro": f"Erro inesperado {dados}"}), 500
      
    return jsonify(dados)


@app.route('/get_exportation_data', methods=['GET'])
def get_exportation_data():
    """
    Obtém dados de exportação de uva da Embrapa.
    ---
    parameters:
      - name: ano
        in: query
        type: number
        required: true
      - name: opcao
        in: query
        type: string
        required: true
        enum: ['Vinhos de mesa', 'Espumantes', 'Uvas frescas', 'Suco de uva']
    
    responses:
        200:
          description: Dados de exportação de uva
          schema:
            type: array
            items:
              type: object
            example:
              - pais: "Argentina"
                quantidade: 123
                ano: 2023
             
        500:
          description: Internal Server Error. Erro inesperado 

        502:
          description: 502 Bad Gateway. Falhas na comunicação com serviços.
    """
    ano = float(request.args.get("ano", 0))
    opcao = request.args.get("opcao", "")

    # Chamada da função que obtém os dados da Embrapa
    dados = GetEmbrapaData().get_exportation_data(ano, opcao)

    if 'erro' in dados:
        if dados['erro'] == "Erro na requisição HTTP: 502 Bad Gateway":
            return jsonify({"erro": "502 Bad Gateway. Falhas na comunicação com serviços."}), 502
        else:
            return jsonify({"erro": f"Erro inesperado {dados}"}), 500
      
    return jsonify(dados)
