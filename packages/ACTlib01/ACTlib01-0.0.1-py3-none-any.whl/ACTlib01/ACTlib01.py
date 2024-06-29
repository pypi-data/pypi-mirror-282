import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image # Lib para carregar imagem 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import requests

from datetime import datetime
from datetime import date
import pytz

#Ref colors: https://hexcolorpedia.com/color/?q=ffffff

def Versao():
    return "ACTlib Versão 0.1"

def Indice():
    Configuracoes_de_Pagina = st.sidebar.popover("Configurações de Página")
    Configuracoes_de_Pagina.page_link("pages/Configurar_Pagina.py", label="	📄 Configurar_Pagina")
    Configuracoes_de_Pagina.page_link("pages/Barra_Lateral_Texto.py", label="⬜ Barra_Lateral_Texto")

def DataHora(TZ = 'America/Sao_Paulo'):
    datetime_br= datetime.now(pytz.timezone(TZ))
    DataHora.TZ = TZ
    DataHora.DH = datetime_br.strftime('%d/%m/%Y %H:%M:%S')
    DataHora.Data = datetime_br.strftime('%d/%m/%Y')
    DataHora.Hora = datetime_br.strftime('%H:%M:%S')
    # Obter dia, mês, ano e dia da semana separadamente
    dia_semana = datetime_br.strftime('%A')  # %A retorna o dia da semana completo
    DataHora.Dia = datetime_br.day
    DataHora.Mes = datetime_br.month
    DataHora.Ano = datetime_br.year
    # Mapear o número do dia da semana para o nome completo (em português)
    dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    DataHora.Nome_Dia_Semana = dias_semana[datetime_br.weekday()]
    return DataHora.DH

def Pt2En(palavraPT):
    tradutor = GoogleTranslator(source= "pt", target= "en")
    traducaoEN = tradutor.translate(palavraPT)
    return traducaoEN
    
def En2Pt(palavraEN):
    tradutor = GoogleTranslator(source= "en", target= "pt")
    traducaoPT = tradutor.translate(palavraEN)
    return traducaoPT
    
def Ler_GooglePlanilha(url, coluna_indice = None):
    r = requests.get(url)
    dataD = r.content
    dfD = pd.read_csv(BytesIO(dataD), index_col=coluna_indice)   
    return dfD

def Substituir_NAN(db, Coluna):
    return db[Coluna].fillna('', inplace=True)

#├──CONFIGURAÇÕES DE PÁGINA
#   └── Configurar_Pagina
#   └── Barra_Lateral_Texto
#   └── Barra_Lateral_Botao_M
#   └── Barra_Lateral_Botao_Colorido
#   └── Barra_Lateral_Container
#   └── Barra_Lateral_Divisor
#   └── Barra_Lateral_Imagem
#   └── Colunas
#   └── Eco
#   └── Container
#   └── Divisor
#   └── Expansor
#   └── Imagem
#   └── Link
#   └── Mudar_Tema

def Configurar_Pagina(titulo  = "ACT - Soluções para Pessoas", layout="amplo", barra_lateral = "auto", ajuda = "https://docs.streamlit.io", bug = "mailto:informacoes.actsp@gmail.com",sobre="#### **ACT - Soluções para Pessoas**. Você pode usar formatação Markdown para adicionar informações neste espaço. Para mais informações acesse *https://www.markdownguide.org*", icone = "	©️"):
    #https://docs.streamlit.io/develop/concepts/architecture/app-chrome
    Configurar_Pagina.titulo = titulo    
    if layout == "amplo":
        Configurar_Pagina.layout = "wide"
    elif layout == "centralizado":
        Configurar_Pagina.layout = "centered"
    else:
        Configurar_Pagina.layout = "wide"
        
    Configurar_Pagina.barra_lateral = barra_lateral
    Configurar_Pagina.icone = icone
    st.set_page_config(page_title=titulo,                        
                        layout = Configurar_Pagina.layout,
                        initial_sidebar_state = barra_lateral,
                        menu_items={
                            'Get Help': (ajuda),
                            'Report a bug': (bug),
                            'About': (sobre)
                        },
                        page_icon=icone)

