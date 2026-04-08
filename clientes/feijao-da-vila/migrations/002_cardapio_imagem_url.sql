-- Feijão da Vila — Migration 002: adiciona coluna imagem_url ao cardápio
-- Executar no PostgreSQL do TKIA02:
--   docker exec -i automation-postgres-1 psql -U tokkio -d tokkio_n8n < 002_cardapio_imagem_url.sql

ALTER TABLE cardapio
    ADD COLUMN IF NOT EXISTS imagem_url TEXT;

-- Atualizar semana run2 (08–13/04/2026) com URLs do GitHub
UPDATE cardapio SET imagem_url = 'https://raw.githubusercontent.com/LuizAlbertoCarvalhal/operus-feijao/master/media/executivo-frango.jpg'
WHERE data IN ('2026-04-08', '2026-04-09', '2026-04-10');

UPDATE cardapio SET imagem_url = 'https://raw.githubusercontent.com/LuizAlbertoCarvalhal/operus-feijao/master/media/carre-mineira.jpg'
WHERE data = '2026-04-11';

UPDATE cardapio SET imagem_url = 'https://raw.githubusercontent.com/LuizAlbertoCarvalhal/operus-feijao/master/media/feijoada.jpg'
WHERE data IN ('2026-04-12', '2026-04-13');

-- Verificar resultado
SELECT data, prato, imagem_url FROM cardapio WHERE data BETWEEN '2026-04-08' AND '2026-04-13' ORDER BY data;
