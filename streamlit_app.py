import streamlit as st
import json

# streamlit run streamlit_app.py


DIVISAO = '# --------------------------'
cont = []
def imprimir_prefixos(objeto_json, prefixo=""):
    if isinstance(objeto_json, dict):
        for chave, valor in objeto_json.items():
            if isinstance(valor, dict):
                imprimir_prefixos(valor, prefixo + chave + ".")
            else:
                st.write('Corpo.' + prefixo + chave," --> ",valor)
                cont.append(1)


def exibir_chaves(objeto_json, prefixo=""):
    if isinstance(objeto_json, dict):
        for chave, valor in objeto_json.items():
            chave_completa = f"{prefixo}.{chave}" if prefixo else chave
            st.write(chave_completa)
            exibir_chaves(valor, chave_completa)
            st.success(valor)
            cont.append(1)
    elif isinstance(objeto_json, list):
        for indice, item in enumerate(objeto_json):
            chave_completa = f"{prefixo}[{indice}]"
            st.write(chave_completa)
            exibir_chaves(item, chave_completa)
            cont.append(1)
            st.success(indice)
        st.code(f"{prefixo}: {len(objeto_json)} itens")


def imprimir_valores_prefixados(objeto_json, prefixo=""):
    if isinstance(objeto_json, dict):
        for chave, valor in objeto_json.items():
            chave_completa = f"{prefixo}.{chave}" if prefixo else chave
            if isinstance(valor, dict):
                st.write('')
                st.text(f"{DIVISAO} {chave_completa}")
                imprimir_valores_prefixados(valor, chave_completa)
            elif isinstance(valor, list):
                st.write('')
                st.text(f"{DIVISAO} {chave_completa}")
                for indice, item in enumerate(valor):
                    item_prefixo = f"{chave_completa}[{indice}]"
                    imprimir_valores_prefixados(item, item_prefixo)
            else:
                st.text(f"{chave_completa}: {valor}")
    elif isinstance(objeto_json, list):
        for indice, item in enumerate(objeto_json):
            chave_completa = f"{prefixo}[{indice}]"
            st.write('')
            st.text(f"{DIVISAO} {chave_completa}")
            imprimir_valores_prefixados(item, chave_completa)
    else:
        st.text(f"{prefixo}: {objeto_json}")

caixa = []
printe = []
printe_caixa = []