def Barra_Lateral_Texto(texto = "Texto exibido na Barra Lateral", estilo = "auto"):
    Barra_Lateral_Texto.texto = texto
    Barra_Lateral_Texto.estilo = estilo
    if estilo.lower()=="auto":
        st.sidebar.write(texto)
    elif estilo.lower() =="codigo":
        st.code(texto)
    elif estilo.lower()=="subcabecalho":
        st.sidebar.subheader(texto)
    elif estilo.lower()=="cabecalho":
        st.sidebar.header(texto)
    elif estilo.lower()=="titulo":
        resp = st.title(texto)
    elif estilo.lower()=="destaque1":
        st.sidebar.info(texto)          
    elif estilo.lower()=="destaque2":
        st.sidebar.warning(texto) 
    elif estilo.lower()=="destaque3":
        st.sidebar.success(texto)
    elif estilo.lower()=="erroexc":
        e = RuntimeError(texto)
        st.sidebar.exception(e)
    elif estilo.lower()=="erro":
        st.sidebar.error(texto, icon="❌")
    else:
        st.sidebar.write(texto)
  
def Barra_Lateral_Botao(rotulo, chave = 1, info="", tipo="secundário", desabilitado="falso", expandido="falso"):
    Barra_Lateral_Botao.rotulo = rotulo
    
    if  desabilitado.lower()=="verdadeiro":
        des = True
    else:
        des = False
      
    if  expandido.lower()=="verdadeiro":
        exp = True
    else:
        exp = False
    respBTNbarra_lateral = st.sidebar.button(label=rotulo, key=chave, help=info, type=Pt2En(tipo), disabled=des, use_container_width=exp)
    Barra_Lateral_Botao.estado = respBTNbarra_lateral
    return respBTNbarra_lateral

