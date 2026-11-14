# Selección de artículos del Règlement Tome 1 (zona UG) por tipo de proyecto.
# Cada grupo: (título, [(código, qué comprobar), ...])
PROYECTOS = [
 {
  'id': 'ite',
  'nom': 'Renovación energética',
  'sub': 'Aislamiento por el exterior (ITE) de muros y cubierta, cambio de carpinterías, protecciones solares, paneles o PAC en un edificio existente.',
  'tramite': [
    'Déclaration préalable (DP): modifica el aspecto exterior. En París el ravalement también va siempre en DP.',
    'No hace falta arquitecto para una DP.',
    'Si el edificio está en un sitio patrimonial o cerca de un monumento histórico, el ABF da su opinión y el plazo pasa de 1 a 2 meses.',
  ],
  'antes': [
    'Atlas del PLU: ¿el edificio está protegido (BP, EPP) o tiene Volumetría existente a conservar (VEC)?',
    '¿El edificio cumple el PLU actual? Si no, mira G-II.2: las obras de mejora energética se admiten igualmente.',
    'Espesor del aislamiento sobre la calle: puede invadir la vía pública (saillie).',
  ],
  'grupos': [
    ('Edificio existente y protecciones', [
      ('G-II.2', 'Obras de mejora energética admitidas aunque el edificio no sea conforme'),
      ('UG.2.4.1', 'Edificio o elemento protegido: aislar sin alterar lo protegido'),
      ('UG.2.4.2', 'VEC: solo se admiten adaptaciones menores del volumen'),
    ]),
    ('Aspecto exterior', [
      ('UG.2.1.1', 'Inserción urbana: criterio general de aceptación o rechazo'),
      ('UG.2.3.1', 'Respetar el carácter de la fachada; carpinterías, barandillas y persianas'),
      ('UG.2.3.2', 'ITE admitida si el resultado es satisfactorio; no pintar piedra de taille, conservar modénatures'),
      ('UG.2.3.3', 'Cubierta existente: lucarnas, paneles solares, PAC con integración cuidada'),
      ('UG.2.1.7', 'Salientes (brise-soleil, etc.): principios estéticos'),
    ]),
    ('Volumen y salientes', [
      ('UG.3.3.1', 'La ITE y el realce de cubierta (≤ 3 m) pueden superar alturas y gabarits'),
      ('UG.3.3.8', 'Saliente de la ITE sobre la vía pública: dimensiones máximas'),
      ('UG.3.3.9', 'Salientes hacia el interior de la parcela'),
    ]),
    ('Rendimiento energético', [
      ('UG.5.2.1', 'Mejorar la calidad bioclimática; materiales compatibles con lo existente'),
      ('UG.5.2.2', 'Objetivos: R ≥ 5 en muros, R ≥ 10 en cubierta, Uw ≤ 1,4 en ventanas'),
      ('UG.5.2.3', 'Protecciones solares exteriores en fachadas soleadas; conservar persianas'),
      ('UG.5.2.4', 'Integrar energías renovables en rehabilitaciones significativas'),
      ('UG.5.2.5', 'Materiales de reempleo, reciclados o biosourcés'),
    ]),
    ('Cubierta vegetada (si se rehace la cubierta)', [
      ('UG.4.2.2', 'Sustrato ≥ 15 cm en cubierta existente; acceso de mantenimiento'),
    ]),
  ],
 },
 {
  'id': 'casa',
  'nom': 'Casa nueva',
  'sub': 'Vivienda unifamiliar de obra nueva en una parcela de la zona UG.',
  'tramite': [
    'Permis de construire de maison individuelle (PCMI).',
    'Arquitecto obligatorio si la superficie de plancher supera 150 m².',
    'RE2020 obligatoria (attestation al depositar el PC y al terminar la obra).',
  ],
  'antes': [
    'Atlas del PLU: altura máxima del Plan général des hauteurs, filets de couleur, prescripciones de vegetación (EVP, EBC…).',
    'Superficie del terreno: fija los espacios libres mínimos (UG.4.1.1).',
    'Si supera 150 m² de SDP: bicis (UG.7.2.3) y externalidades positivas (UG.8.1).',
  ],
  'grupos': [
    ('Implantación', [
      ('UG.3.1.1', 'Respecto a la calle: en la alineación o retranqueo'),
      ('UG.3.1.2', 'Respecto a linderos: medianera en la banda de 18 m; 6 m / 3 m si hay huecos'),
      ('UG.3.1.3', 'Entre construcciones en la misma parcela'),
      ('UG.3.1.4', 'Emprise au sol: solo en ECM y algunos sectores'),
    ]),
    ('Altura y gabarits', [
      ('UG.3.2.1', 'Altura máxima del Plan général; 15 m fuera de la banda de 18 m'),
      ('UG.3.2.4', 'Gabarit sobre calle (H = P + 25 % P)'),
      ('UG.3.2.5', 'Gabarit en linderos'),
      ('UG.3.2.8', 'Inserción en la secuencia de la calle'),
      ('UG.3.3.1', 'Elementos que pueden superar la altura (EnR, barandillas, chimeneas…)'),
    ]),
    ('Arquitectura', [
      ('UG.2.1.1', 'Inserción urbana y paisajística'),
      ('UG.2.1.2', 'Cada pieza principal con un hueco de éclairement premier'),
      ('UG.2.2.2', 'Materiales y colores; priorizar biosourcés y géosourcés'),
      ('UG.2.2.3', 'Integrar paneles e instalaciones en la cubierta'),
      ('UG.2.1.5', 'Valla a la calle: ≤ 2,10 m'),
      ('UG.2.1.6', 'Valla entre vecinos: ≤ 3,20 m'),
    ]),
    ('Espacios libres y vegetación', [
      ('UG.4.1.1', 'Superficie mínima de espacios libres según el tamaño del terreno'),
      ('UG.4.1.2', 'Espacios libres en pleine terre, de una pieza y al nivel del suelo'),
      ('UG.4.1.3', 'Árboles y densidad de plantación'),
      ('UG.4.2.1', 'Índice de vegetación del edificio (IVB) ≥ 3'),
      ('UG.4.2.2', 'Cubierta vegetada: sustrato ≥ 25 cm'),
    ]),
    ('Bioclimatismo', [
      ('UG.5.1.1', 'Principios bioclimáticos y ventilación natural'),
      ('UG.5.1.3', 'Confort de verano: protecciones solares exteriores'),
      ('UG.5.1.4', 'Energías renovables obligatorias salvo imposibilidad'),
      ('UG.5.1.5', 'Carbono: materiales biosourcés y reempleo'),
    ]),
    ('Redes, acceso y otros', [
      ('UG.6.1.2', 'Agua de lluvia gestionada en la parcela'),
      ('UG.7.1.2', 'Accesos desde la calle'),
      ('UG.7.2.3', 'Aparcamiento de bicis (si > 150 m² SDP)'),
      ('UG.8.1', 'Externalidades positivas (si > 150 m² SDP)'),
    ]),
  ],
 },
 {
  'id': 'colectivo',
  'nom': 'Edificio colectivo nuevo',
  'sub': 'Edificio de viviendas de obra nueva, con o sin locales en planta baja.',
  'tramite': [
    'Permis de construire (PC).',
    'Arquitecto obligatorio.',
    'RE2020 con las exigencias reforzadas del PLU para vivienda colectiva (Bbio, Cep,nr, DH, carbono).',
  ],
  'antes': [
    'Atlas del PLU: altura máxima, filets de couleur, protección del comercio en planta baja, emplacements réservés.',
    'Zona de déficit de vivienda social: fija el porcentaje a partir de 500 m² de SDP (UG.1.5.1).',
    'Superficie del terreno: fija los espacios libres mínimos (UG.4.1.1).',
  ],
  'grupos': [
    ('Programa', [
      ('UG.1.4.1', 'Reequilibrio vivienda / empleo según el sector'),
      ('UG.1.4.2', 'Protección del comercio en planta baja'),
      ('UG.1.5.1', 'Vivienda social o BRS a partir de 500 m² de SDP'),
    ]),
    ('Implantación', [
      ('UG.3.1.1', 'Respecto a la calle: en la alineación o retranqueo'),
      ('UG.3.1.2', 'Respecto a linderos: medianera en la banda de 18 m; 6 m / 3 m si hay huecos'),
      ('UG.3.1.3', 'Distancias entre edificios en la misma parcela'),
      ('UG.3.1.4', 'Emprise au sol: solo en ECM y algunos sectores'),
    ]),
    ('Altura y gabarits', [
      ('UG.3.2.1', 'Altura máxima del Plan général; 15 m fuera de la banda de 18 m'),
      ('UG.3.2.4', 'Gabarit sobre calle (H = P + 25 % P, máx. 28 m)'),
      ('UG.3.2.5', 'Gabarit en linderos'),
      ('UG.3.2.6', 'Gabarit entre fachadas en la misma parcela'),
      ('UG.3.2.8', 'Inserción en la secuencia de la calle'),
      ('UG.3.3.1', 'Elementos que pueden superar la altura'),
      ('UG.3.3.8', 'Balcones, oriels y salientes sobre la calle'),
      ('UG.3.3.9', 'Salientes hacia el interior de la parcela'),
    ]),
    ('Arquitectura', [
      ('UG.2.1.1', 'Inserción urbana y paisajística'),
      ('UG.2.1.2', 'Cada pieza principal con un hueco de éclairement premier'),
      ('UG.2.1.3', 'Planta baja sobre el espacio público'),
      ('UG.2.2.1', 'Planta baja ≥ 3,50 m de suelo a suelo'),
      ('UG.2.2.2', 'Materiales y colores; priorizar biosourcés y géosourcés'),
      ('UG.2.2.3', 'Integrar instalaciones técnicas en la cubierta'),
    ]),
    ('Espacios libres y vegetación', [
      ('UG.4.1.1', 'Superficie mínima de espacios libres'),
      ('UG.4.1.2', 'Espacios libres en pleine terre, de una pieza'),
      ('UG.4.1.3', 'Árboles y densidad de plantación'),
      ('UG.4.2.1', 'Índice de vegetación del edificio (IVB) ≥ 3'),
      ('UG.4.2.2', 'Cubierta vegetada: sustrato ≥ 25 cm'),
    ]),
    ('Bioclimatismo y energía', [
      ('UG.5.1.1', 'Principios bioclimáticos y ventilación natural'),
      ('UG.5.1.2', 'Bbio −15 % respecto a la RE2020'),
      ('UG.5.1.3', 'Confort de verano: DH ≤ 625; protecciones solares'),
      ('UG.5.1.4', 'Cep,nr −10 %; energías renovables'),
      ('UG.5.1.5', 'Carbono: Ic construction ≤ 580 kgCO₂/m²'),
    ]),
    ('Redes, residuos y aparcamiento', [
      ('UG.6.1.2', 'Agua de lluvia gestionada en la parcela'),
      ('UG.6.2.1', 'Local de basuras, preferentemente en planta baja'),
      ('UG.7.1.2', 'Accesos desde la calle'),
      ('UG.7.2.1', 'Coches: no exigido en vivienda; prohibido si la fachada ≤ 10 m'),
      ('UG.7.2.3', 'Bicis: 7 % de la SDP, mínimo 2 plazas por vivienda'),
    ]),
    ('Externalidades positivas', [
      ('UG.8.1', 'Más de 150 m² SDP: al menos 3 criterios de 2 temas'),
      ('UG.8.2', 'Tema biodiversidad y medio ambiente'),
      ('UG.8.3', 'Tema programación'),
      ('UG.8.4', 'Tema eficiencia energética y sobriedad'),
    ]),
  ],
 },
]
