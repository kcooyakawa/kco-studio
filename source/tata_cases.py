# -*- coding: utf-8 -*-
# Cases trazidos do Cargo do Otavio Bannwart (época GEO Eventos / Sportsworld). Sem ficha técnica.
J, D, S, R, E = "O projeto", "O desafio", "A solução", "Resultados", "Entregas"
LBL_EN = {J: "The project", D: "The challenge", S: "The solution", R: "Results", E: "Deliverables"}

# heading de seção (como veio do Cargo, em PT) -> EN
H = {
 "Galeria": "Gallery", "Vídeos": "Videos", "Vídeo": "Video", "Peças": "Pieces", "Cenografia": "Set design", "Campanha": "Campaign",
 "Paper toy": "Paper toy", "Apresentação": "Presentation", "Impresso": "Print", "Site": "Website", "Canal no YouTube": "YouTube channel",
 "Roda gigante": "Ferris wheel", "Espaço de sombra": "Shade lounge", "Rock and Recycle": "Rock and Recycle", "Brindes": "Giveaways",
 "Heineken Moment": "Heineken Moment", "Frames do filme": "Film frames", "Anúncio de jornal": "Newspaper ad",
 "Grid de programação": "Schedule reveal", "Concurso de pôster oficial": "Official poster contest", "Métricas": "Metrics",
 "Anúncio interativo": "Interactive ad", "Lineup na linha": "Lineup on the line", "Mídia e campanha": "Media and campaign",
 "Campanha 2012 — Dave Grohl, cinema e digital": "2012 campaign — Dave Grohl, cinema and digital",
 "Campanha 2013 — Ocupe São Paulo com música": "2013 campaign — Occupy São Paulo with music",
 "Billabong Rio Pro 2011 e 2012": "Billabong Rio Pro 2011 and 2012",
}

C = {}
def case(slug, cid, title, title_en, cat, client, year, desc, desc_en, st, st_en, rows, secs, thumb=None):
    C[slug] = dict(id=cid, title=title, title_en=title_en, cat=cat, client=client, year=year, desc=(desc, desc_en), st=(st, st_en), rows=rows, secs=secs, thumb=thumb)

# secs: list of (heading, [items]) ; items: ('i', path) | ('y', youtube_id) | ('p', pt, en)
case("Galinha-Pintadinha-o-Musical", "galinha", "Galinha Pintadinha — O Musical", "Galinha Pintadinha — The Musical", "Teatro", "Galinha Pintadinha", "2012",
 "Campanha do musical infantil da turminha mais famosa da internet brasileira.", "Campaign for the children's musical of the best-known characters on the Brazilian internet.",
 "Da internet para o palco: um musical que junta crianças, pais e avós.", "From the internet to the stage: a musical for children, parents and grandparents.",
 [(J, "Com mais de 250 mil DVDs vendidos, a Galinha Pintadinha virou espetáculo infantil: clássicos da música popular infantil e personagens que moram no imaginário de todo brasileiro.",
      "With over 250,000 DVDs sold, Galinha Pintadinha became a children's show: classic Brazilian children's songs and characters every Brazilian grew up with."),
  (S, "Uma campanha com duas mensagens: diversão garantida para as crianças e uma opção segura de lazer e cultura para pais e avós. O convite: “Quem é que vem cantar com a gente?”",
      "A campaign with two messages: guaranteed fun for kids and a safe leisure and culture option for parents and grandparents. The invitation: “Who's coming to sing with us?”"),
  (E, "Cartaz · Peças de divulgação · Paper toy", "Poster · Promotional pieces · Paper toy")],
 [("Peças", ["4288444/Screen_shot_2012-05-14_at_5.39.13_PM.png.scaled1000_o.png", "4288444/Screen_shot_2012-05-14_at_5.41.52_PM.png.scaled1000_o.png"]),
  ("Paper toy", ["4288444/pintinho.jpg.scaled1000.jpg", "4288444/galinha.jpg.scaled1000.jpg"])])

