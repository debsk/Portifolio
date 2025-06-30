import streamlit as st

# Configuração da página principal
st.set_page_config(page_title="Portfólio - Débora Ferreira", layout="wide", page_icon="💼")

# Menu lateral com as seções
menu = st.sidebar.radio("📂 Seções do Portfólio", [
    "👋 Apresentação",
    "🌐 Sistemas de Informação (MXM)",
    "📑 Geração de Relatórios (Excel → Word)",
    "📊 Excel para .TXT (TransformaX)",
    "🔐 Gerador de Senhas",
    "⚙️ Automação com Plataforma No-Code",
    "🧭 Revisão de ERP",
    "📊 Projeto Cxodiugo - LSTM + MT5",
    "🎬 Edição de Vídeos",
    "📫 Contato"
])

# SEÇÃO 1 - Apresentação
if menu == "👋 Apresentação":
    col1, col2 = st.columns([2, 4])

    with col1:
        st.image("image.png", width=350, caption="Débora Ferreira")

    with col2:
        st.markdown("""
                Olá! Meu nome é **Débora Ferreira** e este é meu portfólio de projetos desenvolvidos.  
                Tenho experiência em **tecnologia, automação, análise de dados e criação de soluções práticas** com ferramentas como Python, Streamlit, Excel e plataformas no-code.

                ---

                ### 👩‍💻 Sobre Mim
                - 🎓 Graduanda em **Sistemas de Informação** pela Universidade Federal Fluminense (UFF)  
                - 💼 Experiência em QA, Backend Python, automação de tarefas e gestão de projetos  
                - 🤝 Colaborei em empresas como **MXM**, **Storm Group** e **IN Jr - UFF**  
                - 🧪 Também atuei em projeto de Iniciação Científica com **desenvolvimento mobile em Dart**

                ---

                ### 💼 Experiência Resumida

                **MXM (2023 – atual)**  
                *Analista de Testes – QA*  
                Testes e automação com Python em sistemas ERP

                **Storm Group (2021 – 2023)**  
                *Desenvolvedora Backend Python*  
                Chalice, testes BDD, S3, Git, Clean Architecture, SOLID, CRUDs

                **IN Jr – UFF (2020 – 2021)**  
                *Backend Ruby & RH*  
                CRUDs, gestão de times, recrutamento e acompanhamento de projetos

                **Projeto IC – UFF (2019)**  
                *Desenvolvedora Dart*  
                App para cálculo de dosagens médicas usado por enfermeiros do HU

                ---

                ### 🧩 Projetos em Destaque
                - 🌐 Apresentação Interativa sobre **Sistemas de Informação**
                - 🔄 Transformação de dados com Excel (.xlsx → .txt)
                - 📑 Geração automática de **relatórios a partir de planilhas**
                - 🔐 Gerador de **senhas seguras** com critérios personalizados
                - ⚙️ Automação de tarefas com ferramentas **No-Code**
                - 🧭 Revisão de telas e módulos ERP para **otimização de processos**
                - 📊 Projeto Cxodiugo – LSTM + Simulação MT5 (Google Colab)
                - 🎥 Edição e produção de vídeos

                ---

                Sinta-se à vontade para explorar cada projeto usando o menu lateral! 👈
                """)


# SEÇÃO 2 - Projeto MXM Sistemas
elif menu == "🌐 Sistemas de Informação (MXM)":
    st.title("🔷 Projeto Acadêmico: MXM Sistemas")
    st.markdown("Este projeto foi desenvolvido como parte de um trabalho acadêmico sobre Sistemas de Informação.")
    st.markdown("➡️ O conteúdo completo da apresentação está [aqui](https://mxm-apresentacao-jhg2aotnt9xbqptnk2vmqe.streamlit.app/) ou confira abaixo:")

    # Você pode colar aqui a mesma estrutura que usou no seu app da MXM (como você já fez)
    st.markdown("Usei **Streamlit, Matplotlib e Plotly** para tornar o conteúdo mais interativo.")
    st.markdown("> **Tópicos abordados:** Introdução a SI, tipos de sistemas, modelo de negócio da MXM, Forças de Porter, soluções tecnológicas e localização das sedes.")

# SEÇÃO 3 - Geração de Relatórios (Excel → Word)
elif menu == "📑 Geração de Relatórios (Excel → Word)":
    st.header("📑 Geração de Relatórios a partir de Excel")
    st.markdown("""
        Esse projeto permite gerar relatórios automáticos em formato `.docx` com base em dados de uma planilha do Excel.

        **Principais funcionalidades:**
        - 📊 Leitura e processamento de dados em Excel
        - 🧾 Geração de relatórios personalizados em Word com Python
        - 🧠 Uso da biblioteca `python-docx` para formatação dos documentos
        - 💡 Ideal para automatizar relatórios mensais, contratos, certificados, etc.

        **Exemplo de uso:**  
        Uma planilha com informações de clientes pode gerar automaticamente um contrato em Word para cada um, poupando horas de trabalho manual.

        🔗 [Ver projeto no GitHub](https://github.com/seu-usuario/seu-repositorio)  
        📄 [Baixar modelo de relatório Word](https://drive.google.com/file/d/SEU_ID_AQUI/view?usp=sharing)
        """)

# SEÇÃO 4 - Excel para TXT (TransformaX)
elif menu == "📊 Excel para .TXT (TransformaX)":
    st.title("📊 TransformaX - Conversor de Excel para .TXT")
    st.markdown("""
    Este projeto automatiza a conversão de arquivos Excel para o formato `.txt`, muito útil em sistemas que exigem layouts específicos para integração (como fiscais ou contábeis).

    **Principais Funcionalidades:**
    - 📥 Upload de arquivos `.xlsx`
    - 📄 Escolha de colunas específicas
    - 🔁 Formatação automatizada do conteúdo
    - 📤 Geração de arquivo `.txt` pronto para envio

    🛠️ Desenvolvido com: `pandas`, `openpyxl`, `Python padrão`
    🔗 [Ver projeto no GitHub](https://github.com/seu-usuario/seu-repositorio)  

    """)

    st.code("""
        import pandas as pd

        df = pd.read_excel('dados.xlsx')
        df.to_csv('saida.txt', sep='|', index=False)
            """, language="python")

