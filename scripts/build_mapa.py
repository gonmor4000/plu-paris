# Construye territorios.geojson (municipios + territorios fusionados) para la portada con mapa.
import json, sys, unicodedata, re
from shapely.geometry import shape, mapping
from shapely.ops import unary_union
G = sys.argv[1]; OUT = sys.argv[2]
def norm(s):
    s = unicodedata.normalize('NFD', s).encode('ascii','ignore').decode().lower()
    s = s.replace('saint','st').replace('sainte','ste')
    return re.sub(r'[^a-z]', '', s)
T = {
 'paris': ('Ville de Paris', 'PLU bioclimatique', 'aprobado', 'https://www.paris.fr/plu', ['Paris']),
 't2': ('Vallée Sud – Grand Paris (T2)', 'PLUi', 'aprobado', 'https://www.valleesud.fr/vos-services/urbanisme/le-plui/le-plui-vallee-sud-grand-paris/',
   'Antony,Bagneux,Bourg-la-Reine,Châtenay-Malabry,Châtillon,Clamart,Fontenay-aux-Roses,Le Plessis-Robinson,Malakoff,Montrouge,Sceaux'.split(',')),
 't3': ('Grand Paris Seine Ouest (T3)', 'PLUi', 'aprobado', 'https://www.seineouest.fr/vos-services/urbanisme/plui',
   "Boulogne-Billancourt,Chaville,Issy-les-Moulineaux,Marnes-la-Coquette,Meudon,Sèvres,Vanves,Ville-d'Avray".split(',')),
 't4': ('Paris Ouest La Défense (T4)', 'PLU municipales', 'municipal', 'https://www.parisouestladefense.fr/les-missions-et-services/amenagement/plui/',
   'Courbevoie,Garches,La Garenne-Colombes,Levallois-Perret,Nanterre,Neuilly-sur-Seine,Puteaux,Rueil-Malmaison,Saint-Cloud,Suresnes,Vaucresson'.split(',')),
 't5': ('Boucle Nord de Seine (T5)', 'PLUi', 'aprobado', 'https://www.bouclenorddeseine.fr/plui-opposable',
   'Argenteuil,Asnières-sur-Seine,Bois-Colombes,Clichy,Colombes,Gennevilliers,Villeneuve-la-Garenne'.split(',')),
 't6': ('Plaine Commune (T6)', 'PLUi', 'aprobado', 'https://plainecommune.fr/plui',
   "Aubervilliers,Épinay-sur-Seine,La Courneuve,L'Île-Saint-Denis,Saint-Denis,Saint-Ouen-sur-Seine,Stains,Villetaneuse".split(',')),
 't7': ("Paris Terres d'Envol (T7)", 'PLUi', 'aprobado', 'https://www.paristerresdenvol.fr/mes-services/urbanisme/connaitre-les-regles-durbanisme-plui/',
   'Aulnay-sous-Bois,Le Blanc-Mesnil,Le Bourget,Drancy,Dugny,Sevran,Tremblay-en-France,Villepinte'.split(',')),
 't8': ('Est Ensemble (T8)', 'PLUi', 'aprobado', 'https://www.est-ensemble.fr/plui-approuve',
   'Bagnolet,Bobigny,Bondy,Le Pré-Saint-Gervais,Les Lilas,Montreuil,Noisy-le-Sec,Pantin,Romainville'.split(',')),
 't9': ('Grand Paris Grand Est (T9)', 'PLUi', 'aprobado', 'https://www.grandparisgrandest.fr/a-mon-service/pour-mon-logement-et-mon-habitat/consulter-les-plans-locaux-durbanisme/consulter-les-pieces-du-plui/',
   'Clichy-sous-Bois,Coubron,Gagny,Gournay-sur-Marne,Livry-Gargan,Montfermeil,Neuilly-Plaisance,Neuilly-sur-Marne,Noisy-le-Grand,Les Pavillons-sous-Bois,Le Raincy,Rosny-sous-Bois,Vaujours,Villemomble'.split(',')),
 't10': ('Paris Est Marne & Bois (T10)', 'PLUi', 'aprobado', 'https://www.parisestmarnebois.fr/fr/plan-local-durbanisme-intercommunal',
   'Bry-sur-Marne,Champigny-sur-Marne,Charenton-le-Pont,Fontenay-sous-Bois,Joinville-le-Pont,Le Perreux-sur-Marne,Maisons-Alfort,Nogent-sur-Marne,Saint-Mandé,Saint-Maur-des-Fossés,Saint-Maurice,Villiers-sur-Marne,Vincennes'.split(',')),
 't11': ('Grand Paris Sud Est Avenir (T11)', 'PLUi', 'aprobado', 'https://sudestavenir.fr/nos-grands-projets/plan-local-durbanisme-intercommunal/',
   'Alfortville,Boissy-Saint-Léger,Bonneuil-sur-Marne,Chennevières-sur-Marne,Créteil,La Queue-en-Brie,Le Plessis-Trévise,Limeil-Brévannes,Mandres-les-Roses,Marolles-en-Brie,Noiseau,Ormesson-sur-Marne,Périgny,Santeny,Sucy-en-Brie,Villecresnes'.split(',')),
 't12': ('Grand-Orly Seine Bièvre (T12)', 'PLUi', 'aprobado', 'https://www.grandorlyseinebievre.fr/plan-local-durbanisme-intercommunal',
   "Ablon-sur-Seine,Arcueil,Cachan,Chevilly-Larue,Choisy-le-Roi,Fresnes,Gentilly,Ivry-sur-Seine,Le Kremlin-Bicêtre,L'Haÿ-les-Roses,Orly,Rungis,Thiais,Valenton,Villejuif,Villeneuve-le-Roi,Villeneuve-Saint-Georges,Vitry-sur-Seine,Athis-Mons,Juvisy-sur-Orge,Morangis,Paray-Vieille-Poste,Savigny-sur-Orge,Viry-Châtillon".split(',')),
}
idx = {}
for tid,(_,_,_,_,names) in T.items():
    for n in names: idx[norm(n)] = tid
feats=[]; geoms={t:[] for t in T}; found=set()
for d in ['75','92','93','94','91','95']:
    for f in json.load(open(f'{G}/d{d}.json'))['features']:
        n=f['properties']['nom']; tid=idx.get(norm(n))
        if not tid:
            if d in ('75','92','93','94'): print('SIN TERRITORIO:', n)
            continue
        found.add(norm(n))
        g=shape(f['geometry']).simplify(0.0002, preserve_topology=True)
        geoms[tid].append(shape(f['geometry']).buffer(0))
        feats.append({'type':'Feature','properties':{'kind':'commune','nom':n,'insee':f['properties']['code'],'t':tid},'geometry':mapping(g)})
for k in idx:
    if k not in found: print('NO ENCONTRADO:', k)
def r(o):
    if isinstance(o,float): return round(o,5)
    if isinstance(o,(list,tuple)): return [r(x) for x in o]
    if isinstance(o,dict): return {k:r(v) for k,v in o.items()}
    return o
terr=[]
for tid,(nom,doc,est,url,names) in T.items():
    u=unary_union(geoms[tid]).simplify(0.0003, preserve_topology=True)
    terr.append({'type':'Feature','properties':{'kind':'territorio','id':tid,'nom':nom,'doc':doc,'estado':est,'url':url,'n':len(names)},'geometry':mapping(u)})
json.dump(r({'type':'FeatureCollection','features':terr+feats}), open(OUT,'w'), ensure_ascii=False, separators=(',',':'))
print(len(terr),'territorios',len(feats),'municipios')
