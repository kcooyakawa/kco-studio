# -*- coding: utf-8 -*-
# Cases da época GEO Eventos / Sportsworld (narrativa a partir do Cargo do Otavio Bannwart). Sem ficha técnica.
# secs: [((titulo_pt, titulo_en), [itens])]; item = 'caminho/img' | ('y', youtube_id) | ('p', pt, en)
J, D, S, R, E = ("O projeto", "The project"), ("O desafio", "The challenge"), ("A solução", "The solution"), ("Resultados", "Results"), ("Entregas", "Deliverables")
C = {}
def case(cid, title, title_en, cat, client, year, desc, desc_en, st, st_en, rows, secs, thumb=None):
    C[cid] = dict(id=cid, title=title, title_en=title_en, cat=cat, client=client, year=year, desc=(desc, desc_en), st=(st, st_en), rows=rows, secs=secs, thumb=thumb)
def p(pt, en): return ('p', pt, en)
def y(i): return ('y', i)

case("galinha", "Galinha Pintadinha — O Musical", "Galinha Pintadinha — The Musical", "Teatro", "Galinha Pintadinha", "2012",
 "Campanha do musical infantil da turminha mais famosa da internet brasileira.", "Campaign for the children's musical of the best-known characters on the Brazilian internet.",
 "Da internet para o palco: um musical que junta crianças, pais e avós.", "From the internet to the stage: a musical for children, parents and grandparents.",
 [(J, "Depois do sucesso na internet brasileira e de mais de 250 mil DVDs vendidos, a turminha mais famosa do Brasil chega a um musical infantil que é diversão para toda a família.",
      "After its success on the Brazilian internet and over 250,000 DVDs sold, Brazil's best-known children's characters arrive in a musical that is fun for the whole family."),
  (E, "Cartaz · Peças de divulgação · Paper toy", "Poster · Promotional pieces · Paper toy")],
 [(("Um espetáculo que une gerações", "A show that brings generations together"), [
    p("Os clássicos da música popular infantil e personagens que moram no imaginário de todos os brasileiros. Para as crianças, diversão garantida. Para pais e avós, uma opção divertida e segura de lazer e cultura.",
      "Classic Brazilian children's songs and characters every Brazilian grew up with. For kids, guaranteed fun. For parents and grandparents, an enjoyable and safe leisure and culture option."),
    "4288444/Screen_shot_2012-05-14_at_5.39.13_PM.png.scaled1000_o.png", "4288444/Screen_shot_2012-05-14_at_5.41.52_PM.png.scaled1000_o.png"]),
  (("Quem é que vem cantar com a gente?", "Who's coming to sing with us?"), [
    p("O convite da campanha: venha cantar e se divertir com os clássicos que a gente aprende brincando. Para levar a turminha para casa, um paper toy dos personagens.",
      "The campaign's invitation: come sing and have fun with the classics we learn through play. To take the characters home, a paper toy."),
    "4288444/pintinho.jpg.scaled1000.jpg", "4288444/galinha.jpg.scaled1000.jpg"])])

case("xxxperience", "XXXPerience — Edição 16 anos", "XXXPerience — 16th anniversary edition", "Campanhas", "XXXPerience", "2012",
 "Campanha integrada da edição especial de 16 anos do festival, com David Guetta.", "Integrated campaign for the festival's 16th anniversary edition, headlined by David Guetta.",
 "Um festival jovem para gente jovem: estar em todo lugar onde esse público está.", "A young festival for young people: be everywhere that audience is.",
 [(D, "Onde encontrar um público que está em todo lugar? Indo a todo lugar.", "Where do you find an audience that is everywhere? By going everywhere."),
  (S, "Uma campanha presente na TV, nas mídias sociais, nas revistas, nos jornais e até nos bares, com o line-up liderado por David Guetta na Arena Maeda, em Itu.",
      "A campaign on TV, social media, magazines, newspapers and even bars, with the line-up headlined by David Guetta at Arena Maeda, Itu."),
  (E, "Cartaz · Flyer · Anúncios · Digital", "Poster · Flyer · Ads · Digital")],
 [(("Peças", "Pieces"), ["4830601/Screen shot 2013-01-23 at 1.41.50 PM_o.png", "4830601/flyerxxx16_45x15_line02_frente_o.jpg"])])

case("fifa-sorteio", "Sorteio Preliminar — Copa do Mundo da FIFA Brasil 2014™", "Preliminary Draw — 2014 FIFA World Cup Brazil™", "Eventos", "FIFA", "2011",
 "O primeiro evento oficial da Copa do Mundo de 2014 no Brasil, no Rio de Janeiro.", "The first official 2014 FIFA World Cup event in Brazil, in Rio de Janeiro.",
 "O futebol une o mundo no Brasil.", "Football unites the world in Brazil.",
 [(J, "O primeiro evento oficial ligado à Copa do Mundo da FIFA 2014 no Brasil. Um evento global e a primeira oportunidade do país de se apresentar como sede da Copa.",
      "The first official event in Brazil related to the 2014 FIFA World Cup. A global event and the country's first opportunity to perform as World Cup host."),
  (E, "Cartaz oficial · Cenografia · Sinalização · Peças do evento", "Official poster · Set design · Signage · Event pieces")],
 [(("O evento", "The event"), ["4335591/Screen shot 2012-10-28 at 12.33.14 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.33.31 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.29.33 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.30.03 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.22 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.36 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.32.07 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.31.54 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.32.23 PM_o.png",
   "4335591/Screen shot 2012-10-28 at 12.32.33 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.32.43 PM_o.png", "4335591/Screen shot 2012-10-28 at 12.59.20 PM_o.png"])],
 thumb="4335591/Screen shot 2012-10-28 at 12.33.14 PM_o.png")

