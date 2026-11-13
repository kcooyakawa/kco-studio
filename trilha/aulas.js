/* Ilustrações das aulas (SVG, tema escuro da trilha) */
window.FIGS = (()=>{
const G='<defs><linearGradient id="fg" x1="0" x2="1"><stop offset="0" stop-color="#7c5cff"/><stop offset=".5" stop-color="#e85d9c"/><stop offset="1" stop-color="#ff9a62"/></linearGradient></defs>';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${o}>${s}</text>`;
const wrap=(svg,cap)=>`<figure class="fig"><div class="sc"><svg viewBox="0 0 640 ${svg[0]}" role="img" aria-label="${cap}">${G}<style>text{fill:#f5f5f7;font:500 14px Inter,system-ui,sans-serif}.s{fill:#9a9aa3;font-size:12.5px}.b{font-weight:700;font-size:16px}.c{fill:#1c1c22;stroke:rgba(255,255,255,.1)}.n{font-weight:700;font-size:26px}</style>${svg[1]}</svg></div><figcaption>${cap}</figcaption></figure>`;
const card=(x,t,a,l1,l2,l3)=>`<rect class="c" x="${x}" y="10" width="196" height="200" rx="18"/><circle cx="${x+34}" cy="46" r="20" fill="url(#fg)"/>${T(x+24,52,a,'class="b" fill="#fff"')}${T(x+64,42,t,'class="b"')}${T(x+64,60,l1,'class="s"')}${T(x+18,104,'Quer',"class='s'")}${T(x+18,124,l2)}${T(x+18,160,'Decide com',"class='s'")}${T(x+18,180,l3)}`;
return {
personas:wrap([220,card(4,'Investidor','I','45–60 anos','Renda e valorização','Números e liquidez')+card(222,'Família','F','35–45, filhos','Espaço, escola, lazer','Emoção e segurança')+card(440,'Downsizer','D','60+, sem filhos em casa','Menor e sofisticado','Confiança, sem pressa')],'Três personas do alto padrão: cada uma pede um anúncio diferente'),
jornada:wrap([230,[['Descoberta','Percebe que precisa mudar','Guia do bairro','Estilo de vida'],['Consideração','Compara bairros e plantas','Tour em vídeo','Comparativo, ficha'],['Decisão','Escolhe imóvel e corretor','Visita privativa','Depoimentos, condições']].map((f,i)=>{const x=4+i*214;return `<rect class="c" x="${x}" y="40" width="200" height="180" rx="18"/><rect x="${x}" y="40" width="200" height="6" rx="3" fill="url(#fg)" opacity="${.45+i*.27}"/>${T(x+18,30,'0'+(i+1),'class="s"')}${T(x+18,80,f[0],'class="b"')}${T(x+18,102,f[1],'class="s"')}${T(x+18,150,'Conteúdo',"class='s'")}${T(x+18,172,f[2])}${T(x+18,194,f[3],'class="s"')}`+(i<2?`<path d="M${x+204} 130h6" stroke="#55555f" stroke-width="2"/>`:'')}).join('')],'A jornada do comprador: mensagem certa para cada fase'),
segmento:wrap([200,`<rect class="c" x="4" y="20" width="250" height="160" rx="18"/>${T(24,54,'Meta bloqueia','class="b"')}${['Idade','Gênero','CEP fino'].map((s,i)=>`<path d="M26 ${82+i*30}l12 12M38 ${82+i*30}l-12 12" stroke="#ff8a8a" stroke-width="2.4"/>`+T(52,94+i*30,s)).join('')}<path d="M270 100h70" stroke="url(#fg)" stroke-width="3"/><path d="M334 92l10 8-10 8" fill="none" stroke="#ff9a62" stroke-width="3"/><rect x="356" y="20" width="280" height="160" rx="18" fill="url(#fg)" opacity=".16"/><rect x="356" y="20" width="280" height="160" rx="18" fill="none" stroke="url(#fg)"/>${T(376,54,'Quem segmenta é o criativo','class="b"')}${['Linguagem da persona','Imagem que ela valoriza','Público por comportamento'].map((s,i)=>`<path d="M378 ${86+i*30}l5 5 10-11" fill="none" stroke="#3ddc97" stroke-width="2.4"/>`+T(404,94+i*30,s)).join('')}`],'Imóveis são categoria especial: o criativo faz a segmentação'),
ciclo:wrap([300,`<circle cx="320" cy="150" r="110" fill="none" stroke="url(#fg)" stroke-width="3" stroke-dasharray="6 8"/>${[['Atrair',320,40,'conteúdo útil'],['Engajar',500,230,'oferta + resposta rápida'],['Encantar',140,230,'atendimento → indicação']].map(([t,x,y,s])=>`<circle cx="${x}" cy="${y}" r="34" fill="#1c1c22" stroke="rgba(255,255,255,.14)"/>${T(x,y+5,t,'class="b" text-anchor="middle"')}${T(x,y+54,s,'class="s" text-anchor="middle"')}`).join('')}${T(320,146,'Cliente','class="b" text-anchor="middle"')}${T(320,166,'no centro','class="s" text-anchor="middle"')}`],'Inbound é um ciclo: cliente encantado indica e alimenta o próximo'),
funil:wrap([290,[['~600','leads totais',600],['60','leads qualificados',470],['12','visitas',340],['4','propostas',230],['1','venda',140]].map(([n,l,w],i)=>{const x=(640-w)/2;return `<rect x="${x}" y="${8+i*56}" width="${w}" height="48" rx="12" fill="url(#fg)" opacity="${.22+i*.18}"/>${T(320,40+i*56,`<tspan class="b">${n}</tspan>  <tspan class="s" style="fill:#e6e6ea">${l}</tspan>`,'text-anchor="middle"')}`}).join('')],'Funil de trás para frente: comece pela venda e volte etapa por etapa'),
smart:wrap([150,['S','M','A','R','T'].map((l,i)=>{const x=4+i*128,w=['Específica','Mensurável','Alcançável','Relevante','Com prazo'][i];return `<rect class="c" x="${x}" y="10" width="116" height="130" rx="16"/>${T(x+58,72,l,'class="n" text-anchor="middle" fill="url(#fg)"')}${T(x+58,108,w,'class="s" text-anchor="middle"')}`}).join('')],'Metas SMART'),
landing:wrap([420,`<rect class="c" x="170" y="6" width="300" height="408" rx="28"/><rect x="186" y="26" width="268" height="28" rx="8" fill="#2a2a32"/>${T(198,45,'1 · Título com benefício','class="s"')}<rect x="186" y="64" width="268" height="110" rx="10" fill="url(#fg)" opacity=".35"/>${T(320,124,'2 · Galeria (6 fotos)','text-anchor="middle"')}<rect x="186" y="184" width="128" height="54" rx="8" fill="#2a2a32"/>${T(196,215,'3 · Ficha técnica','class="s"')}<rect x="326" y="184" width="128" height="54" rx="8" fill="#2a2a32"/>${T(336,215,'4 · Mapa','class="s"')}<rect x="186" y="248" width="268" height="40" rx="8" fill="#2a2a32"/>${T(198,273,'5 · Prova: depoimento, construtora','class="s"')}<rect x="186" y="298" width="268" height="62" rx="10" fill="none" stroke="url(#fg)"/>${T(198,323,'6 · Formulário curto','class="s"')}<rect x="198" y="334" width="140" height="16" rx="4" fill="#2a2a32"/><rect x="186" y="370" width="268" height="32" rx="16" fill="#3ddc97"/>${T(320,391,'WhatsApp fixo','text-anchor="middle" style="fill:#0a0a0c;font-weight:700"')}${T(20,90,'Uma página','class="b"')}${T(20,112,'uma oferta','class="b"')}${T(20,134,'um botão','class="b"')}${T(490,330,'Filtra curiosos:','class="s"')}${T(490,350,'faixa de investimento')}${T(490,370,'prazo · LGPD','class="s"')}`],'Anatomia de uma landing page de imóvel no celular'),
form:wrap([180,`<path d="M40 150h560" stroke="#2a2a32" stroke-width="2"/><path d="M60 40 C200 60 420 120 580 140" fill="none" stroke="#5b8cff" stroke-width="3"/><path d="M60 140 C200 120 420 60 580 40" fill="none" stroke="#e85d9c" stroke-width="3"/>${T(40,172,'2 campos','class="s"')}${T(540,172,'6 campos','class="s"')}${T(500,130,'quantidade de leads','style="fill:#5b8cff"')}${T(470,32,'qualidade dos leads','style="fill:#e85d9c"')}<rect x="250" y="20" width="150" height="140" rx="12" fill="#fff" opacity=".05"/>${T(325,14,'alto padrão: 3–5','class="s" text-anchor="middle"')}`],'Mais campos = menos leads, porém melhores. No alto padrão, de 3 a 5 campos'),
ab:wrap([190,`${[['A','Título: nome do prédio','2,1%',4],['B','Título: 3 suítes a 400 m do parque','3,4%',326]].map(([v,t,r,x])=>`<rect class="c" x="${x}" y="10" width="310" height="170" rx="18"/>${T(x+20,44,'Versão '+v,'class="s"')}${T(x+20,70,t)}<rect x="${x+20}" y="90" width="${v==='A'?110:180}" height="16" rx="8" fill="${v==='A'?'#3a3a42':'url(#fg)'}"/>${T(x+20,150,r,'class="n"')}${T(x+110,150,'conversão','class="s"')}`).join('')}`],'Teste A/B: mude uma coisa por vez e compare (números ilustrativos)'),
temp:wrap([170,[['Frio','baixou material, não respondeu','#5b8cff'],['Morno','respondeu, faltam dados','#ff9a62'],['Quente','orçamento, prazo e decisor','#e85d9c']].map(([t,s,c],i)=>{const x=4+i*214;return `<rect class="c" x="${x}" y="10" width="200" height="150" rx="18"/><circle cx="${x+30}" cy="44" r="10" fill="${c}"/>${T(x+50,50,t,'class="b"')}${T(x+20,90,s,'class="s"')}<rect x="${x+20}" y="120" width="160" height="8" rx="4" fill="#2a2a32"/><rect x="${x+20}" y="120" width="${50+i*55}" height="8" rx="4" fill="${c}"/>`}).join('')],'Temperatura do lead'),
pipeline:wrap([170,['Novo','Contato','Qualificado','Visita','Proposta','Venda'].map((t,i)=>{const x=4+i*106;return `<path d="M${x} 40h88l12 30-12 30h-88l12-30z" fill="url(#fg)" opacity="${.2+i*.15}"/>${T(x+52,75,t,'text-anchor="middle" style="font-size:13px;font-weight:600"')}${T(x+52,130,[18,12,7,4,2,1][i]+' leads','class="s" text-anchor="middle"')}`}).join('')+T(320,160,'Perdido? Registre o motivo: preço, localização, desistiu, comprou outro','class="s" text-anchor="middle"')],'O pipeline: todo lead está em uma etapa (exemplo de um mês)'),
followup:wrap([150,`<path d="M30 70h580" stroke="#2a2a32" stroke-width="3"/>${[[0,'Dia 0','Material'],[2,'Dia 2','Bairro'],[5,'Dia 5','Similares'],[9,'Dia 9','Depoimento'],[14,'Dia 14','Visita']].map(([d,a,b])=>{const x=30+d*41;return `<circle cx="${x}" cy="70" r="12" fill="url(#fg)"/>${T(x,44,a,'class="s" text-anchor="middle"')}${T(x,110,b,'text-anchor="middle"')}`}).join('')}${T(30,140,'Primeira resposta em até 5 minutos','class="s"')}`],'Sequência de nutrição: 5 toques em 14 dias')
};})();

/* Aulas próprias do Curso Tráfego Imóveis by W3W.
   Temas equivalentes aos da HubSpot Academy, escritos do zero para o alto padrão. */
window.AULAS = {
personas: {
  t:'Personas, jornada do comprador e segmentação', min:25,
  caps:[
   {h:'1. Quem compra um imóvel de R$ 3 milhões',f:FIGS.personas,b:`
<p>O comprador de alto padrão chega ao corretor com <b>70% da decisão já tomada</b>. Antes do primeiro contato ele já viu portais, o Instagram da imobiliária, o Google Maps do quarteirão e vídeos do bairro.</p>
<p>Persona é o retrato desse cliente montado a partir de conversas reais — não de achismo. Ela responde: o que ele quer resolver, o que o impede de decidir e onde ele passa tempo online.</p>
<h4>Três personas típicas da W3W</h4>
<ul>
<li><b>Investidor</b> · 45–60 anos, busca renda ou valorização. Pergunta sobre m² do bairro, liquidez, condomínio. Decide com números.</li>
<li><b>Família em expansão</b> · casal 35–45, filhos pequenos. Quer mais espaço, escola perto, lazer no prédio. Decide em casal, com emoção e segurança.</li>
<li><b>Downsizer</b> · 60+, filhos saíram de casa. Troca casa grande por apartamento menor, sofisticado e prático. Decide devagar, valoriza confiança.</li>
</ul>
<p class="tip">Regra de ouro: se você não consegue dizer qual dor cada anúncio resolve para qual persona, o anúncio está falando com ninguém.</p>`},
   {h:'2. A jornada em três fases',f:FIGS.jornada,b:`
<p>Todo comprador passa por três momentos, e cada um pede um conteúdo diferente:</p>
<ol>
<li><b>Descoberta</b> — percebe que precisa mudar. <i>Conteúdo:</i> guia do bairro, estilo de vida, "como é morar em Moema".</li>
<li><b>Consideração</b> — compara bairros, plantas e valores. <i>Conteúdo:</i> comparativos, tour em vídeo, ficha técnica, simulação.</li>
<li><b>Decisão</b> — escolhe o imóvel e quem vai assessorá-lo. <i>Conteúdo:</i> visita privativa, depoimentos, condições de pagamento.</li>
</ol>
<p>Anúncio de "agende sua visita" para quem ainda está na descoberta gera lead frio. Guia de bairro para quem já está decidindo atrasa a venda. <b>Mensagem certa, fase certa.</b></p>`},
   {h:'3. Segmentação: do público ao criativo',f:FIGS.segmento,b:`
<p>Imóveis são <b>categoria especial</b> na Meta: não dá para segmentar por idade, gênero ou CEP fino. Por isso, no alto padrão, <b>o criativo é quem segmenta</b>.</p>
<ul>
<li>Use a linguagem e as imagens da persona: vista e rentabilidade para o investidor, playground e planta para a família.</li>
<li>Monte públicos a partir de comportamento: quem visitou o site, quem assistiu 50% do vídeo, quem engajou no Instagram.</li>
<li>Crie públicos semelhantes a partir de <b>quem visitou ou comprou</b>, não de quem só preencheu formulário.</li>
</ul>
<p class="tip">Exercício mental: para cada imóvel da carteira, escreva uma frase de anúncio para cada persona. Se as três frases forem iguais, refaça.</p>`}
  ],
  quiz:[
   {q:'No alto padrão, o que mais segmenta um anúncio na Meta?',o:['A idade do público','O CEP do bairro','O criativo e a mensagem','O horário de veiculação'],c:2},
   {q:'Um comprador comparando plantas e valores de 3 prédios está em qual fase?',o:['Descoberta','Consideração','Decisão'],c:1},
   {q:'Persona deve ser construída a partir de…',o:['Conversas reais com clientes','Opinião do time de vendas','O perfil médio do Brasil'],c:0}
  ]},

inbound: {
  t:'Fundamentos de Inbound para imóveis', min:20,
  caps:[
   {h:'1. Atrair, engajar, encantar',f:FIGS.ciclo,b:`
<p>Inbound é fazer o cliente vir até você porque você foi útil antes de pedir algo. São três movimentos que viram um ciclo:</p>
<ul>
<li><b>Atrair</b> — conteúdo e anúncios que respondem às dúvidas reais do comprador.</li>
<li><b>Engajar</b> — oferecer algo de valor em troca do contato (book, tabela, visita privativa) e responder rápido.</li>
<li><b>Encantar</b> — atendimento impecável antes, durante e depois da venda. Cliente encantado indica, e a indicação alimenta o próximo ciclo.</li>
</ul>
<p>No alto padrão, a <b>indicação</b> é o canal mais barato que existe. O tráfego pago acelera o ciclo; não substitui o encantamento.</p>`},
   {h:'2. Funil de trás para frente',f:FIGS.funil,b:`
<p>Comece pela meta de vendas e volte etapa por etapa. Um exemplo com taxas de referência (ajuste com os seus números):</p>
<table>
<tr><td>1 venda</td><td>← 4 propostas</td></tr>
<tr><td>4 propostas</td><td>← 12 visitas</td></tr>
<tr><td>12 visitas</td><td>← 60 leads qualificados</td></tr>
<tr><td>60 qualificados</td><td>← ~600 leads totais</td></tr>
</table>
<p>Se a verba do mês é R$ 6.000 e você precisa de 600 leads, o <b>custo por lead máximo</b> é R$ 10. Acima disso a conta não fecha — ou você melhora a qualificação.</p>`},
   {h:'3. Metas SMART',f:FIGS.smart,b:`
<p>"Gerar mais leads" não é meta. Meta boa é:</p>
<ul><li><b>S</b>pecífica · <b>M</b>ensurável · <b>A</b>lcançável · <b>R</b>elevante · com <b>T</b>empo definido.</li></ul>
<p><i>Exemplo:</i> "Gerar 60 leads qualificados para o Síntese Moema até 15 de dezembro, com custo por lead qualificado abaixo de R$ 100."</p>`}
  ],
  quiz:[
   {q:'Qual movimento do inbound gera indicações?',o:['Atrair','Engajar','Encantar'],c:2},
   {q:'Verba de R$ 6.000 e meta de 600 leads: qual o CPL máximo?',o:['R$ 6','R$ 10','R$ 60'],c:1},
   {q:'Qual destas é uma meta SMART?',o:['Vender mais este ano','Aumentar o engajamento','60 leads qualificados até 15/12 com CPL qualificado < R$ 100'],c:2}
  ]},

landing: {
  t:'Formulários e landing pages que convertem', min:20,
  caps:[
   {h:'1. Anatomia de uma landing page de imóvel',f:FIGS.landing,b:`
<p><b>Uma página, uma oferta, um botão.</b> Tudo que não ajuda a converter sai.</p>
<ol>
<li>Título com benefício ("3 suítes a 400 m do Parque Ibirapuera"), não só o nome do prédio.</li>
<li>Galeria com as 6 melhores imagens: fachada, living, vista, suíte, lazer, planta.</li>
<li>Ficha técnica curta: metragem, suítes, vagas, entrega.</li>
<li>Mapa e 3 pontos de interesse a pé.</li>
<li>Prova: depoimento, construtora, prêmios.</li>
<li>Formulário curto + botão de WhatsApp fixo no celular.</li>
</ol>`},
   {h:'2. Ofertas e formulários',f:FIGS.form,b:`
<p>Ninguém deixa telefone de graça. Ofereça troca de valor: <b>book digital, tabela de valores, vídeo exclusivo, visita privativa</b>.</p>
<p>O formulário é o filtro. Para alto padrão, 3 a 5 campos:</p>
<ul><li>Nome e WhatsApp</li><li>Faixa de investimento (ex.: até 3 mi / 3–5 mi / acima de 5 mi)</li><li>Prazo para comprar</li><li>Aceite LGPD</li></ul>
<p>Menos campos = mais leads. Mais campos = leads melhores. No alto padrão, prefira qualidade.</p>
<p class="tip">A página de obrigado é a etapa mais esquecida: mostre o próximo passo ("um consultor fala com você em até 5 minutos") e ofereça agendar a visita ali mesmo.</p>`},
   {h:'3. Teste A/B',f:FIGS.ab,b:`
<p>Mude <b>uma coisa por vez</b>: título, imagem principal, número de campos ou texto do botão. Escreva a hipótese antes ("título com preço converte mais") e espere volume suficiente — pelo menos algumas dezenas de conversões por versão — antes de declarar vencedor.</p>`}
  ],
  quiz:[
   {q:'Qual campo mais ajuda a filtrar curiosos?',o:['E-mail','Faixa de investimento','Cidade'],c:1},
   {q:'Num teste A/B você deve mudar…',o:['Tudo de uma vez','Uma variável por vez','Só a cor'],c:1},
   {q:'O que a página de obrigado deve ter?',o:['Nada, só agradecer','O próximo passo e opção de agendar visita','Outros imóveis aleatórios'],c:1}
  ]},

crm: {
  t:'Gestão de contatos e CRM', min:20,
  caps:[
   {h:'1. Lead não é cliente',f:FIGS.temp,b:`
<p>Classifique todo contato em três temperaturas:</p>
<ul>
<li><b>Frio</b> — baixou material, não respondeu.</li>
<li><b>Morno</b> — respondeu, tem interesse, faltam dados.</li>
<li><b>Quente</b> — orçamento, prazo e decisor confirmados.</li>
</ul>
<h4>Lead scoring simples</h4>
<table>
<tr><td>Faixa de investimento compatível</td><td>+30</td></tr>
<tr><td>Prazo até 6 meses</td><td>+25</td></tr>
<tr><td>Respondeu em menos de 24h</td><td>+15</td></tr>
<tr><td>Pediu visita</td><td>+30</td></tr>
</table>
<p>Acima de 60 pontos, passa para o corretor no mesmo dia.</p>`},
   {h:'2. Pipeline',f:FIGS.pipeline,b:`
<p>Etapas que todo lead percorre — e todo lead precisa estar em uma delas:</p>
<p><b>Novo → Contato feito → Qualificado → Visita agendada → Proposta → Venda / Perdido</b></p>
<p>Ao marcar "Perdido", registre o motivo (preço, localização, desistiu, comprou outro). Em 2 meses esses motivos dizem mais sobre a campanha do que qualquer métrica do Gerenciador.</p>
<p class="tip">Planilha funciona no começo. Quando passar de ~50 leads ativos, migre para um CRM gratuito.</p>`},
   {h:'3. Nutrição e follow-up',f:FIGS.followup,b:`
<p>Responda em até <b>5 minutos</b>. Depois, uma sequência de 5 toques em 14 dias:</p>
<ol>
<li>Dia 0 — boas-vindas + material pedido.</li>
<li>Dia 2 — conteúdo do bairro.</li>
<li>Dia 5 — 2 ou 3 imóveis semelhantes.</li>
<li>Dia 9 — depoimento de cliente.</li>
<li>Dia 14 — convite para visita privativa.</li>
</ol>
<p>Personalize pela persona e pela fase. A mesma mensagem para todos é spam bem-educado.</p>`}
  ],
  quiz:[
   {q:'Tempo ideal de primeira resposta a um lead:',o:['Até 5 minutos','Até 24 horas','Até 3 dias'],c:0},
   {q:'Por que registrar o motivo de perda?',o:['Burocracia','Para ajustar campanha e oferta','Para descartar o lead'],c:1},
   {q:'Um lead com orçamento, prazo e decisor confirmados é…',o:['Frio','Morno','Quente'],c:2}
  ]}
};
