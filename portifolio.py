import streamlit as st


st.set_page_config(
    page_title="Portfolio - Débora Ferreira",
    page_icon="✨",
    layout="wide",
)


PROJECTS = [
    {
        "icon": "🌐",
        "title": "Apresentação MXM Sistemas",
        "subtitle": "Trabalho acadêmico interativo com Streamlit",
        "stack": "Streamlit | Plotly | Matplotlib",
        "impact": "Conecta teoria de SI com análise de negócio e visualização de dados.",
        "link": "https://mxm-apresentacao-jhg2aotnt9xbqptnk2vmqe.streamlit.app/",
    },
    {
        "icon": "📑",
        "title": "Geração de Relatórios",
        "subtitle": "Excel para Word automatizado",
        "stack": "Python | python-docx | pandas",
        "impact": "Reduz tempo manual na criação de contratos, laudos e relatórios.",
        "link": "https://github.com/debsk/Gera-o-de-Relat-rios-Excel-Word-",
    },
    {
        "icon": "📊",
        "title": "TransformaX",
        "subtitle": "Conversor de .xlsx para .txt",
        "stack": "Python | pandas | openpyxl",
        "impact": "Prepara arquivos para integrações fiscais e contábeis com padrão.",
        "link": "https://github.com/debsk/TransformaX",
    },
    {
        "icon": "⚙️",
        "title": "Automação No-Code",
        "subtitle": "Fluxos inteligentes com Orange",
        "stack": "No-code | APIs | Webhooks",
        "impact": "Acelera operações e diminui erros em tarefas repetitivas.",
    },
    {
        "icon": "🧭",
        "title": "Revisão de ERP",
        "subtitle": "Mapeamento e melhoria de usabilidade",
        "stack": "QA | UX | Processos",
        "impact": "Melhora navegação e produtividade em módulos críticos.",
        "link": "https://github.com/debsk/Abertura-de-telas-ERP",
    },
    {
        "icon": "🧠",
        "title": "Cxodiugo Bot",
        "subtitle": "LSTM + Attention para séries temporais",
        "stack": "Deep Learning | sklearn | pandas",
        "impact": "Explora previsão financeira com abordagem de IA aplicada.",
        "link": "https://github.com/debsk/cxodiugo-bot",
    },
    {
        "icon": "🎬",
        "title": "Edição de Vídeos",
        "subtitle": "Conteúdo para social e institucional",
        "stack": "CapCut | Premiere | Criação",
        "impact": "Entrega narrativa visual para produtos, campanhas e marca.",
        "links": [
            {"label": "Video 1", "url": "https://youtu.be/03qPtQGD3OU"},
            {"label": "Video 2", "url": "https://www.youtube.com/shorts/GLjBNQwqYPk"},
        ],
    },
]


def render_project_links(project: dict) -> None:
    links = project.get("links")
    if links:
        for item in links:
            render_link(item["label"], item["url"])
        return

    link = project.get("link")
    if link:
        render_link("Abrir projeto", link)


def render_link(label: str, url: str) -> None:
    st.markdown(
        f'<a class="cta-link" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>',
        unsafe_allow_html=True,
    )


