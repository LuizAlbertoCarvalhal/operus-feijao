# Auditoria Run1 — Feijão da Vila
**Período:** 31/03 a 05/04/2026  
**Fechamento:** 05/04/2026  
**Auditado em:** 08/04/2026  
**Responsável:** Operus

---

## Resumo Executivo

| Dimensão | Meta | Realizado | Status |
|----------|------|-----------|--------|
| Posts Instagram | 5/5 | 1/5 | ❌ 20% |
| WhatsApp Broadcast | 1 disparo | 0 | ❌ 0% |
| iFood — dados coletados | Sim | Não | ❌ Pendente |
| Alcance total estimado | — | 217 | ⚠️ Só 1 post |
| Interações totais | — | 7 | ⚠️ Só 1 post |

**Execução geral: 17% (1 de 6 ações planejadas)**

> Run1 foi um piloto de estrutura, não de performance. A infraestrutura foi validada, mas a execução ficou travada na falta de processo operacional automatizado.

---

## 1. Contexto

| Campo | Valor |
|-------|-------|
| Prato da semana | Executivo de Frango |
| Carro-chefe sexta | Carré à Mineira |
| Carro-chefe domingo | Feijoada |
| Canais ativos | Instagram @feijaodavilaoficial, WhatsApp Business, iFood |
| Horário do restaurante | Terça a domingo, 10h30–17h |
| Localização | São João de Meriti, RJ |

---

## 2. Execução — Instagram

| Dia | Data | Foto planejada | Status | Alcance | Curtidas | Comentários |
|-----|------|----------------|--------|---------|----------|-------------|
| Terça | 31/03 | Feijao_da_Vila-3 | ❌ Não publicado | — | — | — |
| Quarta | 01/04 | Feijao_da_Vila-9 | ✅ Publicado 08h56 | 217 | 7 | — |
| Sexta | 03/04 | Feijao_da_Vila-2 | ❌ Não publicado | — | — | — |
| Sábado | 04/04 | Feijao_da_Vila-4 | ❌ Não publicado | — | — | — |
| Domingo | 05/04 | Feijao_da_Vila-62 | ❌ Não publicado | — | — | — |

**Taxa de publicação: 1/5 (20%)**  
**Alcance total: 217** (único post)  
**Taxa de engajamento post 01/04:** 3,2% (7 interações / 217 alcance)

> Métricas coletadas em 07/04/2026 via Painel Profissional Facebook.

---

## 3. Execução — WhatsApp

| Item | Meta | Realizado |
|------|------|-----------|
| Lista de transmissão criada | Sim | ❌ Não |
| Contatos na lista | ≥ 1 | 0 |
| Disparos realizados | 1 (quinta 02/04) | ❌ 0 |

**Taxa de execução: 0%**

---

## 4. Execução — iFood

| Item | Status |
|------|--------|
| Painel acessado durante run1 | ❌ Não |
| Pedidos semana 31/03–05/04 | ❌ Não coletado |
| Baseline para comparação | ❌ Zerado — não disponível para run2 |

> Dados de iFood não foram coletados. Sem baseline, a run2 começa sem referência de volume de pedidos.

---

## 5. Diagnóstico

### O que funcionou
- Post de quarta 01/04 foi publicado com foco correto em delivery iFood
- Estrutura do calendário semanal estava correta e bem pensada
- Identidade visual já existente (fotos Feijao_da_Vila-*)
- Perfil iFood ativo com nota 5.0

### O que não funcionou
- **Execução crítica:** apenas 1 de 6 ações planejadas (17%)
- WhatsApp broadcast não foi criado nem ativado
- Sem processo automatizado para garantir publicação no horário
- Métricas iFood não coletadas — baseline perdido
- Dependência total de ação manual sem lembretes ou fluxo de aprovação

### Causa-raiz
A run1 foi planejada sem uma camada de automação operacional. O conteúdo existia (fotos, calendário), mas não havia um sistema ativo (n8n + aprovação) para disparar e acompanhar as publicações. Tudo dependia de memória e ação manual.

---

## 6. Score da Run1

| Critério | Peso | Nota | Pontos |
|----------|------|------|--------|
| Taxa de publicação Instagram | 40% | 2/10 | 0,8 |
| Execução WhatsApp | 20% | 0/10 | 0,0 |
| Coleta de métricas | 20% | 1/10 | 0,2 |
| Qualidade do conteúdo publicado | 20% | 7/10 | 1,4 |
| **Total** | 100% | — | **2,4/10** |

> Score baixo esperado: run1 era piloto de estrutura. A nota relevante começa na run2.

---

## 7. Decisões para Run2 (08–13/04/2026)

| Ação | Responsável | Status |
|------|-------------|--------|
| Importar workflow n8n `feijao-conteudo-diario.json` | Infra | ⚠️ Pendente |
| Escanear QR WhatsApp na Evolution API | Operacional | ⚠️ Pendente |
| Preencher placeholders WhatsApp no workflow | Infra | ⚠️ Pendente |
| Criar app Meta Business + token Instagram | Operacional | ⚠️ Pendente |
| Definir URL pública para imagens dos pratos | Infra | ⚠️ Pendente |
| Criar lista de transmissão WhatsApp (celular restaurante) | Cliente | ⚠️ Pendente |
| Ativar workflow no n8n | Infra | ⚠️ Pendente |
| Popular cardápio PostgreSQL 08–13/04 | Infra | ✅ Feito |
| Acessar painel iFood no início da semana | Operacional | ⚠️ Pendente |

**Meta run2:** ≥ 4/6 posts publicados + ≥ 1 disparo WhatsApp + métricas coletadas

---

## 8. Baseline para Run2

| Métrica | Valor baseline (run1) |
|---------|-----------------------|
| Posts Instagram publicados | 1/5 (20%) |
| Alcance por post | 217 (referência: 01/04) |
| Engajamento por post | 3,2% |
| WhatsApp disparos | 0 |
| Pedidos iFood/semana | Não disponível |
