# -*- coding: utf-8 -*-
# Serviços e valores 2026 — v2 (linguagem editorial: grid à mostra, numerais gigantes, índice de página)
import sys, json
from playwright.sync_api import sync_playwright

L = sys.argv[1] if len(sys.argv) > 1 else 'pt'
PT = L == 'pt'
def t(pt, en): return pt if PT else en

CSS = r'''
@font-face{font-family:G;src:url(../g300.woff);font-weight:300}@font-face{font-family:G;src:url(../g500.woff);font-weight:500}
@font-face{font-family:T;src:url(../text.woff)}@font-face{font-family:L;src:url(../label.woff)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:T,Helvetica,sans-serif;font-size:9pt;line-height:1.45;color:#111;background:#F3F1EC}
.pg{width:210mm;height:297mm;padding:14mm 14mm 12mm;position:relative;page-break-after:always;background:#F3F1EC;overflow:hidden}
/* grid de 12 colunas à mostra */
.grid{position:absolute;inset:0 14mm;display:grid;grid-template-columns:repeat(12,1fr);column-gap:4mm;pointer-events:none;z-index:0}
.grid i{border-left:0.2mm solid #E4E0D8;border-right:0.2mm solid #E4E0D8}
.pg > *:not(.grid):not(.foot):not(.giant){position:relative;z-index:1}.foot,.giant{z-index:1}
.lab{font-family:L;font-size:7pt;letter-spacing:.07em;text-transform:uppercase}
.mut{color:#5C5A55}.sm{font-size:7.8pt;line-height:1.45}
.bar{display:grid;grid-template-columns:repeat(12,1fr);column-gap:4mm;border-top:0.3mm solid #111;padding-top:2.2mm;font-family:L;font-size:7pt;letter-spacing:.07em;text-transform:uppercase}
.bar .a{grid-column:1/4}.bar .b{grid-column:4/9}.bar .c{grid-column:9/12}.bar .d{grid-column:12/13;text-align:right}
.dot{display:inline-block;width:2mm;height:2mm;border-radius:9px;background:#E1251B;margin-right:1.6mm;vertical-align:.2mm}
h1{font-family:G;font-weight:300;font-size:50pt;line-height:.95;letter-spacing:-.04em;margin:0}
h2{font-family:G;font-weight:500;font-size:24pt;line-height:1;letter-spacing:-.03em;margin:0}
h3{font-family:G;font-weight:500;font-size:13pt;line-height:1.1;letter-spacing:-.015em;margin:0}
.lead{font-size:11.5pt;line-height:1.4;letter-spacing:-.005em}
.giant{position:absolute;font-family:G;font-weight:300;letter-spacing:-.06em;line-height:.78;color:#111}
.vert{writing-mode:vertical-rl;transform:rotate(180deg)}
.g12{display:grid;grid-template-columns:repeat(12,1fr);column-gap:4mm}
.rule{border-top:0.3mm solid #111}.soft{border-top:0.2mm solid #D3CFC6}
.pr{font-family:G;font-weight:300;font-size:19pt;letter-spacing:-.025em;line-height:1;font-variant-numeric:tabular-nums}
ul.inc{margin:2mm 0 0;padding:0;list-style:none}ul.inc li{padding:1.1mm 0;border-top:0.2mm solid #D3CFC6}
.row{display:grid;grid-template-columns:repeat(12,1fr);column-gap:4mm;padding:2.6mm 0;border-bottom:0.2mm solid #D3CFC6;align-items:baseline}
.row .n{grid-column:1/5;font-weight:normal}.row .d{grid-column:5/9}.row .v{grid-column:9/13;text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.cats{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm;row-gap:7mm}
.ch{display:flex;gap:3mm;align-items:baseline;border-bottom:0.3mm solid #111;padding-bottom:1.6mm}
.r{display:flex;justify-content:space-between;gap:4mm;padding:1.45mm 0;border-bottom:0.2mm solid #D3CFC6;font-size:8.6pt}.num{white-space:nowrap;font-variant-numeric:tabular-nums}
.cat p{margin:1.4mm 0 0}
.foot{position:absolute;left:14mm;right:14mm;bottom:9mm;display:grid;grid-template-columns:repeat(12,1fr);column-gap:4mm;align-items:center;border-top:0.3mm solid #111;padding-top:2.4mm;font-family:L;font-size:6.8pt;letter-spacing:.07em;text-transform:uppercase;color:#5C5A55}
.foot img{height:4.6mm}.foot .x1{grid-column:1/3}.foot .x2{grid-column:4/7}.foot .x3{grid-column:7/11}.foot .x4{grid-column:11/13;text-align:right;color:#111}
.def{border-top:0.3mm solid #111;padding-top:2.4mm}
.def h3{margin:1.5mm 0 1.5mm}
.tag{font-family:L;font-size:6.8pt;letter-spacing:.07em;text-transform:uppercase;color:#5C5A55}
'''