# SEÇÃO 5 - Gerador de Senhas
elif menu == "🔐 Gerador de Senhas":
    st.title("🔐 Gerador de Senhas Seguras")
    st.markdown("""
    Ferramenta simples e útil para gerar senhas aleatórias com critérios de segurança.

    **Características:**
    - Geração com letras, números e símbolos
    - Personalização de tamanho
    - Fácil cópia para área de transferência

    🛠️ Feito com `Python` e `random`
    🔗 [Ver projeto no GitHub](https://github.com/seu-usuario/seu-repositorio)  

    """)

    st.code("""
        import random
        import string

        def gerar_senha(tamanho=12):
            chars = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(chars) for _ in range(tamanho))
            """, language="python")

# SEÇÃO 6 - Automação com No-Code
elif menu == "⚙️ Automação com Plataforma No-Code":
    st.title("⚙️ Automação com Plataforma No-Code")
    st.markdown("""
    Automatizei tarefas repetitivas usando uma plataforma no-code, como o **Make (Integromat)** ou **Zapier**.

    **Exemplo de processo automatizado:**
    - Receber formulário do cliente
    - Criar tarefa em ferramenta de gestão
    - Notificar equipe via Slack/Email

    **Impacto:**
    - Economia de tempo
    - Redução de erros
    - Padronização de processos

    🧩 Usei lógica condicional, webhooks e integração com APIs.
    🔗 [Ver projeto no GitHub](https://github.com/seu-usuario/seu-repositorio)  

    """)

# SEÇÃO 7 - Revisão de ERP
elif menu == "🧭 Revisão de ERP":
    st.header("🧭 Revisão de Telas e Módulos de ERP")
    st.markdown("""
    Projeto focado na **análise de usabilidade e fluxo de módulos de um sistema ERP**.

    Atividades realizadas:
    - Mapeamento das telas utilizadas em cada área do ERP (financeiro, estoque, RH, etc.)
    - Análise crítica de **layout, agrupamento de informações e redundâncias**
    - Propostas de melhoria de navegação e UX
    - Sugestões de **padronização visual entre os módulos**

    O objetivo foi melhorar a **eficiência dos usuários** no uso diário do sistema e otimizar o tempo de operação.

    Ferramentas utilizadas:
    - Inspeção visual e testes manuais no sistema
    - Documentação de fluxo com diagramas (Ex: Draw.io, Figma)
    """)

# SEÇÃO 8 - Edição de Vídeos
elif menu == "🎬 Edição de Vídeos":
    st.title("🎬 Projetos de Edição de Vídeo")
    st.markdown("""
    Além de projetos técnicos, também atuo na edição de vídeos, criando conteúdos para redes sociais, apresentações e vídeos institucionais.

    **Softwares usados:**
    - 🎞️ CapCut
    - 🎬 Adobe Premiere
    - 🧠 IA para voz/sincronização (opcional)

    👉 Confira alguns dos meus vídeos:
    - [Vídeo 1 - Produto](https://youtu.be/03qPtQGD3OU)
    - [Vídeo 2 - Reels](https://www.youtube.com/shorts/GLjBNQwqYPk)
    """)


# SEÇÃO 9 - Projeto Cxodiugo com Google Colab
elif menu == "📊 Projeto Cxodiugo - LSTM + MT5":
    st.title("📊 Projeto Cxodiugo - Análise com LSTM + Simulação MT5 (Google Colab)")
    st.markdown("""
    Este projeto é uma simulação de coleta e análise de dados de mercado inspirada no MetaTrader 5 (MT5),  
    com um modelo de previsão usando **LSTM com Attention**, desenvolvido inteiramente em **Google Colab**.

    O notebook permite:
    - 📈 **Simular dados de mercado como se fossem coletados via MT5**
    - ⚙️ **Treinar um modelo de séries temporais (LSTM com Attention)**
    - 🧠 Utilizar bibliotecas como `TensorFlow`, `pandas`, `seaborn`, `matplotlib` para análise
    - ✅ Rodar tudo direto no navegador, sem instalação local

    **Destaques técnicos:**
    - Uso de `LSTM` para prever séries temporais financeiras
    - Aplicação de mecanismo de **Attention** para identificar padrões importantes
    - Dados simulados para contornar limitações de execução do MT5 no Colab

    🔗 [Abrir projeto no Google Colab](https://colab.research.google.com/drive/17BIPMJTm66GNmQbEmUFrATaa7vth2foS#scrollTo=FfghqukOGU-s)  

    ---
    #### ⚙️ Instalação de dependências (automática no Colab):
    ```bash
    !pip install pandas numpy matplotlib seaborn tensorflow
    ```

    ---
    💬 *Este projeto demonstra como aplicar Deep Learning para análise financeira mesmo em ambientes limitados como o Colab.*
    """)

# SEÇÃO 10 - Contato
elif menu == "📫 Contato":
    st.title("📫 Fale comigo")
    st.markdown("""
    Ficou interessado em algum projeto? Quer conversar sobre uma ideia?

    - 📧 **Email**: deborabf@id.uff.br  
    - 💼 [LinkedIn](https://www.linkedin.com/in/débora-barbosa-1a0179193)  
    - 🧑‍💻 [GitHub](https://github.com/debsk)

    Obrigado pela visita! 👋
    """)