case("tenis-espetacular", "Tênis Espetacular — Guga vs Agassi", "Tênis Espetacular — Guga vs Agassi", "Eventos", "Gillette · Duracell", "2010",
 "O maior duelo de tênis da história do Brasil num espetáculo de música e interatividade, no Maracanãzinho.", "The biggest tennis match in Brazil's history as a show of music and interactivity, at Maracanãzinho.",
 "O maior duelo de tênis da história do Brasil num espetáculo de música e interatividade.", "The biggest tennis match in Brazil's history, staged as a show of music and interactivity.",
 [(J, "Esporte, entretenimento, tecnologia e responsabilidade social: essa foi a fórmula do Tênis Espetacular, no Maracanãzinho, no Rio de Janeiro.",
      "Sport, entertainment, technology and social responsibility: that was the formula for Tênis Espetacular, at Maracanãzinho, Rio de Janeiro."),
  (E, "Campanha integrada · Cartaz · Digital · Interatividade no evento", "Integrated campaign · Poster · Digital · On-site interactivity")],
 [(("Esporte + entretenimento + tecnologia + responsabilidade social", "Sport + entertainment + technology + social responsibility"), [
    p("Nas quadras, Guga vs Agassi, relembrando o duelo em que o brasileiro se tornou o número 1 do ranking mundial. Nos palcos, Luciano Huck e Frejat comandando a festa. Nas UPPs, clínicas de tênis e diversas outras atrações.",
      "On court, Guga vs Agassi, recalling the match in which the Brazilian became world number one. On stage, Luciano Huck and Frejat hosting the party. In the UPP communities, tennis clinics and many other attractions."),
    y("DL7Dpvw2WHI")]),
  (("Resultados", "Results"), [
    p("Líder de audiência no horário de exibição · 2 trending topics no Twitter por 6 horas no dia do evento · 2.500 crianças atendidas · 10 mil pessoas presentes, lotação máxima · Mais de R$ 15 milhões em exposição de mídia · Mais de 5 mil SMS enviados pelo público · R$ 40 mil em doações ao Criança Esperança",
      "Top-rated in its time slot · 2 Twitter trending topics for 6 hours on event day · 2,500 children served · 10,000 people, sold out · Over R$ 15 million in media exposure · Over 5,000 text messages from the audience · R$ 40,000 donated to Criança Esperança")])],
 thumb="4382149/prt_220x317_1352146659.jpg")

case("ck-lolla", "Calvin Klein Jeans — Lollapalooza Brasil", "Calvin Klein Jeans — Lollapalooza Brasil", "Eventos", "Calvin Klein Jeans", "2012",
 "Ativação do jeans oficial do Lollapalooza Brasil: espaço de sombra, cabine de fotos e desfile.", "Activation for Lollapalooza Brasil's official jeans: shade lounge, photo booth and catwalk.",
 "Moda e música andam juntas: o jeans oficial do Lollapalooza Brasil.", "Fashion and music go together: Lollapalooza Brasil's official jeans.",
 [(J, "A Calvin Klein Jeans levou o conceito da sua última campanha para o festival. E fez bonito por lá.", "Calvin Klein Jeans brought its latest campaign concept to the festival, and it looked great there."),
  (E, "Espaço de marca · Cabine de fotos · Backdrop · Ação com promotoras", "Brand space · Photo booth · Backdrop · Brand ambassador action")],
 [(("Moda e música andam juntas", "Fashion and music go together"), [
    p("Foi da marca o espaço de sombra que garantiu momentos de descontração e conforto no Lolla: pufes coloridos e 10 carregadores de celular espalhados pela tenda davam o tom de relax ao local.",
      "The brand owned the shade lounge that brought relaxation and comfort to Lolla: colourful poufs and 10 phone chargers across the tent set a laid-back mood."),
    "4287777/ck1_1000.png"]),
  (("Cabine de fotos", "Photo booth"), [
    p("Os convidados tiravam fotos com um backdrop da marca e postavam direto no Facebook. Uma ação simples que fez um sucesso enorme: mais de 1.000 fotos, com muita visibilidade e mídia espontânea para a marca.",
      "Guests took photos against a brand backdrop and posted them straight to Facebook. A simple action that was a huge hit: over 1,000 photos, with strong visibility and earned media for the brand."),
    "4287777/ck3_1000.png"]),
  (("Desfile", "Catwalk"), [
    p("Promotoras desfilaram pela Cabana vestidas com a nova coleção, divulgando a marca e o espaço de sombra no espaço mais exclusivo do festival. Não teve quem não viu.",
      "Models walked through the Cabana wearing the new collection, promoting the brand and the shade lounge in the festival's most exclusive area. Nobody missed it."),
    "4287777/ck2_1000.png"])], thumb="4287777/ck1_1000.png")

