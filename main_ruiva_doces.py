
import os
lista = []
valor_total = 0
condicao = True
while condicao: 
    print('')
    print('Digite o tipo de doce sem acentos (ex.: limao)')
    tipo = input('- Digite o tipo de doce: ')
    tipo = tipo.lower()

    quantos = input('- Digite quantidade: ')
    print('')
    os.system('clear')
    try:
        quantos = int(quantos)

    # Doces Finos
        limao = float(320)
        ninho_trufado_com_nutella = float(330)
        geleia_de_morango = float(320)
        maracuja = float(320)
        pistache = float(340)
        physalis = float(340)
        brigadeiro_gourmet = float(330)
        caramelo_salgado = float(330)
        surpresa_de_uva = float(250)
        cereja = float(340)
        camafeu_de_nozes = float(340)
        creme_brulee_com_nozes = float(330)
        ganache_branco_com_morango = float(330)
        ganache_ao_leite_com_praline = float(330)
        trufa_meio_amarga = float(340)
        frutas_vermelhas = float(340)
        trufa_de_coco = float(340)
    # Brigadeiros Gourmet
        beijinho = float(180)
        leite_ninho = float(180)
        amendoim = float(180)
        bicho_de_pe_morango = float(180)
        casadinho = float(180)
        tradicional_com_amendoim = float(180)
        olho_de_sogra_ameixa = float(180)
        damasco = float(180)
        creme_brulee = float(180)
        tradicional = float(190)
        churros = float(190)
        tradicional_dourado = float(190)
        ninho_com_nutella = float(190)
    # Mini Cupcakes
        mini_cupcakes_chantininho_glitter = float(4.5)
        mini_cupcakes_pasta_americana = float(5.4)
    # Mini Brownie
        mini_brownie = float(2.5)
    # Pirulitos
        pirulito_de_chocolate = float(7)
    # Bolo Vulcão
        bolo_vulcao_creme_de_ninho_pequeno = float(27)
        bolo_vulcao_creme_de_ninho_com_morango_pequeno  = float(30)
        bolo_vulcao_creme_de_ninho_com_nutella_pequeno  = float(35)
        bolo_vulcao_creme_de_ninho_grande = float(55)
        bolo_vulcao_creme_de_ninho_com_morango_grande  = float(60)
        bolo_vulcao_creme_de_ninho_com_nutella_grande  = float(70)
    # Doces Finos
        if tipo == 'limao':
            print(f'{tipo} R${limao:.2f}')
            resultado_limao = (limao / 100) * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_limao:.2f}')
            quantos_limao = quantos
            resultado = resultado_limao

        elif tipo == 'ninho trufado com nutella':
            print(f'{tipo} R${ninho_trufado_com_nutella:.2f}')
            resultado_ninho_trufado_com_nutella = (ninho_trufado_com_nutella / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_ninho_trufado_com_nutella:.2f}')
            quantos_ninho_trufado_com_nutella = quantos
            resultado = resultado_ninho_trufado_com_nutella

        elif tipo == 'geleia de morango':
            print(f'{tipo} R${geleia_de_morango:.2f}')
            resultado_geleia_de_morango = (geleia_de_morango / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_geleia_de_morango:.2f}')
            quantos_geleia_de_morango = quantos
            resultado = resultado_geleia_de_morango

        elif tipo == 'maracuja':
            print(f'{tipo} R${maracuja:.2f}')
            resultado_maracuja = (maracuja / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_maracuja:.2f}')
            quantos_maracuja = quantos
            resultado = resultado_maracuja

        elif tipo == 'pistache':
            print(f'{tipo} R${pistache:.2f}')
            resultado_pistache = (pistache / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_pistache:.2f}')
            quantos_pistache = quantos
            resultado = resultado_pistache

        elif tipo == 'physalis':
            print(f'{tipo} R${physalis:.2f}')
            resultado_physalis = (physalis / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_physalis:.2f}')
            quantos_physalis = quantos
            resultado = resultado_physalis

        elif tipo == 'brigadeiro gourmet':
            print(f'{tipo} R${brigadeiro_gourmet:.2f}')
            resultado_brigadeiro_gourmet = (brigadeiro_gourmet / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_brigadeiro_gourmet:.2f}')
            quantos_brigadeiro_gourmet = quantos
            resultado = resultado_brigadeiro_gourmet

        elif tipo == 'caramelo salgado':
            print(f'{tipo} R${caramelo_salgado:.2f}')
            resultado_caramelo_salgado = (caramelo_salgado / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_caramelo_salgado:.2f}')
            quantos_caramelo_salgado = quantos
            resultado = resultado_caramelo_salgado

        elif tipo == 'surpresa de uva':
            print(f'{tipo} R${surpresa_de_uva:.2f}')
            resultado_surpresa_de_uva = (surpresa_de_uva / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_surpresa_de_uva:.2f}')
            quantos_surpresa_de_uva = quantos
            resultado = resultado_surpresa_de_uva

        elif tipo == 'cereja':
            print(f'{tipo} R${cereja:.2f}')
            resultado_cereja = (cereja / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_cereja:.2f}')
            quantos_cereja = quantos
            resultado = resultado_cereja

        elif tipo == 'camafeu de nozes':
            print(f'{tipo} R${camafeu_de_nozes:.2f}')
            resultado_camafeu_de_nozes = (camafeu_de_nozes / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_camafeu_de_nozes:.2f}')
            quantos_camafeu_de_nozes = quantos
            resultado = resultado_camafeu_de_nozes

        elif tipo == 'creme brulee com nozes':
            print(f'{tipo} R${creme_brulee_com_nozes:.2f}')
            resultado_creme_brulee_com_nozes = (creme_brulee_com_nozes / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_creme_brulee_com_nozes:.2f}')
            quantos_creme_brulee_com_nozes = quantos
            resultado = resultado_creme_brulee_com_nozes

        elif tipo == 'ganache branco com morango':
            print(f'{tipo} R${ganache_branco_com_morango:.2f}')
            resultado_ganache_branco_com_morango = (ganache_branco_com_morango / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_ganache_branco_com_morango:.2f}')
            quantos_ganache_branco_com_morango = quantos
            resultado = resultado_ganache_branco_com_morango

        elif tipo == 'ganache ao leite com praline':
            print(f'- {tipo} R${ganache_ao_leite_com_praline:.2f}')
            resultado_ganache_ao_leite_com_praline = (ganache_ao_leite_com_praline / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_ganache_ao_leite_com_praline:.2f}')
            quantos_ganache_ao_leite_com_praline = quantos
            resultado = resultado_ganache_ao_leite_com_praline

        elif tipo == 'trufa meio amarga':
            print(f'{tipo} R${trufa_meio_amarga:.2f}')
            resultado_trufa_meio_amarga = (trufa_meio_amarga / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_trufa_meio_amarga:.2f}')
            quantos_trufa_meio_amarga = quantos
            resultado = resultado_trufa_meio_amarga

        elif tipo == 'frutas vermelhas':
            print(f'{tipo} R${frutas_vermelhas:.2f}')
            resultado_frutas_vermelhas = (frutas_vermelhas / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_frutas_vermelhas:.2f}')
            quantos_frutas_vermelhas = quantos
            resultado = resultado_frutas_vermelhas

        elif tipo == 'trufa de coco':
            print(f'{tipo} R${trufa_de_coco:.2f}')
            resultado_trufa_de_coco = (trufa_de_coco / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_trufa_de_coco:.2f}')
            quantos_trufa_de_coco = quantos
            resultado = resultado_trufa_de_coco

    # Brigadeiros Gourmet
        elif tipo == 'beijinho':
            print(f'{tipo} R${beijinho:.2f}')
            resultado_beijinho = (beijinho / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_beijinho:.2f}')
            quantos_beijinho = quantos
            resultado = resultado_beijinho

        elif tipo == 'leite ninho':
            print(f'{tipo} R${leite_ninho:.2f}')
            resultado_leite_ninho = (leite_ninho / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_leite_ninho:.2f}')
            quantos_leite_ninho = quantos
            resultado = resultado_leite_ninho

        elif tipo == 'amendoim':
            print(f'{tipo} R${amendoim:.2f}')
            resultado_amendoim = (amendoim / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_amendoim:.2f}')
            quantos_amendoim = quantos
            resultado = resultado_amendoim

        elif tipo == 'bicho de pe morango':
            print(f'{tipo} R${bicho_de_pe_morango:.2f}')
            resultado_bicho_de_pe_morango = (bicho_de_pe_morango / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_bicho_de_pe_morango:.2f}')
            quantos_bicho_de_pe_morango = quantos
            resultado = resultado_bicho_de_pe_morango

        elif tipo == 'casadinho':
            print(f'{tipo} R${casadinho:.2f}')
            resultado_casadinho = (casadinho / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_casadinho:.2f}')
            quantos_casadinho = quantos
            resultado = resultado_casadinho

        elif tipo == 'tradicional com amendoim':
            print(f'{tipo} R${tradicional_com_amendoim:.2f}')
            resultado_tradicional_com_amendoim = (tradicional_com_amendoim / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_tradicional_com_amendoim:.2f}')
            quantos_tradicional_com_amendoim = quantos
            resultado = resultado_tradicional_com_amendoim

        elif tipo == 'olho de sogra ameixa':
            print(f'{tipo} R${olho_de_sogra_ameixa:.2f}')
            resultado_olho_de_sogra_ameixa = (olho_de_sogra_ameixa / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_olho_de_sogra_ameixa:.2f}')
            quantos_olho_de_sogra_ameixa = quantos
            resultado = resultado_olho_de_sogra_ameixa

        elif tipo == 'damasco':
            print(f'{tipo} R${damasco:.2f}')
            resultado_damasco = (damasco / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_damasco:.2f}')
            quantos_damasco = quantos
            resultado = resultado_damasco

        elif tipo == 'creme brulee':
            print(f'{tipo} R${creme_brulee:.2f}')
            resultado_creme_brulee = (creme_brulee / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_creme_brulee:.2f}')
            quantos_creme_brulee = quantos
            resultado = resultado_creme_brulee

        elif tipo == 'tradicional':
            print(f'{tipo} R${tradicional:.2f}')
            resultado_tradicional = (tradicional / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_tradicional:.2f}')
            quantos_tradicional = quantos
            resultado = resultado_tradicional

        elif tipo == 'churros':
            print(f'{tipo} R${churros:.2f}')
            resultado_churros = (churros / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_churros:.2f}')
            quantos_churros = quantos
            resultado = resultado_churros

        elif tipo == 'tradicional dourado':
            print(f'{tipo} R${tradicional_dourado:.2f}')
            resultado_tradicional_dourado = (tradicional_dourado / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_tradicional_dourado:.2f}')
            quantos_tradicional_dourado = quantos
            resultado = resultado_tradicional_dourado

        elif tipo == 'ninho com nutella':
            print(f'{tipo} R${ninho_com_nutella:.2f}')
            resultado_ninho_com_nutella = (ninho_com_nutella / 100) * quantos
            print(f'{quantos} unidades de {tipo}: R${resultado_ninho_com_nutella:.2f}')
            quantos_ninho_com_nutella = quantos
            resultado = resultado_ninho_com_nutella

    # Mini Cupcakes
        elif 'mini cupcakes chantininho glitter' in tipo:
            print(f'{tipo} R${mini_cupcakes_chantininho_glitter:.2f}')
            resultado_mini_cupcakes_chantininho_glitter = mini_cupcakes_chantininho_glitter * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_mini_cupcakes_chantininho_glitter:.2f}')
            quantos_mini_cupcakes_chantininho_glitter = quantos
        
        elif 'mini cupcakes pasta americana' in tipo:
            print(f'{tipo} R${mini_cupcakes_pasta_americana:.2f}')
            resultado_mini_cupcakes_pasta_americana = mini_cupcakes_pasta_americana * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_mini_cupcakes_pasta_americana:.2f}')
            quantos_mini_cupcakes_pasta_americana = quantos
            resultado = resultado_mini_cupcakes_pasta_americana

    # Mini Brownie
        elif 'mini brownie' in tipo:
            print(f'{tipo} R${mini_brownie:.2f}')
            resultado_mini_brownie = mini_brownie * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_mini_brownie:.2f}')
            quantos_mini_brownie = quantos
            resultado = resultado_mini_brownie

    # Pirulitos
        elif 'pirulito de chocolate' in tipo:
            print(f'{tipo} R${pirulito_de_chocolate:.2f}')
            resultado_pirulito_de_chocolate = pirulito_de_chocolate * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_pirulito_de_chocolate:.2f}')
            quantos_pirulito_de_chocolate = quantos
            resultado = resultado_pirulito_de_chocolate

    # Bolo Vulcão
        elif 'creme de ninho p' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_pequeno:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_pequeno = bolo_vulcao_creme_de_ninho_pequeno * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_pequeno:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_pequeno = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_pequeno

        elif 'creme de ninho com morango p' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_morango_pequeno:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno = bolo_vulcao_creme_de_ninho_com_morango_pequeno * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_com_morango_pequeno = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno

        elif 'creme de ninho com nutella p' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_nutella_pequeno:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno = bolo_vulcao_creme_de_ninho_com_nutella_pequeno * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_com_nutella_pequeno = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno

        elif 'creme de ninho g' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_grande:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_grande = bolo_vulcao_creme_de_ninho_grande * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_grande:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_grande = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_grande

        elif 'creme de ninho com morango g' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_morango_grande:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_com_morango_grande = bolo_vulcao_creme_de_ninho_com_morango_grande * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_grande:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_com_morango_grande = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_com_morango_grande

        elif 'creme de ninho com nutella g' in tipo:
            print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_nutella_grande:.2f}')
            resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande = bolo_vulcao_creme_de_ninho_com_nutella_grande * quantos
            print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande:.2f}')
            quantos_bolo_vulcao_creme_de_ninho_com_nutella_grande = quantos
            resultado = resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande
        else:
            print(f' {tipo} não encontrado, tente novamente.')
    except:
        print('Ops! As quantidades precisam ser números inteiros, tente novamente, os números anteriores estão salvos.')
        continue
    print('')

    valor_total = valor_total + resultado    
    print(f'Total: R${valor_total:.2f}')
    lista.append(f'{quantos} - {tipo}: R${resultado:.2f}')
    for item in lista:
        print(item)
    
        