case("Camarote-Quem-Carnaval-de-Salvador-2013", "camarote-quem", "Camarote Quem — Carnaval de Salvador", "Camarote Quem — Salvador Carnival", "Eventos", "Revista Quem", "2013",
 "Identidade e comunicação do camarote da revista Quem no Carnaval de Salvador.", "Identity and communication for Quem magazine's VIP box at the Salvador Carnival.",
 "O camarote de uma revista de celebridades no maior carnaval de rua do mundo.", "A celebrity magazine's VIP box at the world's largest street carnival.",
 [(J, "Marketing de evento, conteúdo de marca e patrocínio para o camarote da revista Quem no circuito do Carnaval de Salvador 2013.",
      "Event marketing, branded content and sponsorship for Quem magazine's VIP box on the 2013 Salvador Carnival circuit."),
  (E, "Identidade visual · Key visual · Peças do camarote", "Visual identity · Key visual · VIP box pieces")],
 [], thumb="4641086/prt_220x190_1356024005.jpg")

case("Campanha-XXXPerience-2012", "xxxperience", "XXXPerience — Edição 16 anos", "XXXPerience — 16th anniversary edition", "Campanhas", "XXXPerience", "2012",
 "Campanha integrada da edição especial de 16 anos do festival, com David Guetta.", "Integrated campaign for the festival's 16th anniversary edition, headlined by David Guetta.",
 "Um festival jovem para gente jovem: estar em todo lugar onde esse público está.", "A young festival for young people: be everywhere that audience is.",
 [(D, "Onde encontrar um público que está em todo lugar? Indo a todo lugar.", "Where do you find an audience that is everywhere? By going everywhere."),
  (S, "Uma campanha presente na TV, nas mídias sociais, nas revistas, nos jornais e até nos bares, com o line-up liderado por David Guetta na Arena Maeda, em Itu.",
      "A campaign on TV, social media, magazines, newspapers and even bars, with the line-up headlined by David Guetta at Arena Maeda, Itu."),
  (E, "Cartaz · Flyer · Anúncios · Digital", "Poster · Flyer · Ads · Digital")],
 [("Peças", ["4830601/Screen shot 2013-01-23 at 1.41.50 PM_o.png", "4830601/flyerxxx16_45x15_line02_frente_o.jpg"])])

case("Preliminary-Draw-for-FIFA-World-Cup-Brazil", "fifa-sorteio", "Sorteio Preliminar — Copa do Mundo da FIFA Brasil 2014™", "Preliminary Draw — 2014 FIFA World Cup Brazil™", "Eventos", "FIFA", "2011",
 "O primeiro evento oficial da Copa do Mundo de 2014 no Brasil, no Rio de Janeiro.", "The first official 2014 FIFA World Cup event in Brazil, in Rio de Janeiro.",
 "A primeira vez que o Brasil se apresentou ao mundo como país-sede da Copa.", "The first time Brazil presented itself to the world as World Cup host.",
 [(J, "Um evento global, transmitido para o mundo todo, e a primeira oportunidade do Brasil de atuar como anfitrião da Copa do Mundo da FIFA 2014.",
      "A global event broadcast worldwide, and Brazil's first chance to act as host of the 2014 FIFA World Cup."),
  (S, "Uma linguagem visual que une o futebol e o Brasil: “o futebol une o mundo no Brasil”, aplicada da comunicação ao palco.",
      "A visual language bringing football and Brazil together — “football unites the world in Brazil” — applied from communication to stage."),
  (E, "Cartaz oficial · Cenografia · Sinalização · Peças do evento", "Official poster · Set design · Signage · Event pieces")],
 [("Galeria", ["4335591/Screen shot 2012-10-28 at 12.33.14 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.33.31 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.29.33 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.30.03 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.22 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.36 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.32.07 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.54 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.32.23 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.32.33 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.32.43 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.59.20 PM_o.png"])],
 thumb="4335591/prt_220x340_1351434899.png")