case("f1-rocks", "F1 Rocks — São Paulo", "F1 Rocks — São Paulo", "Eventos", "Formula 1 · LG", "2010",
 "Evento musical criado para acompanhar as etapas do circuito mundial de F1, com Eminem como headliner.", "A music event created to accompany the Formula 1 world championship, headlined by Eminem.",
 "Os melhores do automobilismo e os melhores da música no mesmo palco.", "The best of motorsport and the best of music on one stage.",
 [(J, "O F1 Rocks é um evento musical criado para acompanhar as etapas do circuito mundial de Fórmula 1. Campanha integrada e evento.",
      "F1 Rocks is a music event created to accompany the Formula 1 world championship. Integrated campaign and event."),
  (E, "Campanha integrada · Key visual · Cenografia · Digital · Promoção", "Integrated campaign · Key visual · Set design · Digital · Promotion")],
 [(("Conceito", "Concept"), [
    p("A-list: os melhores do automobilismo mundial reunidos com os melhores da música. Glamour: o glamour da F1 e o showbiz no mesmo palco. Adrenalina: música e velocidade unidas numa experiência inovadora.",
      "A-list: the world's best in motorsport together with the best in music. Glamour: F1 glamour and showbiz on the same stage. Adrenaline: music and speed joined in an innovative experience."),
    y("cUAtnICfzlE")]),
  (("Badalação e agito", "Buzz and excitement"), [
    p("Áreas VIP com celebridades, personalidades do automobilismo, pilotos, equipes e artistas: festas de backstage, tapete vermelho, área de autógrafos e coletiva de imprensa.",
      "VIP areas with celebrities, motorsport personalities, drivers, teams and artists: backstage parties, red carpet, autograph area and press conference.")]),
  (("Plataforma de comunicação", "Communication platform"), [
    p("O F1 Rocks foi planejado para ser uma plataforma de comunicação e marketing eficiente: alta visibilidade de arena, ativações e espaços proprietários, forte presença na mídia, alto envolvimento editorial e geração de conteúdo de marca.",
      "F1 Rocks was planned as an efficient communication and marketing platform: high arena visibility, activations and proprietary spaces, strong media presence, high editorial engagement and branded content.")]),
  (("Plano de comunicação integrado", "Integrated communication plan"), [
    p("Com investimento de R$ 2,5 milhões em mídia, um plano integrado com forte presença digital: TV, rádio, jornal, revista, RP, influenciadores, digital, redes sociais, ativação e evento.",
      "With R$ 2.5 million invested in media, an integrated plan with a strong digital presence: TV, radio, newspapers, magazines, PR, influencers, digital, social media, activation and event."),
    "4330737/s2_1067.jpg", "4330737/s3_1067.jpg", "4330737/s4_1067.jpg", "4330737/s5_1067.jpg", "4330737/s8_1067.jpg", "4330737/s9_1067.jpg", "4330737/s10_1067.jpg",
    "4330737/s11_1067.jpg", "4330737/s12_1067.jpg", "4330737/s13_1067.jpg", "4330737/s14_1067.jpg", "4330737/s15_1067.jpg", "4330737/s16_1067.jpg", "4330737/s17_1067.jpg"]),
  (("Cenografia", "Set design"), ["4330737/c9_1000.jpg", "4330737/c8_1000.jpg", "4330737/c7_1000.jpg", "4330737/c6_1000.jpg", "4330737/c5_1000.jpg", "4330737/c4_1000.jpg", "4330737/c3_1000.jpg", "4330737/c2_1000.jpg", "4330737/c1_1000.jpg"]),
  (("Resultado", "Results"), [
    p("35 mil pessoas, sold out · 74 mil visitantes únicos · 255 mil pagáveis em um mês · Mais de 100 novos seguidores por dia no Twitter, com média de 450 conversas diárias · Mais de 500 mil visualizações da campanha no Facebook · R$ 17,4 milhões em mídia espontânea · Promoção “Vai de Limo”: 20 mil pageviews por dia e 4 mil conversas",
      "35,000 people, sold out · 74,000 unique visitors · 255,000 page views in one month · Over 100 new Twitter followers a day, averaging 450 daily conversations · Over 500,000 campaign views on Facebook · R$ 17.4 million in earned media · “Vai de Limo” promotion: 20,000 page views a day and 4,000 conversations")]),
  (("Transmissão", "Broadcast"), [
    p("Um evento pensado para ser transmitido para todo o Brasil pelo Multishow, com programas distribuídos para 170 emissoras no mundo e audiência acima de 26 milhões de telespectadores, avaliada em mais de US$ 47 milhões.",
      "An event designed to be broadcast across Brazil on Multishow, with programmes distributed to 170 stations worldwide and an audience above 26 million viewers, valued at over US$ 47 million.")])],
 thumb="4330737/s2_1067.jpg")

case("lolla-anuncios-2013", "Lollapalooza Brasil — Anúncios do line-up 2013", "Lollapalooza Brasil — 2013 line-up ads", "Campanhas", "Lollapalooza Brasil", "2013",
 "Anúncios de lançamento do line-up da segunda edição do festival, com ilustração e o chamado “Garanta já seu ingresso”.", "Launch ads for the line-up of the festival's second edition, with illustration and the call “Get your ticket now”.",
 "O line-up como um espetáculo: a cortina se abre para as bandas.", "The line-up as a show: the curtain opens on the bands.",
 [(J, "Anúncios de jornal e revista para revelar as atrações do Lollapalooza Brasil 2013 e abrir as vendas de ingressos.", "Newspaper and magazine ads revealing the Lollapalooza Brasil 2013 acts and opening ticket sales."),
  (E, "Anúncios de jornal e revista · Cartaz do line-up", "Newspaper and magazine ads · Line-up poster")],
 [(("Peças", "Pieces"), ["4289473/An_Lolla_297x52a2.jpg.scaled696.jpg"])])

case("heineken-lolla-2012", "Heineken — Lollapalooza Brasil 2012", "Heineken — Lollapalooza Brasil 2012", "Eventos", "Heineken", "2012",
 "Ativações da cerveja oficial na primeira edição do Lollapalooza Brasil.", "Activations for the official beer at the first Lollapalooza Brasil.",
 "Sinal verde para a música no Lollapalooza Brasil.", "Green light for music at Lollapalooza Brasil.",
 [(J, "135 mil pessoas curtiram as mais de 50 atrações do festival embaladas pelo sabor marcante de Heineken.", "135,000 people enjoyed the festival's 50-plus acts with the distinctive taste of Heineken."),
  (E, "Ativações de marca · Espaços proprietários · Brindes · Visibilidade de arena", "Brand activations · Proprietary spaces · Giveaways · Arena visibility")],
 [(("Sinal verde para a música", "Green light for music"), [
    p("Além de não sair das mãos do público, a cerveja oficial do Lollapalooza Brasil não saiu da cabeça de quem passou por lá. A marca foi responsável por ativações memoráveis dentro do Jockey Club, garantindo experiências também fora dos palcos: Beer Station, Backpackers, Heineken in the Sky, Heineken Moments, sticks de neon, chopeiras, visibilidade de arena e responsabilidade social.",
      "Besides never leaving the crowd's hands, the official beer of Lollapalooza Brasil never left their minds. The brand delivered memorable activations across the Jockey Club, with experiences off stage too: Beer Station, Backpackers, Heineken in the Sky, Heineken Moments, neon sticks, draft stations, arena visibility and social responsibility."),
    "4286085/h1_1000.png", "4286085/h2_1000.png", "4286085/h3_1000.png"]),
  (("Resultados", "Results"), [
    p("Para 60% do público que também foi ao Rock in Rio ou ao SWU, a Heineken teve mais e melhores atividades no Lollapalooza. A marca foi associada ao consumo responsável por 65% dos entrevistados, e 31% perceberam relação com a sustentabilidade. A Heineken foi protagonista do festival, com o maior recall de marca.",
      "For 60% of attendees who also went to Rock in Rio or SWU, Heineken had more and better activities at Lollapalooza. 65% linked the brand to responsible drinking and 31% to sustainability. Heineken was the festival's leading brand, with the highest recall.")])],
 thumb="4286085/h1_1000.png")

