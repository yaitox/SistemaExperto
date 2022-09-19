import tkinter as tk

def Screen(root, name, size):
    root.title(name)
    root.geometry(size)
    
    return root

def FitotoxicidadPesticidas():
    global colorMarron
    global hinchazonAnormal
    global ausenciaMoho
    
    if ausenciaMoho.get():
        return True
    
    if colorMarron.get() and hinchazonAnormal.get():
        return True
    
    return False

def PudricionRaizBaseTronco():
    global malDrenaje
    global sueloMalCompactado
    global raicesPodridas
    global colorMarronOscuro
    global amarilloHojaBaseCorona
    global detenerCrecimiento
    global pudricionRacimos
    global abortoInflorecencias
    
    patogeno = False
    bulbaAzulada = False
    aspectoMoribundo = False
    noExpandeFoliculos = False
    
    if malDrenaje.get() and sueloMalCompactado.get():
        patogeno = True
        print("La palmera presenta un patogeno")
    
    if raicesPodridas.get() and colorMarronOscuro.get():
        bulbaAzulada = True
        print("La palmera presenta una bulba azulada")
        
    if amarilloHojaBaseCorona.get() and detenerCrecimiento.get():
        aspectoMoribundo = True
        print("La palmera presenta un aspecto moribundo")
        
    if pudricionRacimos.get() and abortoInflorecencias.get():
        noExpandeFoliculos = True
        print("La palmera no expande foliculos")
        
    return patogeno and bulbaAzulada and aspectoMoribundo and noExpandeFoliculos

def PudricionBasalTronco():
    global orejasPalo
    global producenFructificaciones
    global caraInferiorPerforada
    global numeroFlechasPerforadas
    global tejidoColorMarronClaro
    global tejidoConBandasOscurasIrregulares
    
    ganodermaLucidum = False
    hojasBajerasSecas = False
    tejidoInvadido = False
    
    if orejasPalo.get() and producenFructificaciones.get():
        ganodermaLucidum = True
        print("La palmera tiene Ganoderma Lucidum")
    
    if caraInferiorPerforada.get() and numeroFlechasPerforadas.get():
        hojasBajerasSecas = True
        print("La palmera tiene las hojas bajeras secas")
        
    if tejidoColorMarronClaro.get() and tejidoConBandasOscurasIrregulares.get():
        tejidoInvadido = True
        print("La palmera tiene el tejido invadido")
        
    return ganodermaLucidum and hojasBajerasSecas and tejidoInvadido

def ManchasFoliares():
    global insectoTingidae
    global perdidaFollaje
    global disminucionRendimiento
    global manchaGris
    global tejidoNecrosanado
    global manchasSecas
    global centroGris
    global aumentaTamano
    global puntosNegrosPequenos
    global colorMarronClaro
    global bordeAmarilloPalido
    
    hongoPatogenoPestalotiopsis = False
    secamientoHojas = False
    puntosNegrosHongos = False
    botryodiplodia = False
    melanconium = False
    
    if insectoTingidae.get():
        hongoPatogenoPestalotiopsis = True
        print("La palmera tiene el hongo patógeno Pestalotiopsis")
        
    if perdidaFollaje.get() and disminucionRendimiento.get():
        secamientoHojas = True
        print("La palmera tiene secamiento de hojas")
        
    if manchaGris.get() and tejidoNecrosanado.get():
        puntosNegrosHongos = True
        print("La palmera tiene puntos negros por hongos")
        
    if (manchasSecas.get() and centroGris.get()) or (aumentaTamano.get() and puntosNegrosPequenos.get()):
        botryodiplodia = True
        print("La palmera tiene la bacteria Botryodiplodia")
        
    if colorMarronClaro.get() and bordeAmarilloPalido.get():
        melanconium = True
        print("La palmera tiene la bacteria Melanconium")
        
    return hongoPatogenoPestalotiopsis and secamientoHojas and puntosNegrosHongos and botryodiplodia and melanconium

