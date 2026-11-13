/* Ilustrações das aulas (SVG, tema escuro da trilha) */
window.FIGS = (()=>{
const G='<defs><linearGradient id="fg" x1="0" x2="1"><stop offset="0" stop-color="#7c5cff"/><stop offset=".5" stop-color="#e85d9c"/><stop offset="1" stop-color="#ff9a62"/></linearGradient></defs>';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${o}>${s}</text>`;
const wrap=(svg,cap)=>`<figure class="fig"><div class="sc"><svg viewBox="0 0 640 ${svg[0]}" role="img" aria-label="${cap}">${G}<style>text{fill:#f5f5f7;font:500 14px Inter,system-ui,sans-serif}.s{fill:#9a9aa3;font-size:12.5px}.b{font-weight:700;font-size:16px}.c{fill:#1c1c22;stroke:rgba(255,255,255,.1)}.n{font-weight:700;font-size:26px}</style>${svg[1]}</svg></div><figcaption>${cap}</figcaption></figure>`;
const card=(x,t,a,l1,l2,l3)=>`<rect class="c" x="${x}" y="10" width="196" height="200" rx="18"/><circle cx="${x+34}" cy="46" r="20" fill="url(#fg)"/>${T(x+24,52,a,'class="b" fill="#fff"')}${T(x+64,42,t,'class="b"')}${T(x+64,60,l1,'class="s"')}${T(x+18,104,'Quer',"class='s'")}${T(x+18,124,l2)}${T(x+18,160,'Decide com',"class='s'")}${T(x+18,180,l3)}`;
return {
personas:wrap([220,card(4,'Investidor','I','45–60 anos','Renda e valorização','Números e liquidez')+card(222,'Família','F','35–45, filhos','Espaço, escola, lazer','Emoção e segurança')+card(440,'Downsizer','D','60+, sem filhos em casa','Menor e sofisticado','Confiança, sem pressa')],'Três personas do alto padrão: cada uma pede um anúncio diferente'),
jornada:wrap([230,[['Descoberta','Percebe que precisa mudar','Guia do bairro','Estilo de vida'],['Consideração','Compara bairros e plantas','Tour em vídeo','Comparativo, ficha'],['Decisão','Escolhe imóvel e corretor','Visita privativa','Depoimentos, condições']].map((f,i)=>{const x=4+i*214;return `<rect class="c" x="${x}" y="40" width="200" height="180" rx="18"/><rect x="${x}" y="40" width="200" height="6" rx="3" fill="url(#fg)" opacity="${.45+i*.27}"/>${T(x+18,30,'0'+(i+1),'class="s"')}${T(x+18,80,f[0],'class="b"')}${T(x+18,102,f[1],'class="s"')}${T(x+18,150,'Conteúdo',"class='s'")}${T(x+18,172,f[2])}${T(x+18,194,f[3],'class="s"')}`+(i<2?`<path d="M${x+204} 130h6" stroke="#55555f" stroke-width="2"/>`:'')}).join('')],'A jornada do comprador: mensagem certa para cada fase'),
fontes:wrap([200,[['01','Quem já comprou','10–20 vendas'],['02','Corretores','objeções reais'],['03','Entrevistas','5 conversas'],['04','Dados digitais','buscas, directs']].map(([n,t,s],i)=>{const x=4+i*160;return `<rect class="c" x="${x}" y="20" width="148" height="160" rx="18"/>${T(x+18,58,n,'class="n" fill="url(#fg)"')}${T(x+18,110,t,'class="b"')}${T(x+18,134,s,'class="s"')}`}).join('')],'Quatro fontes para pesquisar a persona, em ordem de prioridade'),
canvas:wrap([330,`<rect class="c" x="4" y="6" width="632" height="318" rx="20"/>${[['Perfil',20,24],['Gatilho de mudança',226,24],['Critérios de decisão',432,24],['Objeções',20,128],['Influenciadores',226,128],['Canais',432,128]].map(([t,x,y])=>`<rect x="${x}" y="${y}" width="190" height="90" rx="12" fill="#26262e"/>${T(x+14,y+28,t,'class="s"')}<rect x="${x+14}" y="${y+44}" width="140" height="6" rx="3" fill="#3a3a44"/><rect x="${x+14}" y="${y+60}" width="100" height="6" rx="3" fill="#3a3a44"/>`).join('')}<rect x="20" y="232" width="602" height="76" rx="12" fill="url(#fg)" opacity=".18"/><rect x="20" y="232" width="602" height="76" rx="12" fill="none" stroke="url(#fg)"/>${T(36,262,'Frase-síntese','class="s"')}${T(36,290,'"Esse tem que ser o apartamento dos próximos 15 anos."','class="b"')}`],'Canvas da persona: os campos que mudam a mensagem do anúncio'),
matriz:wrap([290,`${['Descoberta','Consideração','Decisão'].map((f,i)=>T(196+i*148,26,f,'class="s" text-anchor="middle"')).join('')}${['Investidor','Família','Downsizer'].map((p,r)=>T(10,84+r*86,p,'class="b"')+[0,1,2].map(c=>`<rect x="${124+c*148}" y="${44+r*86}" width="140" height="76" rx="12" fill="url(#fg)" opacity="${.12+c*.12}"/>${T(194+c*148,88+r*86,'criativo '+(r*3+c+1),'class="s" text-anchor="middle" style="fill:#e6e6ea"')}`).join('')).join('')}`],'Matriz persona × fase: 9 mensagens, 9 criativos'),
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
  t:'Personas, jornada do comprador e segmentação', min:55,
  caps:[
   {h:'1. Por que persona decide o seu custo por lead',b:`
<p>No alto padrão, o erro mais caro do tráfego não é técnico: é falar com a pessoa errada. Um anúncio de cobertura de R$ 6 milhões que atrai curiosos gera lead barato e venda zero. O mesmo anúncio, escrito para o comprador certo, gera menos leads, mas leads que visitam.</p>
<table>
<tr><td>Campanha genérica ("apartamento de luxo em Moema")</td><td>CPL R$ 18 · 3% qualificados</td></tr>
<tr><td>Campanha por persona ("3 suítes a 5 min da escola X, com vaga para 3 carros")</td><td>CPL R$ 45 · 22% qualificados</td></tr>
</table>
<p>Faça a conta do <b>custo por lead qualificado</b>: R$ 18 ÷ 3% = <b>R$ 600</b> contra R$ 45 ÷ 22% = <b>R$ 205</b>. O lead "caro" sai três vezes mais barato. <i>(Números ilustrativos, mas a proporção é típica.)</i></p>
<p class="tip">A métrica que importa nunca é o CPL sozinho. É o custo por lead qualificado, por visita e por proposta. A persona é o que move esses números.</p>`},
   {h:'2. Como pesquisar a persona (sem achismo)',f:FIGS.fontes,b:`
<p>Persona boa nasce de dados e conversas. Use quatro fontes, nesta ordem:</p>
<ol>
<li><b>Quem já comprou.</b> Puxe as últimas 10–20 vendas da W3W: idade, profissão, de onde veio, por que comprou, quanto tempo levou, quem decidiu.</li>
<li><b>Os corretores.</b> Eles ouvem as objeções todo dia. Pergunte: "quais são as 3 frases que você mais escuta antes de alguém desistir?"</li>
<li><b>Entrevistas com clientes.</b> 5 conversas de 20 minutos já mostram padrões.</li>
<li><b>Dados digitais.</b> Comentários e directs no Instagram, termos buscados no Google (Planejador de palavras-chave), perguntas recorrentes nos portais.</li>
</ol>
<h4>Roteiro de entrevista (copie e use)</h4>
<ol>
<li>O que fez você começar a procurar um imóvel naquele momento?</li>
<li>Onde pesquisou primeiro? E depois?</li>
<li>O que quase fez você desistir ou escolher outro imóvel?</li>
<li>Quem mais participou da decisão?</li>
<li>O que fez você confiar na imobiliária / no corretor?</li>
</ol>
<p class="tip">Pergunte sobre o que a pessoa <b>fez</b>, não sobre o que ela <b>faria</b>. Comportamento passado prevê muito melhor que intenção declarada.</p>`},
   {h:'3. O canvas da persona de alto padrão',f:FIGS.canvas,b:`
<p>Persona não é "homem, 45 anos, classe A". Isso descreve metade de Moema. O que importa para o tráfego são os campos que mudam a <b>mensagem</b>:</p>
<ul>
<li><b>Gatilho de mudança</b>: o evento que fez a busca começar (filho nasceu, bônus, venda de empresa, filhos saíram de casa).</li>
<li><b>Critérios de decisão</b>: o que precisa ser verdade para comprar (escola perto, planta para home office, liquidez).</li>
<li><b>Objeções</b>: o que trava (condomínio alto, prazo de entrega, "vou esperar os juros caírem").</li>
<li><b>Influenciadores</b>: quem opina (cônjuge, contador, filhos, arquiteto).</li>
<li><b>Canais</b>: onde ele está quando pensa nisso (Instagram à noite, Google no trabalho, indicação de amigo).</li>
<li><b>Frase-síntese</b>: algo que ele diria. Ela vira gancho de anúncio.</li>
</ul>
<h4>Exemplo preenchido: "Família Helena"</h4>
<table>
<tr><td>Perfil</td><td>Casal 38–44, médica e engenheiro, 2 filhos (3 e 7)</td></tr>
<tr><td>Gatilho</td><td>Segundo filho; apartamento atual de 2 dormitórios ficou pequeno</td></tr>
<tr><td>Critérios</td><td>3 suítes, escola a 10 min, lazer infantil, 2+ vagas</td></tr>
<tr><td>Objeções</td><td>Medo de obra atrasar; condomínio acima de R$ 4 mil</td></tr>
<tr><td>Influenciadores</td><td>Os dois decidem; a mãe dela opina sobre bairro</td></tr>
<tr><td>Canais</td><td>Instagram 21h–23h; Google em pesquisa de escola</td></tr>
<tr><td>Frase</td><td>"A gente quer parar de mudar. Esse tem que ser o apartamento dos próximos 15 anos."</td></tr>
</table>
<p class="tip">Faça no máximo 3 personas por empreendimento. Mais que isso, você não consegue produzir criativo bom para todas.</p>`},
   {h:'4. A jornada: fases, sinais e métricas',f:FIGS.jornada,b:`
<p>No alto padrão, a jornada leva de <b>3 a 12 meses</b>. Seu trabalho é estar presente em cada fase com o conteúdo certo e saber <b>em que fase cada lead está</b>.</p>
<table>
<tr><td><b>Descoberta</b> · sinal: consome conteúdo de bairro, salva posts, não pede preço</td><td>KPI: alcance, ThruPlay, seguidores</td></tr>
<tr><td><b>Consideração</b> · sinal: pede book, tabela, planta; compara 2–3 opções</td><td>KPI: leads, CPL, % qualificados</td></tr>
<tr><td><b>Decisão</b> · sinal: pede visita, pergunta condições, traz o cônjuge</td><td>KPI: visitas, propostas, custo por visita</td></tr>
</table>
<h4>Os erros clássicos</h4>
<ul>
<li>Mandar "agende sua visita" para quem está em descoberta: vira lead frio e corretor frustrado.</li>
<li>Mandar guia de bairro para quem já pediu proposta: atrasa a venda.</li>
<li>Medir a campanha de descoberta por CPL: ela não foi feita para gerar lead, e sim para encher o público de remarketing.</li>
</ul>
<p class="tip">Estrutura recomendada: 20–30% da verba em descoberta (vídeo e conteúdo), 60–70% em captação (cadastro e WhatsApp), 10% em remarketing para quem já engajou.</p>`},
   {h:'5. Matriz de mensagens: persona × fase',f:FIGS.matriz,b:`
<p>Cruzando 3 personas com 3 fases, você tem 9 mensagens. Elas viram o seu plano de criativos.</p>
<table>
<tr><td><b>Investidor · Descoberta</b></td><td>"Moema valorizou acima da média de SP nos últimos 5 anos. Veja por quê."</td></tr>
<tr><td><b>Investidor · Consideração</b></td><td>"Studio a 300 m do metrô: simulação de renda de locação no book."</td></tr>
<tr><td><b>Investidor · Decisão</b></td><td>"Últimas 2 unidades na tabela de lançamento. Condição válida até sexta."</td></tr>
<tr><td><b>Família · Descoberta</b></td><td>"Como é crescer em Moema: parques, escolas e ruas para pedalar."</td></tr>
<tr><td><b>Família · Consideração</b></td><td>"3 suítes, playground coberto e 3 vagas. Baixe a planta."</td></tr>
<tr><td><b>Família · Decisão</b></td><td>"Visita privativa no sábado, com espaço kids enquanto vocês conhecem."</td></tr>
<tr><td><b>Downsizer · Descoberta</b></td><td>"Menos metros, mais vida: o novo jeito de morar depois que os filhos crescem."</td></tr>
<tr><td><b>Downsizer · Consideração</b></td><td>"Planta compacta, acabamento de casa grande. Tour em vídeo."</td></tr>
<tr><td><b>Downsizer · Decisão</b></td><td>"Avaliamos seu imóvel atual na troca. Fale com um consultor."</td></tr>
</table>
<p class="tip">Cada linha vira um criativo e cada fase vira um conjunto de anúncios. É assim que a estratégia de persona chega no Gerenciador.</p>`},
   {h:'6. Segmentação na prática (Meta e Google)',f:FIGS.segmento,b:`
<p>Imóveis estão na <b>categoria especial de anúncios</b> da Meta: não dá para segmentar por idade, gênero ou CEP, e o raio mínimo é de cerca de 25 km. Por isso, no alto padrão, quem segmenta é o <b>criativo</b>.</p>
<h4>O que fazer no Meta</h4>
<ul>
<li><b>Público amplo + criativo específico</b>: deixe o algoritmo achar quem reage à mensagem da persona.</li>
<li><b>Públicos personalizados</b>: visitantes do site, quem assistiu 50%+ do vídeo, quem engajou no Instagram nos últimos 90 dias.</li>
<li><b>Semelhantes (lookalike)</b>: a partir de quem <b>visitou ou comprou</b> (lista do CRM), nunca de todos os leads.</li>
<li><b>Exclusões</b>: tire quem já é cliente e quem já virou lead nos últimos 30 dias.</li>
<li><b>Formulário que filtra</b>: faixa de investimento e prazo. O formulário também segmenta.</li>
</ul>
<h4>O que fazer no Google</h4>
<ul>
<li>Palavras de intenção da persona: "apartamento 3 suítes Moema", "studio para investir perto do metrô".</li>
<li>Negativas: "aluguel", "barato", "minha casa minha vida", "leilão".</li>
<li>Imóveis também é categoria sensível no Google: sem segmentação demográfica, então a palavra-chave faz o filtro.</li>
</ul>
<p class="tip">LGPD: use só dados que o cliente autorizou. Para subir a lista do CRM como público, o aceite no formulário precisa prever isso.</p>`}
  ],
  quiz:[
   {q:'Campanha A: CPL R$ 20 com 5% qualificados. Campanha B: CPL R$ 50 com 25% qualificados. Qual tem o menor custo por lead qualificado?',o:['A (R$ 400)','B (R$ 200)','São iguais'],c:1},
   {q:'Qual a melhor fonte para começar a construir uma persona?',o:['Perfil médio do Brasil no IBGE','Os últimos compradores e os corretores','Opinião do dono do empreendimento'],c:1},
   {q:'Qual campo do canvas mais ajuda a escrever o gancho do anúncio?',o:['Faixa etária','Frase-síntese e gatilho de mudança','Estado civil'],c:1},
   {q:'Um lead pediu a planta e comparou com outros 2 prédios. Que mensagem enviar?',o:['Guia de estilo de vida do bairro','Comparativo, tour em vídeo e ficha técnica','"Últimas unidades, feche hoje"'],c:1},
   {q:'Por que a campanha de descoberta não deve ser julgada por CPL?',o:['Porque o CPL dela é sempre zero','Porque o papel dela é gerar público de remarketing, não lead','Porque o Meta não mostra CPL'],c:1},
   {q:'Na categoria especial de imóveis do Meta, de qual público você deve criar o lookalike?',o:['Todos os leads do formulário','Quem visitou ou comprou (lista do CRM)','Seguidores de concorrentes'],c:1}
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
