from ruiva_doces_dados import menu
print(menu)

# Doces Finos
resultado_limao = 0
resultado_ninho_trufado_com_nutella = 0
resultado_geleia_de_morango = 0
resultado_maracuja = 0
resultado_pistache = 0
resultado_physalis = 0
resultado_brigadeiro_gourmet = 0
resultado_caramelo_salgado = 0
resultado_surpresa_de_uva = 0
resultado_cereja = 0
resultado_camafeu_de_nozes = 0
resultado_creme_brulee_com_nozes = 0
resultado_ganache_branco_com_morango = 0
resultado_ganache_ao_leite_com_praline = 0
resultado_trufa_meio_amarga = 0
resultado_frutas_vermelhas = 0
resultado_trufa_de_coco = 0
# Brigadeiros Gourmet
resultado_beijinho = 0
resultado_leite_ninho = 0
resultado_amendoim = 0
resultado_bicho_de_pe_morango = 0
resultado_casadinho = 0
resultado_tradicional_com_amendoim = 0
resultado_olho_de_sogra_ameixa = 0
resultado_damasco = 0
resultado_creme_brulee = 0
resultado_tradicional = 0
resultado_churros = 0
resultado_tradicional_dourado = 0
resultado_ninho_com_nutella = 0
# Mini Cupcakes
resultado_mini_cupcakes_chantininho_glitter = 0
resultado_mini_cupcakes_pasta_americana = 0
# Mini Brownie
resultado_mini_brownie = 0
# Pirulitos
resultado_pirulito_de_chocolate = 0
# Bolo Vulcão
resultado_bolo_vulcao_creme_de_ninho_pequeno = 0
resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno = 0
resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno = 0
resultado_bolo_vulcao_creme_de_ninho_grande = 0
resultado_bolo_vulcao_creme_de_ninho_com_morango_grande = 0
resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande = 0

print('Digite o tipo de doce sem acentos ex.: limao')
print('')