def grid(): return '<div class="grid">' + '<i></i>' * 12 + '</div>'
def bar(a, b, c, d): return f'<div class="bar"><span class="a">{a}</span><span class="b mut">{b}</span><span class="c">{c}</span><span class="d">{d}</span></div>'
def foot(p): return f'<div class="foot"><span class="x1"><img src="../logo.svg"></span><span class="x2">Kco Oyakawa — Head of Art</span><span class="x3">kcodigital@gmail.com · +55 11 99577-7475</span><span class="x4">P.{p:02d}</span></div>'

pages = []
# ---------------- P.01 CAPA
idx = [('01', t('Como contratar', 'How to hire'), 2), ('02', t('Pacotes', 'Packages'), 3), ('03', t('Serviços estratégicos', 'Strategic services'), 4),
       ('04', t('Consultoria criativa', 'Creative consulting'), 4), ('05', t('Tabela de referência', 'Reference table'), 5), ('06', t('Condições comerciais', 'Commercial terms'), 7)]
idxh = ''.join(f'<div style="display:grid;grid-template-columns:8mm 1fr 10mm;padding:1.5mm 0;border-bottom:0.2mm solid #D3CFC6"><span class="lab mut">{n}</span><span>{s}</span><span class="lab" style="text-align:right">P.{p:02d}</span></div>' for n, s, p in idx)
pages.append(f'''<section class="pg">{grid()}{bar('KCO Creative Studio', t('Serviços e valores', 'Services and rates'), '<span class="dot"></span>' + t('Agenda aberta', 'Booking open'), t('Índice', 'Index'))}
<div class="g12" style="margin-top:34mm"><div style="grid-column:1/9"><h1>{t('Serviços<br>e valores', 'Services<br>and rates')}<span style="color:#E1251B">.</span></h1>
<p class="lead mut" style="margin:9mm 0 0;max-width:105mm">{t('Direção criativa, design e experiências de marca. Valores de referência — cada proposta é fechada a partir do briefing: escopo, complexidade, volume e prazo.', 'Creative direction, design and brand experiences. Reference rates — every proposal is built from the brief: scope, complexity, volume and timing.')}</p></div>
<div style="grid-column:9/13;padding-top:2mm"><div class="lab" style="border-top:0.3mm solid #111;padding-top:2mm;margin-bottom:1mm">{t('Índice', 'Index')}</div>{idxh}</div></div>
<div class="giant" style="left:12mm;right:12mm;bottom:22mm;font-size:228pt;white-space:nowrap">2026</div>
{foot(1)}</section>''')