case("Tenis-Espetacular-2010", "tenis-espetacular", "Tênis Espetacular — Guga vs Agassi", "Tênis Espetacular — Guga vs Agassi", "Eventos", "Gillette · Duracell", "2010",
 "O maior duelo de tênis da história do Brasil num espetáculo de música e interatividade, no Maracanãzinho.", "The biggest tennis match in Brazil's history as a show of music and interactivity, at Maracanãzinho.",
 "Esporte, entretenimento, tecnologia e responsabilidade social na mesma quadra.", "Sport, entertainment, technology and social responsibility on the same court.",
 [(J, "Guga e Agassi de volta à quadra, relembrando o duelo em que o brasileiro se tornou número 1 do mundo. Nos palcos, Luciano Huck e Frejat comandando a festa; nas UPPs, clínicas de tênis e outras atrações.",
      "Guga and Agassi back on court, recalling the match in which the Brazilian became world number one. On stage, Luciano Huck and Frejat hosting the party; in the UPP communities, tennis clinics and more."),
  (R, "10 mil pessoas, lotação máxima · Líder de audiência no horário · 2 trending topics por 6 horas · 2.500 crianças atendidas · R$ 40 mil em doações ao Criança Esperança · Mais de R$ 15 milhões em exposição de mídia",
      "10,000 people, sold out · Top-rated in its time slot · 2 trending topics for 6 hours · 2,500 children served · R$ 40,000 donated to Criança Esperança · Over R$ 15 million in media exposure"),
  (E, "Campanha integrada · Cartaz · Digital · Interatividade no evento", "Integrated campaign · Poster · Digital · On-site interactivity")],
 [("Vídeo", [("y", "DL7Dpvw2WHI")])], thumb="4382149/prt_220x317_1352146659.jpg")

case("Ativacao-Calvin-Klein-Jeans-Lollapalooza-Brasil-2012", "ck-lolla", "Calvin Klein Jeans — Lollapalooza Brasil", "Calvin Klein Jeans — Lollapalooza Brasil", "Eventos", "Calvin Klein Jeans", "2012",
 "Ativação do jeans oficial do Lollapalooza Brasil: espaço de sombra, cabine de fotos e desfile.", "Activation for Lollapalooza Brasil's official jeans: shade lounge, photo booth and catwalk.",
 "Moda e música andam juntas: o jeans oficial do Lollapalooza Brasil.", "Fashion and music go together: Lollapalooza Brasil's official jeans.",
 [(S, "A Calvin Klein Jeans levou para o festival o conceito da sua última campanha: um espaço de sombra com pufes coloridos e carregadores de celular, uma cabine de fotos e promotoras desfilando a nova coleção pela Cabana.",
      "Calvin Klein Jeans brought its latest campaign concept to the festival: a shade lounge with colourful poufs and phone chargers, a photo booth and models wearing the new collection around the Cabana."),
  (R, "Mais de 1.000 fotos tiradas na cabine e postadas direto no Facebook, com muita visibilidade e mídia espontânea para a marca.",
      "Over 1,000 photos taken in the booth and posted straight to Facebook, earning the brand strong visibility and earned media."),
  (E, "Espaço de marca · Cabine de fotos · Backdrop · Ação com promotoras", "Brand space · Photo booth · Backdrop · Brand ambassador action")],
 [("Galeria", ["4287777/ck1_1000.png", "4287777/ck3_1000.png", "4287777/ck2_1000.png"])], thumb="4287777/prt_275x144_1468637217.jpg")

case("F1-Rocks-2010", "f1-rocks", "F1 Rocks — São Paulo", "F1 Rocks — São Paulo", "Eventos", "Formula 1 · LG", "2010",
 "Evento musical criado para acompanhar as etapas do circuito mundial de F1, com Eminem como headliner.", "A music event created to accompany the Formula 1 world championship, headlined by Eminem.",
 "Os melhores do automobilismo e os melhores da música no mesmo palco.", "The best of motorsport and the best of music on one stage.",
 [(J, "A-list, glamour e adrenalina: áreas VIP com celebridades, pilotos e equipes, festas de backstage, tapete vermelho, área de autógrafos e coletiva de imprensa.",
      "A-list, glamour and adrenaline: VIP areas with celebrities, drivers and teams, backstage parties, red carpet, autograph area and press conference."),
  (S, "Uma plataforma de comunicação com visibilidade de arena, espaços proprietários e geração de conteúdo, apoiada por um plano integrado de R$ 2,5 milhões em mídia: TV, rádio, jornal, revista, RP, influenciadores, digital e redes sociais.",
      "A communication platform with arena visibility, proprietary spaces and content, backed by an integrated R$ 2.5 million media plan: TV, radio, print, PR, influencers, digital and social."),
  (R, "35 mil pessoas, sold out · R$ 17,4 milhões em mídia espontânea · Transmissão pelo Multishow e para 170 emissoras, com audiência acima de 26 milhões de telespectadores",
      "35,000 people, sold out · R$ 17.4 million in earned media · Broadcast on Multishow and to 170 stations, with an audience above 26 million viewers"),
  (E, "Campanha integrada · Key visual · Cenografia · Digital", "Integrated campaign · Key visual · Set design · Digital")],
 [("Vídeo", [("y", "cUAtnICfzlE")]),
  ("Campanha", ["4330737/s2_1067.jpg", "4330737/s3_1067.jpg", "4330737/s4_1067.jpg", "4330737/s5_1067.jpg", "4330737/s8_1067.jpg", "4330737/s9_1067.jpg", "4330737/s10_1067.jpg",
                "4330737/s11_1067.jpg", "4330737/s12_1067.jpg", "4330737/s13_1067.jpg", "4330737/s14_1067.jpg", "4330737/s15_1067.jpg", "4330737/s16_1067.jpg", "4330737/s17_1067.jpg"]),
  ("Cenografia", ["4330737/c9_1000.jpg", "4330737/c8_1000.jpg", "4330737/c7_1000.jpg", "4330737/c6_1000.jpg", "4330737/c5_1000.jpg", "4330737/c4_1000.jpg", "4330737/c3_1000.jpg", "4330737/c2_1000.jpg", "4330737/c1_1000.jpg"])],
 thumb="4330737/prt_220x268_1351371796.jpg")

