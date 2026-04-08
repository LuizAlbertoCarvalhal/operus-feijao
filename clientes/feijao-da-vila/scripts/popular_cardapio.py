#!/usr/bin/env python3
"""
Feijão da Vila — Popular cardápio semanal
Uso: python3 popular_cardapio.py

Preencha a SEMANA abaixo e rode. O script insere ou atualiza os dias no PostgreSQL.
"""

import subprocess
import sys
from datetime import date, timedelta

# ─── CONFIGURAR ───────────────────────────────────────────────────────────────
# Roda via docker exec no TKIA02 (sem precisar de psycopg2)
POSTGRES_CONTAINER = "automation-postgres-1"
POSTGRES_USER = "tokkio"
POSTGRES_DB = "tokkio_n8n"

# Segunda-feira da semana que quer preencher (YYYY, M, D)
INICIO_SEMANA = date(2026, 4, 7)

# Base para URLs de imagens no GitHub
GITHUB_MEDIA = "https://raw.githubusercontent.com/LuizAlbertoCarvalhal/operus-feijao/master/media"

# Cardápio da semana — preencha os dias que o restaurante abre (ter–dom)
# canal: 'instagram' | 'whatsapp' | 'ambos'
CARDAPIO = [
    # (dia_semana, prato, descricao, preco, canal, slug_imagem)
    # 0=seg(fechado), 1=ter, 2=qua, 3=qui, 4=sex, 5=sab, 6=dom
    (1, "Executivo de Frango",  "Frango grelhado com arroz, feijão, farofa e salada",       22.90, "ambos",     "executivo-frango"),
    (2, "Executivo de Frango",  "Frango grelhado com arroz, feijão, farofa e salada",       22.90, "ambos",     "executivo-frango"),
    (3, "Executivo de Frango",  "Frango grelhado com arroz, feijão, farofa e salada",       22.90, "whatsapp",  "executivo-frango"),
    (4, "Carré à Mineira",      "Carré suíno com tutu de feijão, couve e farofa",           29.90, "ambos",     "carre-mineira"),
    (5, "Feijoada Completa",    "Feijoada com arroz, couve, farofa, laranja e torresmo",    35.90, "ambos",     "feijoada"),
    (6, "Feijoada Completa",    "Feijoada com arroz, couve, farofa, laranja e torresmo",    35.90, "ambos",     "feijoada"),
]
# ──────────────────────────────────────────────────────────────────────────────


def psql(sql):
    result = subprocess.run(
        ["docker", "exec", "-i", POSTGRES_CONTAINER, "psql", "-U", POSTGRES_USER, "-d", POSTGRES_DB, "-c", sql],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ERRO: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def main():
    inseridos = 0
    atualizados = 0

    for (dia_semana, prato, descricao, preco, canal, slug_imagem) in CARDAPIO:
        data = INICIO_SEMANA + timedelta(days=dia_semana)
        imagem_url = f"{GITHUB_MEDIA}/{slug_imagem}.jpg"
        sql = (
            f"INSERT INTO cardapio (data, prato, descricao, preco, canal, imagem_url) "
            f"VALUES ('{data}', $${prato}$$, $${descricao}$$, {preco}, '{canal}', '{imagem_url}') "
            f"ON CONFLICT (data) DO UPDATE SET "
            f"prato=EXCLUDED.prato, descricao=EXCLUDED.descricao, "
            f"preco=EXCLUDED.preco, canal=EXCLUDED.canal, imagem_url=EXCLUDED.imagem_url, atualizado_em=NOW() "
            f"RETURNING (xmax = 0) AS inserido;"
        )
        out = psql(sql)
        if "t" in out:
            print(f"  ✔ {data} ({dia_semana_nome(dia_semana)}) — inserido: {prato}")
            inseridos += 1
        else:
            print(f"  ↻ {data} ({dia_semana_nome(dia_semana)}) — atualizado: {prato}")
            atualizados += 1

    print(f"\nPronto. {inseridos} inseridos, {atualizados} atualizados.")
    print("Semana:", INICIO_SEMANA, "→", INICIO_SEMANA + timedelta(days=6))


def dia_semana_nome(n):
    return ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"][n]


if __name__ == "__main__":
    main()
