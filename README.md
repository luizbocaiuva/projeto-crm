# 🚀 WhatsApp CRM Automator (Python + Playwright)

Este é um sistema de automação para disparos de mensagens via WhatsApp utilizando **Python** e **Playwright**. O projeto foi desenhado para um cenário real de CRM, onde uma empresa possui múltiplas vendedoras e precisa realizar disparos em massa a partir de uma planilha Excel, respeitando limites de hardware e evitando banimentos.

## 🎯 Objetivo do Projeto
Automatizar o envio de mensagens personalizadas para clientes em segundo plano (headless), gerenciando múltiplas sessões de WhatsApp de forma sequencial para otimizar o uso de memória RAM (ideal para máquinas com 8GB).

## 🏗️ Arquitetura e Padrões de Projeto
O projeto foi desenvolvido seguindo o padrão **MVC (Model-View-Controller)** e os princípios de **POO (Programação Orientada a Objetos)**:

- **Models**: Classes `Cliente` e `Vendedora` para representação e validação de dados.
- **Controllers**: `DisparadorController` encapsula toda a lógica de automação e interação com o navegador.
- **Data-Driven**: A fonte de dados é uma planilha Excel (`.xlsx`) processada com a biblioteca **Pandas**.
- **Persistência de Sessão**: Utiliza `launch_persistent_context` para que o login (QR Code) de cada vendedora seja realizado apenas uma vez, salvando os cookies em pastas separadas.

## 🛠️ Tecnologias Utilizadas
- **Python 3.14+**
- **Playwright** (Automação de navegador moderna e resiliente)
- **Pandas** (Manipulação de dados e leitura de Excel)
- **Openpyxl** (Engine para arquivos Excel)

## 🛡️ Estratégias Anti-Ban e Resiliência
Para garantir a segurança dos números de WhatsApp da empresa, foram implementadas as seguintes técnicas:
1. **Delays Randômicos**: Intervalos variáveis entre 20 a 60 segundos entre cada mensagem.
2. **Humanização**: Simulação de foco em elementos e uso de comandos de teclado (`Enter`) em vez de apenas cliques em seletores instáveis.
3. **User-Agent Real**: Emulação de um navegador Chrome real para evitar detecção como bot.
4. **Tratamento de Exceções**: Identificação automática de números que não possuem WhatsApp, evitando que o script trave em modais de erro.
5. **Gestão de Recursos**: Processamento sequencial de vendedoras para manter o consumo de RAM estável.

## 📋 Pré-requisitos
Antes de rodar o projeto, você precisará ter o Python instalado e seguir os passos abaixo:

```bash
# Clone o repositório
git clone https://github.com

# Acesse a pasta do projeto
cd projeto-crm-whatsapp

# Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install pandas openpyxl playwright

# Instale os binários do navegador
playwright install chromium

## 🚀 Como Usar
1. **Prepare a Planilha:** Edite o arquivo em `data/clientes.xlsx` seguindo rigorosamente as colunas: **Nome**, **WhatsApp**, **Texto** e **Vendedora**.
2. **Primeiro Acesso**: No primeiro uso de cada vendedora, o sistema abrirá o navegador visivelmente para que o QR Code seja escaneado.
3. **Execuções Subsequentes**: As execuções seguintes ocorrerão automaticamente em segundo plano (headless), utilizando a sessão salva.
4. **Execução do Script**:
```bash
python app.py


⚠️ **Aviso: Use o código com cuidado e respeite os limites de envio para evitar banimentos.**

📈 **Melhorias Futuras (Roadmap)**
- **Logs de Auditoria**: Implementação de registros detalhados em arquivo .log para monitoramento.
- **Persistência de Dados**: Integração com banco de dados SQLite para controle de histórico de envios e evitar duplicidade.
- **Interface Web**: Criação de uma interface simples em Streamlit para que o usuário final carregue planilhas sem interagir com o código.

** Desenvolvido por [Luiz Bocaiuva] **