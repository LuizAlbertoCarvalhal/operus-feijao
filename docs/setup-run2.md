# Setup Run2 — Feijão da Vila
**Data:** 05/04/2026  
**Status:** Em progresso — Evolution API rodando, falta: WhatsApp scan + Instagram + n8n import

---

## O que já está pronto

| Item | Status |
|------|--------|
| Tabela `cardapio` no PostgreSQL | ✅ Criado |
| Cardápio 08–13/04 populado | ✅ Feito |
| Evolution API rodando (porta 8083) | ✅ Ativo |
| Instância `feijao-da-vila` criada | ✅ Criada |
| Workflow atualizado com Evolution API | ✅ Feito |

---

## Passo 1 — Escanear QR Code do WhatsApp

Acesse o **manager** da Evolution API e escaneie com o celular do restaurante:

```
http://192.168.31.10:8083/manager
```

- Login: admin / `2fa304790fd29c88609bb63012f5b0a410659a71fc3b8342ed7dea5717db7985`
- Clique na instância `feijao-da-vila` → "Connect" → escanear QR com WhatsApp Business

Após conectar, buscar o ID do grupo/broadcast:

```bash
curl -s http://192.168.31.10:8083/chat/findChats/feijao-da-vila \
  -H "apikey: 2fa304790fd29c88609bb63012f5b0a410659a71fc3b8342ed7dea5717db7985" | \
  python3 -m json.tool | grep -i "id\|name" | head -40
```

---

## Passo 2 — Preencher números WhatsApp no workflow

Depois de escanear, editar o arquivo do workflow:

```
/home/l7/operus-feijao/workflows/feijao-conteudo-diario.json
```

Substituir:
- `PLACEHOLDER_SEU_NUMERO_WHATSAPP` → número do Luiz com DDI (ex: `5521999999999`)
- `PLACEHOLDER_GRUPO_OU_BROADCAST_WHATSAPP` → JID do grupo ou lista de transmissão (formato `5521xxxxxxx@g.us` para grupos ou `5521xxxxxxx@s.whatsapp.net` para contatos)

---

## Passo 3 — Instagram Graph API

### 3.1 Criar app Meta Business

1. Acessar: https://developers.facebook.com/apps/
2. Criar novo app → tipo **Business**
3. Adicionar produto: **Instagram Graph API**

### 3.2 Conectar conta Instagram Business

1. No app → Instagram → Configurações básicas
2. Conectar a conta `@feijaodavilaoficial`
3. A conta no Instagram precisa estar configurada como **Conta Comercial** (Business Account)
4. Vincular a uma **Página do Facebook** (requisito da Graph API)

### 3.3 Obter Access Token

1. No App → Instagram → Gerar token
2. Ou usar o **Graph API Explorer**: https://developers.facebook.com/tools/explorer/
3. Permissões necessárias:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_read_engagement`
4. Gerar **Long-Lived Token** (válido 60 dias):
   ```
   GET https://graph.facebook.com/v19.0/oauth/access_token?
     grant_type=fb_exchange_token&
     client_id={APP_ID}&
     client_secret={APP_SECRET}&
     fb_exchange_token={SHORT_LIVED_TOKEN}
   ```

### 3.4 Obter Instagram Account ID

```bash
curl -s "https://graph.facebook.com/v19.0/me/accounts?access_token={SEU_TOKEN}"
# Pegar o id da página, então:
curl -s "https://graph.facebook.com/v19.0/{PAGE_ID}?fields=instagram_business_account&access_token={SEU_TOKEN}"
```

### 3.5 Preencher no workflow

Substituir no arquivo `feijao-conteudo-diario.json`:
- `PLACEHOLDER_INSTAGRAM_ACCOUNT_ID` → ID numérico da conta Instagram
- `PLACEHOLDER_INSTAGRAM_ACCESS_TOKEN` → Token de acesso

### 3.6 URL das imagens

As imagens precisam estar em uma **URL pública** para o Instagram conseguir publicar.

**Opção A (rápida):** Subir no Nextcloud e gerar link público  
**Opção B (permanente):** Servir com nginx/Caddy do TKIA01  

Substituir `PLACEHOLDER_URL_IMAGEM_DO_DIA` no nó "Instagram — Criar Container" por uma expressão que busca a imagem correta para o dia.

---

## Passo 4 — Importar workflow no n8n

1. Acessar: `http://tkia02.tail82b03c.ts.net:8080` (Tailscale) ou `http://192.168.31.10:8080`
2. Menu → **Workflows** → **Import from File**
3. Selecionar: `/home/l7/operus-feijao/workflows/feijao-conteudo-diario.json`

### 4.1 Configurar credencial PostgreSQL no n8n

Após importar:
1. Abrir o nó **"PostgreSQL — Prato do Dia"**
2. Criar nova credencial:
   - Host: `192.168.31.10`
   - Port: `5432`
   - Database: `tokkio_n8n`
   - User: `tokkio`
   - Password: `Tokkio@2026!`
3. Salvar como "TKIA02 PostgreSQL"

### 4.2 Ativar workflow

Toggle **Active** no canto superior direito do workflow.

---

## Configurações do serviço Evolution API

| Item | Valor |
|------|-------|
| URL interna (n8n) | `http://evolution-api:8080` |
| URL externa (browser) | `http://192.168.31.10:8083` |
| Manager UI | `http://192.168.31.10:8083/manager` |
| API Key | `2fa304790fd29c88609bb63012f5b0a410659a71fc3b8342ed7dea5717db7985` |
| Instância WhatsApp | `feijao-da-vila` |
| Token instância | `feijao-da-vila-token` |
| Compose | `/home/l7/tokkio/compose/feijao/docker-compose.yml` |

---

## Checklist final (antes de terça 08/04)

- [ ] Escanear QR WhatsApp no manager (`http://192.168.31.10:8083/manager`)
- [ ] Preencher `PLACEHOLDER_SEU_NUMERO_WHATSAPP` no workflow
- [ ] Preencher `PLACEHOLDER_GRUPO_OU_BROADCAST_WHATSAPP` no workflow
- [ ] Criar app Meta Business e obter Instagram token
- [ ] Preencher `PLACEHOLDER_INSTAGRAM_ACCOUNT_ID` e `PLACEHOLDER_INSTAGRAM_ACCESS_TOKEN`
- [ ] Definir URL pública para imagens dos pratos
- [ ] Importar workflow no n8n e configurar credencial PostgreSQL
- [ ] Ativar o workflow
- [ ] Criar lista de transmissão WhatsApp no celular do restaurante