# ---------------- P.02 COMO CONTRATAR
defs = [
 ('A', t('Pacote', 'Package'), t('Solução integrada, com entregas definidas do início ao fim. Para quem precisa do resultado completo, com um único responsável pela direção.', 'An integrated solution with defined deliverables from start to finish. For clients who need the complete result, with one person leading the direction.'), t('Ex.: Campanha Essencial', 'E.g. Essential Campaign')),
 ('B', t('Serviço estratégico', 'Strategic service'), t('Direção, conceituação e supervisão de um desafio específico. O foco é a ideia e a linguagem; produção e desdobramentos entram à parte.', 'Direction, concept and supervision of a specific challenge. The focus is the idea and the visual language; production and roll-outs are quoted separately.'), t('Ex.: Direção criativa para eventos', 'E.g. Creative direction for events')),
 ('C', t('Consultoria criativa', 'Creative consulting'), t('Repertório e visão para destravar um desafio, revisar um projeto ou orientar um time — em sprint estruturado ou sessões pontuais.', 'Experience and vision to unblock a challenge, review a project or guide a team — as a structured sprint or one-off sessions.'), t('Ex.: Sprint de direção de arte', 'E.g. Art direction sprint')),
 ('D', t('Tabela de referência', 'Reference table'), t('Entregas individuais com escopo delimitado e conteúdo definido pelo cliente. Faixas de partida para peças avulsas.', 'Individual deliverables with a defined scope and client-supplied content. Starting ranges for one-off pieces.'), t('Ex.: Landing page de vendas', 'E.g. Sales landing page')),
]
dh = ''.join(f'<div class="def" style="grid-column:span 6;margin-bottom:8mm"><span class="tag">{k}</span><h3>{h}</h3><p style="margin:0 0 2mm">{d}</p><span class="tag">{e}</span></div>' for k, h, d, e in defs)
models = [(t('Parceria com agências', 'Agency partnerships'), t('Reforço sênior para o time da agência, por job ou em volume recorrente.', 'Senior support for the agency team, per job or on a recurring basis.')),
          (t('Projetos diretos', 'Direct projects'), t('Para empresas, marcas, produtoras e eventos — de uma peça a um projeto completo.', 'For companies, brands, producers and events — from one piece to a full project.')),
          (t('Consultoria criativa', 'Creative consulting'), t('Sprint, revisão de projetos, orientação de equipes e mentoria.', 'Sprints, project reviews, team guidance and mentoring.'))]
mh = ''.join(f'<div style="grid-column:span 4;border-top:0.2mm solid #D3CFC6;padding-top:2mm"><h3 style="font-size:11pt">{a}</h3><p class="sm mut" style="margin:1.5mm 0 0">{b}</p></div>' for a, b in models)
pages.append(f'''<section class="pg">{grid()}{bar('01 — ' + t('Como contratar', 'How to hire'), t('Quatro formas de trabalhar juntos', 'Four ways to work together'), '', 'P.02')}
<div class="giant vert" style="right:10mm;top:24mm;font-size:200pt">01</div>
<div class="g12" style="margin-top:16mm"><div style="grid-column:1/9"><h2>{t('Como contratar', 'How to hire')}</h2><p class="lead mut" style="margin:5mm 0 0;max-width:110mm">{t('A diferença está no que você recebe: uma solução completa, a direção de um desafio, uma consultoria ou uma entrega pontual.', 'The difference is what you receive: a complete solution, direction on a challenge, consulting, or a one-off deliverable.')}</p></div></div>
<div class="g12" style="margin-top:14mm;grid-column-end:auto;max-width:150mm">{dh}</div>
<div class="g12" style="margin-top:4mm"><div class="lab" style="grid-column:1/13;margin-bottom:3mm">{t('Modelos de trabalho', 'Working models')}</div>{mh}</div>
{foot(2)}</section>''')

