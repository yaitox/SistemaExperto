import tkinter as tk

def Screen(root, name, size):
    root.title(name)
    root.geometry(size)
    
    return root

def ChangeColor(item, on : bool):
    canvas.itemconfig(item, fill = 'green' if on else 'red')
    
def ResetColors():
    for rule in rules:
        ChangeColor(rule, False)
        
def CreateRules():
    x = 20
    y = 20
    r1 = 75
    r2 = 75
    
    textX = 47.5
    textY = 47.5
    for i in range(1, 21):
        rule = canvas.create_oval(x, y, r1, r2, fill = 'red')
        rules.append(rule)
        canvas.create_text(textX, textY, text = ('R%d' % i), font = ('consolas 12 bold'))
        
        y += 60
        r2 += 60
        textY += 60
        
        if i % 5 == 0:
            y = 20
            r2 = 75
            textY = 47.5
            
            x += 170
            r1 += 170
            textX += 170
        
def FitotoxicidadPesticidas():
    global timeDiff
    sick = False
    
    if ausenciaMoho.get():
        ChangeColor(rules[1], True)
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[1], True))
        sick = True
    
    if colorMarron.get() and hinchazonAnormal.get():
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[0], True))
        sick = True
    
    return sick

def PudricionRaizBaseTronco():
    global timeDiff
    
    patogeno = False
    bulbaAzulada = False
    aspectoMoribundo = False
    noExpandeFoliculos = False
    
    if malDrenaje.get() and sueloMalCompactado.get():
        patogeno = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[5], True))
        print("La palmera presenta un patogeno")
    
    if raicesPodridas.get() and colorMarronOscuro.get():
        bulbaAzulada = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[6], True))
        print("La palmera presenta una bulba azulada")
        
    if amarilloHojaBaseCorona.get() and detenerCrecimiento.get():
        aspectoMoribundo = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[7], True))
        print("La palmera presenta un aspecto moribundo")
        
    if pudricionRacimos.get() and abortoInflorecencias.get():
        noExpandeFoliculos = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[8], True))
        print("La palmera no expande foliculos")
        
    return patogeno and bulbaAzulada and aspectoMoribundo and noExpandeFoliculos

def PudricionBasalTronco():
    global timeDiff
    
    ganodermaLucidum = False
    hojasBajerasSecas = False
    tejidoInvadido = False
    
    if orejasPalo.get() and producenFructificaciones.get():
        ganodermaLucidum = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[9], True))
        print("La palmera tiene Ganoderma Lucidum")
    
    if caraInferiorPerforada.get() and numeroFlechasPerforadas.get():
        hojasBajerasSecas = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[10], True))
        print("La palmera tiene las hojas bajeras secas")
        
    if tejidoColorMarronClaro.get() and tejidoConBandasOscurasIrregulares.get():
        tejidoInvadido = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[11], True))
        print("La palmera tiene el tejido invadido")
        
    return ganodermaLucidum and hojasBajerasSecas and tejidoInvadido

def ManchasFoliares():
    global timeDiff
    
    hongoPatogenoPestalotiopsis = False
    secamientoHojas = False
    puntosNegrosHongos = False
    botryodiplodia = False
    melanconium = False
    
    if insectoTingidae.get():
        hongoPatogenoPestalotiopsis = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[12], True))
        print("La palmera tiene el hongo patógeno Pestalotiopsis")
        
    if perdidaFollaje.get() and disminucionRendimiento.get():
        secamientoHojas = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[13], True))
        print("La palmera tiene secamiento de hojas")
        
    if manchaGris.get() and tejidoNecrosanado.get():
        puntosNegrosHongos = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[14], True))
        print("La palmera tiene puntos negros por hongos")
        
    if manchasSecas.get() and centroGris.get():
        botryodiplodia = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[2], True))
        print("La palmera tiene la bacteria Botryodiplodia")
        
    if aumentaTamano.get() and puntosNegrosPequenos.get():
        botryodiplodia = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[3], True))
        print("La palmera tiene la bacteria Botryodiplodia")
        
    if colorMarronClaro.get() and bordeAmarilloPalido.get():
        melanconium = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[4], True))
        print("La palmera tiene la bacteria Melanconium")
        
    return hongoPatogenoPestalotiopsis and secamientoHojas and puntosNegrosHongos and botryodiplodia and melanconium

