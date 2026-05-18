import streamlit as st
import requests

# 1. Configuração da página para o Portfólio
st.set_page_config(
    page_title="Sistema de Apoio Médico - RAG",
    page_icon="🩺",
    layout="centered"
)

# Título do Cabeçalho
st.title("🩺 Sistema de Apoio à Decisão Médica")
st.markdown("**Arquitetura:** Backend SQL (SQLite) + IA Gemini 2.0 Flash via RAG")
st.write("Esta interface simula a tela de acesso de recepcionistas e médicos ao servidor central.")
st.divider()

# Endereço onde o seu app.py (FastAPI) está rodando localmente
BASE_URL = "http://127.0.0.1:8000"

# Criação das abas visuais para organizar os fluxos
aba_cadastro, aba_consulta = st.tabs(["📝 Cadastrar Paciente (Fluxo 1)", "🧠 Consultar IA / RAG (Fluxo 2)"])

# ==========================================
# ABA 1: INGESTÃO DE DADOS (Substitui dsa_api_cliente_1.py)
# ==========================================
with aba_cadastro:
    st.subheader("📋 Ingestão: Cadastro de Novo Paciente")
    st.info("Preencha os dados abaixo. O sistema enviará um payload JSON via POST para salvar o histórico no banco de dados relacional sem acionar a IA.")
    
    with st.form("form_cadastro"):
        nome = st.text_input("Nome do Paciente*")
        idade = st.number_input("Idade*", min_value=0, max_value=120, step=1)
        genero = st.selectbox("Gênero*", ["Masculino", "Feminino", "Outro"])
        sintomas_input = st.text_area(
            "Sintomas apresentados* (separe por vírgulas)", 
            placeholder="ex: tosse, febre alta, dores no corpo"
        )
        
        btn_salvar = st.form_submit_button("💾 Salvar no Banco SQL")
        
    if btn_salvar:
        if not nome or not sintomas_input:
            st.warning("⚠️ Por favor, preencha o Nome e os Sintomas do paciente.")
        else:
            # Limpa e formata a lista de sintomas exatamente como o script original fazia
            sintomas_lista = [s.strip() for s in sintomas_input.split(",") if s.strip()]
            
            # Estrutura do payload espelhando a validação do FastAPI
            payload = {
                "nome_paciente": nome.strip(),
                "idade": int(idade),
                "genero": genero,
                "sintomas": sintomas_lista
            }
            
            with st.spinner("Enviando dados para a API central..."):
                try:
                    resposta = requests.post(f"{BASE_URL}/dsa_cadastra_paciente", json=payload)
                    if resposta.status_code == 200:
                        st.success("✅ Sucesso! Registro processado no banco de dados.")
                        st.json(resposta.json())
                    else:
                        st.error(f"Falha na API ({resposta.status_code}): {resposta.text}")
                except Exception as e:
                    st.error(f"🚨 Erro ao conectar com o servidor: {e}")
                    st.write("Dica: Confirme se o `app.py` está rodando ativamente no terminal.")

# ==========================================
# ABA 2: SISTEMA DE RECOMENDACÃO (Substitui dsa_api_cliente_2.py)
# ==========================================
with aba_consulta:
    st.subheader("🧠 Assistente de Decisão RAG (Gemini)")
    st.info("Informe a identificação. A API fará o Retrieval (SQL) do histórico salvo e orquestrará um Prompt Enriquecido para o Gemini sugerir o tratamento.")
    
    with st.form("form_consulta"):
        col1, col2 = st.columns(2)
        with col1:
            busca_nome = st.text_input("Nome do Paciente*")
        with col2:
            busca_id = st.number_input("ID do Registro*", min_value=1, step=1)
            
        btn_consultar = st.form_submit_button("✨ Solicitar Apoio da IA")
        
    if btn_consultar:
        if not busca_nome:
            st.warning("⚠️ Insira o Nome do paciente para prosseguir.")
        else:
            with st.spinner("Resgatando histórico SQL e processando IA no Google AI Studio..."):
                try:
                    # Envio via GET passando os parâmetros na URL de forma limpa
                    params = {
                        "nome_paciente": busca_nome.strip(),
                        "id_paciente": int(busca_id)
                    }
                    resposta = requests.get(f"{BASE_URL}/dsa_llm_recomenda_tratamento/", params=params)
                    
                    if resposta.status_code == 200:
                        dados = resposta.json()
                        st.success(f"Análise concluída para o paciente: **{dados.get('nome_paciente', busca_nome)}**")
                        
                        # Exibição elegante do retorno textual gerado pelo Gemini
                        st.markdown("### 📜 Parecer de Apoio ao Médico")
                        st.container(border=True).write(dados.get("recomendações", dados))
                    elif resposta.status_code == 404:
                        st.warning("🔍 Paciente não localizado. Verifique se o Nome e o ID coincidem com o cadastro.")
                    else:
                        st.error(f"Erro retornado pelo servidor ({resposta.status_code}): {resposta.text}")
                except Exception as e:
                    st.error(f"🚨 Erro de conexão: {e}")