# ---------------- P.03 PACOTES
pk = [
 ('01', t('Campanha Essencial', 'Essential Campaign'), 'R$ 8.000–15.000',
  t('Conceito criativo, key visual master, sistema visual e conjunto inicial de desdobramentos.', 'Creative concept, master key visual, visual system and an initial set of roll-outs.'),
  [t('Imersão no briefing e objetivos', 'Brief and goals immersion'), t('Conceito e key visual master', 'Concept and master key visual'), t('Sistema visual da campanha', 'Campaign visual system'), t('Desdobramentos iniciais', 'Initial roll-outs')],
  t('Produção audiovisual, mídia e grandes volumes de adaptação à parte.', 'Video production, media and large adaptation volumes quoted separately.')),
 ('02', 'Business Presentation', 'R$ 7.000–14.000',
  t('Apresentação comercial ou para investidores, do diagnóstico ao design final.', 'A sales or investor presentation, from diagnosis to final design.'),
  [t('Diagnóstico do que precisa ser vendido', 'Diagnosis of what needs selling'), t('Estrutura narrativa', 'Narrative structure'), t('Organização da informação', 'Information architecture'), t('Direção de arte e design', 'Art direction and design')],
  t('Difere da apresentação da tabela: aqui a narrativa é construída junto. Na tabela, o roteiro e o conteúdo chegam prontos.', 'Unlike the table item, the narrative is built together here. In the table, script and content arrive ready.')),
 ('03', 'Brand Experience', 'R$ 12.000–25.000+',
  t('Conceito, narrativa e direção de arte para evento, estande ou ativação.', 'Concept, narrative and art direction for an event, booth or activation.'),
  [t('Conceito e narrativa da experiência', 'Experience concept and narrative'), t('Direção de arte e linguagem visual', 'Art direction and visual language'), t('Sistema visual aplicado', 'Applied visual system'), t('Acompanhamento criativo', 'Creative follow-up')],
  t('Projeto executivo, engenharia, renders, produção e montagem à parte.', 'Technical drawings, engineering, renders, production and build quoted separately.')),
]
ph = ''.join(f'''<div style="grid-column:span 4"><div class="def"><span class="tag">{t('Pacote', 'Package')} {n}</span><h3 style="margin:1.5mm 0 4mm">{h}</h3><div class="pr">{p}</div></div>
<p style="margin:4mm 0 2mm">{d}</p><div class="tag" style="margin-top:3mm">{t('Inclui', 'Includes')}</div><ul class="inc">{''.join(f'<li>{x}</li>' for x in inc)}</ul><p class="sm mut" style="margin:3mm 0 0">{note}</p></div>''' for n, h, p, d, inc, note in pk)
pages.append(f'''<section class="pg">{grid()}{bar('02 — ' + t('Pacotes', 'Packages'), t('Soluções completas, escopo claro', 'Complete solutions, clear scope'), '', 'P.03')}
<div class="giant vert" style="right:10mm;top:24mm;font-size:200pt">02</div>
<div class="g12" style="margin-top:16mm"><div style="grid-column:1/9"><h2>{t('Pacotes', 'Packages')}</h2><p class="lead mut" style="margin:5mm 0 0;max-width:110mm">{t('Três tipos de projeto em que a direção de arte faz mais diferença — com entregas definidas e um único responsável.', 'Three kinds of project where art direction makes the biggest difference — defined deliverables, one person in charge.')}</p></div></div>
<div class="g12" style="margin-top:30mm;max-width:152mm;column-gap:6mm">{ph}</div>
{foot(3)}</section>''')

# ---------------- P.04 SERVIÇOS ESTRATÉGICOS + CONSULTORIA
sv = [(t('Direção de arte para campanhas', 'Art direction for campaigns'), t('Linguagem visual, referências, composição e supervisão criativa.', 'Visual language, references, composition and creative supervision.'), 'R$ 5.000–10.000'),
      (t('Branding e identidade visual', 'Branding and visual identity'), t('Estratégia de marca, conceito, identidade, sistema gráfico e aplicações.', 'Brand strategy, concept, identity, graphic system and applications.'), 'R$ 8.000–20.000+'),
      (t('Pitch e proposta para concorrência', 'Pitch and competitive proposals'), t('Narrativa e apresentação visual de propostas comerciais e concorrências.', 'Narrative and visual presentation of proposals and pitches.'), 'R$ 6.000–15.000+'),
      (t('Direção criativa para eventos', 'Creative direction for events'), t('Conceito, narrativa e linguagem visual para ambientes e ativações.', 'Concept, narrative and visual language for spaces and activations.'), t('A partir de R$ 8.000', 'From R$ 8,000'))]