case("cocazero-lolla", "Coca-Cola Zero — Lollapalooza Brasil", "Coca-Cola Zero — Lollapalooza Brasil", "Eventos", "Coca-Cola", "2012",
 "O Simulador de Mosh: uma foto de você dando um mosh no Lolla, pronta para compartilhar.", "The Mosh Simulator: a photo of you crowd-surfing at Lolla, ready to share.",
 "Qual é a possibilidade de você dar um mosh no Lolla Brasil?", "What are the odds of you crowd-surfing at Lolla Brasil?",
 [(S, "O Simulador de Mosh: os convidados tiravam uma foto simulando um mosh sobre a plateia e compartilhavam com os amigos pelo Facebook. Foi a ação que mais bombou no festival.",
      "The Mosh Simulator: guests took a photo crowd-surfing over the audience and shared it with friends on Facebook. It was the festival's most popular activation."),
  (E, "Ativação · Cenário fotográfico · Compartilhamento social", "Activation · Photo set · Social sharing")],
 [(("Simulador de Mosh", "Mosh Simulator"), [y("g0GC5T98tnE"),
    "4286045/Screen_shot_2012-08-10_at_10.32.08_AM.png.scaled1000_o.png", "4286045/Screen_shot_2012-08-10_at_10.32.57_AM.png.scaled1000_o.png", "4286045/Screen_shot_2012-08-10_at_10.33.19_AM.png.scaled1000_o.png"])])

case("yahoo-bic", "Yahoo! Big Idea Chair", "Yahoo! Big Idea Chair", "Eventos", "Yahoo! Brasil", "2007",
 "O prêmio global do Yahoo! adaptado ao mercado brasileiro, com uma única categoria: a grande ideia.", "Yahoo!'s global award adapted to the Brazilian market, with a single category: the big idea.",
 "Não as pequenas boas ideias: a grande ideia.", "Not the little good ideas: the big idea.",
 [(J, "Em 2007, o Yahoo! trouxe ao Brasil o prêmio Y! Big Idea Chair. Planejamento, posicionamento, evento e campanha integrada de comunicação.",
      "In 2007 Yahoo! brought the Y! Big Idea Chair award to Brazil. Planning, positioning, event and integrated communication campaign."),
  (E, "Posicionamento · Evento de premiação · Campanha integrada · Impressos", "Positioning · Award event · Integrated campaign · Print")],
 [(("Desafio", "Challenge"), [
    p("Adaptar o prêmio à realidade brasileira e aumentar a relevância do Yahoo! no mercado local. Em outros países, o prêmio funcionava como uma espécie de hospedeiro de outros grandes prêmios, valorizando peças que usavam a plataforma Y!.",
      "Adapt the award to the Brazilian market and raise Yahoo!'s relevance locally. In other countries the award piggybacked on other major awards, recognising work that used the Y! platform."),
    "11739313/BIC2_877.jpg", "11739313/BIC4_877.jpg"]),
  (("Construção do insight", "Building the insight"), [
    p("O Yahoo! encontrava uma grande barreira no Brasil: poucos eventos específicos da categoria, ou de players concorrentes. Barreira de entrada vs. oportunidade de diferenciação: transformamos o problema em solução.",
      "Yahoo! faced a big barrier in Brazil: few events specific to the category, or owned by competitors. Barrier to entry vs. an opportunity to stand out: we turned the problem into the solution.")]),
  (("Nossa proposta", "Our proposal"), [
    p("Sair dos formatos convencionais e valorizar não as little good ideas, mas THE BIG IDEA: um prêmio com uma única grande categoria, que valoriza toda a cadeia por trás de uma grande ideia.",
      "Break away from conventional formats and celebrate not the little good ideas but THE BIG IDEA: an award with one single category, recognising the whole chain behind a big idea."),
    "11739313/BIC1_1000.jpg", "11739313/bic5_1000.jpg", "11739313/Screen-Shot-2016-07-11-at-4.33.50-PM_1186.png", "11739313/Screen-Shot-2016-07-11-at-4.34.06-PM_1187.png", "11739313/Screen-Shot-2016-07-11-at-4.22.32-PM_1178.png"]),
  (("Impresso", "Print"), ["11739313/Screen-Shot-2016-07-15-at-9.57.23-PM_933.png", "11739313/Screen-Shot-2016-07-15-at-10.04.08-PM_938.png", "11739313/Screen-Shot-2016-07-15-at-10.05.43-PM_924.png", "11739313/Screen-Shot-2016-07-15-at-10.05.10-PM_932.png"])],
 thumb="11739313/BIC2_877.jpg")

