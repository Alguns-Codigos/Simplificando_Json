import streamlit.components.v1 as components
import time

def Digitacao_Html(frase, larg, aling, tenp):
    i = '{'
    ii = '}'
    n = larg
    c = 0

    estilo = f'''       
        <style>  
            @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'); 
        </style>    
        <style>   

         .animate {i}   
            font-family: "Press Start 2P", monospace;    
            border-right: 3px solid;
            letter-spacing: 3px;
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid;
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 3px;
            animation:
              typing {tenp}s steps(100),                     /* 10s velocidade */
              blink-caret .5s step-end infinite;            
            animation-fill-mode: forwards;                   /* adicionado */
            text-align: {aling};
          {ii}        
          @keyframes typing {i} 
            from {i} color: orange; width: 0; opacity: 5 ; border-right: 1px solid; {ii}
            to {i} color: blue; width: 100%; opacity: ; border-right: 10px solid; border-right-width: 0; {ii}   /* some com a barra */
          {ii}
          @keyframes blink-caret {i}
            from, to {i} border-color: transparent {ii}
            50% {i} border-color: orange {ii}
          {i}

        </style>
    '''

    while c < len(frase):
        linha = frase[c:c + n]

        if len(linha) == n and not linha.endswith(' '):
            j = linha.rfind(' ')
            if j > 0:
                linha = linha[:j]
            else:
                j = linha.find(' ')
                if j > 0:
                    linha = linha[:j]

        if '.' in linha:
            posicao_ponto = linha.rfind('.')
            if posicao_ponto > 0 and len(linha[posicao_ponto + 1:].strip()) > 0:
                linha = linha[:posicao_ponto + 1]

        components.html(f'{estilo}<p class="animate">{linha.strip()}</p>', height=50)
        c += len(linha)
        time.sleep(tenp / 2)

def Digitacao_Html2(frase, larg, aling, tenp):
    i = '{'
    ii = '}'
    n = larg
    c = 0

    estilo = f'''       
        <style>  
            @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'); 
        </style>    
        <style>   

         .animate {i}   
            font-family: "Press Start 2P", monospace;    
            border-right: 3px solid;
            letter-spacing: 3px;
            padding-bottom: 10px;
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid;            
            font-weight: bold;
            letter-spacing: 3px;
            animation:
              typing {tenp}s steps(100),                     /* 10s velocidade */
              blink-caret .5s step-end infinite;            
            animation-fill-mode: forwards;                   /* adicionado */
            text-align: {aling};
          {ii}        
          @keyframes typing {i} 
            from {i} color: orange; width: 0; opacity: 5 ; border-right: 1px solid; {ii}
            to {i} color: black; width: 100%; opacity: ; border-right: 10px solid; border-right-width: 0; {ii}   /* some com a barra */
          {ii}
          @keyframes blink-caret {i}
            from, to {i} border-color: transparent {ii}
            50% {i} border-color: orange {ii}
          {i}

        </style>
    '''

    while c < len(frase):
        linha = frase[c:c + n]

        if len(linha) == n and not linha.endswith(' '):
            j = linha.rfind(' ')
            if j > 0:
                linha = linha[:j]
            else:
                j = linha.find(' ')
                if j > 0:
                    linha = linha[:j]

        if '.' in linha:
            posicao_ponto = linha.rfind('.')
            if posicao_ponto > 0 and len(linha[posicao_ponto + 1:].strip()) > 0:
                linha = linha[:posicao_ponto + 1]

        components.html(f'{estilo}<p class="animate" style="font-size: 8px; padding-bottom: 10px;  ">{linha.strip()}</p>', height=25)
        c += len(linha)
        time.sleep(tenp / 2)
def Botao_Html(texto, link):
    return components.html(f'''
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            #meu-botao {{
                border: 2px dashed #000;
                border-radius: 5px;
                padding: 5px 10px;
                font-weight: bold;

    color: black;
                background-color: orange;
            }}

            #meu-botao:hover {{
                background-color: #C0C0C0;
                color: white;
                border-color: white;
            }}
        </style>
        <a href="{link}">
            <button id="meu-botao" style="padding: 15px; cursor: progress;  font-size: 16px;">{texto}</button>
        </a>
    ''', height=500)


def Texto_Link(texto, link, linha, op):
    i = '{'
    ii = '}'
    div = f'''
       <style>  
           @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'); 
       div {i}     
           font-size:15px;        
           border-radius: 10px; 
           padding-top: 10px;  
           height: 25px;
           width: 20vw;
           background-color: #E8E6E6;
           font-weight: lighter;
           padding-left: 10px; 

       {ii}
       a:hover {i} 
          color: orange;
        {i}
    </style> 
       '''
    return components.html(f'''   
                    {div} 
    <!-- 
    none: sem decoração de texto. 
    underline: adiciona uma linha sob o texto. 
    overline: adiciona uma linha acima do texto. 
    line-through: adiciona uma linha no meio do texto.
    ----------------------------------------------------
    "_self" (abre o link na mesma janela), 
    "_blank" (abre o link em uma nova janela do navegador), 
    "_parent" (abre o link na janela pai da janela atual), 
    "_top" (abre o link na janela principal). -->

    <div style="font-family: 'Press Start 2P', monospace; font-size: 13px;">    
    <a style="text-decoration:{linha};" target="{op}" href="{link}">{texto}↴</a>
</div> 

             ''', height=45)  # Altura