svh = ''.join(f'<div class="row"><span class="n"><b style="font-weight:normal">{a}</b></span><span class="d mut sm">{b}</span><span class="v">{c}</span></div>' for a, b, c in sv)
cons = [
 (t('Sprint de direção de arte', 'Art direction sprint'), 'R$ 2.500–4.000',
  t('Intervenção estruturada para um desafio visual ou comercial.', 'A structured intervention on a visual or commercial challenge.'),
  [(t('Duração', 'Length'), t('1 a 3 dias de imersão', '1 to 3 days of immersion')), (t('Como', 'Format'), t('Briefing, análise e sessão de trabalho', 'Brief, analysis and working session')), (t('Você recebe', 'You receive'), t('Diagnóstico e recomendações documentadas em PDF, apresentadas ao time', 'Diagnosis and documented recommendations (PDF), presented to the team'))]),
 (t('Sessão de consultoria', 'Consulting session'), t('R$ 350–500 / hora', 'R$ 350–500 / hour'),
  t('Atendimento pontual: revisão de projeto, orientação de equipe ou mentoria.', 'One-off support: project review, team guidance or mentoring.'),
  [(t('Duração', 'Length'), t('Mínimo de 2 horas, online ou presencial', 'Minimum 2 hours, online or in person')), (t('Como', 'Format'), t('Conversa guiada sobre o material enviado', 'Guided conversation on the material sent')), (t('Você recebe', 'You receive'), t('Pontos de ajuste e próximos passos por escrito', 'Written adjustments and next steps'))]),
]
ch = ''.join(f'''<div style="grid-column:span 6"><div class="def"><span class="tag">{t('Consultoria', 'Consulting')}</span><h3 style="margin:1.5mm 0 3mm">{h}</h3><div class="pr" style="font-size:15pt">{p}</div></div><p style="margin:3mm 0 2mm">{d}</p>
{''.join(f'<div style="display:grid;grid-template-columns:22mm 1fr;gap:3mm;padding:1.4mm 0;border-top:0.2mm solid #D3CFC6"><span class="tag" style="padding-top:.4mm">{a}</span><span class="sm">{b}</span></div>' for a, b in rows)}</div>''' for h, p, d, rows in cons)
pages.append(f'''<section class="pg">{grid()}{bar('03 — ' + t('Serviços estratégicos', 'Strategic services'), t('Direção de um desafio específico', 'Direction on a specific challenge'), '', 'P.04')}
<div class="giant vert" style="right:10mm;top:24mm;font-size:200pt">03</div>
<div style="margin-top:16mm;max-width:126mm"><h2>{t('Quando o desafio é estratégico', 'When the challenge is strategic')}</h2>
<div class="rule" style="margin-top:9mm"></div>{svh}
<p class="sm mut" style="margin:2.5mm 0 0">{t('Produção, desdobramentos e fornecedores são orçados à parte.', 'Production, roll-outs and suppliers are quoted separately.')}</p></div>
<div style="margin-top:16mm;max-width:150mm">{bar('04 — ' + t('Consultoria criativa', 'Creative consulting'), t('Repertório para destravar e orientar', 'Experience to unblock and guide'), '', '')}
<div class="g12" style="margin-top:8mm;column-gap:6mm">{ch}</div></div>
{foot(4)}</section>''')

# ---------------- P.05–06 TABELA
def cat(k, h, items, note):
    return f'<div class="cat"><div class="ch"><span class="lab mut">{k}</span><h3 style="font-size:10.5pt">{h}</h3></div>' + ''.join(f'<div class="r"><span>{a}</span><span class="num">{b}</span></div>' for a, b in items) + f'<p class="sm mut">{note}</p></div>'
