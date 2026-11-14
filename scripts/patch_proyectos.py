# Añade la vista "Por proyecto" al explorador (template.html y/o un HTML ya construido).
# Uso: python3 patch_proyectos.py archivo.html [archivo2.html ...]
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos import PROYECTOS

CSS = """
.pj-tabs{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin:0 0 18px}
.pj-tabs a{display:block;text-decoration:none;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.pj-tabs a b{display:block;font-size:15.5px;margin-bottom:2px}
.pj-tabs a span{font-size:12.5px;color:var(--muted)}
.pj-tabs a.on{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent) inset}
.pj-cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.pj-cols ul{margin:0;padding-left:18px}.pj-cols li{margin:3px 0;font-size:14px}
.pj-bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:6px 0 14px}
.pj-prog{flex:1;min-width:160px;height:8px;background:var(--chip);border-radius:99px;overflow:hidden}
.pj-prog i{display:block;height:100%;background:var(--accent);border-radius:99px;transition:width .2s}
.pj-bar button{font:inherit;font-size:13px;padding:6px 10px;border-radius:8px;border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer}
.pj-g h3{margin:0 0 6px;font-size:15px}
.pj-a{display:grid;grid-template-columns:22px 1fr;gap:6px;align-items:start;padding:6px 0;border-top:1px solid var(--line)}
.pj-a:first-of-type{border-top:0}
.pj-a input{margin-top:3px;width:16px;height:16px;accent-color:var(--accent)}
.pj-a a{text-decoration:none;color:var(--ink)}
.pj-a .cd{color:var(--code);font-weight:600;margin-right:6px;font-size:13px}
.pj-a .tt{color:var(--muted);font-size:12.5px;display:block}
.pj-a.ok a{opacity:.55}
@media (max-width:760px){.pj-cols{grid-template-columns:1fr}}
@media print{.pj-tabs,.pj-bar button{display:none!important}.pj-a input{accent-color:#000}}
"""

JS = r"""
function viewProy(id){
  tabOn('proy'); curCode=null; markCur();
  const P=PROY, p=P.find(x=>x.id===id)||P[0];
  const byC={}; DATA.secs.forEach(s=>byC[s.c]=s);
  const key='plu-proy-'+p.id; let ok=store.get(key,{});
  const all=p.grupos.flatMap(g=>g[1].map(a=>a[0]));
  const done=()=>all.filter(c=>ok[c]).length;
  $('#main').innerHTML=`<h1 class="st">Artículos por tipo de proyecto</h1>
  <p style="color:var(--muted);margin-top:0">Selección de artículos de la zona UG (la mayor parte de París) que hay que revisar según el proyecto. Marca cada uno cuando lo hayas comprobado; la lista se guarda en este navegador.</p>
  <div class="pj-tabs">${P.map(x=>`<a href="#proy/${x.id}" class="${x.id===p.id?'on':''}"><b>${esc(x.nom)}</b><span>${x.grupos.reduce((n,g)=>n+g[1].length,0)} artículos</span></a>`).join('')}</div>
  <div class="box"><h3 style="margin-top:0">${esc(p.nom)}</h3><p style="margin:0 0 10px">${esc(p.sub)}</p>
   <div class="pj-cols"><div><b style="font-size:13px">Trámite</b><ul>${p.tramite.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></div>
   <div><b style="font-size:13px">Antes de empezar</b><ul>${p.antes.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></div></div></div>
  <div class="pj-bar"><span id="pjN"></span><div class="pj-prog"><i id="pjBar"></i></div><button id="pjPrint">Imprimir lista</button><button id="pjReset">Desmarcar todo</button></div>
  ${p.grupos.map(([g,arts])=>`<div class="box pj-g"><h3>${esc(g)}</h3>${arts.map(([c,w])=>{const s=byC[c];return `<div class="pj-a ${ok[c]?'ok':''}"><input type="checkbox" data-c="${c}" ${ok[c]?'checked':''} aria-label="Revisado ${c}"><a href="#s/${c}"><span class="cd">${esc(c.replace(/^G-/,''))}</span>${esc(w)}<span class="tt">${s?esc(s.t)+' · p. '+s.p:''}</span></a></div>`}).join('')}</div>`).join('')}
  <p style="color:var(--muted);font-size:13px">Lista orientativa: comprueba también el Atlas (planos), el Tome 2 y, si aplica, el PSMV. El régimen DP/PC depende de las superficies y del sitio.</p>`;
  const upd=()=>{const n=done();$('#pjN').textContent=n+' de '+all.length+' revisados';$('#pjBar').style.width=(100*n/all.length)+'%'};
  upd();
  document.querySelectorAll('.pj-a input').forEach(i=>i.onchange=()=>{const c=i.dataset.c; if(i.checked) ok[c]=1; else delete ok[c]; store.set(key,ok); i.parentElement.classList.toggle('ok',i.checked); upd()});
  $('#pjPrint').onclick=()=>print();
  $('#pjReset').onclick=()=>{ok={};store.set(key,ok);viewProy(p.id)};
}
"""

def patch(path):
    t = open(path, encoding='utf-8').read()
    if 'function viewProy' in t:
        print(path, 'ya tiene la vista; se actualizan los datos')
        import re
        t = re.sub(r'const PROY=.*?;\n', lambda m: 'const PROY=' + json.dumps(PROYECTOS, ensure_ascii=False).replace('</','<\\/') + ';\n', t, count=1, flags=re.S)
        open(path, 'w', encoding='utf-8').write(t); return
    rep = [
      ('@media print{', CSS + '@media print{'),
      ('<a href="#obras" data-t="obras">Guía DP / PC</a>', '<a href="#proy" data-t="proy">Por proyecto</a>\n    <a href="#obras" data-t="obras">Guía DP / PC</a>'),
      ('<h3>Empieza por</h3>', '<h3>Empieza por</h3><a href="#proy">→ Artículos por tipo de proyecto</a><br>'),
      ('function viewObras(){', JS + 'function viewObras(){'),
      ("  if(h==='obras') return viewObras();", "  if(h==='proy') return viewProy();\n  if(h.startsWith('proy/')) return viewProy(h.slice(5));\n  if(h==='obras') return viewObras();"),
      ('const store=', 'const PROY=' + json.dumps(PROYECTOS, ensure_ascii=False).replace('</','<\\/') + ';\nconst store='),
    ]
    for a, b in rep:
        n = t.count(a)
        assert n == 1, (path, a, n)
        t = t.replace(a, b)
    open(path, 'w', encoding='utf-8').write(t)
    print(path, 'OK')

for p in sys.argv[1:]:
    patch(p)