# Função para criar um texto decorado
def Texto_Decora(texto, larg):
    i = '{'
    ii = '}'
    div = f'''
       <style>  
           @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'); 
       div {i}     
           font-size:15px;        
           border-radius: 5px; 
           padding-top: 10px;  
           height: 25px;
           width: {larg}vw;
           color: orange; 
           background-color: #E8E6E6;
           font-weight: lighter;
           padding-left: 10px; 
           text-shadow: 0 0 3px black;                       
           -webkit-text-stroke-width: 5x;
           -webkit-text-stroke-color: black;
       {ii}
       </style> 
       '''
    return components.html(f'''   
                    {div} 

                    <div style="font-family: 'Press Start 2P', monospace; font-size: 13px;">{texto}↴</div>  

             ''', height=45)  # Altura


# Função para criar uma caixa decorada com texto e descrição
def Caixa_Decora(texto1, larg, texto2, larg2):
    i = '{'
    ii = '}'
    div = f'''
    <style>  
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'); 
    div {i}           
        border-radius: 5px;  
        padding-top: 10px; 
        height: 25px;
        width: {larg}vw;
        color: orange; 
        background-color: #E8E6E6;
        font-weight: lighter;
        padding-left: 10px; 
        text-shadow: 0 0 3px black;                       
        -webkit-text-stroke-width: 5x;
        -webkit-text-stroke-color: black;
    {ii}
    </style>  
    '''
    return components.html(f'''   
                {div} 
                <div style="font-family: 'Press Start 2P', monospace; font-size: 13px;">{texto1}↴</div>  
                <p style="font-family: 'Press Start 2P', monospace; font-size: 9px; padding-left: 10px; width: {larg2}vw; border: 1px dashed black; height: 15px; padding-top: 10px;background-color: white; ">{texto2}↴</p> 


''', height=90)  # Altura


# Definindo uma função chamada "Func_Texto_Cop" com quatro argumentos: txt, desc, LARG e TAM (opcional)
def Func_Texto_Cop(txt, desc, LARG, TAM=''):
    # Transformando o argumento "txt" em uma string e removendo algumas tags HTML
    TXt = str(txt).replace('<p>', '').replace('</p>', '').replace("--> ", '').replace("<br/>", '')

    # Criando uma lista vazia chamada "Tam"
    Tam = []

    # Verificando se o argumento TAM está vazio
    if TAM == '':
        # Verificando o tamanho do texto e adicionando um valor à lista "Tam" com base em seu tamanho
        if len(str(TXt)) < 99:
            Tam.append(200)
        if len(str(TXt)) > 100 and len(str(TXt)) < 300:
            Tam.append(250)
        if len(str(TXt)) > 100 and len(str(TXt)) < 199:
            Tam.append(250)
        if len(str(TXt)) > 500:
            Tam.append(500)
        else:
            Tam.append(len(str(TXt)))
    else:
        # Adicionando o valor do argumento TAM à lista "Tam"
        Tam.append(TAM)

    # Criando uma lista "larg" com um valor padrão de 90
    larg = [90]

    # Verificando se o argumento LARG não está vazio e adicionando seu valor à lista "larg"
    if LARG != '':
        larg.append(LARG)

    # Criando uma string HTML para exibir o texto
    Caixa_Text = f'''
          <head>
          <link href='https://fonts.googleapis.com/css?family=VT323' rel='stylesheet'>
          </head>
    <div style="background-color: white ;
        font-size:20px;
        width: {int(larg[-1])}vw;
        border-radius: 5px;
        padding: 10px;
        box-shadow:  0 0 0.1em black;
        font-family: 'VT323', monospace;
        height: auto;
        word-wrap: break-word;">
      <div id="texto">
      {txt}
      </div>

    '''

    # Criando uma string HTML para o estilo do botão de cópia de texto
    Estilo = '''#meu-botao {
               border-color: #000;
               background-color: #F8F8FF;
               border-radius: 5px; 
               padding: 5px 10px; 
               border: 2px dashed; 
               font-weight: bold;
           }

           #meu-botao:hover {
               background-color: #C0C0C0;
               color: white;
               border-color: white;

       }'''

    # Criando uma string JavaScript para copiar o texto para a área de transferência e alterar o botão
    Func_Copia_Troca_Nome = """
                       function copiarTexto() {
                  var texto = document.getElementById('texto').innerText;
                  navigator.clipboard.writeText(texto)
                    .then(() => {
                      alert('Texto copiado para a área de transferência.');
                      var botao = document.getElementById('meu-botao');
                      botao.innerHTML = '✔ Copiado';
                      botao.style.backgroundColor = '#C0C0C0';
                      botao.style.borderColor = 'black';
                      botao.style.color = 'blue';
                    })
                    .catch(() => {
                      alert('Não foi possível copiar o texto.');
                    });
                }

                var botao = document.getElementById('meu-botao');
                botao.addEventListener('click', copiarTexto);
                   """
    components.html(f"""
            <style>{Estilo}</style> 
            <button id="meu-botao" style="background-color: lightgray;" onclick="copiarTexto()"> 📃 Copiar Texto</button> {desc} 
            {Caixa_Text}
            <script>{Func_Copia_Troca_Nome}</script>

        """, scrolling=True, height=Tam[0] - 50)  # Altura