cats1 = [
 cat('A', t('Web e experiência digital', 'Web and digital'), [(t('Landing page de lançamento ou vendas', 'Launch or sales landing page'), 'R$ 3.500–6.000'), (t('Site institucional — home + 4 páginas', 'Corporate site — home + 4 pages'), 'R$ 7.000–14.000'), (t('Layout de e-commerce — home + produto', 'E-commerce layout — home + product'), 'R$ 8.000–16.000'), (t('Página de captura', 'Lead capture page'), 'R$ 2.000–3.500')], t('Design visual e UI. Copywriting, desenvolvimento e integrações à parte.', 'Visual and UI design. Copywriting, development and integrations quoted separately.')),
 cat('B', t('Redes sociais', 'Social media'), [(t('Carrossel estratégico — 5 a 10 slides', 'Strategic carousel — 5 to 10 slides'), 'R$ 600–1.200'), (t('Post avulso de alta complexidade', 'High-complexity single post'), 'R$ 250–500'), (t('Stories — 3 a 5 telas', 'Stories — 3 to 5 frames'), 'R$ 400–800'), (t('Kit de 6 templates editáveis', 'Kit of 6 editable templates'), 'R$ 2.500–4.500')], t('Peças autorais com conceito são orçadas diferente de adaptações.', 'Original pieces with a concept are priced differently from adaptations.')),
 cat('C', t('Apresentações', 'Presentations'), [(t('Apresentação institucional ou comercial', 'Corporate or sales presentation'), 'R$ 5.000–12.000'), (t('Slide adicional, em projeto aprovado', 'Additional slide, approved project'), 'R$ 200–400'), (t('Template mestre de apresentação', 'Master presentation template'), 'R$ 2.500–5.000')], t('Até 15 slides, com roteiro e conteúdo prontos. Para construir a narrativa junto, ver Pacote 02.', 'Up to 15 slides, with script and content ready. To build the narrative together, see Package 02.')),
 cat('D', t('Marketing e campanhas', 'Marketing and campaigns'), [(t('Key visual — conceito de campanha', 'Key visual — campaign concept'), 'R$ 6.000–12.000'), (t('Pack de 10 criativos para anúncios', 'Pack of 10 ad creatives'), 'R$ 3.000–5.500'), (t('E-mail marketing', 'E-mail marketing'), 'R$ 600–1.000'), (t('E-book ou material rico', 'E-book or rich content'), 'R$ 3.000–7.000')], t('O KV master é orçado separado dos desdobramentos.', 'The master KV is quoted separately from roll-outs.')),
 cat('E', t('Papelaria corporativa', 'Corporate stationery'), [(t('Cartão de visitas especial', 'Special business card'), 'R$ 500–900'), (t('Kit de papelaria básica', 'Basic stationery kit'), 'R$ 1.200–2.200'), (t('Pasta de proposta com faca especial', 'Proposal folder with special die-cut'), 'R$ 900–1.800'), (t('Crachá e cordão', 'Badge and lanyard'), 'R$ 350–650')], t('Design e arquivos. Provas, produção gráfica e acabamentos à parte.', 'Design and files. Proofs, printing and finishes quoted separately.')),
 cat('F', t('Promocional e PDV', 'Promotional and POS'), [(t('Flyer — frente e verso', 'Flyer — double-sided'), 'R$ 800–1.400'), (t('Folder de 6 faces', '6-panel folder'), 'R$ 1.500–3.000'), (t('Broadside ou tabloide', 'Broadside or tabloid'), 'R$ 2.000–4.000'), (t('Cartaz ou pôster para PDV', 'POS poster'), 'R$ 1.000–1.800')], t('Volume de conteúdo, versões e tratamento de imagens podem alterar o valor.', 'Content volume, versions and image retouching may change the price.')),
]
cats2 = [
 cat('G', t('Editorial e vendas', 'Editorial and sales'), [(t('Catálogo — conceito gráfico e capa', 'Catalogue — graphic concept and cover'), 'R$ 2.000–4.000'), (t('Diagramação de miolo, por página', 'Inner page layout, per page'), 'R$ 150–300'), (t('Anúncio de revista ou jornal', 'Magazine or newspaper ad'), 'R$ 800–1.800')], t('Sistema gráfico e diagramação extensa entram no orçamento do catálogo.', 'Graphic system and extensive layout go into the catalogue quote.')),
 cat('H', t('Brindes e merchandising', 'Merchandise'), [(t('Camiseta ou uniforme — estampa', 'T-shirt or uniform — print'), 'R$ 600–1.200'), (t('Kit de brindes simples', 'Simple gift kit'), 'R$ 800–1.500'), (t('Embalagem ou rótulo', 'Packaging or label'), 'R$ 2.000–6.000')], t('Embalagens com estrutura e faca técnica podem exigir valores maiores.', 'Structural packaging and technical die-cuts may cost more.')),
 cat('I', t('Sinalização e grandes formatos', 'Signage and large formats'), [(t('Banner ou roll-up', 'Banner or roll-up'), 'R$ 600–1.000'), (t('Outdoor ou busdoor', 'Billboard or bus ad'), 'R$ 1.000–2.000'), (t('Adesivagem de tapume', 'Hoarding graphics'), 'R$ 3.000–6.000')], t('Tapumes e grandes áreas consideram metragem, módulos e arquivos técnicos.', 'Hoardings and large areas consider size, modules and technical files.')),
]
pages.append(f'''<section class="pg">{grid()}{bar('05 — ' + t('Tabela de referência', 'Reference table'), t('Faixas de partida por entrega', 'Starting ranges per deliverable'), '', 'P.05')}
<div style="margin-top:12mm;max-width:182mm"><div class="cats">{''.join(cats1)}</div></div>{foot(5)}</section>''')
pages.append(f'''<section class="pg">{grid()}{bar('05 — ' + t('Tabela de referência', 'Reference table'), t('Continuação', 'Continued'), '', 'P.06')}
<div style="margin-top:12mm;max-width:182mm"><div class="cats">{''.join(cats2)}</div></div>
<div class="giant" style="left:12mm;bottom:24mm;font-size:150pt">A—I<span style="color:#E1251B">.</span></div>
{foot(6)}</section>''')

