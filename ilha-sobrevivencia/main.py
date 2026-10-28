import time


def jogo_sobrevivencia():
  print("=== BEM-VINDO AO JOGO: SOBREVIVÊNCIA NA ILHA DESERTA ===")
  print("Seu objetivo é sobreviver por 3 dias tomando as decisões certas!\n")

  vidas = 3
  tem_faca = False
  tem_madeira = False

  dia = 1

  # 1. Uso do WHILE (Loop principal que controla os dias)
  while dia <= 3 and vidas > 0:
    print(f"\n================ DIA {dia} ================")
    print(
        f"Status atual -> Vidas: {vidas} | Faca: {tem_faca} | Madeira:"
        f" {tem_madeira}"
    )

    print("\nO que você deseja fazer?")
    print("1. Explorar a mata fechada em busca de ferramentas")
    print("2. Ir pescar na praia")
    print("3. Descansar no acampamento")

    escolha = input("Digite o número da sua escolha (1, 2 ou 3): ")

    # 2. Uso do IF e ELIF (Múltiplas condições)
    if escolha == "1":
      print(
          "\n🌲 Você entrou na mata e encontrou galhos e uma faca perdida na"
          " lama!"
      )
      tem_madeira = True
      tem_faca = True

    elif escolha == "2":
      print("\n🐟 Você foi pescar na praia...")

      # 3. Uso do OR e AND dentro de condicionais
      if tem_faca or tem_madeira:
        print(
            "Com a ajuda dos seus itens, você conseguiu pescar um belo peixe e"
            " se alimentou bem!"
        )
      else:
        print(
            "Sem ferramentas adequadas, você não conseguiu pegar nada e ficou"
            " com fome."
        )
        vidas -= 1

    elif escolha == "3":
      print(
          "\n⛺ Você passou o dia descansando, recuperou energias e evitou"
          " perigos."
      )

    # 4. Uso do ELSE (Caso o usuário digite algo inválido)
    else:
      print("\n❌ Opção inválida! Você perdeu o dia inteiro confuso.")
      vidas -= 1

    dia += 1

  print("\n================ FIM DA JORNADA ================")

  # 5. Uso do FOR para exibir o resumo do inventário
  print("Analisando seu inventário final...")
  inventario = [
      "Faca de Sobrevivência" if tem_faca else "Nenhuma faca",
      "Madeira Coletada" if tem_madeira else "Nenhuma madeira",
  ]

  for item in inventario:
    print(f"-> Item: {item}")

  # 6. Condicionais finais usando AND e OR para definir o desfecho
  if vidas > 0 and (tem_faca and tem_madeira):
    print(
        "\n🏆 VITÓRIA! Você sobreviveu aos 3 dias e coletou todos os recursos"
        " essenciais!"
    )
  elif vidas > 0 and not (tem_faca and tem_madeira):
    print(
        "\n⚠️ SOBREVIVÊNCIA PARCIAL. Você sobreviveu, mas passou muitos apuros"
        " por falta de itens."
    )
  else:
    print("\n💀 GAME OVER! Suas vidas acabaram e você não resistiu à ilha.")


if __name__ == "__main__":
  jogo_sobrevivencia()