condicao = True
while condicao: 
    print('')
    tipo = input('- Digite o tipo de doce: ')
    tipo = tipo.lower()
    
    quantos = input('- Digite quantidade: ')
    print('')
    
    try:
        quantos = int(quantos)

    except:
        print('Ops! As quantidades precisam ser números inteiros, tente novamente.')
        break

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

    elif tipo == 'ninho trufado com nutella':
        print(f'{tipo} R${ninho_trufado_com_nutella:.2f}')
        resultado_ninho_trufado_com_nutella = (ninho_trufado_com_nutella / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_ninho_trufado_com_nutella:.2f}')
        quantos_ninho_trufado_com_nutella = quantos

    elif tipo == 'geleia de morango':
        print(f'{tipo} R${geleia_de_morango:.2f}')
        resultado_geleia_de_morango = (geleia_de_morango / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_geleia_de_morango:.2f}')
        quantos_geleia_de_morango = quantos
        
    elif tipo == 'maracuja':
        print(f'{tipo} R${maracuja:.2f}')
        resultado_maracuja = (maracuja / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_maracuja:.2f}')
        quantos_maracuja = quantos

    elif tipo == 'pistache':
        print(f'{tipo} R${pistache:.2f}')
        resultado_pistache = (pistache / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_pistache:.2f}')
        quantos_pistache = quantos

    elif tipo == 'physalis':
        print(f'{tipo} R${physalis:.2f}')
        resultado_physalis = (physalis / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_physalis:.2f}')
        quantos_physalis = quantos

    elif tipo == 'brigadeiro gourmet':
        print(f'{tipo} R${brigadeiro_gourmet:.2f}')
        resultado_brigadeiro_gourmet = (brigadeiro_gourmet / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_brigadeiro_gourmet:.2f}')
        quantos_brigadeiro_gourmet = quantos

    elif tipo == 'caramelo salgado':
        print(f'{tipo} R${caramelo_salgado:.2f}')
        resultado_caramelo_salgado = (caramelo_salgado / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_caramelo_salgado:.2f}')
        quantos_caramelo_salgado = quantos


    elif tipo == 'surpresa de uva':
        print(f'{tipo} R${surpresa_de_uva:.2f}')
        resultado_surpresa_de_uva = (surpresa_de_uva / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_surpresa_de_uva:.2f}')
        quantos_surpresa_de_uva = quantos

    elif tipo == 'cereja':
        print(f'{tipo} R${cereja:.2f}')
        resultado_cereja = (cereja / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_cereja:.2f}')
        quantos_cereja = quantos

    elif tipo == 'camafeu de nozes':
        print(f'{tipo} R${camafeu_de_nozes:.2f}')
        resultado_camafeu_de_nozes = (camafeu_de_nozes / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_camafeu_de_nozes:.2f}')
        quantos_camafeu_de_nozes = quantos

    elif tipo == 'creme brulee com nozes':
        print(f'{tipo} R${creme_brulee_com_nozes:.2f}')
        resultado_creme_brulee_com_nozes = (creme_brulee_com_nozes / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_creme_brulee_com_nozes:.2f}')
        quantos_creme_brulee_com_nozes = quantos

    elif tipo == 'ganache branco com morango':
        print(f'{tipo} R${ganache_branco_com_morango:.2f}')
        resultado_ganache_branco_com_morango = (ganache_branco_com_morango / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_ganache_branco_com_morango:.2f}')
        quantos_ganache_branco_com_morango = quantos

    elif tipo == 'ganache ao leite com praline':
        print(f'- {tipo} R${ganache_ao_leite_com_praline:.2f}')
        resultado_ganache_ao_leite_com_praline = (ganache_ao_leite_com_praline / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_ganache_ao_leite_com_praline:.2f}')
        quantos_ganache_ao_leite_com_praline = quantos


    elif tipo == 'trufa meio amarga':
        print(f'{tipo} R${trufa_meio_amarga:.2f}')
        resultado_trufa_meio_amarga = (trufa_meio_amarga / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_trufa_meio_amarga:.2f}')
        quantos_trufa_meio_amarga = quantos

    elif tipo == 'frutas vermelhas':
        print(f'{tipo} R${frutas_vermelhas:.2f}')
        resultado_frutas_vermelhas = (frutas_vermelhas / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_frutas_vermelhas:.2f}')
        quantos_frutas_vermelhas = quantos

    elif tipo == 'trufa de coco':
        print(f'{tipo} R${trufa_de_coco:.2f}')
        resultado_trufa_de_coco = (trufa_de_coco / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_trufa_de_coco:.2f}')
        quantos_trufa_de_coco = quantos