# ---------------- P.07 CONDIÇÕES
cond = [(t('Até R$ 5.000', 'Up to R$ 5,000'), t('50% na aprovação e 50% na entrega', '50% on approval, 50% on delivery')),
        (t('Acima de R$ 5.000', 'Above R$ 5,000'), t('40% na aprovação, 30% na aprovação criativa e 30% na entrega', '40% on approval, 30% on creative approval, 30% on delivery')),
        (t('Validade', 'Validity'), t('15 dias corridos', '15 calendar days')),
        (t('Revisões', 'Revisions'), t('Até 2 rodadas consolidadas por etapa', 'Up to 2 consolidated rounds per stage')),
        (t('Rodadas extras', 'Extra rounds'), t('Por hora ou orçamento complementar', 'Hourly or a complementary quote')),
        (t('Urgência', 'Rush'), t('Adicional de 30% a 50%', 'Surcharge of 30% to 50%')),
        (t('Mudança de escopo', 'Scope change'), t('Novo orçamento e ajuste de prazo', 'New quote and adjusted timeline')),
        (t('Terceiros', 'Third parties'), t('Produção e fornecedores orçados à parte', 'Production and suppliers quoted separately')),
        (t('Arquivos abertos', 'Source files'), t('Conforme contrato e natureza do projeto', 'Per contract and nature of the project')),
        (t('Direitos de uso', 'Usage rights'), t('Por finalidade, canais, prazo e território', 'By purpose, channels, term and territory'))]
coh = ''.join(f'<div class="row" style="padding:2.2mm 0"><span class="lab" style="grid-column:1/5">{a}</span><span style="grid-column:5/13">{b}</span></div>' for a, b in cond)
glos = [(t('O que é uma rodada de revisão', 'What a revision round is'), t('Um conjunto único e consolidado de ajustes, enviado de uma vez por um responsável, sobre a etapa entregue e dentro do briefing aprovado. Ajustes enviados em partes contam como rodadas separadas.', 'A single, consolidated set of changes, sent at once by one person, on the delivered stage and within the approved brief. Changes sent in parts count as separate rounds.')),
        (t('O que muda o escopo', 'What changes the scope'), t('Nova peça, formato ou versão; novo conteúdo; troca de um conceito já aprovado; mudança de objetivo ou público; ajustes além das rodadas previstas.', 'A new piece, format or version; new content; replacing an approved concept; a change of goal or audience; changes beyond the agreed rounds.'))]
gh = ''.join(f'<div class="def" style="grid-column:span 6"><h3 style="font-size:11pt">{a}</h3><p class="sm" style="margin:0">{b}</p></div>' for a, b in glos)
pages.append(f'''<section class="pg">{grid()}{bar('06 — ' + t('Condições comerciais', 'Commercial terms'), t('Como cada projeto anda', 'How each project runs'), '', 'P.07')}
<div class="giant vert" style="right:10mm;top:24mm;font-size:200pt">06</div>
<div style="margin-top:16mm;max-width:126mm"><h2>{t('Condições comerciais', 'Commercial terms')}</h2><div class="rule" style="margin-top:9mm"></div>{coh}
<div class="g12" style="margin-top:12mm;column-gap:6mm">{gh}</div>
<p class="sm mut" style="margin-top:12mm">{t('Valores de referência 2026, sujeitos a alteração sem aviso prévio. A proposta comercial de cada projeto detalha escopo, entregáveis, investimento, cronograma e condições.', '2026 reference rates, subject to change without notice. Each project proposal details scope, deliverables, investment, timeline and terms.')}</p>
<h1 style="margin-top:16mm;font-size:40pt">{t('Vamos conversar', 'Let’s talk')}<span style="color:#E1251B">.</span></h1></div>
{foot(7)}</section>''')

html = f'<!doctype html><html lang="{t("pt-BR","en")}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
name = 'Kco_Oyakawa_Servicos_e_Valores_2026' if PT else 'Kco_Oyakawa_Services_and_Rates_2026'
open(f'/home/claude/pdf/v2/{name}.html', 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto(f'file:///home/claude/pdf/v2/{name}.html'); pg.wait_for_timeout(800)
    pg.pdf(path=f'/home/claude/pdf/v2/{name}.pdf', format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
print(name)