case("Anuncios-de-Lancamento-Lineup-2013", "lolla-anuncios-2013", "Lollapalooza Brasil — Anúncios do line-up 2013", "Lollapalooza Brasil — 2013 line-up ads", "Campanhas", "Lollapalooza Brasil", "2013",
 "Anúncios de lançamento do line-up da segunda edição do festival, com ilustração e o chamado “Ocupe SP com música”.", "Launch ads for the line-up of the festival's second edition, with illustration and the call “Occupy SP with music”.",
 "O line-up como um espetáculo: a cortina se abre para as bandas.", "The line-up as a show: the curtain opens on the bands.",
 [(J, "Anúncios de jornal e revista para revelar as atrações do Lollapalooza Brasil 2013 e abrir as vendas de ingressos.",
      "Newspaper and magazine ads revealing the Lollapalooza Brasil 2013 acts and opening ticket sales."),
  (E, "Anúncios de jornal e revista · Cartaz do line-up", "Newspaper and magazine ads · Line-up poster")],
 [("Peças", ["4289473/An_Lolla_297x52a2.jpg.scaled696.jpg"])], thumb="4289473/prt_220x386_1350702699.jpg")

case("Ativacao-Heineken-Lollapalooza-Brasil-2012", "heineken-lolla-2012", "Heineken — Lollapalooza Brasil 2012", "Heineken — Lollapalooza Brasil 2012", "Eventos", "Heineken", "2012",
 "Ativações da cerveja oficial na primeira edição do Lollapalooza Brasil.", "Activations for the official beer at the first Lollapalooza Brasil.",
 "Sinal verde para a música no Lollapalooza Brasil.", "Green light for music at Lollapalooza Brasil.",
 [(J, "135 mil pessoas, mais de 50 atrações e a Heineken presente em todo o Jockey Club: Beer Station, Backpackers, Heineken in the Sky, Heineken Moments, sticks de neon, chopeiras e visibilidade de arena.",
      "135,000 people, over 50 acts and Heineken across the whole Jockey Club: Beer Station, Backpackers, Heineken in the Sky, Heineken Moments, neon sticks, draft stations and arena visibility."),
  (R, "Para 60% do público que também foi ao Rock in Rio ou ao SWU, a Heineken teve mais e melhores atividades no Lollapalooza. 65% associaram a marca ao consumo responsável. Maior recall de marca do festival.",
      "For 60% of attendees who also went to Rock in Rio or SWU, Heineken had more and better activities at Lollapalooza. 65% linked the brand to responsible drinking. Highest brand recall of the festival."),
  (E, "Ativações de marca · Espaços proprietários · Brindes · Visibilidade de arena", "Brand activations · Proprietary spaces · Giveaways · Arena visibility")],
 [("Galeria", ["4286085/h1_1000.png", "4286085/h2_1000.png", "4286085/h3_1000.png"])], thumb="4286085/prt_275x155_1468635303_2x.jpg")