# Brigadeiros Gourmet
    elif tipo == 'beijinho':
        print(f'{tipo} R${beijinho:.2f}')
        resultado_beijinho = (beijinho / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_beijinho:.2f}')
        quantos_beijinho = quantos

    elif tipo == 'leite ninho':
        print(f'{tipo} R${leite_ninho:.2f}')
        resultado_leite_ninho = (leite_ninho / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_leite_ninho:.2f}')
        quantos_leite_ninho = quantos

    elif tipo == 'amendoim':
        print(f'{tipo} R${amendoim:.2f}')
        resultado_amendoim = (amendoim / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_amendoim:.2f}')
        quantos_amendoim = quantos

    elif tipo == 'bicho de pe morango':
        print(f'{tipo} R${bicho_de_pe_morango:.2f}')
        resultado_bicho_de_pe_morango = (bicho_de_pe_morango / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_bicho_de_pe_morango:.2f}')
        quantos_bicho_de_pe_morango = quantos

    elif tipo == 'casadinho':
        print(f'{tipo} R${casadinho:.2f}')
        resultado_casadinho = (casadinho / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_casadinho:.2f}')
        quantos_casadinho = quantos

    elif tipo == 'tradicional com amendoim':
        print(f'{tipo} R${tradicional_com_amendoim:.2f}')
        resultado_tradicional_com_amendoim = (tradicional_com_amendoim / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_tradicional_com_amendoim:.2f}')
        quantos_tradicional_com_amendoim = quantos

    elif tipo == 'olho de sogra ameixa':
        print(f'{tipo} R${olho_de_sogra_ameixa:.2f}')
        resultado_olho_de_sogra_ameixa = (olho_de_sogra_ameixa / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_olho_de_sogra_ameixa:.2f}')
        quantos_olho_de_sogra_ameixa = quantos

    elif tipo == 'damasco':
        print(f'{tipo} R${damasco:.2f}')
        resultado_damasco = (damasco / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_damasco:.2f}')
        quantos_damasco = quantos

    elif tipo == 'creme brulee':
        print(f'{tipo} R${creme_brulee:.2f}')
        resultado_creme_brulee = (creme_brulee / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_creme_brulee:.2f}')
        quantos_creme_brulee = quantos

    elif tipo == 'tradicional':
        print(f'{tipo} R${tradicional:.2f}')
        resultado_tradicional = (tradicional / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_tradicional:.2f}')
        quantos_tradicional = quantos

    elif tipo == 'churros':
        print(f'{tipo} R${churros:.2f}')
        resultado_churros = (churros / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_churros:.2f}')
        quantos_churros = quantos

    elif tipo == 'tradicional dourado':
        print(f'{tipo} R${tradicional_dourado:.2f}')
        resultado_tradicional_dourado = (tradicional_dourado / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_tradicional_dourado:.2f}')
        quantos_tradicional_dourado = quantos

    elif tipo == 'ninho com nutella':
        print(f'{tipo} R${ninho_com_nutella:.2f}')
        resultado_ninho_com_nutella = (ninho_com_nutella / 100) * quantos
        print(f'{quantos} unidades de {tipo}: R${resultado_ninho_com_nutella:.2f}')
        quantos_ninho_com_nutella = quantos

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

    # Mini Brownie
    elif 'mini brownie' in tipo:
        print(f'{tipo} R${mini_brownie:.2f}')
        resultado_mini_brownie = mini_brownie * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_mini_brownie:.2f}')
        quantos_mini_brownie = quantos

    # Pirulitos
    elif 'pirulito de chocolate' in tipo:
        print(f'{tipo} R${pirulito_de_chocolate:.2f}')
        resultado_pirulito_de_chocolate = pirulito_de_chocolate * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_pirulito_de_chocolate:.2f}')
        quantos_pirulito_de_chocolate = quantos

    # Bolo Vulcão
    elif 'creme de ninho p' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_pequeno:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_pequeno = bolo_vulcao_creme_de_ninho_pequeno * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_pequeno:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_pequeno = quantos

    elif 'creme de ninho com morango p' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_morango_pequeno:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno = bolo_vulcao_creme_de_ninho_com_morango_pequeno * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_com_morango_pequeno = quantos

    elif 'creme de ninho com nutella p' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_nutella_pequeno:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno = bolo_vulcao_creme_de_ninho_com_nutella_pequeno * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_com_nutella_pequeno = quantos

    elif 'creme de ninho g' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_grande:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_grande = bolo_vulcao_creme_de_ninho_grande * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_grande:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_grande = quantos

    elif 'creme de ninho com morango g' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_morango_grande:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_com_morango_grande = bolo_vulcao_creme_de_ninho_com_morango_grande * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_grande:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_com_morango_grande = quantos

    elif 'creme de ninho com nutella g' in tipo:
        print(f'{tipo} R${bolo_vulcao_creme_de_ninho_com_nutella_grande:.2f}')
        resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande = bolo_vulcao_creme_de_ninho_com_nutella_grande * quantos
        print(f'{quantos} unidade(s) de {tipo}: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande:.2f}')
        quantos_bolo_vulcao_creme_de_ninho_com_nutella_grande = quantos

    else:
        print(f' {tipo} não encontrado, tente novamente.')

    

    print('')
    if quantos >= 0:
        
        valor_total = resultado_total = resultado_limao + resultado_ninho_trufado_com_nutella + resultado_geleia_de_morango + resultado_maracuja + resultado_pistache + resultado_physalis + resultado_brigadeiro_gourmet + resultado_caramelo_salgado + resultado_surpresa_de_uva + resultado_cereja + resultado_camafeu_de_nozes + resultado_creme_brulee_com_nozes + resultado_ganache_branco_com_morango + resultado_ganache_ao_leite_com_praline + resultado_trufa_meio_amarga + resultado_frutas_vermelhas + resultado_trufa_de_coco + resultado_beijinho + resultado_leite_ninho + resultado_amendoim + resultado_bicho_de_pe_morango + resultado_casadinho + resultado_tradicional_com_amendoim + resultado_olho_de_sogra_ameixa + resultado_damasco + resultado_creme_brulee + resultado_tradicional + resultado_churros + resultado_tradicional_dourado + resultado_ninho_com_nutella + resultado_mini_cupcakes_chantininho_glitter + resultado_mini_cupcakes_pasta_americana + resultado_mini_brownie + resultado_pirulito_de_chocolate + resultado_bolo_vulcao_creme_de_ninho_pequeno + resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno + resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno + resultado_bolo_vulcao_creme_de_ninho_grande + resultado_bolo_vulcao_creme_de_ninho_com_morango_grande + resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande
        
        print(f'Total: R${valor_total:.2f}')
        
