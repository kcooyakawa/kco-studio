import json,os,re,shutil
K='/tmp/claude-0/-home-claude/d4bfc18a-5055-5a1d-a520-34d96f9a30c8/scratchpad/kco/project/'
AF='/tmp/claude-0/-home-claude/d4bfc18a-5055-5a1d-a520-34d96f9a30c8/scratchpad/artifact-files/b66e94c1-00fa-4efc-b497-d0ed7572ecdc'
m=json.load(open('/home/claude/blobmap.json'))
for f in os.listdir(AF):
    k=f.split('.')[0]
    if re.fullmatch(r'[0-9a-f]{32}',k): m[k]=os.path.join(AF,f)
out='/home/claude/site/kcoland'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out+'/assets'); os.makedirs(out+'/en')
srcs={'pt':open(K+'Main.dc.html').read(),'en':open(K+'Main_en.dc.html').read()}
used=set()
for t in srcs.values():
    used|=set(re.findall(r'/_blob/([0-9a-f]{32})',t)); used|=(set(re.findall(r'[0-9a-f]{32}',t))&set(m))
missing=used-set(m); assert not missing, missing
ext={}
for k in used:
    e=os.path.splitext(m[k])[1].lower(); ext[k]=e; shutil.copy(m[k],f'{out}/assets/{k}{e}')
META={'pt':dict(lang='pt-BR',title='KCO Creative Studio — Kco Oyakawa, Head of Art',desc='Kco Oyakawa — Head of Art. Direção criativa, design, branding e experiências de marca em São Paulo. Cases para Coca-Cola, Lollapalooza, Billabong, FIFA™ 2014, Stap Feelings e mais.',ns='Ative o JavaScript para ver o portfólio de Kco Oyakawa.'),
      'en':dict(lang='en',title='KCO Creative Studio — Kco Oyakawa, Head of Art',desc='Kco Oyakawa — Head of Art. Creative direction, design, branding and brand experiences from São Paulo. Cases for Coca-Cola, Lollapalooza, Billabong, FIFA™ 2014, Stap Feelings and more.',ns='Enable JavaScript to see Kco Oyakawa\'s portfolio.')}
for lang,t in srcs.items():
    pre='' if lang=='pt' else '../'
    helmet=re.search(r'<helmet>(.*?)</helmet>',t,re.S).group(1)
    tpl=re.sub(r'<helmet>.*?</helmet>','',re.search(r'<x-dc>(.*?)</x-dc>',t,re.S).group(1),flags=re.S)
    props=re.search(r"data-props='(.*?)'",t).group(1)
    js=re.search(r'data-dc-script[^>]*>(.*?)</script>',t,re.S).group(1)
    fix=lambda s: re.sub(r'/_blob/([0-9a-f]{32})',lambda mm:pre+'assets/'+mm.group(1)+ext[mm.group(1)],s)
    M=META[lang]
    alt_pt='https://kcoland.netlify.app/'; alt_en='https://kcoland.netlify.app/en/'
    html=f'''<!doctype html>
<html lang="{M['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{M['title']}</title>
<meta name="description" content="{M['desc']}">
<link rel="alternate" hreflang="pt-BR" href="{alt_pt}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<meta property="og:type" content="website">
<meta property="og:title" content="KCO Creative Studio — Kco Oyakawa">
<meta property="og:description" content="{M['desc']}">
<meta property="og:image" content="{pre}assets/a373c121e4d40748d81761f2831b4f56.jpg">
<meta name="theme-color" content="#F3F1EC">
{fix(helmet)}
<script>window.KCO_ASSET_EXT={json.dumps(ext)};window.KCO_ASSET_BASE="{pre}";</script>
<script src="{pre}runtime.js"></script>
<script>
{js}
window.Component = Component;
</script>
<script type="application/json" id="kco-props">{props}</script>
</head>
<body>
<template id="kco-template">{tpl}</template>
<div id="app"></div>
<noscript><p style="padding:40px;font-family:sans-serif">{M['ns']}</p></noscript>
</body>
</html>
'''
    open(out+('/index.html' if lang=='pt' else '/en/index.html'),'w').write(html)
shutil.copy('runtime.js',out+'/runtime.js')
open(out+'/_headers','w').write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n")
open(out+'/robots.txt','w').write("User-agent: *\nAllow: /\n")
print(len(used),'arquivos')
