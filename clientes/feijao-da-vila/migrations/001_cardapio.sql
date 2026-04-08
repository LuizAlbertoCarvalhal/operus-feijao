-- Feijão da Vila — Tabela de cardápio para workflow de conteúdo diário
-- Executar no PostgreSQL do TKIA02 (192.168.31.10)

CREATE TABLE IF NOT EXISTS cardapio (
    id          SERIAL PRIMARY KEY,
    data        DATE        NOT NULL UNIQUE,
    prato       TEXT        NOT NULL,
    descricao   TEXT,
    preco       NUMERIC(8,2),
    canal       TEXT        NOT NULL DEFAULT 'ambos' CHECK (canal IN ('instagram', 'whatsapp', 'ambos')),
    ativo       BOOLEAN     NOT NULL DEFAULT TRUE,
    criado_em   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    atualizado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Índice para busca por data (usada pelo n8n diariamente)
CREATE INDEX IF NOT EXISTS idx_cardapio_data ON cardapio (data);

-- Trigger para atualizar atualizado_em automaticamente
CREATE OR REPLACE FUNCTION atualizar_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.atualizado_em = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_cardapio_atualizado
    BEFORE UPDATE ON cardapio
    FOR EACH ROW EXECUTE FUNCTION atualizar_timestamp();

-- Dados de exemplo (semana típica do Feijão da Vila)
INSERT INTO cardapio (data, prato, descricao, preco, canal) VALUES
    (CURRENT_DATE,     'Executivo de Frango',  'Frango grelhado com arroz, feijão, farofa e salada',  22.90, 'ambos'),
    (CURRENT_DATE + 1, 'Executivo de Frango',  'Frango grelhado com arroz, feijão, farofa e salada',  22.90, 'ambos'),
    (CURRENT_DATE + 2, 'Carré à Mineira',      'Carré suíno com tutu de feijão, couve e farofa',      29.90, 'instagram'),
    (CURRENT_DATE + 3, 'Feijoada Completa',    'Feijoada com arroz, couve, farofa, laranja e torresmo', 35.90, 'ambos')
ON CONFLICT (data) DO NOTHING;