case("Ativacao-Coca-Cola-Zero-Lollapalooza-Brasil-2012", "cocazero-lolla", "Coca-Cola Zero — Lollapalooza Brasil", "Coca-Cola Zero — Lollapalooza Brasil", "Eventos", "Coca-Cola", "2012",
 "O Simulador de Mosh: uma foto de você dando um mosh no Lolla, pronta para compartilhar.", "The Mosh Simulator: a photo of you crowd-surfing at Lolla, ready to share.",
 "Qual é a possibilidade de você dar um mosh no Lolla Brasil?", "What are the odds of you crowd-surfing at Lolla Brasil?",
 [(S, "O Simulador de Mosh: os convidados tiravam uma foto simulando um mosh sobre a plateia e compartilhavam com os amigos pelo Facebook.",
      "The Mosh Simulator: guests took a photo crowd-surfing over the audience and shared it with friends on Facebook."),
  (R, "A ação mais comentada do festival.", "The most talked-about activation of the festival."),
  (E, "Ativação · Cenário fotográfico · Compartilhamento social", "Activation · Photo set · Social sharing")],
 [("Vídeo", [("y", "g0GC5T98tnE")]),
  ("Galeria", ["4286045/Screen_shot_2012-08-10_at_10.32.08_AM.png.scaled1000_o.png", "4286045/Screen_shot_2012-08-10_at_10.32.57_AM.png.scaled1000_o.png", "4286045/Screen_shot_2012-08-10_at_10.33.19_AM.png.scaled1000_o.png"])],
 thumb="4286045/prt_220x220_1409757929_2x.jpg")

case("Yahoo-Big-Idea-Chair", "yahoo-bic", "Yahoo! Big Idea Chair", "Yahoo! Big Idea Chair", "Eventos", "Yahoo! Brasil", "2007",
 "O prêmio global do Yahoo! adaptado ao mercado brasileiro, com uma única categoria: a grande ideia.", "Yahoo!'s global award adapted to the Brazilian market, with a single category: the big idea.",
 "Não as pequenas boas ideias: a grande ideia.", "Not the little good ideas: the big idea.",
 [(D, "Trazer o prêmio Y! Big Idea Chair para o Brasil, adaptá-lo à realidade local e aumentar a relevância do Yahoo! no mercado publicitário, onde havia poucos eventos da categoria.",
      "Bring the Y! Big Idea Chair award to Brazil, adapt it to the local market and raise Yahoo!'s relevance among advertisers, where there were few events in the category."),
  (S, "Transformar a barreira em diferencial: um prêmio com uma única grande categoria, The Big Idea, valorizando toda a cadeia por trás de uma grande ideia.",
      "Turn the barrier into an edge: an award with one single category, The Big Idea, celebrating the whole chain behind a big idea."),
  (E, "Posicionamento · Evento de premiação · Campanha integrada · Impressos", "Positioning · Award event · Integrated campaign · Print")],
 [("Galeria", ["11739313/BIC2_877.jpg", "11739313/BIC4_877.jpg", "11739313/BIC1_1000.jpg", "11739313/bic5_1000.jpg",
               "11739313/Screen-Shot-2016-07-11-at-4.33.50-PM_1186.png", "11739313/Screen-Shot-2016-07-11-at-4.34.06-PM_1187.png", "11739313/Screen-Shot-2016-07-11-at-4.22.32-PM_1178.png"]),
  ("Impresso", ["11739313/Screen-Shot-2016-07-15-at-9.57.23-PM_933.png", "11739313/Screen-Shot-2016-07-15-at-10.04.08-PM_938.png", "11739313/Screen-Shot-2016-07-15-at-10.05.43-PM_924.png", "11739313/Screen-Shot-2016-07-15-at-10.05.10-PM_932.png"])],
 thumb="11739313/prt_275x96_1468263979_2x.png")