case("heineken-lolla-2013", "Heineken — Lollapalooza Brasil 2013", "Heineken — Lollapalooza Brasil 2013", "Eventos", "Heineken", "2013",
 "Pulseiras de LED, roda gigante e o Jockey aceso em verde durante os três dias de festival.", "LED wristbands, a Ferris wheel and the Jockey Club lit green across the three festival days.",
 "O verde trazia refrescância de dia e acendia o Jockey à noite.", "Green refreshed the day and lit up the Jockey Club at night.",
 [(J, "Em 2013, a Heineken se destacou ainda mais no Lollapalooza. Além do verde predominante, as ativações marcaram a experiência do público nos três dias de festival.",
      "In 2013 Heineken stood out even more at Lollapalooza. Beyond the dominant green, its activations shaped the audience's experience across all three festival days."),
  (E, "Ativações · Espaços de marca · Brindes · Vídeos", "Activations · Brand spaces · Giveaways · Videos")],
 [(("O verde no festival", "Green across the festival"), [
    p("Reunindo o melhor da experiência do Lollapalooza com o prazer de uma Heineken, as ativações da cerveja oficial foram ainda mais marcantes. Presente durante todo o festival, o verde trazia refrescância de dia e energia à noite, acendendo o Jockey com luzes verdes.",
      "Combining the best of the Lollapalooza experience with the pleasure of a Heineken, the official beer's activations were even more memorable. Present throughout the festival, green brought freshness by day and energy by night, lighting up the Jockey Club."),
    y("b8uuWsYiN8I")]),
  (("Heineken Moment", "Heineken Moment"), [
    p("Em parceria com a PixMob, trouxemos ao Brasil pulseiras de LED controladas por radiofrequência, que se acendiam ao som da trilha da Heineken durante a exibição de um vídeo, emocionando o público com um espetáculo de luzes.",
      "Together with PixMob, we brought radio-controlled LED wristbands to Brazil, lighting up to the Heineken soundtrack during a video and thrilling the crowd with a light show."),
    "8496984/Crowd_3-1130x430_1130.jpg", y("dR-rlh3hFxY"), y("Uc8Vp0QNmOQ")]),
  (("Roda gigante", "Ferris wheel"), [
    p("Atração tradicional dos maiores festivais do mundo, a roda gigante da Heineken tinha um lounge com o Chopp Perfeito, fotocabine e wi-fi gratuito.",
      "A classic at the world's biggest festivals, the Heineken Ferris wheel had a lounge serving the Perfect Draught, a photo booth and free wi-fi."),
    "8496984/h4_1600_c.jpg", "8496984/h6_1600_c.jpg", "8496984/h5_1600_c.jpg", "8496984/h7_1600_c.jpg", "8496984/h8_1600_c.jpg"]),
  (("Espaço de sombra", "Shade lounge"), [p("60 pufes personalizados com a marca Heineken.", "60 Heineken-branded poufs."), "8496984/h9_1600_c.jpg", "8496984/sombra_1600_c.jpg"]),
  (("Rock and Recycle", "Rock and Recycle"), [p("Copos descartáveis coletados pelo público eram trocados por brindes.", "Disposable cups collected by the audience were swapped for giveaways."),
    "8496984/hs1_1600_c.jpg", "8496984/hs2_1600_c.jpg", "8496984/hs3_1600_c.jpg"]),
  (("Brindes", "Giveaways"), ["8496984/hb1_1600_c.jpg"])],
 thumb="8496984/h4_1600_c.jpg")

case("lolla-lineup-na-linha", "Lollapalooza Brasil — Lineup na linha", "Lollapalooza Brasil — Lineup on the line", "Campanhas", "Lollapalooza Brasil", "2012",
 "Anúncio interativo na linha amarela do metrô de São Paulo, a 600 metros do festival.", "An interactive ad on São Paulo's yellow metro line, 600 metres from the festival.",
 "Lineup na linha: o festival começa no metrô.", "Lineup on the line: the festival starts on the metro.",
 [(D, "Promover o festival e incentivar o público a ir de metrô até o Jockey Club.", "Promote the festival and encourage people to take the metro to the Jockey Club."),
  (S, "A linha amarela do metrô de São Paulo foi a primeira linha “mobile friendly” do país, e uma das suas paradas, a estação Butantã, fica a 600 metros do Jockey Club. Ali, criamos um anúncio interativo: com o celular, o público lia um QR code e acessava o aplicativo para montar e compartilhar o line-up do festival.",
      "São Paulo's yellow metro line was the country's first “mobile friendly” line, and one of its stops, Butantã, is 600 metres from the Jockey Club. There we created an interactive ad: people scanned a QR code with their phones and opened the app to build and share the festival line-up."),
  (E, "Mídia em metrô · QR code · Aplicativo", "Metro media · QR code · App")],
 [(("Peças", "Pieces"), ["4286006/_.jpg.scaled1000.jpg", "4286006/iveco-iphone.jpg.scaled696.jpg", "4286006/PORTA_SEGURANCA_METRO.jpg.scaled1000.jpg", "4286006/estacao-butanta.jpg.scaled1000_o.jpg"])],
 thumb="4286006/iveco-iphone.jpg.scaled696.jpg")

case("lolla-anuncio-interativo", "Lollapalooza Brasil — Anúncio interativo", "Lollapalooza Brasil — Interactive ad", "Campanhas", "Lollapalooza Brasil", "2012",
 "Um anúncio impresso que ganha vida no celular, na revista Rolling Stone.", "A print ad that comes alive on your phone, in Rolling Stone magazine.",
 "Interativo como um aplicativo.", "As interactive as an app.",
 [(D, "Divulgar o festival e o lançamento do aplicativo oficial do Lolla. Para isso, o anúncio também tinha que ser interativo.", "Promote the festival and the launch of Lolla's official app, so the ad had to be interactive too."),
  (S, "Um anúncio na Rolling Stone em que o leitor via, na prática, um pouco de como seria o aplicativo do festival.", "A Rolling Stone ad in which readers could try out what the festival app would be like."),
  (R, "Mais de 50 mil interações.", "Over 50,000 interactions."),
  (E, "Anúncio de revista · Realidade aumentada", "Magazine ad · Augmented reality")],
 [(("Peças", "Pieces"), ["4285967/ad_lolla_interativo.jpg.scaled1000_o.jpg"])])

case("lolla-grid-reveal", "Lollapalooza Brasil — Grid reveal", "Lollapalooza Brasil — Grid reveal", "Campanhas", "Lollapalooza Brasil", "2013",
 "Cada like no Facebook erguia um pouco a cortina que escondia a programação do festival.", "Every Facebook like raised the curtain hiding the festival schedule a little more.",
 "Quem vai revelar os shows de cada dia? Você e seus amigos.", "Who will reveal each day's shows? You and your friends.",
 [(J, "Queríamos que os fãs no Facebook fizessem parte do anúncio da programação, o momento que revela quais bandas tocam em cada dia. Cada like no post da campanha erguia um pouco a cortina que escondia os nomes; com likes suficientes, os fãs viam a programação completa de cada dia.",
      "We wanted Facebook fans to be part of announcing the schedule, the moment that reveals which bands play on which day. Every like on the campaign post raised the curtain hiding the names a little; with enough likes, fans saw each day's full line-up."),
  (R, "26.302 likes, 1.204 comentários e 487 compartilhamentos, com 12% de engajamento na página · No site da transmissão ao vivo, 49.973 views e 22% de engajamento.",
      "26,302 likes, 1,204 comments and 487 shares, with a 12% page engagement rate · On the live-stream site, 49,973 views and 22% engagement."),
  (E, "Ação em redes sociais · Peças digitais · Live stream", "Social media action · Digital pieces · Live stream")],
 [(("A cortina", "The curtain"), ["4431328/Cortina_o.jpg", "11739808/Screen-Shot-2016-07-11-at-9.54.09-PM_1103.png", "11739808/Screen-Shot-2016-07-11-at-9.54.39-PM_1121.png"]),
  (("Métricas", "Metrics"), ["11739808/Screen-Shot-2016-07-11-at-9.55.00-PM_1116.png", "11739808/Screen-Shot-2016-07-11-at-9.56.09-PM_1124.png"])],
 thumb="4431328/Cortina_o.jpg")