def inject_style() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Space+Grotesk:wght@400;500;700&display=swap');

        :root {
            --bg-1: #fff5e8;
            --bg-2: #ffd7b5;
            --ink: #1f1a17;
            --accent: #e85d04;
            --accent-2: #0f4c5c;
            --card: rgba(255,255,255,0.78);
            --line: rgba(15, 76, 92, 0.24);
        }

        .stApp {
            background:
                radial-gradient(circle at 8% 4%, rgba(255, 148, 92, 0.34), transparent 26%),
                radial-gradient(circle at 92% 10%, rgba(15, 76, 92, 0.16), transparent 30%),
                linear-gradient(145deg, var(--bg-1), var(--bg-2));
            color: var(--ink);
            font-family: 'Space Grotesk', sans-serif;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f4c5c 0%, #124559 100%);
            border-right: 1px solid rgba(255,255,255,0.14);
        }

        section[data-testid="stSidebar"] * {
            color: #f8f8f8 !important;
        }

        section[data-testid="stSidebar"] .material-symbols-rounded,
        section[data-testid="stSidebar"] .material-icons {
            font-family: "Material Symbols Rounded", "Material Icons" !important;
        }

        .hero {
            border: 1px solid var(--line);
            border-radius: 20px;
            padding: 1.4rem 1.6rem;
            background: linear-gradient(140deg, rgba(255,255,255,0.8), rgba(255,255,255,0.52));
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.12);
            animation: rise 0.7s ease-out;
        }

        .hero h1 {
            margin: 0;
            color: var(--accent-2);
            font-size: clamp(2rem, 3.2vw, 3.1rem);
            font-family: 'DM Serif Display', serif;
            line-height: 1.08;
        }

        .hero p {
            margin: 0.7rem 0 0 0;
            font-size: 1.03rem;
            max-width: 62ch;
        }

        .chipline {
            margin-top: 0.75rem;
            font-size: 0.92rem;
            color: #3a3a3a;
            letter-spacing: 0.2px;
        }

        .project-card {
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 1rem 1rem 0.9rem 1rem;
            background: var(--card);
            box-shadow: 0 9px 24px rgba(0, 0, 0, 0.08);
            margin-bottom: 0.9rem;
            transition: transform 0.22s ease;
            animation: rise 0.6s ease-out;
        }

        .project-card:hover {
            transform: translateY(-3px);
        }

        .project-card h3 {
            margin: 0;
            color: var(--accent-2);
            font-size: 1.18rem;
            font-family: 'DM Serif Display', serif;
        }

        .project-card .subtitle {
            margin-top: 0.3rem;
            font-size: 0.95rem;
            color: #2e2a27;
        }

        .project-card .meta {
            margin-top: 0.55rem;
            color: #4a4541;
            font-size: 0.9rem;
        }

        .kpi {
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 0.85rem 0.9rem;
            background: rgba(255,255,255,0.7);
            text-align: center;
            margin-bottom: 0.75rem;
        }

        .kpi .num {
            font-size: 1.35rem;
            color: var(--accent);
            font-weight: 700;
        }

        .kpi .txt {
            font-size: 0.86rem;
            color: #34312f;
        }

        .cta-link {
            display: block;
            width: 100%;
            text-align: center;
            background: linear-gradient(90deg, #0f4c5c, #16697a);
            color: #ffffff !important;
            text-decoration: none !important;
            padding: 0.62rem 0.8rem;
            border-radius: 10px;
            font-weight: 600;
            margin: 0.35rem 0 0.8rem 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: filter 0.2s ease;
        }

        .cta-link:hover {
            filter: brightness(1.08);
        }

        @keyframes rise {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0px);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero() -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>Débora Ferreira</h1>
            <p>
                Portfólio de projetos com foco em automação, dados e desenvolvimento de soluções práticas.
                Aqui você encontra trabalhos em Python, Streamlit, QA e projetos orientados a resultado.
            </p>
            <div class="chipline">Python • Streamlit • QA • Automação • Dados • Produto</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def home_section() -> None:
    pic_col, hero_col = st.columns([1, 2.4])
    with pic_col:
        st.image("image.png", use_container_width=True, caption="Débora Ferreira")
    with hero_col:
        hero()

    st.write("")

    left, right = st.columns([2.2, 1])
    with left:
        st.markdown("### Projetos em destaque")

        for project in PROJECTS[:4]:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{project['icon']} {project['title']}</h3>
                    <div class="subtitle">{project['subtitle']}</div>
                    <div class="meta"><b>Stack:</b> {project['stack']}</div>
                    <div class="meta">{project['impact']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            render_project_links(project)

    with right:
        st.markdown("### Números")
        st.markdown('<div class="kpi"><div class="num">7+</div><div class="txt">Projetos ativos</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi"><div class="num">3</div><div class="txt">Áreas principais: QA, Dados e Automação</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi"><div class="num">100%</div><div class="txt">Foco em solução prática</div></div>', unsafe_allow_html=True)
        render_link("LinkedIn", "https://www.linkedin.com/in/débora-barbosa-1a0179193")
        render_link("GitHub", "https://github.com/debsk")


def projects_section() -> None:
    st.markdown("## Projetos")
    st.caption("Links diretos para seus projetos e entregas")

    cols = st.columns(2)
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{project['icon']} {project['title']}</h3>
                    <div class="subtitle">{project['subtitle']}</div>
                    <div class="meta"><b>Tecnologias:</b> {project['stack']}</div>
                    <div class="meta">{project['impact']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            links = project.get("links")
            if links:
                for item in links:
                    render_link(item["label"], item["url"])
            elif project.get("link"):
                render_link("Ver link", project["link"])


def about_section() -> None:
    st.markdown("## Sobre mim")
    st.markdown(
        """
        Sou graduanda em Sistemas de Informação pela UFF, com experiência em QA, backend Python,
        automação de processos e melhoria contínua de produtos.

        Minha proposta é simples: transformar tarefas manuais em fluxos mais inteligentes,
        com ganho de velocidade, padronização e confiabilidade.
        """
    )

    st.markdown("### Experiência")
    st.markdown(
        """
        - MXM (2023 - atual): Analista de Testes (QA) com foco em ERP e automação com Python.
        - Storm Group (2021 - 2023): Desenvolvimento backend Python, testes BDD e boas práticas de arquitetura.
        - IN Jr UFF (2020 - 2021): Backend e gestão de equipes/projetos.
        - Projeto de IC UFF (2019): App em Dart para dosagens médicas.
        """
    )


def contact_section() -> None:
    st.markdown("## Contato")
    st.markdown("Vamos conversar sobre projetos, automação e tecnologia?")
    st.markdown("- Email: deborabf@id.uff.br")
    st.markdown("- LinkedIn: https://www.linkedin.com/in/débora-barbosa-1a0179193")
    st.markdown("- GitHub: https://github.com/debsk")


inject_style()

st.sidebar.markdown("## Navegação")
menu = st.sidebar.radio(
    "Escolha uma seção",
    ["Início", "Projetos", "Sobre", "Contato"],
)

if menu == "Início":
    home_section()
elif menu == "Projetos":
    projects_section()
elif menu == "Sobre":
    about_section()
else:
    contact_section()