def PudricionLetalYCogollo():
    global pudricionFlechas
    global tejidoMeristematicoMarronOscuro
    global pudricionHumeda
    global hojaCoronaVerdeAmarillo
    global foliosCompactos
    global centroCoronaAmarilloBrillante
    global areaPocoDrenaje
    global suelosCompactos
    
    flechaDesgaja = False
    hojasSecas = False
    clorosis = False
    
    if pudricionFlechas.get():
        return True
    
    if areaPocoDrenaje.get() and suelosCompactos.get():
        return True
    
    if tejidoMeristematicoMarronOscuro.get() and pudricionHumeda.get():
        flechaDesgaja = True
        print("La palmera tiene la flecha desgajada")
        
    if hojaCoronaVerdeAmarillo.get():
        hojasSecas = True
        print("Las hojas de la palmera se comenzarán a secar")
        
    if foliosCompactos.get() and centroCoronaAmarilloBrillante.get():
        clorosis = True
        print("La palmera tiene clorosis")
        
    return flechaDesgaja and hojasSecas and clorosis

def ReconocerEnfermad():
    if FitotoxicidadPesticidas():
        print("La palmera tiene la enfermedad de fitotoxicidad por pesticidas")
        print("Prevencion: tratar a la palmera con productos a base de BHC-gama, cobre y mercurio.")
    
    elif PudricionRaizBaseTronco():
        print("La palmera presenta la enfermedad de pudriciones de las raices y base del tronco")
        print("Prevencion: TODO")
    
    elif PudricionBasalTronco():
        print("La palmera presenta la enfermedad de pudricion del basal del tronco")
        print("Prevencion: TODO")
        
    elif ManchasFoliares():
        print("La palmera presenta la enfermedad de manchas foliares")
        print("Prevencion: TODO")
        
    elif PudricionLetalYCogollo():
        print("La palmera presenta la enfermedad de pudricion letal y del cogollo")
        print("Prevencion: TODO")
        
    else:
        print("Enfermedad no reconocida.\n")