case("lolla-filme-2013", "Lollapalooza Brasil — Filme do line-up 2013", "Lollapalooza Brasil — 2013 line-up film", "Campanhas", "Lollapalooza Brasil", "2013",
 "Filme animado de lançamento do line-up, cruzando os prédios de São Paulo.", "Animated line-up launch film, crossing São Paulo's buildings.",
 "Animação sobre a cidade: o line-up atravessa São Paulo.", "Animation over the city: the line-up crosses São Paulo.",
 [(J, "Filme de lançamento do line-up do Lollapalooza Brasil 2013, com animação desenhada sobre imagens reais de São Paulo, produzido pela Paranoid.",
      "Launch film for the Lollapalooza Brasil 2013 line-up, with animation drawn over real footage of São Paulo, produced by Paranoid."),
  (E, "Filme de lançamento · Frames para digital", "Launch film · Frames for digital")],
 [(("Filme", "Film"), [y("86JdkOh4A5o")]),
  (("Frames do filme", "Film frames"), ["4282906/bike.gif", "4282906/01_670.jpg", "4282906/02_670.jpg", "4282906/03_670.jpg", "4282906/04_670.jpg", "4282906/05_670.jpg", "4282906/06_670.jpg",
    "4282906/07_670.jpg", "4282906/08_670.jpg", "4282906/09_670.jpg", "4282906/10_670.jpg", "4282906/pordosol_lolla_670.jpg"])],
 thumb="4282906/01_670.jpg")

case("corrida-cartoon", "Corrida Cartoon Network", "Cartoon Network Run", "Eventos", "Cartoon Network", "2015",
 "Corrida em família em que as crianças correm em equipe com um adulto, levada pela primeira vez ao Rio de Janeiro.", "A family run where kids race in teams with an adult, taken to Rio de Janeiro for the first time.",
 "Corra do seu jeito: ganha quem se diverte mais.", "Run your way: whoever has the most fun wins.",
 [(J, "A Corrida Cartoon é um evento para a família: as crianças correm em equipe com um adulto, seja pai, mãe, amigo, tio ou qualquer adulto que queira participar da experiência.",
      "The Cartoon Run is a family event: kids run in a team with an adult, whether a parent, friend, uncle or any adult who wants to join the experience."),
  (E, "Conceito · Identidade do evento · Ativações · Peças de comunicação", "Concept · Event identity · Activations · Communication pieces")],
 [(("Desafio", "Challenge"), [
    p("Propor a evolução de um projeto de sucesso de público e de vendas, num cenário com frequência 20% maior que em 2014 em São Paulo, e levar o conceito do evento pela primeira vez ao Rio de Janeiro.",
      "Evolve a project that was already a hit with audiences and sponsors, with 20% more attendance than in 2014 in São Paulo, and take the event concept to Rio de Janeiro for the first time.")]),
  (("Solução", "Solution"), [
    p("Fomos estudar as motivações e os interesses do público de 4 a 14 anos e entender quem são essas crianças e pré-adolescentes fãs do canal, atingindo os pais indiretamente.",
      "We studied the motivations and interests of the 4-to-14 audience to understand who these young fans of the channel are, reaching parents indirectly.")]),
  (("Geração Z", "Generation Z"), [
    p("Crianças e pré-adolescentes que nasceram no mundo da internet, dos muitos canais de TV, dos smartphones, tablets e principalmente dos videogames, hoje a maior indústria de entretenimento do mundo. Foi pensando nessa geração que chegamos à gamificação: estratégias de interação com incentivos que estimulam o engajamento de forma lúdica.",
      "Children and pre-teens born into the world of the internet, countless TV channels, smartphones, tablets and above all video games, today the world's biggest entertainment industry. With this generation in mind we arrived at gamification: interaction strategies with incentives that drive engagement through play."),
    "11726640/Screen-Shot-2016-07-07-at-3.55.22-PM_992.png", "11726640/Screen-Shot-2016-07-07-at-4.06.05-PM_947.png", "11726640/Screen-Shot-2016-07-07-at-4.05.19-PM_948.png",
    "11726640/Screen-Shot-2016-07-07-at-4.05.11-PM_948.png", "11726640/Screen-Shot-2016-07-07-at-4.04.45-PM_949.png", "11726640/Screen-Shot-2016-07-07-at-4.04.04-PM_948.png",
    "11726640/Screen-Shot-2016-07-07-at-4.03.45-PM_948.png", "11726640/Screen-Shot-2016-07-07-at-4.03.09-PM_946.png"]),
  (("Corra do seu jeito", "Run your way"), [
    p("Em 2015, a Corrida Cartoon ficou muito mais divertida e irreverente, do jeito que a criançada gosta: uma corrida interativa e desafiadora, em que ganha quem se diverte mais.",
      "In 2015 the Cartoon Run became much more fun and irreverent, the way kids like it: an interactive, challenging run where whoever has the most fun wins."),
    y("VsCFZM3oeEA")])],
 thumb="11726640/Screen-Shot-2016-07-07-at-3.55.22-PM_992.png")