# Doces Finos
    if resultado_limao > 0:
        print(f'{quantos_limao} - Limão: R${resultado_limao:.2f}')
    if resultado_ninho_trufado_com_nutella > 0:
        print(f'{quantos_ninho_trufado_com_nutella} - Ninho Trufado com Nutella: R${resultado_ninho_trufado_com_nutella:.2f}')
    if resultado_geleia_de_morango > 0:
        print(f'{quantos_geleia_de_morango} - Geleia de Morango: R${resultado_geleia_de_morango:.2f}')
    if resultado_maracuja > 0:
        print(f'{quantos_maracuja} - Maracujá: R${resultado_maracuja:.2f}')
    if resultado_pistache > 0:
        print(f'{quantos_pistache} - Pistache: R${resultado_pistache:.2f}')
    if resultado_physalis > 0:
        print(f'{quantos_physalis} - Physalis: R${resultado_physalis:.2f}')
    if resultado_brigadeiro_gourmet > 0:
        print(f'{quantos_brigadeiro_gourmet} - Brigadeiro Gourmet: R${resultado_brigadeiro_gourmet:.2f}')
    if resultado_caramelo_salgado > 0:
        print(f'{quantos_caramelo_salgado} - Caramelo Salgado: R${resultado_caramelo_salgado:.2f}')
    if resultado_surpresa_de_uva > 0:
        print(f'{quantos_surpresa_de_uva} - Surpresa de Uva: R${resultado_surpresa_de_uva:.2f}')
    if resultado_cereja > 0:
        print(f'{quantos_cereja} - Cereja: R${resultado_cereja:.2f}')
    if resultado_camafeu_de_nozes > 0:
        print(f'{quantos_camafeu_de_nozes} - Camafeu de Nozes: R${resultado_camafeu_de_nozes:.2f}')
    if resultado_creme_brulee_com_nozes > 0:
        print(f'{quantos_creme_brulee_com_nozes} - Creme Brulée com Nozes: R${resultado_creme_brulee_com_nozes:.2f}')
    if resultado_ganache_branco_com_morango > 0:
        print(f'{quantos_ganache_branco_com_morango} - Ganache Branco com Morango: R${resultado_ganache_branco_com_morango:.2f}')
    if resultado_ganache_ao_leite_com_praline > 0:
        print(f'{quantos_ganache_ao_leite_com_praline} - Ganache ao Leite com Praliné: R${resultado_ganache_ao_leite_com_praline:.2f}')
    if resultado_trufa_meio_amarga > 0:
        print(f'{quantos_trufa_meio_amarga} - Trufa Meio Amarga: R${resultado_trufa_meio_amarga:.2f}')
    if resultado_frutas_vermelhas > 0:
        print(f'{quantos_frutas_vermelhas} - Frutas Vermelhas: R${resultado_frutas_vermelhas:.2f}')
    if resultado_trufa_de_coco > 0:
        print(f'{quantos_trufa_de_coco} - Trufa de Coco: R${resultado_trufa_de_coco:.2f}')