def Valores_Consumo(objeto_json, prefixo=""):
    if isinstance(objeto_json, dict):
        for chave, valor in objeto_json.items():


            if prefixo:
                chave_completa = f''' {prefixo+'_'+chave} = Json_[{'"'+prefixo+'"'}][{'"'+chave+'"'}]'''
            else:
                chave_completa = chave
            if isinstance(valor, dict):
                if '=' in chave_completa:
                    caixa.append(f"*|*")
                    caixa.append(f"{DIVISAO} {chave_completa.split('=')[0]}")
                    Valores_Consumo(valor, chave_completa.split('=')[0])
                else:
                    caixa.append(f"*|*")
                    caixa.append(f"{DIVISAO} {chave_completa}")
                    Valores_Consumo(valor, chave_completa)

            elif isinstance(valor, list):
                if '=' in chave_completa:
                    caixa.append(f"*|*")
                    caixa.append(f"{DIVISAO} {chave_completa.split('=')[0]}")
                    for indice, item in enumerate(valor):
                        item_prefixo = f"{chave_completa.split('=')[0]}|{indice}/"
                        Valores_Consumo(item, item_prefixo)

                else:
                    caixa.append(f"*|*")
                    caixa.append(f"{DIVISAO} {chave_completa}")
                    for indice, item in enumerate(valor):
                        item_prefixo = f"{chave_completa}|{indice}/"
                        Valores_Consumo(item, item_prefixo)

            else:
                if '=' in chave_completa:
                    if '|' in chave_completa and '/' in chave_completa:
                        CHAVE = f'''{(chave_completa).replace("*|- ",'_').replace('/"]["', ']["').replace('|', '"][')}'''.strip()\
                            .replace('"][1/_', '_').replace('"][0/_', '_').replace('"][2/_', '_').replace('"][3/_', '_').replace(' _','_')
                        caixa.append(CHAVE)
                        printe.append(f'''print("{(CHAVE.split(' =')[0]).upper()}: ",{(CHAVE.split(' =')[0])})''')
                        printe_caixa.append(f'''print("{(CHAVE.split(' =')[0]).upper()}: ",{(CHAVE.split(' =')[1])})''')
                    else:
                        CHAVE = f'''{chave_completa.replace(' _','_')}''' .strip()
                        caixa.append(f'''{CHAVE}''' .strip())
                        printe.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[0]})''')
                        printe_caixa.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[1]})''')
                else:
                    if '|' in chave_completa and '/' in chave_completa:
                        CHAVE = f'''{(chave_completa).replace("*|- ", '_').replace('/"]["', ']["').replace('|', '"][')}'''.strip() \
                            .replace('"][1/_', '_').replace('"][0/_', '_').replace('"][2/_', '_').replace('"][3/_', '_').replace(' _','_')
                        caixa.append(CHAVE)
                        printe.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[0]})''')
                        printe_caixa.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[1]})''')

                    else:
                        CHAVE = f'''{chave_completa.replace(' _','_')} = Json_[{'"'+chave_completa+'"'}]'''.strip()
                        caixa.append(CHAVE)
                        printe.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[0]})''')
                        printe_caixa.append(f'''print("{(CHAVE.split(' =')[0]).upper()}:",{CHAVE.split(' =')[1]})''')



    elif isinstance(objeto_json, list):
        for indice, item in enumerate(objeto_json):
            chave_completa = f'''{prefixo}|{indice}/'''

            st.text(f"{DIVISAO} {chave_completa}")
            Valores_Consumo(item, chave_completa)

    else:
        st.code(f"{prefixo}: {objeto_json}")

from contextlib import redirect_stdout

import io

def execute_code(code):
    # Cria um objeto de buffer para capturar a saída
    buffer = io.StringIO()

    try:
        # Redireciona a saída padrão para o objeto de buffer
        with redirect_stdout(buffer):
            # Executa o código fornecido
            exec(code, globals())
    except Exception as e:
        # Captura e exibe erros
        buffer.write(str(e))

    # Obtém a saída capturada
    output = buffer.getvalue()
    return output

def Titulo(texto):
    html = f'''
            <font color="white">
            <div style="background-color: black; padding: 10px; text-align: center;">
                <strong> {texto}</strong>
            </div>
            </font>'''
    return st.markdown(html, unsafe_allow_html=True)
def main():
    Titulo('Editor de Código Símples')
    top, Top2 = st.columns([6, 4])
    code = top.text_area('Escreva seu código:', height=500)

    output = execute_code(code)
    # st.code(code, language='python')
    Top2.write('Retorno do Código:')
    Top2.code(output)
    Top2.success(output)

    resp = ''
    if st.button('Executar'):
        resp = output
    JASON = str(st.text_area('AQUIVO JSON():', resp)).replace("'", '"')
    Cop1, Cop2 = st.columns([5, 5])

    with Cop1:
        if JASON != '':
            Titulo('Json Saida')
            json_objeto = json.loads(JASON)
            json_formatado = json.dumps(json_objeto, indent=4)
            st.code(json_formatado, language='json')
            Titulo('Print Variaveis')
            objeto_json = json.loads(JASON)
            Valores_Consumo(objeto_json)
            st.code('\n'.join(printe).strip())
    with Cop2:
        if JASON != '':
            Titulo('Todas as Variaveis')

            objeto_json = json.loads(JASON)
            Valores_Consumo(objeto_json)
            st.code('\n'.join(caixa).replace("*|*", '\n').strip())
            Titulo('Print Completo')
            st.code('''data = response.json()  # Obtenha os dados JSON da resposta
# Exiba os dados corretamente
for item in data:
    print(item)
    Json_ = json.loads(item)''')
            st.code('\n'.join(printe_caixa).strip())
    '''-----'''
    Cop1, Cop2 = st.columns([5, 5])

    if JASON != '':
        with Cop1:
            Titulo('Linha Unica')
            objeto_json = json.loads(JASON)
            imprimir_valores_prefixados(objeto_json)
        with Cop2:
            Titulo('Interativa')
            try:
                objeto_json = json.loads(JASON)
                imprimir_prefixos(objeto_json)
            except json.JSONDecodeError as e:
                st.error('Erro de decodificação JSON:', e.msg)
            st.write(sum(cont))
            cont.clear()

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    main()