case("lolla-2012", "Lollapalooza Brasil 2012 — Campanha integrada", "Lollapalooza Brasil 2012 — Integrated campaign", "Campanhas", "Lollapalooza Brasil", "2012",
 "A campanha da primeira edição brasileira do festival: Dave Grohl, cinema, metrô, revista interativa e redes sociais.", "The campaign for the festival's first Brazilian edition: Dave Grohl, cinema, metro, an interactive magazine ad and social media.",
 "O sonho da nação rock'n'roll nos palcos brasileiros.", "The rock'n'roll nation's dream on Brazilian stages.",
 [(J, "Teve quem foi de verdade, quem foi pela TV e quem acompanhou pelas redes sociais. A primeira edição do Lollapalooza Brasil foi sucesso ao vivo, nas notícias e em todas as mídias sociais.",
      "Some went in person, some watched on TV and some followed on social media. The first Lollapalooza Brasil was a hit live, in the news and across social media."),
  (E, "Campanha integrada · Filmes · Mídia em cinema e metrô · Anúncio interativo · Redes sociais", "Integrated campaign · Films · Cinema and metro media · Interactive ad · Social media")],
 [(("Em todo lugar", "Everywhere"), [
    p("Um festival jovem para gente jovem. Onde encontrar esse público que está em todo lugar? Indo a todo lugar: cinema, redes sociais, revistas, aeroportos, metrô, rádios, bares e até o iTunes. Com R$ 10,2 milhões em mídia, um plano integrado que não só divulgou o festival, mas contou a história dos seus 20 anos.",
      "A young festival for young people. Where do you find an audience that is everywhere? By going everywhere: cinema, social media, magazines, airports, the metro, radio, bars and even iTunes. With R$ 10.2 million in media, an integrated plan that not only promoted the festival but told the story of its 20 years.")]),
  (("Nosso garoto-propaganda: Dave Grohl", "Our spokesman: Dave Grohl"), [
    p("Mais de 1 milhão de views na entrevista em que Dave Grohl anuncia sua vinda e apresenta o line-up do festival.", "Over 1 million views of the interview in which Dave Grohl announces he's coming and presents the festival line-up."),
    y("XeMLJpoLBgQ")]),
  (("Lolla Brasil no cinema", "Lolla Brasil at the cinema"), [
    p("Nada melhor que a tela do cinema para contar os 20 anos do Lollapalooza, seu conceito e sua chegada ao Brasil. Uma parceria com o Cinemark levou um mini-doc às sessões das salas digitais.",
      "Nothing better than the cinema screen to tell the story of Lollapalooza's 20 years, its concept and its arrival in Brazil. A partnership with Cinemark brought a mini-doc to its digital screens."),
    y("8zZbTQC1YzM")]),
  (("Interativo como um aplicativo", "As interactive as an app"), [
    p("Para divulgar o festival e o aplicativo oficial, um anúncio interativo na Rolling Stone. E, na linha amarela do metrô, a 600 metros do Jockey Club, um QR code para montar e compartilhar o line-up.",
      "To promote the festival and the official app, an interactive ad in Rolling Stone. And on the yellow metro line, 600 metres from the Jockey Club, a QR code to build and share the line-up."),
    "4285967/ad_lolla_interativo.jpg.scaled1000_o.jpg", "4286006/PORTA_SEGURANCA_METRO.jpg.scaled1000.jpg", "4286006/estacao-butanta.jpg.scaled1000_o.jpg"]),
  (("Social media e digital", "Social media and digital"), [
    p("O grande foco da campanha foram as redes sociais: de 0 a 600 mil seguidores em dois anos, mais de 80 mil cadastrados e um público que não só consome o conteúdo, mas gera o seu próprio. 150 mil likes no Facebook no primeiro mês, 1 milhão de visitas ao site, 3 mil downloads do aplicativo e 12 vezes nos trending topics.",
      "Social media was the campaign's main focus: from 0 to 600,000 followers in two years, over 80,000 sign-ups and an audience that not only consumes content but creates its own. 150,000 Facebook likes in the first month, 1 million site visits, 3,000 app downloads and 12 times in trending topics."),
    y("6eoTXGcXBv4")]),
  (("Ao vivo, onde você estiver", "Live, wherever you are"), [
    p("O Multishow transmitiu ao vivo os palcos principais, e os palcos Perry e Alternativo foram transmitidos pela internet. Mais de 43 milhões de pessoas passaram pelo Multishow nas 20 horas de transmissão, com 1,2 milhão de pageviews no site do canal e quase 260 mil views ao vivo.",
      "Multishow broadcast the main stages live, while the Perry and Alternative stages streamed online. Over 43 million people tuned into Multishow during 20 hours of coverage, with 1.2 million page views on the channel's site and nearly 260,000 live views.")])],
 thumb="4285967/ad_lolla_interativo.jpg.scaled1000_o.jpg")