case("Ativacao-Heineken-Lollapalooza-Brasil-2013", "heineken-lolla-2013", "Heineken — Lollapalooza Brasil 2013", "Heineken — Lollapalooza Brasil 2013", "Eventos", "Heineken", "2013",
 "Pulseiras de LED, roda gigante e o Jockey aceso em verde durante os três dias de festival.", "LED wristbands, a Ferris wheel and the Jockey Club lit green across the three festival days.",
 "O verde trazia refrescância de dia e acendia o Jockey à noite.", "Green refreshed the day and lit up the Jockey Club at night.",
 [(J, "Em 2013, a Heineken se destacou ainda mais: ativações que uniam a experiência do Lollapalooza ao prazer de uma Heineken, presentes do primeiro ao último show.",
      "In 2013 Heineken stood out even more: activations joining the Lollapalooza experience with the pleasure of a Heineken, from the first show to the last."),
  (S, "Heineken Moment com pulseiras de LED da PixMob acendendo ao som da trilha da marca · Roda gigante com lounge, chopp perfeito, fotocabine e wi-fi · Espaço de sombra com 60 pufes · Rock and Recycle, copos trocados por brindes",
      "Heineken Moment with PixMob LED wristbands lighting up to the brand's soundtrack · Ferris wheel with lounge, perfect draft, photo booth and wi-fi · Shade lounge with 60 poufs · Rock and Recycle, cups swapped for giveaways"),
  (E, "Ativações · Espaços de marca · Brindes · Vídeos", "Activations · Brand spaces · Giveaways · Videos")],
 [("Heineken Moment", [("y", "b8uuWsYiN8I"), "8496984/Crowd_3-1130x430_1130.jpg", ("y", "dR-rlh3hFxY"), ("y", "Uc8Vp0QNmOQ")]),
  ("Roda gigante", ["8496984/h4_1600_c.jpg", "8496984/h6_1600_c.jpg", "8496984/h5_1600_c.jpg", "8496984/h7_1600_c.jpg", "8496984/h8_1600_c.jpg"]),
  ("Espaço de sombra", ["8496984/h9_1600_c.jpg", "8496984/sombra_1600_c.jpg"]),
  ("Rock and Recycle", ["8496984/hs1_1600_c.jpg", "8496984/hs2_1600_c.jpg", "8496984/hs3_1600_c.jpg"]),
  ("Brindes", ["8496984/hb1_1600_c.jpg"])], thumb="8496984/prt_275x252_1468874626.png")

case("Lineup-na-linha-Lollapalooza-Brasil-2012", "lolla-lineup-na-linha", "Lollapalooza Brasil — Lineup na linha", "Lollapalooza Brasil — Lineup on the line", "Campanhas", "Lollapalooza Brasil", "2012",
 "Anúncio interativo na linha amarela do metrô de São Paulo, a 600 metros do festival.", "An interactive ad on São Paulo's yellow metro line, 600 metres from the festival.",
 "Lineup na linha: o festival começa no metrô.", "Lineup on the line: the festival starts on the metro.",
 [(D, "Promover o festival e incentivar o público a ir de metrô até o Jockey Club.", "Promote the festival and encourage people to take the metro to the Jockey Club."),
  (S, "A linha amarela foi a primeira linha “mobile friendly” do país, e a estação Butantã fica a 600 metros do Jockey. Ali, um anúncio com QR code levava ao aplicativo oficial para montar e compartilhar o seu line-up.",
      "The yellow line was the country's first “mobile friendly” line, and Butantã station is 600 metres from the Jockey Club. There, a QR-code ad led to the official app to build and share your own line-up."),
  (E, "Mídia em metrô · QR code · Aplicativo", "Metro media · QR code · App")],
 [("Galeria", ["4286006/_.jpg.scaled1000.jpg", "4286006/iveco-iphone.jpg.scaled696.jpg", "4286006/PORTA_SEGURANCA_METRO.jpg.scaled1000.jpg", "4286006/estacao-butanta.jpg.scaled1000_o.jpg"])],
 thumb="4286006/prt_220x326_1350655711.jpg")

case("Anuncio-Interativo-Lollapalooza-Brasil-2012", "lolla-anuncio-interativo", "Lollapalooza Brasil — Anúncio interativo", "Lollapalooza Brasil — Interactive ad", "Campanhas", "Lollapalooza Brasil", "2012",
 "Um anúncio impresso que ganha vida no celular, na revista Rolling Stone.", "A print ad that comes alive on your phone, in Rolling Stone magazine.",
 "Interativo como um aplicativo.", "As interactive as an app.",
 [(D, "Divulgar o festival e o lançamento do aplicativo oficial do Lolla.", "Promote the festival and the launch of Lolla's official app."),
  (S, "Um anúncio na Rolling Stone em que o leitor via, na prática, um pouco de como seria o aplicativo do festival.", "A Rolling Stone ad in which readers could try out what the festival app would be like."),
  (R, "Mais de 50 mil interações.", "Over 50,000 interactions."),
  (E, "Anúncio de revista · Realidade aumentada", "Magazine ad · Augmented reality")],
 [("Peças", ["4285967/ad_lolla_interativo.jpg.scaled1000_o.jpg"])], thumb="4285967/prt_220x156_1350655073.jpg")

