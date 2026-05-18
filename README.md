# 🏥 Sistema de Apoio à Decisão Médica com IA (RAG)

## 📌 Sobre o Projeto
[cite_start]Este projeto é uma aplicação de apoio ao profissional de saúde[cite: 46]. [cite_start]Ele atua como um sistema de recomendação personalizado que utiliza Inteligência Artificial e a arquitetura RAG (Retrieval-Augmented Generation) para analisar o histórico de pacientes e sugerir planos de tratamento, exames e cuidados[cite: 10, 71].

[cite_start]A aplicação foi desenvolvida focando em boas práticas de mercado, adotando o **Padrão de Microsserviços** para separar as responsabilidades da interface de usuário e da lógica de servidor[cite: 395].

## 🏗️ Arquitetura do Sistema
[cite_start]O projeto é dividido em dois serviços principais que se comunicam via rede[cite: 52]:

* [cite_start]**Front-End (Interface Web):** Construído com Streamlit, oferece uma interface amigável e interativa onde o médico pode cadastrar informações e visualizar os relatórios gerados pela IA[cite: 199, 330].
* [cite_start]**Back-End (API Central):** Desenvolvido com FastAPI, atua como o maestro do sistema[cite: 50, 100]. [cite_start]Ele gerencia a conexão com o banco de dados e orquestra a comunicação com o motor de Inteligência Artificial[cite: 111].
* [cite_start]**Banco de Dados:** Utiliza SQLite para armazenamento relacional dos dados biométricos e sintomas dos pacientes, servindo como a "fonte de verdade" para a IA[cite: 53, 54, 635].

## 🧠 Como o RAG (Retrieval-Augmented Generation) Funciona Aqui
O núcleo inteligente do sistema segue 4 etapas rigorosas para evitar alucinações da IA:
1.  [cite_start]**Input:** O médico informa o ID e nome do paciente via interface Web[cite: 64].
2.  [cite_start]**Retrieval (Recuperação):** O Back-End executa uma query SQL (`SELECT *`) no banco de dados para resgatar o histórico real e exato de sintomas daquele paciente[cite: 67, 471].
3.  [cite_start]**Augmentation (Enriquecimento):** O código Python injeta esses dados puros dentro de um *Prompt Template* rigoroso, instruindo a IA a agir como um especialista médico[cite: 68, 69].
4.  [cite_start]**Generation (Geração):** O prompt enriquecido é enviado para a API do Google Gemini (modelo `gemini-2.5-flash`), que analisa o quadro clínico e gera o relatório final de recomendações[cite: 70, 71, 579].

## 💻 Tecnologias Utilizadas
* [cite_start]**Linguagem:** Python 3.12 [cite: 89]
* [cite_start]**Back-End Framework:** FastAPI & Uvicorn [cite: 99, 100]
* [cite_start]**Front-End Framework:** Streamlit [cite: 323]
* [cite_start]**Banco de Dados:** SQLite (`sqlite3`) [cite: 53]
* [cite_start]**Inteligência Artificial:** Google Gemini API (`google-generativeai` / `google-genai`) [cite: 585]
* [cite_start]**Requisições HTTP:** `requests` & `httpx` [cite: 55, 105]

## 🚀 Instruções de Instalação e Uso local

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