case("lolla-2013", "Lollapalooza Brasil 2013 — Ocupe SP com música", "Lollapalooza Brasil 2013 — Occupy SP with music", "Campanhas", "Lollapalooza Brasil", "2013",
 "Campanha e evento da segunda edição: 167 mil pessoas e uma marca de festival ligada à descoberta.", "Campaign and event for the second edition: 167,000 people and a festival brand built on discovery.",
 "A festa da música veio para ficar.", "The music party is here to stay.",
 [(J, "A segunda edição do Lollapalooza levou 167 mil pessoas ao Jockey Club de São Paulo e consolidou o festival como o evento musical mais importante da cidade.",
      "The second Lollapalooza drew 167,000 people to São Paulo's Jockey Club and established the festival as the city's most important music event."),
  (E, "Conceito · Campanha integrada · Filme do line-up · Anúncios · Grid reveal · Concurso de pôster", "Concept · Integrated campaign · Line-up film · Ads · Grid reveal · Poster contest")],
 [(("Desafio", "Challenge"), [
    p("Uma pesquisa com a Limo Inc no Lolla 2012 mostrou que mais de 70% do público comprou ingresso pelos headliners, 20% para viver uma experiência de festival internacional e quase 10% para acompanhar os amigos. O desafio era aumentar o desejo de viver a experiência de festival e depender menos das grandes bandas: construir uma marca forte, ligada à descoberta de novos sons. Outro dado: 70% do público veio de fora de São Paulo no feriado de Páscoa.",
      "Research with Limo Inc at Lolla 2012 showed over 70% of the audience bought tickets for the headliners, 20% for an international festival experience and nearly 10% to join friends. The challenge was to grow the desire for the festival experience and rely less on big bands: build a strong brand tied to discovering new sounds. Another insight: 70% of the audience came from outside São Paulo over the Easter holiday.")]),
  (("Ocupe São Paulo com música", "Occupy São Paulo with music"), [
    p("Com R$ 24 milhões em mídia, o Lolla 2013 queria mais que revelar o line-up e vender ingressos: queria posicionar o festival no país todo. O conceito convocava os fãs a viver a música não só nos 3 dias no Jockey Club, mas durante toda a semana de Páscoa, pela cidade: shows gratuitos na Galeria do Rock e nas periferias, side shows, concurso de pôster oficial com a Urban Arts e conteúdo exclusivo nos dois meses antes do festival.",
      "With R$ 24 million in media, Lolla 2013 wanted more than to reveal the line-up and sell tickets: it wanted to position the festival nationwide. The concept invited fans to live the music not only for 3 days at the Jockey Club but all Easter week across the city: free shows at Galeria do Rock and in the outskirts, side shows, an official poster contest with Urban Arts and exclusive content in the two months before the festival."),
    "4289473/An_Lolla_297x52a2.jpg.scaled696.jpg"]),
  (("Filme de lançamento do line-up", "Line-up launch film"), [y("86JdkOh4A5o")]),
  (("Lançamento do grid de programação", "Schedule reveal"), [
    p("Cada like no post da campanha no Facebook erguia um pouco a cortina que escondia os nomes das bandas. Com likes suficientes, os fãs viam a programação completa de cada dia.",
      "Every like on the campaign's Facebook post raised the curtain hiding the band names a little. With enough likes, fans saw each day's full line-up."),
    "11739808/Screen-Shot-2016-07-11-at-9.54.09-PM_1103.png", "11739808/Screen-Shot-2016-07-11-at-9.54.39-PM_1121.png"]),
  (("Concurso do pôster oficial", "Official poster contest"), [
    p("O público foi convidado a criar o cartaz oficial do festival num concurso com a Urban Arts. Foram mais de 600 pôsteres inscritos e mais de R$ 10 milhões em mídia espontânea.",
      "The public was invited to create the festival's official poster in a contest with Urban Arts. Over 600 posters were entered, generating over R$ 10 million in earned media."),
    "11739808/481645_436356623117880_198609129_n_557.jpg", "11739808/559908_436356633117879_587724297_n_557.jpg", "11739808/poster0_557.jpg", "11739808/posters_1250.jpg"]),
  (("Resultados", "Results"), [
    p("167 mil pessoas nos 3 dias · Mais de 40 mil downloads do aplicativo, 5º lugar em música na App Store · Líder de audiência na TV paga nos 3 dias · Mais de 500 mil pessoas no show do Pearl Jam ao vivo · 9 milhões de pessoas alcançadas no Facebook · R$ 75,1 milhões em mídia espontânea · 1,3 milhão de visitas ao site em março · Trending topics nos 3 dias de festival",
      "167,000 people over 3 days · Over 40,000 app downloads, 5th in music on the App Store · Top-rated on pay TV all 3 days · Over 500,000 people watching Pearl Jam live · 9 million people reached on Facebook · R$ 75.1 million in earned media · 1.3 million site visits in March · Trending topics on all 3 festival days"),
    "11739808/Screen-Shot-2016-07-11-at-9.55.00-PM_1116.png", "11739808/Screen-Shot-2016-07-11-at-9.56.09-PM_1124.png"])],
 thumb="11739808/posters_1250.jpg")

# narrativa extra no case Billabong que já existe
EXTRA = {
 "billabong": [
  (("Billabong Rio Pro 2011 e 2012", "Billabong Rio Pro 2011 and 2012"), [
    p("Um evento histórico para o Rio, o Brasil e o surfe nacional. A única etapa do circuito mundial na América Latina levou em 2011 mais de 80 mil pessoas à praia, passou de 2 milhões de espectadores na transmissão ao vivo, distribuiu US$ 625 mil em prêmios e chegou aos trending topics durante a final masculina.",
      "A historic event for Rio, Brazil and Brazilian surfing. The only world tour stop in Latin America drew over 80,000 people to the beach in 2011, passed 2 million live-stream viewers, awarded US$ 625,000 in prize money and hit trending topics during the men's final."),
    y("ViscVgqLpmc")]),
  (("Plataforma e plano de comunicação", "Platform and communication plan"), [
    p("O Rio Pro foi planejado como plataforma de comunicação e marketing: visibilidade de arena, ativações e espaços proprietários, presença na mídia e conteúdo de marca. O plano integrado, avaliado em R$ 930 mil, foi da TV e do rádio a ações dirigidas nas novas mídias, para engajar o público antes mesmo do evento começar.",
      "The Rio Pro was planned as a communication and marketing platform: arena visibility, activations and proprietary spaces, media presence and branded content. The integrated plan, valued at R$ 930,000, ran from TV and radio to targeted new-media actions, engaging people before the event even began."),
    "4317779/Screen-Shot-2016-07-17-at-10.53.14-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.55-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.46-PM_1250.png",
    "4317779/Screen-Shot-2016-07-17-at-10.53.28-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.53.02-PM_1250.png", "4317779/Screen-Shot-2016-07-17-at-10.55.37-PM_1250.png"]),
  (("Um evento sustentável", "A sustainable event"), [
    p("Um evento que depende da natureza não podia esquecer a sustentabilidade. Um inventário das emissões de gases de efeito estufa do evento virou plano de neutralização, com plantio de mudas nativas da Mata Atlântica no Rio. Lonas de banners viraram capas de prancha em ONGs, e houve palestras para crianças, mutirões de reciclagem e ações nas duas arenas.",
      "An event that depends on nature couldn't ignore sustainability. An inventory of the event's greenhouse gas emissions became an offset plan, planting native Atlantic Forest seedlings in Rio. Banner vinyl became surfboard bags at NGOs, alongside talks for children, recycling drives and actions in both arenas.")]),
  (("Rio Pro 2012", "Rio Pro 2012"), [y("QrBRtu_9w6w"),
    "4317779/Billabong-Rio-Pro---May-11---22--2011_1308147227705_1600_c.png", "4317779/Screen-Shot-2016-07-13-at-4.25.02-PM_1109.png", "4317779/billa_2_o.jpg",
    "4317779/01-FRONTAL_o.jpg", "4317779/JH_Bilabong RIO Pro 2012_Programacao visual_Geral_10_o.jpg"])],
}