# Brigadeiros Gourmet    
    if resultado_beijinho > 0:
        print(f'{quantos_beijinho} - Beijinho: R${resultado_beijinho:.2f}')
    if resultado_leite_ninho > 0:
        print(f'{quantos_leite_ninho} - Leite Ninho: R${resultado_leite_ninho:.2f}')
    if resultado_amendoim > 0:
        print(f'{quantos_amendoim} - Amendoim: R${resultado_amendoim:.2f}')
    if resultado_bicho_de_pe_morango > 0:
        print(f'{quantos_bicho_de_pe_morango} - Bicho de Pé Morango: R${resultado_bicho_de_pe_morango:.2f}')
    if resultado_casadinho > 0:
        print(f'{quantos_casadinho} - Casadinho: R${resultado_casadinho:.2f}')
    if resultado_tradicional_com_amendoim > 0:
        print(f'{quantos_tradicional_com_amendoim} - Tradicional com Amendoim: R${resultado_tradicional_com_amendoim:.2f}')
    if resultado_olho_de_sogra_ameixa > 0:
        print(f'{quantos_olho_de_sogra_ameixa} - Olho de Sogra Ameixa: R${resultado_olho_de_sogra_ameixa:.2f}')
    if resultado_damasco > 0:
        print(f'{quantos_damasco} - Damasco: R${resultado_damasco:.2f}')
    if resultado_creme_brulee > 0:
        print(f'{quantos_creme_brulee} - Creme Brulée: R${resultado_creme_brulee:.2f}')
    if resultado_tradicional > 0:
        print(f'{quantos_tradicional} - Tradicional: R${resultado_tradicional:.2f}')
    if resultado_churros > 0:
        print(f'{quantos_churros} - Churros: R${resultado_churros:.2f}')
    if resultado_tradicional_dourado > 0:
        print(f'{quantos_tradicional_dourado} - Tradicional Dourado: R${resultado_tradicional_dourado:.2f}')
    if resultado_ninho_com_nutella > 0:
        print(f'{quantos_ninho_com_nutella} - Ninho com Nutella: R${resultado_ninho_com_nutella:.2f}')
# Mini Cup
    if resultado_mini_cupcakes_chantininho_glitter > 0:
        print(f'{quantos_mini_cupcakes_chantininho_glitter} - Mini Brownie: R${resultado_mini_cupcakes_chantininho_glitter:.2f}')
    if resultado_mini_cupcakes_pasta_americana > 0:
        print(f'{quantos_mini_cupcakes_pasta_americana} - Mini Brownie: R${resultado_mini_cupcakes_pasta_americana:.2f}')    
# Mini Brownie
    if resultado_mini_brownie > 0:
        print(f'{quantos_mini_brownie} - Mini Brownie: R${resultado_mini_brownie:.2f}')
# Pirulitos
    if resultado_pirulito_de_chocolate > 0:
        print(f'{quantos_pirulito_de_chocolate} - Pirulito de Chocolate: R${resultado_pirulito_de_chocolate:.2f}')
# Bolo Vulcão 
    if resultado_bolo_vulcao_creme_de_ninho_pequeno > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_pequeno} - Bolo Vulcão Creme de Ninho P: R${resultado_bolo_vulcao_creme_de_ninho_pequeno:.2f}')
    if resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_com_morango_pequeno} - Bolo Vulcão Creme de Ninho com Morango P: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_pequeno:.2f}')
    if resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_com_nutella_pequeno} - Bolo Vulcão Creme de Ninho com Nutella P: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_pequeno:.2f}')
    if resultado_bolo_vulcao_creme_de_ninho_grande > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_grande} - Bolo Vulcão Creme de Ninho G: R${resultado_bolo_vulcao_creme_de_ninho_grande:.2f}')
    if resultado_bolo_vulcao_creme_de_ninho_com_morango_grande > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_com_morango_grande} - Bolo Vulcão Creme de Ninho com Morango G: R${resultado_bolo_vulcao_creme_de_ninho_com_morango_grande:.2f}')
    if resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande > 0:
        print(f'{quantos_bolo_vulcao_creme_de_ninho_com_nutella_grande} - Bolo Vulcão Creme de Ninho com Nutella G: R${resultado_bolo_vulcao_creme_de_ninho_com_nutella_grande:.2f}')


