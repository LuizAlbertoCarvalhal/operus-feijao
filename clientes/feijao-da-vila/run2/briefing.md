# Run2 — Feijão da Vila
**Período:** 08/04 a 13/04/2026
**Foco:** Corrigir execução da run1 — meta ≥ 4/6 posts publicados
**Prato da semana:** Executivo de Frango
**Carro-chefe sexta:** Carré à Mineira
**Carro-chefe sábado/domingo:** Feijoada Completa

## Calendário

| Dia         | Data  | Canal               | Cardápio              | Preço |
|-------------|-------|---------------------|-----------------------|-------|
| Terça       | 08/04 | Instagram           | Executivo de Frango   | R$ 22,90 |
| Quarta      | 09/04 | Instagram           | Executivo de Frango   | R$ 22,90 |
| Quinta      | 10/04 | WhatsApp Transmissão| Executivo de Frango   | R$ 22,90 |
| Sexta       | 11/04 | Instagram           | Carré à Mineira       | R$ 29,90 |
| Sábado      | 12/04 | Instagram           | Feijoada Completa     | R$ 35,90 |
| Domingo     | 13/04 | Instagram           | Feijoada Completa     | R$ 35,90 |

## Mudanças vs run1

1. **Workflow n8n ativo** — `feijao-conteudo-diario.json` importado e configurado
2. **Cardápio no PostgreSQL** — populado, workflow lê automaticamente
3. **Lista de transmissão WhatsApp** — criar antes de terça-feira

## Checklist de ativação (antes de 08/04)

- [ ] Importar `feijao-conteudo-diario.json` no n8n (tkia02.tail82b03c.ts.net:5678)
- [ ] Configurar credencial PostgreSQL no n8n: host=192.168.31.10, db=tokkio_n8n, user=tokkio
- [ ] Configurar credencial WhatsApp no n8n (Evolution API ou similar)
- [ ] Configurar credencial Instagram no n8n (Graph API token)
- [ ] Criar lista de transmissão WhatsApp no celular do restaurante
- [ ] Ativar o workflow no n8n (toggle Active)

## Métricas baseline (run1)

| Métrica | Valor |
|---------|-------|
| Posts publicados | 1/6 (17%) |
| Alcance post 01/04 | 217 (fonte: Painel Profissional Facebook, 07/04/2026) |
| Interações post 01/04 | 7 |
| Pedidos iFood semana | não coletado — sem baseline |

## Meta run2

- ≥ 4/6 posts publicados
- ≥ 1 disparo WhatsApp broadcast
- Métricas coletadas ao final (não deixar pendente)