case("Grid-Reveal-Lollapalooza-Brasil-2013", "lolla-grid-reveal", "Lollapalooza Brasil — Grid reveal", "Lollapalooza Brasil — Grid reveal", "Campanhas", "Lollapalooza Brasil", "2013",
 "Cada like no Facebook erguia um pouco a cortina que escondia a programação do festival.", "Every Facebook like raised the curtain hiding the festival schedule a little more.",
 "Quem vai revelar os shows de cada dia? Você e seus amigos.", "Who will reveal each day's shows? You and your friends.",
 [(J, "O lançamento do grid de programação, que revela quais bandas tocam em cada dia, feito junto com os fãs no Facebook: cada like ajudava a erguer a cortina.",
      "The launch of the schedule grid, revealing which bands play each day, done together with fans on Facebook: every like helped raise the curtain."),
  (E, "Ação em redes sociais · Peças digitais", "Social media action · Digital pieces")],
 [("Peças", ["4431328/Cortina_o.jpg"])], thumb="4431328/prt_220x221_1352839565.jpg")

case("Filme-de-Lancamento-Lineup-Lollapalooza-Brasil-2013", "lolla-filme-2013", "Lollapalooza Brasil — Filme do line-up 2013", "Lollapalooza Brasil — 2013 line-up film", "Campanhas", "Lollapalooza Brasil", "2013",
 "Filme animado de lançamento do line-up, cruzando os prédios de São Paulo.", "Animated line-up launch film, crossing São Paulo's buildings.",
 "Animação sobre a cidade: o line-up atravessa São Paulo.", "Animation over the city: the line-up crosses São Paulo.",
 [(J, "Filme de lançamento do line-up do Lollapalooza Brasil 2013, com animação desenhada sobre imagens reais de São Paulo, produzido pela Paranoid.",
      "Launch film for the Lollapalooza Brasil 2013 line-up, with animation drawn over real footage of São Paulo, produced by Paranoid."),
  (E, "Filme de lançamento · Frames para digital", "Launch film · Frames for digital")],
 [("Vídeo", [("y", "86JdkOh4A5o")]),
  ("Frames do filme", ["4282906/bike.gif", "4282906/01_670.jpg", "4282906/02_670.jpg", "4282906/03_670.jpg", "4282906/04_670.jpg", "4282906/05_670.jpg", "4282906/06_670.jpg",
                       "4282906/07_670.jpg", "4282906/08_670.jpg", "4282906/09_670.jpg", "4282906/10_670.jpg", "4282906/pordosol_lolla_670.jpg"])],
 thumb="4282906/prt_220x339_1356025461.jpg")

case("Corrida-Cartoon-Network", "corrida-cartoon", "Corrida Cartoon Network", "Cartoon Network Run", "Eventos", "Cartoon Network", "2015",
 "Corrida em família em que as crianças correm em equipe com um adulto, levada pela primeira vez ao Rio de Janeiro.", "A family run where kids race in teams with an adult, taken to Rio de Janeiro for the first time.",
 "Corra do seu jeito: ganha quem se diverte mais.", "Run your way: whoever has the most fun wins.",
 [(D, "Evoluir um projeto de sucesso de público e de vendas, com frequência 20% maior que em 2014 em São Paulo, e levar o conceito pela primeira vez ao Rio de Janeiro.",
      "Evolve a project that already succeeded with audiences and sponsors, with 20% more attendance than 2014 in São Paulo, and take it to Rio de Janeiro for the first time."),
  (S, "Um estudo das motivações do público do canal, de 4 a 14 anos, a geração Z, nascida com a internet e os videogames. Daí veio a gamificação: uma corrida interativa e desafiadora, mais divertida e irreverente, do jeito que a criançada gosta.",
      "A study of the channel's audience aged 4 to 14, Generation Z, born with the internet and video games. That led to gamification: an interactive, challenging run, more fun and irreverent, the way kids like it."),
  (E, "Conceito · Identidade do evento · Ativações · Peças de comunicação", "Concept · Event identity · Activations · Communication pieces")],
 [("Apresentação", ["11726640/Screen-Shot-2016-07-07-at-3.55.22-PM_992.png", "11726640/Screen-Shot-2016-07-07-at-4.06.05-PM_947.png", "11726640/Screen-Shot-2016-07-07-at-4.05.19-PM_948.png",
                    "11726640/Screen-Shot-2016-07-07-at-4.05.11-PM_948.png", "11726640/Screen-Shot-2016-07-07-at-4.04.45-PM_949.png", "11726640/Screen-Shot-2016-07-07-at-4.04.04-PM_948.png",
                    "11726640/Screen-Shot-2016-07-07-at-4.03.45-PM_948.png", "11726640/Screen-Shot-2016-07-07-at-4.03.09-PM_946.png"]),
  ("Vídeo", [("y", "VsCFZM3oeEA")])], thumb="11726640/prt_275x155_1467916574_2x.jpg")

