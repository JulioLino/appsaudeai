# 🏥 Sistema de Apoio à Decisão Médica com IA (RAG)

## 📌 Sobre o Projeto
Este projeto é uma aplicação de apoio ao profissional de saúde. Ele atua como um sistema de recomendação personalizado que utiliza Inteligência Artificial e a arquitetura RAG (Retrieval-Augmented Generation) para analisar o histórico de pacientes e sugerir planos de tratamento, exames e cuidados.

A aplicação foi desenvolvida focando em boas práticas de mercado, adotando o **Padrão de Microsserviços** para separar as responsabilidades da interface de usuário e da lógica de servidor.

## 🏗️ Arquitetura do Sistema
O projeto é dividido em dois serviços principais que se comunicam via rede:

* **Front-End (Interface Web):** Construído com Streamlit, oferece uma interface amigável e interativa onde o médico pode cadastrar informações e visualizar os relatórios gerados pela IA.
* **Back-End (API Central):** Desenvolvido com FastAPI, atua como o maestro do sistema. Ele gerencia a conexão com o banco de dados e orquestra a comunicação com o motor de Inteligência Artificial.
* **Banco de Dados:** Utiliza SQLite para armazenamento relacional dos dados biométricos e sintomas dos pacientes, servindo como a "fonte de verdade" para a IA.

## 🧠 Como o RAG (Retrieval-Augmented Generation) Funciona Aqui
O núcleo inteligente do sistema segue 4 etapas rigorosas para evitar alucinações da IA:
1. **Input:** O médico informa o ID e nome do paciente via interface Web.
2. **Retrieval (Recuperação):** O Back-End executa uma query SQL no banco de dados para resgatar o histórico real e exato de sintomas daquele paciente.
3. **Augmentation (Enriquecimento):** O código Python injeta esses dados puros dentro de um Prompt Template rigoroso, instruindo a IA a agir como um especialista médico.
4. **Generation (Geração):** O prompt enriquecido é enviado para a API do Google Gemini (modelo `gemini-2.0-flash`), que analisa o quadro clínico e gera o relatório final de recomendações.

## 💻 Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Back-End Framework:** FastAPI & Uvicorn
* **Front-End Framework:** Streamlit
* **Banco de Dados:** SQLite (`sqlite3`)
* **Inteligência Artificial:** Google Gemini API (`google-genai`)
* **Requisições HTTP:** `requests` & `httpx`

## 🚀 Instruções de Instalação e Uso local

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