def PudricionLetalYCogollo():
    global timeDiff
    
    flechaDesgaja = False
    hojasSecas = False
    clorosis = False
    
    sick = False
    
    if pudricionFlechas.get():
        sick = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[15], True))
    
    if areaPocoDrenaje.get() and suelosCompactos.get():
        sick = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[19], True))
    
    if tejidoMeristematicoMarronOscuro.get() and pudricionHumeda.get():
        flechaDesgaja = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[16], True))
        print("La palmera tiene la flecha desgajada")
        
    if hojaCoronaVerdeAmarillo.get():
        hojasSecas = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[17], True))
        print("Las hojas de la palmera se comenzarán a secar")
        
    if foliosCompactos.get() and centroCoronaAmarilloBrillante.get():
        clorosis = True
        timeDiff += 1000
        screen.after(timeDiff, lambda: ChangeColor(rules[18], True))
        print("La palmera tiene clorosis")
        
    if sick:
        return True
    
    return flechaDesgaja and hojasSecas and clorosis

def ReconocerEnfermad():
    global timeDiff
    
    ResetColors()
    timeDiff = 0
    
    if FitotoxicidadPesticidas():
        print("La palmera tiene la enfermedad de fitotoxicidad por pesticidas")
        print("Prevencion: tratar a la palmera con productos a base de BHC-gama, cobre y mercurio.")
    
    if PudricionRaizBaseTronco():
        print("La palmera presenta la enfermedad de pudriciones de las raices y base del tronco")
        print("Prevencion: TODO")
    
    if PudricionBasalTronco():
        print("La palmera presenta la enfermedad de pudricion del basal del tronco")
        print("Prevencion: TODO")
        
    if ManchasFoliares():
        print("La palmera presenta la enfermedad de manchas foliares")
        print("Prevencion: TODO")
        
    if PudricionLetalYCogollo():
        print("La palmera presenta la enfermedad de pudricion letal y del cogollo")
        print("Prevencion: TODO")

