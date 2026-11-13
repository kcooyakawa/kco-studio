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
   {h:'1. Por que persona decide o seu custo por lead',w:'cplq',b:`
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
   {h:'4. A jornada: fases, sinais e métricas',f:FIGS.jornada,d:{q:'Um lead respondeu ao anúncio de guia do bairro, salvou 3 posts e nunca perguntou preço. O corretor quer ligar oferecendo visita. O que você recomenda?',o:['Ligar já: lead é lead','Colocar em remarketing com conteúdo de consideração (tour, planta) e esperar um sinal de interesse','Descartar o lead'],c:1,why:'Ele está em <b>descoberta</b>. Oferecer visita agora queima o contato. O remarketing com conteúdo de consideração faz ele avançar e mostrar um sinal claro, como pedir a planta ou a tabela.'},b:`
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
   {h:'5. Matriz de mensagens: persona × fase',f:FIGS.matriz,d:{q:'Qual destes ganchos é o melhor para a persona Família na fase de consideração?',o:['"O empreendimento mais exclusivo de Moema"','"3 suítes, playground coberto e 3 vagas: baixe a planta"','"Condição especial até sexta"'],c:1,why:'Na consideração, a família compara plantas e itens concretos. "Exclusivo" não diz nada, e urgência de preço é mensagem de decisão.'},b:`
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
  t:'Inbound para imóveis de alto padrão', min:50,
  caps:[
   {h:'1. O comprador chega sozinho — se você estiver lá',f:FIGS.ciclo,b:`
<p>Inbound é a lógica de ser encontrado em vez de interromper. No alto padrão isso pesa ainda mais: o comprador pesquisa por meses, compara com calma e só fala com quem já ganhou a confiança dele antes do primeiro contato.</p>
<p>O ciclo tem três movimentos que se alimentam:</p>
<ul>
<li><b>Atrair</b>: conteúdo e anúncios que respondem perguntas reais (quanto vale o m² aqui? como é morar nesse bairro? vale a pena comprar na planta?).</li>
<li><b>Engajar</b>: trocar valor por contato (book, tabela, visita privativa) e responder rápido, com contexto.</li>
<li><b>Encantar</b>: atendimento acima do esperado antes, durante e depois da venda. Quem foi encantado indica, e a indicação é o lead mais barato e mais quente que existe.</li>
</ul>
<p class="tip">Tráfego pago acelera o ciclo, mas não substitui nenhuma das etapas. Anúncio bom para uma operação lenta só gera reclamação mais rápido.</p>`},
   {h:'2. O funil de trás para frente',f:FIGS.funil,w:'funil',b:`
<p>Todo planejamento começa pela meta de vendas, não pela verba. Volte etapa por etapa usando as taxas reais da operação; enquanto não tiver as suas, use referências do mercado e ajuste em 30 dias.</p>
<p>Brinque com o simulador abaixo: mude as taxas e veja como uma melhora no atendimento (qualificado → visita) reduz a verba necessária mais do que qualquer ajuste de anúncio.</p>`,
    d:{q:'Seu funil precisa de 600 leads para 1 venda. Qual destas ações costuma reduzir mais o custo da venda?',o:['Trocar a cor do botão do anúncio','Responder leads em até 5 minutos e qualificar por telefone','Dobrar a verba'],c:1,why:'A velocidade e a qualidade do atendimento mexem nas taxas do meio do funil (qualificado → visita), que costumam ser as mais baixas. Dobrar verba sem mexer nisso só dobra o custo.'}},
   {h:'3. Conteúdo que atrai o comprador certo',b:`
<p>Um bom plano de conteúdo para alto padrão gira em 4 pilares, cada um ligado a uma fase da jornada:</p>
<table>
<tr><td><b>Bairro e estilo de vida</b></td><td>Descoberta. Guias, rotas a pé, restaurantes, escolas, parques.</td></tr>
<tr><td><b>Mercado e investimento</b></td><td>Descoberta e consideração. Valorização, m², rentabilidade de locação, financiamento.</td></tr>
<tr><td><b>Produto</b></td><td>Consideração. Tour, planta comentada, acabamentos, comparativos.</td></tr>
<tr><td><b>Bastidores e prova</b></td><td>Decisão. Curadoria W3W, depoimentos, entregas, a equipe.</td></tr>
</table>
<h4>Um conteúdo, dez peças</h4>
<p>Produza um conteúdo-pilar por mês (ex.: "Guia completo para morar em Moema") e desdobre: 1 reel, 2 carrosséis, 4 stories, 1 e-mail, 1 post no Google Meu Negócio e 1 criativo de anúncio. Coerência e economia de produção.</p>
<p class="tip">Teste de qualidade: o conteúdo seria útil mesmo para quem não comprar com a W3W? Se sim, ele gera confiança. Se é só propaganda disfarçada, o público percebe.</p>`},
   {h:'4. Ofertas de engajamento: o que trocar pelo contato',b:`
<p>Ninguém deixa telefone em troca de "saiba mais". A oferta precisa ter valor claro e combinar com a fase do lead:</p>
<table>
<tr><td>Guia do bairro em PDF</td><td>Topo · gera muito lead, pouco qualificado</td></tr>
<tr><td>Book digital + plantas</td><td>Meio · o padrão do mercado</td></tr>
<tr><td>Tabela de valores e condições</td><td>Meio/fundo · filtra por intenção</td></tr>
<tr><td>Simulação de investimento personalizada</td><td>Fundo · ótima para investidor</td></tr>
<tr><td>Visita privativa / tour por vídeo ao vivo</td><td>Fundo · menos leads, muito mais quentes</td></tr>
</table>
<p>Rode pelo menos duas ofertas em paralelo: uma de meio de funil, para volume e remarketing, e uma de fundo, para leads prontos.</p>`,
    d:{q:'Para um investidor, qual oferta tende a gerar o lead mais qualificado?',o:['E-book "10 dicas para comprar imóvel"','Simulação de rentabilidade da unidade, enviada por um consultor','Sorteio de um vale-jantar'],c:1,why:'A simulação exige que ele informe dados reais e mostra intenção concreta. O e-book genérico e o sorteio atraem quem não compra.'}},
   {h:'5. Encantar: o pós-venda que vira canal de aquisição',b:`
<p>Na W3W, cada cliente encantado deve gerar, em média, pelo menos uma indicação. Isso só acontece com método:</p>
<ol>
<li><b>Entrega memorável</b>: chave entregue com um kit de boas-vindas e o guia do bairro.</li>
<li><b>Contato aos 30, 90 e 365 dias</b>: como está a adaptação? precisa de indicação de arquiteto ou mudança?</li>
<li><b>Pedido de indicação na hora certa</b>: depois de um elogio espontâneo, não no fechamento.</li>
<li><b>Depoimento em vídeo</b>: vira prova social nos anúncios de decisão.</li>
</ol>
<p class="tip">Para o tráfego, o cliente encantado ainda vale mais uma coisa: a lista de compradores vira a semente do público semelhante (lookalike) mais valioso da conta.</p>`},
   {h:'6. Metas SMART e o painel do inbound',f:FIGS.smart,b:`
<p>"Gerar mais leads" não é meta. Meta boa é específica, mensurável, alcançável, relevante e com prazo:</p>
<p class="tip">"Gerar 60 leads qualificados para o Síntese Moema até 15/12, com custo por lead qualificado abaixo de R$ 150 e pelo menos 8 visitas."</p>
<h4>Os 6 números do painel semanal</h4>
<table>
<tr><td>Investimento</td><td>quanto foi gasto</td></tr>
<tr><td>Leads e CPL</td><td>volume e custo</td></tr>
<tr><td>% qualificados</td><td>a saúde da mensagem e do formulário</td></tr>
<tr><td>Tempo de primeira resposta</td><td>a saúde do atendimento</td></tr>
<tr><td>Visitas e custo por visita</td><td>o que a diretoria quer ver</td></tr>
<tr><td>Indicações recebidas</td><td>a saúde do encantamento</td></tr>
</table>`}
  ],
  quiz:[
   {q:'Qual movimento do inbound gera o lead mais barato a longo prazo?',o:['Atrair','Engajar','Encantar (indicação)'],c:2},
   {q:'Verba de R$ 6.000 e o funil pede 600 leads. Qual o CPL máximo?',o:['R$ 6','R$ 10','R$ 60'],c:1},
   {q:'Que oferta combina com um lead em consideração?',o:['Guia do bairro','Book com plantas e tabela','Pesquisa de satisfação'],c:1},
   {q:'Qual é o melhor momento para pedir indicação?',o:['Na assinatura do contrato','Depois de um elogio espontâneo do cliente','Nunca: é invasivo'],c:1},
   {q:'Qual destas é uma meta SMART?',o:['Vender mais neste ano','Aumentar o engajamento no Instagram','60 leads qualificados até 15/12 com custo por qualificado abaixo de R$ 150'],c:2},
   {q:'Um conteúdo-pilar mensal serve principalmente para…',o:['Substituir os anúncios','Gerar várias peças coerentes com menos produção','Ranquear no Google em uma semana'],c:1}
  ]},

landing: {
  t:'Landing pages e formulários que convertem', min:50,
  caps:[
   {h:'1. A página é onde o dinheiro do anúncio vira (ou não) lead',b:`
<p>Você pode ter o melhor anúncio do mercado: se a página decepciona, o clique pago vai embora. Uma landing page de imóvel tem um único trabalho, que é fazer a pessoa certa dar o próximo passo.</p>
<table>
<tr><td>Taxa de conversão de LP fraca</td><td>3–5%</td></tr>
<tr><td>LP de imóvel bem feita</td><td>10–20%</td></tr>
</table>
<p>Com R$ 3.000 e CPC de R$ 2, você tem 1.500 visitas. A 4% são 60 leads; a 15%, são 225 leads, <b>com a mesma verba</b>. Otimizar a página costuma render mais que otimizar o anúncio. <i>(Faixas de referência; meça as suas.)</i></p>`},
   {h:'2. Anatomia: os 8 blocos de uma LP de imóvel',f:FIGS.landing,b:`
<ol>
<li><b>Título com benefício</b>: "3 suítes a 400 m do Ibirapuera", não "Residencial Aurora".</li>
<li><b>Imagem de impacto</b> na primeira dobra, com o botão visível sem rolar.</li>
<li><b>Galeria curada</b>: 6 a 8 imagens (fachada, living, vista, suíte, lazer, planta).</li>
<li><b>Ficha técnica</b> em até 5 linhas: metragens, suítes, vagas, entrega.</li>
<li><b>Localização</b>: mapa e 3 pontos de interesse a pé, com tempo.</li>
<li><b>Prova</b>: construtora, entregas anteriores, depoimentos, prêmios.</li>
<li><b>Formulário</b> curto e honesto sobre o que acontece depois.</li>
<li><b>WhatsApp fixo</b> no celular, para quem não quer formulário.</li>
</ol>
<p class="tip">Regra da coerência: a página precisa continuar a promessa do anúncio. Se o anúncio falou de "vista para o parque", a primeira imagem da página é a vista.</p>`},
   {h:'3. Faça o teste: sua página passa?',w:'lpcheck',b:`
<p>Abra uma landing page real (sua ou de um concorrente) e marque item por item. É o mesmo checklist que um gestor de tráfego sênior usa antes de liberar verba.</p>`},
   {h:'4. Formulário: o filtro mais barato que existe',f:FIGS.form,b:`
<p>Cada campo a mais reduz o volume e aumenta a qualidade. No alto padrão, vale perder volume para ganhar qualidade:</p>
<ul>
<li><b>Nome e WhatsApp</b> (obrigatórios)</li>
<li><b>Faixa de investimento</b>: até R$ 3 mi / R$ 3–5 mi / acima de R$ 5 mi</li>
<li><b>Prazo</b>: até 3 meses / 3–12 meses / só pesquisando</li>
<li><b>Forma de pagamento</b>: à vista / financiamento / permuta</li>
<li><b>Aceite LGPD</b>, prevendo contato e uso para públicos de anúncio</li>
</ul>
<p>No formulário instantâneo da Meta, use o tipo <b>"maior intenção"</b>, que adiciona uma tela de revisão antes do envio: menos leads acidentais.</p>
<p class="tip">"Só pesquisando" não é lead ruim, é lead de nutrição. O formulário serve para mandar cada um para o fluxo certo, não para descartar.</p>`,
    d:{q:'Seu formulário gera 200 leads por mês, mas só 4% são qualificados. O que testar primeiro?',o:['Tirar campos para gerar ainda mais leads','Adicionar faixa de investimento e prazo, e trocar para o formulário de maior intenção','Mudar a cor do botão'],c:1,why:'O problema é qualidade, não volume. As perguntas de qualificação e o formulário de maior intenção reduzem os leads acidentais e permitem priorizar quem está pronto.'}},
   {h:'5. Rastreamento: sem medir, é palpite',b:`
<p>Uma página sem rastreamento não deixa o algoritmo aprender. O mínimo profissional:</p>
<ul>
<li><b>Pixel da Meta + API de Conversões</b>: registra o lead mesmo com bloqueadores e restrições do iOS.</li>
<li><b>Tag do Google e GA4</b> com o evento de conversão "generate_lead".</li>
<li><b>UTMs padronizadas</b> em todos os links: <code>utm_source=meta&amp;utm_medium=paid&amp;utm_campaign=sintese_familia_consideracao</code>.</li>
<li><b>Página de obrigado com URL própria</b>: facilita medir a conversão em qualquer ferramenta.</li>
</ul>
<p class="tip">Nome de campanha é documentação: empreendimento_persona_fase. Daqui a 3 meses, você vai agradecer.</p>`},
   {h:'6. Teste A/B: melhorar com método',f:FIGS.ab,b:`
<p>O teste A/B compara duas versões mudando <b>uma variável por vez</b>. Ordem de impacto típica para testar:</p>
<ol><li>Oferta (book vs. visita privativa)</li><li>Título</li><li>Imagem principal</li><li>Número de campos</li><li>Texto do botão</li></ol>
<p>Escreva a hipótese antes: "título com a distância do parque converte mais que título com o nome do prédio, porque a família valoriza lazer". Espere volume suficiente (algumas dezenas de conversões por versão) antes de decidir.</p>`,
    d:{q:'A versão B teve 3 leads e a A teve 1, depois de 2 dias. O que fazer?',o:['Declarar B vencedora e pausar A','Continuar o teste até ter volume suficiente','Criar a versão C imediatamente'],c:1,why:'Com tão poucas conversões, a diferença pode ser puro acaso. Decisões com amostra pequena custam caro.'}}
  ],
  quiz:[
   {q:'Com 1.500 visitas, quantos leads a mais uma LP de 15% gera em relação a uma de 4%?',o:['105','165','225'],c:1},
   {q:'A primeira imagem da página deve…',o:['Ser sempre a fachada','Continuar a promessa do anúncio','Ser o logo da construtora'],c:1},
   {q:'Para que serve o formulário de maior intenção da Meta?',o:['Gerar mais leads','Adicionar uma tela de revisão que reduz os leads acidentais','Pular o aceite LGPD'],c:1},
   {q:'O que a API de Conversões resolve?',o:['Cria anúncios sozinha','Registra conversões mesmo com bloqueadores e restrições do iOS','Substitui o CRM'],c:1},
   {q:'Qual variável costuma ter mais impacto num teste A/B?',o:['Cor do botão','A oferta','A fonte do texto'],c:1},
   {q:'Um lead que marca "só pesquisando" deve…',o:['Ser descartado','Entrar no fluxo de nutrição','Ir direto para o corretor'],c:1}
  ]},

crm: {
  t:'CRM, qualificação e follow-up', min:50,
  caps:[
   {h:'1. Onde as campanhas boas morrem',b:`
<p>A maior parte das vendas perdidas no digital não se perde no anúncio. Ela se perde entre o lead chegar e alguém falar com ele. Estudos de mercado mostram de forma consistente que a chance de contato cai muito depois dos primeiros minutos.</p>
<table>
<tr><td>Resposta em até 5 minutos</td><td>contato e qualificação muito mais prováveis</td></tr>
<tr><td>Resposta depois de 1 hora</td><td>o lead já falou com outra imobiliária</td></tr>
<tr><td>Resposta no dia seguinte</td><td>"não lembro de ter pedido nada"</td></tr>
</table>
<p class="tip">Para o gestor de tráfego, o CRM não é "coisa do comercial". É a única forma de saber quais campanhas geram visita e venda, e não só lead.</p>`},
   {h:'2. Temperatura e lead scoring',f:FIGS.temp,w:'score',b:`
<p>Nem todo lead merece o corretor hoje. A temperatura organiza a prioridade e o lead scoring transforma a temperatura em número, para ninguém decidir no achismo. Teste a régua da W3W no simulador:</p>`,
    d:{q:'Lead com faixa compatível, prazo de 2 meses e que pediu visita, mas respondeu só depois de 3 dias. Qual a prioridade?',o:['Frio: demorou para responder','Quente: passa para o corretor hoje','Descartar'],c:1,why:'Faixa compatível (+30), prazo curto (+25) e pedido de visita (+30) somam 85 pontos. A demora pesa menos que os sinais de intenção.'}},
   {h:'3. O pipeline e os motivos de perda',f:FIGS.pipeline,b:`
<p>Todo lead está em exatamente uma etapa. Sem isso, não existe previsão de vendas:</p>
<p><b>Novo → Contato feito → Qualificado → Visita agendada → Visita feita → Proposta → Venda / Perdido</b></p>
<h4>Motivos de perda (padronize a lista)</h4>
<ul><li>Fora da faixa de preço</li><li>Localização</li><li>Comprou com outro</li><li>Desistiu / adiou</li><li>Nunca respondeu</li><li>Lead inválido</li></ul>
<p>Depois de 60 dias, os motivos dizem onde ajustar: "fora da faixa" demais pede mudança de mensagem ou de formulário; "nunca respondeu" demais pede mais velocidade; "localização" pede ajustar a geografia da campanha.</p>`},
   {h:'4. Primeiro contato: o roteiro de 5 minutos',b:`
<p>O primeiro contato decide se o lead vira conversa ou silêncio. Estrutura que funciona no WhatsApp:</p>
<ol>
<li><b>Contexto</b>: "Oi, Helena! Aqui é a Adriana, da W3W. Você pediu a planta do Síntese Moema agora há pouco."</li>
<li><b>Entrega imediata</b>: mande o que foi pedido logo de cara, sem pedir nada antes.</li>
<li><b>Uma pergunta aberta</b>: "O que fez vocês começarem a procurar agora?"</li>
<li><b>Qualificação conversada</b>: prazo, faixa e quem decide, ao longo da conversa e não como interrogatório.</li>
<li><b>Próximo passo com data</b>: "Tenho horários no sábado de manhã para uma visita privativa. 10h ou 11h funciona?"</li>
</ol>
<p class="tip">Ofereça duas opções de horário em vez de "quando você pode?". Fica mais fácil dizer sim.</p>`,
    d:{q:'Qual a melhor primeira mensagem para um lead que pediu o book?',o:['"Olá! Qual sua renda mensal?"','"Oi, Helena! Aqui é a Adriana, da W3W. Segue o book do Síntese que você pediu. O que fez vocês começarem a procurar agora?"','"Bom dia, podemos agendar uma visita?"'],c:1,why:'Contexto, entrega imediata e uma pergunta aberta geram conversa. Pedir renda logo de cara afasta, e pedir visita sem entregar o que foi pedido parece pressão.'}},
   {h:'5. Nutrição: 5 toques em 14 dias',f:FIGS.followup,b:`
<p>A maioria dos leads de alto padrão não compra no primeiro mês. A sequência mantém a W3W presente sem ser chata:</p>
<table>
<tr><td>Dia 0</td><td>Boas-vindas + material pedido</td></tr>
<tr><td>Dia 2</td><td>Conteúdo do bairro ligado à persona (escolas para a família, valorização para o investidor)</td></tr>
<tr><td>Dia 5</td><td>2 ou 3 imóveis semelhantes da curadoria</td></tr>
<tr><td>Dia 9</td><td>Depoimento de cliente parecido com ele</td></tr>
<tr><td>Dia 14</td><td>Convite para visita privativa com data</td></tr>
</table>
<p>Quem não responder entra numa nutrição mensal leve: novidades do mercado e oportunidades da curadoria.</p>`},
   {h:'6. Fechando o ciclo com o algoritmo',b:`
<p>Aqui o CRM vira arma de tráfego. Quando você devolve para a Meta e para o Google a informação de <b>quais leads viraram visita e venda</b>, o algoritmo passa a procurar mais gente parecida com eles, e não só gente que preenche formulário.</p>
<ul>
<li><b>Meta</b>: conversões offline / API de Conversões para CRM, marcando o evento "Visita" ou "Lead qualificado".</li>
<li><b>Google</b>: importação de conversões offline com o GCLID guardado no lead.</li>
<li><b>Público semelhante</b>: lista de quem visitou e comprou, atualizada todo mês.</li>
</ul>
<p class="tip">Contas que otimizam para "lead qualificado" em vez de "lead" costumam ver o CPL subir e o custo por visita cair. É exatamente o que você quer.</p>`}
  ],
  quiz:[
   {q:'Tempo ideal de primeira resposta a um lead:',o:['Até 5 minutos','Até 24 horas','Até 3 dias'],c:0},
   {q:'Muitos leads perdidos por "fora da faixa de preço" indicam que você deve…',o:['Ligar mais vezes','Ajustar a mensagem do anúncio e as perguntas do formulário','Baixar o preço do imóvel'],c:1},
   {q:'Qual é a melhor forma de propor uma visita?',o:['"Quando você pode?"','"Sábado às 10h ou às 11h funciona?"','"Me avisa quando quiser"'],c:1},
   {q:'Por que devolver conversões offline para a Meta?',o:['Para o algoritmo buscar pessoas parecidas com quem visita e compra','Porque é obrigatório pela LGPD','Para baixar o CPM'],c:0},
   {q:'Um lead que não respondeu à sequência de 14 dias deve…',o:['Ser apagado do CRM','Entrar na nutrição mensal leve','Receber ligações diárias'],c:1},
   {q:'No lead scoring da W3W, quantos pontos fazem o lead ir para o corretor no mesmo dia?',o:['Acima de 30','Acima de 60','Acima de 90'],c:1}
  ]}
};
