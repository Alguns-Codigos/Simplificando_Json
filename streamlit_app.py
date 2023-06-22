import streamlit as st
import json
from Func_Html import *
# streamlit run streamlit_app.py


DIVISAO = '--------------------------'
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

def main():
    top, Top2 = st.columns([6, 4])
    code = top.text_area('Entrada', height=500)

    output = execute_code(code)
    # st.code(code, language='python')
    Top2.write('Saida:')
    Top2.code(output)
    Top2.success(output)

    resp = ''
    if st.button('Executar'):
        resp = output
    JASON = str(st.text_area('AQUIVO JSON():', resp)).replace("'", '"')
    Cop1, Cop2 = st.columns([5, 5])

    with Cop1:
        if JASON != '':

            json_objeto = json.loads(JASON)
            json_formatado = json.dumps(json_objeto, indent=4)
            st.code(json_formatado, language='json')

    with Cop2:
        if JASON != '':
            try:
                objeto_json = json.loads(JASON)
                imprimir_prefixos(objeto_json)
            except json.JSONDecodeError as e:
                st.error('Erro de decodificação JSON:', e.msg)
            st.write(sum(cont))
            cont.clear()
    if JASON != '':
        objeto_json = json.loads(JASON)
        imprimir_valores_prefixados(objeto_json)


if __name__ == '__main__':
    st.set_page_config(layout="wide")
    main()


