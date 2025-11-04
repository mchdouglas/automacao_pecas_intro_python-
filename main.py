#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema simples de automação de inspeção de peças
Curso introdutório — Algoritmos e Lógica de Programação
Regras de qualidade:
- Peso entre 95 e 105 gramas (inclusive)
- Cor azul ou verde
- Comprimento entre 10 e 20 cm (inclusive)
Armazenamento:
- Caixas de capacidade 10 peças. Ao atingir 10, a caixa é "fechada".
Menu:
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada (por ID)
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
Observações de implementação (nível introdutório):
- Usamos listas e dicionários simples (sem classes/OO, sem arquivos externos).
- Usamos condicionais (if/elif/else) e laços (while/for) quando necessário.
- Para manter tudo consistente ao remover uma peça, re-montamos as caixas a partir das peças aprovadas atuais.
"""

# ------------------------------
# Dados em memória (estrutura simples)
# ------------------------------
pecas = []  # cada peça é um dicionário: {id, peso, cor, comprimento, status, motivo}
caixas_fechadas = []  # lista de caixas; cada caixa é lista de IDs de peças
caixa_atual = []  # caixa em uso (aberta, capacidade < 10)

CAPACIDADE_CAIXA = 10
CORES_VALIDAS = ["azul", "verde"]

# ------------------------------
# Funções de domínio (lógica de qualidade e armazenamento)
# ------------------------------

def avaliar_peca(peso, cor, comprimento):
    """
    Retorna (status, motivo)
    status: "aprovada" ou "reprovada"
    motivo: texto explicando caso reprovada
    """
    if peso < 95 or peso > 105:
        return "reprovada", "Peso fora da faixa (95-105g)."
    if cor.lower() not in CORES_VALIDAS:
        return "reprovada", "Cor inválida (apenas azul/verde)."
    if comprimento < 10 or comprimento > 20:
        return "reprovada", "Comprimento fora da faixa (10-20cm)."
    return "aprovada", ""


def embalar_peca_aprovada(peca_id):
    """
    Coloca uma peça aprovada na caixa atual.
    Se a caixa atingir a capacidade, fecha e inicia nova.
    """
    global caixa_atual, caixas_fechadas
    caixa_atual.append(peca_id)
    if len(caixa_atual) >= CAPACIDADE_CAIXA:
        # Fecha a caixa
        caixas_fechadas.append(caixa_atual)
        caixa_atual = []


def remontar_caixas():
    """
    Reconstrói todas as caixas a partir das peças aprovadas existentes.
    Mantém a regra de 10 por caixa e fecha quando cheia.
    (Usada após remoção, por simplicidade e consistência.)
    """
    global caixas_fechadas, caixa_atual
    caixas_fechadas = []
    caixa_atual = []
    for p in pecas:
        if p["status"] == "aprovada":
            embalar_peca_aprovada(p["id"])


# ------------------------------
# Funções utilitárias do menu
# ------------------------------

def cadastrar_peca():
    print("\n== Cadastrar nova peça ==")
    p_id = input("ID da peça: ").strip()
    # Verifica duplicidade de ID
    for p in pecas:
        if p["id"] == p_id:
            print("⚠️ Já existe uma peça com esse ID. Escolha outro.")
            return

    try:
        peso = float(input("Peso (g): ").replace(",", "."))
        cor = input("Cor (azul/verde): ").strip().lower()
        comprimento = float(input("Comprimento (cm): ").replace(",", "."))
    except ValueError:
        print("⚠️ Valores numéricos inválidos para peso ou comprimento.")
        return

    status, motivo = avaliar_peca(peso, cor, comprimento)

    nova = {
        "id": p_id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivo": motivo
    }
    pecas.append(nova)

    if status == "aprovada":
        embalar_peca_aprovada(p_id)
        print("✅ Peça APROVADA e alocada na caixa em uso.")
    else:
        print(f"❌ Peça REPROVADA. Motivo: {motivo}")


def listar_pecas():
    print("\n== Listagem de peças ==")
    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    print(f"\nAprovadas ({len(aprovadas)}):")
    for p in aprovadas:
        print(f"- ID {p['id']} | {p['peso']}g | {p['cor']} | {p['comprimento']}cm")

    print(f"\nReprovadas ({len(reprovadas)}):")
    for p in reprovadas:
        print(f"- ID {p['id']} | motivo: {p['motivo']}")


def remover_peca():
    print("\n== Remover peça ==")
    alvo = input("Informe o ID da peça a remover: ").strip()
    indice = -1
    for i in range(len(pecas)):
        if pecas[i]["id"] == alvo:
            indice = i
            break

    if indice == -1:
        print("⚠️ Peça não encontrada.")
        return

    removida = pecas.pop(indice)
    print(f"🗑️ Peça {removida['id']} removida com sucesso.")
    # Reorganiza as caixas conforme peças aprovadas restantes
    remontar_caixas()


def listar_caixas_fechadas():
    print("\n== Caixas fechadas ==")
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa foi fechada ainda.")
        return

    for idx, cx in enumerate(caixas_fechadas, start=1):
        print(f"- Caixa {idx} ({len(cx)} peças): {', '.join(cx)}")


def gerar_relatorio():
    print("\n== Relatório final ==")
    total_aprovadas = sum(1 for p in pecas if p["status"] == "aprovada")
    total_reprovadas = sum(1 for p in pecas if p["status"] == "reprovada")

    # Contagem de motivos de reprovação
    motivos = {}
    for p in pecas:
        if p["status"] == "reprovada":
            m = p["motivo"]
            if m not in motivos:
                motivos[m] = 0
            motivos[m] += 1

    # Quantidade de caixas utilizadas (fechadas + a atual se tiver peças)
    caixas_utilizadas = len(caixas_fechadas) + (1 if len(caixa_atual) > 0 else 0)

    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print("Motivos de reprovação:")
    if len(motivos) == 0:
        print("- (nenhum)")
    else:
        for k, v in motivos.items():
            print(f"- {k}: {v}")

    print(f"Quantidade de caixas utilizadas: {caixas_utilizadas}")
    if len(caixa_atual) > 0:
        print(f"  (Caixa atual aberta com {len(caixa_atual)} peças)")

    if len(caixas_fechadas) > 0:
        print(f"  Caixas fechadas: {len(caixas_fechadas)}")


def mostrar_menu():
    print("\n==============================")
    print(" Automação de Peças — MENU ")
    print("==============================")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")


def loop_principal():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    loop_principal()