def Barra_Lateral_Botao_Colorido(texto, cor = "#7e7b7b"):
    Botao_Colorido.rotulo = texto
    Botao_Colorido.cor = cor
    st.sidebar.markdown("""<style>  .element-container:has(style){display: none;} #button-afterL {display: none;}
                            .element-container:has(#button-afterL) {display: none;}
                            .element-container:has(#button-afterL) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.sidebar.markdown('<span id="button-afterL"></span>', unsafe_allow_html=True)
    respBTNColorL = st.sidebar.button(texto)
    return respBTNColorL
def Barra_Lateral_Container(borda = "ativa"):
    if borda == "desativa":
        Border = False
    else:
        Border = True
    return st.sidebar.container(border = Border)

def Barra_Lateral_Divisor():
    st.sidebar.divider()

def Barra_Lateral_Imagem(caminho='imgs/Webapp1.png', rotulo = None, dimensao=300, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto"):
    if preencher.lower() == "verdadeiro":
        preencher = True
    else:
        preencher = False
        
    if clamp.lower() == "verdadeiro":
        clamp = True
    else:
        clamp = False
        
    image = Image.open(caminho)
    st.sidebar.image(image, caption=rotulo, width=dimensao, use_column_width=preencher, channels=padrao_cor, output_format=formato_saida)

def Colunas(ncol):
    return st.columns(ncol)

def Eco():
    return st.echo()
    
def Container(borda = "ativa"):
    if borda == "desativa":
        Border = False
    else:
        Border = True
    return st.container(border = Border)
    
def Divisor():
    st.divider()

def Expansor(Titulo = "Título"):
    return st.expander(Titulo)

def Imagem(caminho='imgs/Webapp1.png', rotulo = None, dimensao=None, preencher="falso", clamp = "falso", padrao_cor="RGB", formato_saida = "auto"):
    if preencher.lower() == "verdadeiro":
        preencher = True
    else:
        preencher = False
        
    if clamp.lower() == "verdadeiro":
        clamp = True
    else:
        clamp = False
        
    image = Image.open(caminho)
    st.image(image, caption=rotulo, width=dimensao, use_column_width=preencher, channels=padrao_cor, output_format=formato_saida)

def Link(caminho, rotulo = "Link de Página"):
    Link.caminho = caminho
    Link.rotulo = rotulo
    st.page_link(caminho, label=rotulo)

def Mudar_Tema():
    #REF: https://discuss.streamlit.io/t/customize-theme/39156/4
    dark = '''
    <style>
        .stApp {
        background-color: black;  
        }
    </style>
    '''

    light = '''
    <style>
        .stApp {
        background-color: gray;
        }
    </style>
    '''
    st.markdown(light, unsafe_allow_html=True)

    # Create a toggle button
    toggle = st.button("Mudar Tema")

    # Use a global variable to store the current theme
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Change the theme based on the button state
    if toggle:
        if st.session_state.theme == "light":
            st.session_state.theme = "dark"
        else:
            st.session_state.theme = "light"

    # Apply the theme to the app
    if st.session_state.theme == "dark":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)

    # Display some text
    st.write("This is a streamlit app with a toggle button for themes.")

#├──BOTÕES
#   └── Botao_M
#   └── Botao_Colorido
def Botao(rotulo, chave = 1, info=None, tipo="secundário", desabilitado="falso", expandido="falso"):
    
    if  desabilitado.lower()=="verdadeiro":
        des = True
    else:
        des = False
      
    if  expandido.lower()=="verdadeiro":
        exp = True
    else:
        exp = False
    respBTNMono = st.button(label=rotulo, key=chave, help=info, type=Pt2En(tipo), disabled=des, use_container_width=exp)
    return respBTNMono
    
def Botao_Colorido(rotulo, cor = "#7e7b7b"):
    Botao_Colorido.cor = cor
    st.markdown("""<style>  .element-container:has(style){display: none;} #button-after {display: none;}
                            .element-container:has(#button-after) {display: none;}
                            .element-container:has(#button-after) + div button {background-color: %s;font-weight: bolder; color:black;}
                </style>"""%(Botao_Colorido.cor), unsafe_allow_html=True)
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    respBTNColor = st.button(rotulo)
    return respBTNColor
    
#├──RECURSOS DE ENTRADA
#   └── Ler
#   └──   

def Ler(rotulo = "", valor=None, nmax=None, chave=None, tipo="padrão", info=None, autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder=None, desabilitada="falso", visibilidade="visivel"):
    Ler.rotulo = rotulo
    Ler.valor = valor 
    Ler.nmax = nmax 
    Ler.chave = chave, 
    Ler.tipo = tipo 
    Ler.info = info
    Ler.autocompletar = autocompletar
    Ler.na_mudanca = na_mudanca
    Ler.desabilitada = desabilitada
    Ler.visibilidade = visibilidade
    #visibilidade: "visível", "oculto" ou "recolhido"
    if tipo.lower() == "senha":
        tipo = "password"
    else:
        tipo = "default"

    if desabilitada.lower() == "falso":
        desabilitada = False
    else:
        desabilitada = True
    
    if visibilidade.lower()=="oculto":
        visibilidade = "hidden"
    elif visibilidade.lower()=="recolhido":
        visibilidade = "collapsed"
    else:
        visibilidade = "visible"   

    return st.text_input(label = rotulo, value=valor, max_chars=nmax, key=chave, type=Pt2En(tipo), help=info, autocomplete=autocompletar, on_change=na_mudanca, args=args, kwargs=kwargs, placeholder=placeholder, disabled=desabilitada, label_visibility=visibilidade)
    
#├──RECURSOS DE SAÍDA
#   └── Escrever
#   └── Subcabecalho
#   └── Cabecalho
#   └── Texto_em_Coluna
#   └── Titulo
#   └── Exibir_Indicador
#   └── Exibir_Tabela
#   └── Grafico_Pizza
#   └── Grafico_Barra_Mono

def Escrever(texto, estilo = "auto"):
    Escrever.texto = texto
    Escrever.estilo = estilo
    if estilo.lower()=="auto":
        st.write(texto)
    elif estilo.lower() =="codigo":
        st.code(texto)
    elif estilo.lower()=="subcabecalho":
        st.subheader(texto)
    elif estilo.lower()=="cabecalho":
        st.header(texto)
    elif estilo.lower()=="titulo":
        resp = st.title(texto)
    elif estilo.lower()=="destaque1":
        st.info(texto)          
    elif estilo.lower()=="destaque2":
        st.warning(texto) 
    elif estilo.lower()=="destaque3":
        st.success(texto)
    elif estilo.lower()=="erroexc":
        e = RuntimeError(texto)
        st.exception(e)
    elif estilo.lower()=="erro":
        st.error(texto, icon="❌")
    else:
        st.write(texto)

def Subcabecalho(texto):
    Subcabecalho.texto = texto
    st.subheader(texto)

def Cabecalho(texto):
    Cabecalho.texto = texto
    st.header(texto)
    
def MKD(texto, alinhamento = "esquerda", tamanho_fonte = 28, cor_fonte = "preto"):
    if alinhamento.lower()=="justificado":
        alinhamento = "justified" 
    elif alinhamento.lower()=="esquerda":
        alinhamento = "left"
    elif alinhamento.lower()=="direita":
        alinhamento = "right"
    elif alinhamento.lower()=="centro":
        alinhamento = "center"
    elif alinhamento.lower()=="centralizado":
        alinhamento = "center"        
    else:
        alinhamento = "justified"
        
    conteudo = '<p style="font-weight: bolder; color:%s; font-size: %spx;">%s</p>'%(Pt2En(cor_fonte), tamanho_fonte, texto)    
    st.markdown(conteudo, unsafe_allow_html=True)
    mystyle0 = '''<style> p{text-align:%s;}</style>'''%(alinhamento)
    st.markdown(mystyle0, unsafe_allow_html=True) 
    

def Titulo(texto):
    Titulo.texto = texto
    st.title(texto)

def Exibir_Indicador(Rotulo = "Rotulo", Valor = 0.0, Variacao = 0.0, Unidade = " "):
    st.metric(label = Rotulo, value = str(Valor) + Unidade, delta = str(Variacao) + Unidade)

def Exibir_Tabela(Dados=None, 
                Largura = None, 
                Altura = None, 
                Esconder_Indice = None, 
                Ordenar_Coluna = None, 
                Configurar_Coluna=None, 
                Chave=None, 
                Na_Selecao='ignore', 
                Modo_Selecao='multi-row',
                Preencher_Container = False
                ):

    st.dataframe(Dados, 
                Largura, 
                Altura, 
                hide_index = Esconder_Indice, 
                column_order = Ordenar_Coluna, 
                column_config = Configurar_Coluna, 
                key = Chave, 
                on_select = Na_Selecao, 
                selection_mode = Modo_Selecao,
                use_container_width=Preencher_Container
                )

def Grafico_Pizza(Rotulos, Quantias, Legenda, posExplode, LocLEG, Larg = 16, Alt = 9, Titulo_Grafico = 'Título da Legenda', Titulo_legenda = 'Título da Legenda'):
    # Rotulos: etiquetamento dos dados
    # Quantias: dados numéricos referente a cada rótulo
    # Legenda: etiquetamento da legenda
    # posExplode: posição na qual se encontra a fatia da pizza que se deseja ressaltar (explodir)
    # LocLEG: Localização onde será posicionada a Legenda do Gráfico (Ref: https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/)

    #fig, ax = plt.subplots(figsize =(16, 9))
    fig, ax = plt.subplots(figsize =(Larg, Alt))
    explode = []
    for i in range(len(Rotulos)):
        if i !=posExplode:
            explode.append(0)
        else:
            explode.append(0.1)
    ax.pie(Quantias,
        explode=explode,
        labels=Legenda,
        autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title(Titulo_Grafico)
    
    ax.legend(title=Titulo_legenda,
            loc=LocLEG,
            bbox_to_anchor=(1, 0, 0.5, 1))
    #fig
    st.pyplot(fig)

def Grafico_Barra_Horizontal(Rotulos, Quantias, Legenda, Largura = 16, Altura = 9, Titulo_Grafico = 'Título do Gráfico', Titulo_x = 'Titulo do Eixo x', Titulo_y = 'Titulo do Eixo y'):
    if len(Rotulos)==15:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal', 'navy', 'gold']
    elif len(Rotulos)==14:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal', 'navy']
    elif len(Rotulos)==13:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime', 'teal']
    elif len(Rotulos)==12:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink', 'lime']
    elif len(Rotulos)==11:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown', 'pink']
    elif len(Rotulos)==10:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey', 'brown']
    elif len(Rotulos)==9:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'grey']
    elif len(Rotulos)==8:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
    elif len(Rotulos)==7:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta']
    elif len(Rotulos)==6:
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']
    elif len(Rotulos)==5:
        colors = ['red', 'green', 'blue', 'orange', 'purple']
    elif len(Rotulos)==4:
        colors = ['red', 'green', 'blue', 'orange']
    elif len(Rotulos)==3:
        colors = ['red', 'green', 'blue']
    elif len(Rotulos)==2:
        colors = ['red', 'green']
    elif len(Rotulos)==1:
        colors = ['black']
    else:
        colors = 'blue'

    # Criar o gráfico de barras horizontal
    fig, ax = plt.subplots(figsize =(Largura, Altura))
    bars = ax.barh(Rotulos, Quantias, color=colors)

    # Adicionar rótulos e título aos eixos
    ax.set_ylabel(Titulo_y)
    ax.set_xlabel(Titulo_x)
    ax.set_title(Titulo_Grafico)

    # Adicionar legenda
    ax.legend(bars, Rotulos)

    # Adicionar os valores ao lado das barras
    for bar, value in zip(bars, Quantias):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)