if __name__ == "__main__":
    screen = Screen(tk.Tk(), 'Sistema Experto', '1920x1080')
    
    ''' Variables '''
    # Fitotoxicidad por pesticidas
    colorMarron = tk.IntVar()
    hinchazonAnormal = tk.IntVar()
    ausenciaMoho = tk.IntVar()
    rules = []
    timeDiff = 0
    
    # Manchas foliares
    insectoTingidae = tk.IntVar()
    perdidaFollaje = tk.IntVar()
    disminucionRendimiento = tk.IntVar()
    manchaGris = tk.IntVar()
    tejidoNecrosanado = tk.IntVar()
    manchasSecas = tk.IntVar()
    centroGris = tk.IntVar()
    aumentaTamano = tk.IntVar()
    puntosNegrosPequenos = tk.IntVar()
    colorMarronClaro = tk.IntVar()
    bordeAmarilloPalido = tk.IntVar()
    
    # Pudricion de raiz y base de tronco
    malDrenaje = tk.IntVar()
    sueloMalCompactado = tk.IntVar()
    raicesPodridas = tk.IntVar()
    colorMarronOscuro = tk.IntVar()
    amarilloHojaBaseCorona = tk.IntVar()
    detenerCrecimiento = tk.IntVar()
    pudricionRacimos = tk.IntVar()
    abortoInflorecencias = tk.IntVar()
    
    # Pudricion basal de tronco
    orejasPalo = tk.IntVar()
    producenFructificaciones = tk.IntVar()
    caraInferiorPerforada = tk.IntVar()
    numeroFlechasPerforadas = tk.IntVar()
    tejidoColorMarronClaro = tk.IntVar()
    tejidoConBandasOscurasIrregulares  = tk.IntVar()
    
    # Pudricion letal y del cogollo
    pudricionFlechas = tk.IntVar()
    tejidoMeristematicoMarronOscuro = tk.IntVar()
    pudricionHumeda = tk.IntVar()
    hojaCoronaVerdeAmarillo = tk.IntVar()
    foliosCompactos = tk.IntVar()
    centroCoronaAmarilloBrillante = tk.IntVar()
    areaPocoDrenaje = tk.IntVar()
    suelosCompactos = tk.IntVar()
    
    ''' Label '''
    tk.Label(screen, text = 'Entradas', font = ('consolas 40 bold')).place(x = 20, y = 850)
    tk.Label(screen, text = 'Simulacion', font = ('consolas 40 bold')).place(x = 700, y = 850)
    tk.Label(screen, text = 'Resultados', font = ('consolas 40 bold')).place(x = 1450, y = 850)
    
    ''' Buttons '''
    btnReconocerEnfermedad = tk.Button(screen, text = 'Reconocer enfermedad', command = ReconocerEnfermad, width = 20)
    btnReconocerEnfermedad.place(x = 20, y = 800)

    ''' Checkboxes '''
    
    # Fitotoxicidad por pesticidas
    chkColorMarron = tk.Checkbutton(screen, text = 'Color marron', variable = colorMarron)
    chkColorMarron.place(x = 0, y = 10)
    
    chkHinchazonAnormal = tk.Checkbutton(screen, text = 'Hinchazon anormal', variable = hinchazonAnormal)
    chkHinchazonAnormal.place(x = 0, y = 30)
    
    chkAusenciaMoho = tk.Checkbutton(screen, text = 'Ausencia de moho', variable = ausenciaMoho)
    chkAusenciaMoho.place(x = 0, y = 50)
    
    # Pudricion de las raices y base del tronco
    chkMalDrenaje = tk.Checkbutton(screen, text = 'Condiciones con mal drenaje', variable = malDrenaje)
    chkMalDrenaje.place(x = 0, y = 70)
    
    chkSueloMalCompactado = tk.Checkbutton(screen, text = 'Suelo mal compactado', variable = sueloMalCompactado)
    chkSueloMalCompactado.place(x = 0, y = 90)
    
    chkRaicesPodridas = tk.Checkbutton(screen, text = 'Raices podridas', variable = raicesPodridas)
    chkRaicesPodridas.place(x = 0, y = 110)
    
    chkColorMarronOscuro = tk.Checkbutton(screen, text = 'Color marron oscuro', variable = colorMarronOscuro)
    chkColorMarronOscuro.place(x = 0, y = 130)
    
    chkAmarilloHojaBaseCorona = tk.Checkbutton(screen, text = 'Amarillamiento de hojas \nbase de corona', variable = amarilloHojaBaseCorona)
    chkAmarilloHojaBaseCorona.place(x = 0, y = 150)
    
    chkDetenerCrecimiento = tk.Checkbutton(screen, text = 'Crecimiento detenido', variable = detenerCrecimiento)
    chkDetenerCrecimiento.place(x = 0, y = 190)
    
    chkPudricionRacimos = tk.Checkbutton(screen, text = 'Pudricion de racimos', variable = pudricionRacimos)
    chkPudricionRacimos.place(x = 0, y = 210)
    
    chkAbortoInflorecencias = tk.Checkbutton(screen, text = 'Aborto de inflorecencias', variable = abortoInflorecencias)
    chkAbortoInflorecencias.place(x = 0, y = 230)
    
    # Pudricion basal del tronco    
    chkOrejasPalo = tk.Checkbutton(screen, text = 'Orejas de palo', variable = orejasPalo)
    chkOrejasPalo.place(x = 0, y = 250)
    
    chkProducenFructificaciones = tk.Checkbutton(screen, text = 'Produce fructificaciones', variable = producenFructificaciones)
    chkProducenFructificaciones.place(x = 0, y = 270)
    
    chkCaraInferiorPerforada = tk.Checkbutton(screen, text = 'Cara inferior perforada', variable = caraInferiorPerforada)
    chkCaraInferiorPerforada.place(x = 0, y = 290)
    
    chkNumeroFlechasPerforadas = tk.Checkbutton(screen, text = 'Tiene flechas perforadas', variable = numeroFlechasPerforadas)
    chkNumeroFlechasPerforadas.place(x = 0, y = 310)
    
    chkTejidoColorMarronClaro = tk.Checkbutton(screen, text = 'Tejido color marron claro', variable = tejidoColorMarronClaro)
    chkTejidoColorMarronClaro.place(x = 0, y = 330)
    
    chkTejidoConBandasOscurasIrregulares = tk.Checkbutton(screen, text = 'Tejido con bandas oscuras irregulares', variable = tejidoConBandasOscurasIrregulares)
    chkTejidoConBandasOscurasIrregulares.place(x = 0, y = 350)
    
    # Manchas foliares    
    chkInsectoTingidae = tk.Checkbutton(screen, text = 'Tiene el insecto Tingidae', variable = insectoTingidae)
    chkInsectoTingidae.place(x = 0, y = 370)
    
    chkPerdidaFollaje = tk.Checkbutton(screen, text = 'Perdida de follaje', variable = perdidaFollaje)
    chkPerdidaFollaje.place(x = 0, y = 390)
    
    chkDisminucionRendimiento = tk.Checkbutton(screen, text = 'Disminucion de rendimiento', variable = disminucionRendimiento)
    chkDisminucionRendimiento.place(x = 0, y = 410)
    
    chkManchaGris = tk.Checkbutton(screen, text = 'Manchas grises', variable = manchaGris)
    chkManchaGris.place(x = 0, y = 430)
    
    chkTejidoNecrosanado = tk.Checkbutton(screen, text = 'Tejido necrosanado', variable = tejidoNecrosanado)
    chkTejidoNecrosanado.place(x = 0, y = 450)
    
    chkManchasSecas = tk.Checkbutton(screen, text = 'Manchas secas', variable = manchasSecas)
    chkManchasSecas.place(x = 0, y = 470)
    
    chkCentroGris = tk.Checkbutton(screen, text = 'Centro color gris', variable = centroGris)
    chkCentroGris.place(x = 0, y = 490)
    
    chkAumentaTamano = tk.Checkbutton(screen, text = 'Aumento de tamaño', variable = aumentaTamano)
    chkAumentaTamano.place(x = 0, y = 510)
    
    chkPuntosNegrosPequenos = tk.Checkbutton(screen, text = 'Puntos negros pequeños', variable = puntosNegrosPequenos)
    chkPuntosNegrosPequenos.place(x = 0, y = 530)
    
    chkColorMarronClaro = tk.Checkbutton(screen, text = 'Color marrón claro', variable = colorMarronClaro)
    chkColorMarronClaro.place(x = 0, y = 550)
    
    chkBordeAmarilloPalido = tk.Checkbutton(screen, text = 'Borde amarillo pálido', variable = bordeAmarilloPalido)
    chkBordeAmarilloPalido.place(x = 0, y = 570)
    
    # Pudricion letal y del cogollo
    chkPudricionFlechas = tk.Checkbutton(screen, text = 'Pudrición de las flechas', variable = pudricionFlechas)
    chkPudricionFlechas.place(x = 0, y = 590)
    
    chkTejidoMeristematicoMarronOscuro = tk.Checkbutton(screen, text = 'Tejido meristemático de color marrón oscuro', variable = tejidoMeristematicoMarronOscuro)
    chkTejidoMeristematicoMarronOscuro.place(x = 0, y = 610)
    
    chkPudricionHumeda = tk.Checkbutton(screen, text = 'Pudrición humeda', variable = pudricionHumeda)
    chkPudricionHumeda.place(x = 0, y = 630)
    
    chkHojaCoronaVerdeAmarillo = tk.Checkbutton(screen, text = 'Hoja de corona color verde amarillo', variable = hojaCoronaVerdeAmarillo)
    chkHojaCoronaVerdeAmarillo.place(x = 0, y = 650)
    
    chkFoliosCompactos = tk.Checkbutton(screen, text = 'Folios compactos', variable = foliosCompactos)
    chkFoliosCompactos.place(x = 0, y = 670)
    
    chkCentroCoronaAmarilloBrillante = tk.Checkbutton(screen, text = 'Centro de corona de color amarillo brillante', variable = centroCoronaAmarilloBrillante)
    chkCentroCoronaAmarilloBrillante.place(x = 0, y = 690)
    
    chkAreaPocoDrenaje = tk.Checkbutton(screen, text = 'Area con poco drenaje', variable = areaPocoDrenaje)
    chkAreaPocoDrenaje.place(x = 0, y = 710)
    
    chkSuelosCompactos = tk.Checkbutton(screen, text = 'Suelos compactos', variable = suelosCompactos)
    chkSuelosCompactos.place(x = 0, y = 730)
    
    canvas = tk.Canvas(width = 650, height = 400)
    canvas.place(x = 500, y = 200)
    
    CreateRules()
    
    screen.mainloop()