if __name__ == "__main__":
    screen = Screen(tk.Tk(), 'Sistema Experto', '750x300')
    
    ''' Variables '''
    # Fitotoxicidad por pesticidas
    colorMarron = tk.IntVar()
    hinchazonAnormal = tk.IntVar()
    ausenciaMoho = tk.IntVar()
    
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
    
    
    ''' Buttons '''
    btnReconocerEnfermedad = tk.Button(screen, text = 'Reconocer enfermedad', command = ReconocerEnfermad, width = 20)
    btnReconocerEnfermedad.place(x = 500, y = 200)

    ''' Checkboxes '''
    
    # Fitotoxicidad por pesticidas
    chkColorMarron = tk.Checkbutton(screen, text = 'Color marron', variable = colorMarron)
    chkColorMarron.place(x = 0, y = 10)
    
    chkHinchazonAnormal = tk.Checkbutton(screen, text = 'Hinchazon anormal', variable = hinchazonAnormal)
    chkHinchazonAnormal.place(x = 0, y = 30)
    
    chkAusenciaMoho = tk.Checkbutton(screen, text = 'Ausencia de moho', variable = ausenciaMoho)
    chkAusenciaMoho.place(x = 0, y = 50)
    
    ''' ################################################## '''
    
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
    
    ''' ################################################## '''
    
    # Pudricion basal del tronco    
    chkOrejasPalo = tk.Checkbutton(screen, text = 'Orejas de palo', variable = orejasPalo)
    chkOrejasPalo.place(x = 240, y = 10)
    
    chkProducenFructificaciones = tk.Checkbutton(screen, text = 'Produce fructificaciones', variable = producenFructificaciones)
    chkProducenFructificaciones.place(x = 240, y = 30)
    
    chkCaraInferiorPerforada = tk.Checkbutton(screen, text = 'Cara inferior perforada', variable = caraInferiorPerforada)
    chkCaraInferiorPerforada.place(x = 240, y = 50)
    
    chkNumeroFlechasPerforadas = tk.Checkbutton(screen, text = 'Tiene flechas perforadas', variable = numeroFlechasPerforadas)
    chkNumeroFlechasPerforadas.place(x = 240, y = 70)
    
    chkTejidoColorMarronClaro = tk.Checkbutton(screen, text = 'Tejido color marron claro', variable = tejidoColorMarronClaro)
    chkTejidoColorMarronClaro.place(x = 240, y = 90)
    
    chkTejidoConBandasOscurasIrregulares = tk.Checkbutton(screen, text = 'Tejido con bandas oscuras irregulares', variable = tejidoConBandasOscurasIrregulares)
    chkTejidoConBandasOscurasIrregulares.place(x = 240, y = 110)
    
    ''' ################################################## '''
    
    # Manchas foliares
    bordeAmarilloPalido = tk.IntVar()
    
    chkInsectoTingidae = tk.Checkbutton(screen, text = 'Tiene el insecto Tingidae', variable = insectoTingidae)
    chkInsectoTingidae.place(x = 240, y = 130)
    
    chkPerdidaFollaje = tk.Checkbutton(screen, text = 'Perdida de follaje', variable = perdidaFollaje)
    chkPerdidaFollaje.place(x = 240, y = 150)
    
    chkDisminucionRendimiento = tk.Checkbutton(screen, text = 'Disminucion de rendimiento', variable = disminucionRendimiento)
    chkDisminucionRendimiento.place(x = 240, y = 170)
    
    chkManchaGris = tk.Checkbutton(screen, text = 'Manchas grises', variable = manchaGris)
    chkManchaGris.place(x = 240, y = 190)
    
    chkTejidoNecrosanado = tk.Checkbutton(screen, text = 'Tejido necrosanado', variable = tejidoNecrosanado)
    chkTejidoNecrosanado.place(x = 240, y = 210)
    
    chkManchasSecas = tk.Checkbutton(screen, text = 'Manchas secas', variable = manchasSecas)
    chkManchasSecas.place(x = 500, y = 10)
    
    chkCentroGris = tk.Checkbutton(screen, text = 'Centro color gris', variable = centroGris)
    chkCentroGris.place(x = 500, y = 30)
    
    chkAumentaTamano = tk.Checkbutton(screen, text = 'Aumento de tamaño', variable = aumentaTamano)
    chkAumentaTamano.place(x = 500, y = 50)
    
    chkPuntosNegrosPequenos = tk.Checkbutton(screen, text = 'Puntos negros pequeños', variable = puntosNegrosPequenos)
    chkPuntosNegrosPequenos.place(x = 500, y = 70)
    
    chkColorMarronClaro = tk.Checkbutton(screen, text = 'Color marrón claro', variable = colorMarronClaro)
    chkColorMarronClaro.place(x = 500, y = 90)
    
    chkBordeAmarilloPalido = tk.Checkbutton(screen, text = 'Borde amarillo pálido', variable = bordeAmarilloPalido)
    chkBordeAmarilloPalido.place(x = 500, y = 110)
    
    ''' ################################################## '''
    
    # Pudricion letal y del cogollo
    chkPudricionFlechas = tk.Checkbutton(screen, text = 'Pudrición de las flechas', variable = pudricionFlechas)
    chkPudricionFlechas.place(x = 500, y = 130)
    
    chkTejidoMeristematicoMarronOscuro = tk.Checkbutton(screen, text = 'Tejido meristemático de color marrón oscuro', variable = tejidoMeristematicoMarronOscuro)
    chkTejidoMeristematicoMarronOscuro.place(x = 500, y = 150)
    
    chkPudricionHumeda = tk.Checkbutton(screen, text = 'Pudrición humeda', variable = pudricionHumeda)
    chkPudricionHumeda.place(x = 500, y = 170)
    
    chkHojaCoronaVerdeAmarillo = tk.Checkbutton(screen, text = 'Hoja de corona color verde amarillo', variable = hojaCoronaVerdeAmarillo)
    chkHojaCoronaVerdeAmarillo.place(x = 500, y = 190)
    
    chkFoliosCompactos = tk.Checkbutton(screen, text = 'Folios compactos', variable = foliosCompactos)
    chkFoliosCompactos.place(x = 500, y = 210)
    
    chkCentroCoronaAmarilloBrillante = tk.Checkbutton(screen, text = 'Centro de corona de color amarillo brillante', variable = centroCoronaAmarilloBrillante)
    chkCentroCoronaAmarilloBrillante.place(x = 500, y = 230)
    
    chkAreaPocoDrenaje = tk.Checkbutton(screen, text = 'Area con poco drenaje', variable = areaPocoDrenaje)
    chkAreaPocoDrenaje.place(x = 500, y = 250)
    
    chkSuelosCompactos = tk.Checkbutton(screen, text = 'Suelos compactos', variable = suelosCompactos)
    chkSuelosCompactos.place(x = 500, y = 270)
    
    screen.mainloop()