# ---- seções extras para cases que já existem (lolla, billabong)
EXTRA = {
 "lolla": [
  ("Campanha 2012 — Dave Grohl, cinema e digital", [("p", "Com R$ 10,2 milhões em mídia, a primeira edição teve um plano integrado que levou o festival ao cinema, aeroportos, metrô, rádio, bares e até ao iTunes. O garoto-propaganda foi Dave Grohl: a entrevista em que ele anuncia o line-up passou de 1 milhão de views. Nas redes, de 0 a 600 mil seguidores em dois anos.",
     "With R$ 10.2 million in media, the first edition had an integrated plan that took the festival to cinemas, airports, the metro, radio, bars and even iTunes. Its spokesman was Dave Grohl: the interview in which he announced the line-up passed 1 million views. On social media, from 0 to 600,000 followers in two years."),
     ("y", "XeMLJpoLBgQ"), ("y", "8zZbTQC1YzM"), ("y", "6eoTXGcXBv4")]),
  ("Campanha 2013 — Ocupe São Paulo com música", [("p", "Pesquisa da edição anterior mostrou que 70% do público comprava ingresso pelos headliners. O desafio de 2013 foi construir uma marca de festival ligada à descoberta: o conceito “Ocupe São Paulo com música” levou shows gratuitos à Galeria do Rock e às periferias, side shows pela cidade e um concurso de pôster oficial com a Urban Arts. 167 mil pessoas no Jockey Club.",
     "Research at the previous edition showed 70% of the audience bought tickets for the headliners. The 2013 challenge was to build a festival brand tied to discovery: the concept “Occupy São Paulo with music” brought free shows to Galeria do Rock and the outskirts, side shows across the city and an official poster contest with Urban Arts. 167,000 people at the Jockey Club."),
     "11739808/Screen-Shot-2016-07-11-at-9.54.09-PM_1103.png", "11739808/Screen-Shot-2016-07-11-at-9.54.39-PM_1121.png",
     "11739808/481645_436356623117880_198609129_n_557.jpg", "11739808/559908_436356633117879_587724297_n_557.jpg", "11739808/poster0_557.jpg", "11739808/posters_1250.jpg",
     "11739808/Screen-Shot-2016-07-11-at-9.55.00-PM_1116.png", "11739808/Screen-Shot-2016-07-11-at-9.56.09-PM_1124.png"]),
 ],
 "billabong": [
  ("Billabong Rio Pro 2011 e 2012", [("p", "A única etapa do circuito mundial na América Latina levou mais de 80 mil pessoas à praia e passou de 2 milhões de espectadores na transmissão ao vivo. Um evento sustentável, com inventário de emissões compensado com plantio de mudas nativas da Mata Atlântica.",
     "The only world tour stop in Latin America drew over 80,000 people to the beach and over 2 million viewers on the live stream. A sustainable event, with its emissions inventory offset by planting native Atlantic Forest seedlings."),
     ("y", "ViscVgqLpmc"), ("y", "QrBRtu_9w6w"),
     "4317779/Screen-Shot-2016-07-17-at-10.53.14-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.55-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.46-PM_1250.png",
     "4317779/Screen-Shot-2016-07-17-at-10.53.28-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.02-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.55.37-PM_1250.png",
     "4317779/Billabong-Rio-Pro---May-11---22--2011_1308147227705_1600_c.png", "4317779/Screen-Shot-2016-07-13-at-4.25.02-PM_1109.png", "4317779/billa_2_o.jpg",
     "4317779/01-FRONTAL_o.jpg", "4317779/JH_Bilabong RIO Pro 2012_Programacao visual_Geral_10_o.jpg"]),
 ],
}
