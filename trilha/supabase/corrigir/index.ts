// Supabase Edge Function "corrigir" — correção automática das entregas pelo Claude.
// Segredo necessário: ANTHROPIC_API_KEY  (SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY já existem na função)
import { createClient } from "npm:@supabase/supabase-js@2";

const MODEL = "claude-sonnet-5-5";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type" };

// Critérios por entrega (chave = módulo-tarefa, igual à trilha)
const RUBRICA: Record<string, { t: string; c: string[] }> = {
  "0-3": { t: "Exercício: 5 empreendimentos, 3 perfis de comprador", c: [
    "Analisa 5 empreendimentos de alto padrão reais com localização, faixa de preço e diferenciais",
    "Cria 3 perfis de comprador distintos (ex.: investidor, família, downsizer) com dores, objeções e motivações",
    "Liga cada perfil a quais empreendimentos fazem sentido e por quê",
    "Indica onde cada perfil passa tempo online e que mensagem funcionaria"] },
  "0-4": { t: "Entrega: diagnóstico de mercado e mapa de compradores", c: [
    "Panorama do mercado de alto padrão da região (preço/m², oferta, concorrentes, como anunciam)",
    "Mapa de compradores com personas e jornada (descoberta, consideração, decisão)",
    "Conteúdo/mensagem recomendado para cada fase da jornada",
    "Conclusões acionáveis, não só descrição"] },
  "1-3": { t: "Exercício: estratégia para um imóvel de R$ 5 milhões", c: [
    "Público-alvo definido com persona principal e secundária",
    "Mensagem central e argumentos de venda específicos do imóvel",
    "Canais escolhidos com justificativa (Meta, Google, portais, WhatsApp, indicação)",
    "Verba e metas calculadas com funil de trás para frente (venda ← propostas ← visitas ← leads) e CPL máximo"] },
  "1-4": { t: "Entrega: plano estratégico de mídia e aquisição", c: [
    "Objetivo e metas SMART",
    "Distribuição de verba por canal e por fase do funil",
    "Cronograma e plano de testes",
    "Métricas de acompanhamento (CPL, custo por lead qualificado, custo por visita)"] },
  "2-5": { t: "Exercício: 3 campanhas Meta + 3 campanhas Google", c: [
    "Estrutura correta: campanha (objetivo) → conjunto (público, verba) → anúncio",
    "Meta: objetivo de cadastros ou mensagens, respeitando a categoria especial de imóveis",
    "Google: palavras-chave de intenção, correspondência adequada e lista de negativas",
    "Empreendimentos de regiões diferentes com abordagem adaptada a cada um"] },
  "2-6": { t: "Entrega: campanhas estruturadas e plano de mídia", c: [
    "Campanhas montadas (prints ou descrição detalhada) com públicos e criativos",
    "Orçamento diário e total coerente com as metas",
    "Plano de otimização: o que olhar e quando pausar/escalar",
    "Rastreamento previsto (Pixel, conversões, UTMs)"] },
  "3-5": { t: "Exercício: landing page + conjunto de anúncios", c: [
    "LP com título de benefício, galeria, ficha técnica, mapa, prova social e um único CTA",
    "Formulário curto que qualifica (faixa de investimento, prazo) e aceite LGPD",
    "Anúncios coerentes com a LP (mesma promessa e visual)",
    "Botão de WhatsApp e página de obrigado com próximo passo"] },
  "3-6": { t: "Entrega: página, formulários e plano de rastreamento", c: [
    "Página publicada ou protótipo completo",
    "Formulários com campos de qualificação",
    "Plano de rastreamento: Pixel/API de Conversões, GA4, UTMs padronizadas",
    "Hipótese de teste A/B definida"] },
  "4-4": { t: "Exercício: sistema de qualificação de compradores", c: [
    "Critérios por perfil, faixa de investimento declarada, intenção e prazo",
    "Lead scoring com pontos e corte para passar ao corretor",
    "Classificação frio/morno/quente com ação para cada um",
    "Roteiro de primeiro contato com perguntas de qualificação"] },
  "4-5": { t: "Entrega: CRM, pipeline e metodologia de qualificação", c: [
    "Pipeline com etapas claras e motivos de perda",
    "CRM ou planilha estruturada em uso",
    "Sequência de nutrição/follow-up com prazos",
    "Devolução de leads bons para a Meta (conversão offline) prevista"] },
  "5-4": { t: "Exercício: campanha real supervisionada", c: [
    "Campanha ativada com objetivo e verba informados",
    "Resultados de 2 semanas com números (investimento, leads, CPL, qualificados, visitas)",
    "Análise do que funcionou e do que não funcionou, com hipóteses",
    "Próximas ações de otimização"] },
  "5-5": { t: "Entrega: dashboard de performance e plano de otimização", c: [
    "Dashboard (Looker Studio ou similar) juntando mídia e CRM",
    "Métricas certas: CPL, custo por lead qualificado, custo por visita e por proposta",
    "Leitura dos dados com conclusões",
    "Plano de otimização e escala priorizado"] },
};

const SYS = `Você é o professor-corretor do "Curso Tráfego Imóveis by W3W", formação em tráfego pago e geração de leads para imóveis de alto padrão em São Paulo.
Corrija a entrega do aluno com rigor e generosidade, em português do Brasil, tom de mentor: direto, específico, encorajador.
Regras:
- Avalie SOMENTE contra os critérios dados. Cite trechos/elementos concretos da entrega.
- "fortes": 2–3 acertos específicos e por que importam.
- "melhorar": 1–3 ajustes concretos, cada um com um exemplo de como fazer no contexto de imóveis de alto padrão.
- "proximo": uma única ação clara para a próxima versão.
- "nota": inteiro de 0 a 10.
- "status": "aprovado" se nota >= 7 e todos os critérios essenciais foram atendidos; senão "ajustar".
- Se a entrega estiver vazia, fora do tema ou incompleta demais, nota baixa e "ajustar", explicando o que falta.
Responda APENAS com JSON: {"fortes":"...","melhorar":"...","proximo":"...","nota":0,"status":"ajustar"}`;

const b64 = (buf: ArrayBuffer) => { let s = ""; const b = new Uint8Array(buf); for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode(...b.subarray(i, i + 0x8000)); return btoa(s); };

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...cors, "Content-Type": "application/json" } });
  try {
    const { entrega_id } = await req.json();
    const url = Deno.env.get("SUPABASE_URL")!;
    const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    // confere quem chamou
    const jwt = (req.headers.get("Authorization") || "").replace("Bearer ", "");
    const { data: { user } } = await admin.auth.getUser(jwt);
    if (!user) return json({ error: "não autenticado" }, 401);

    const { data: e } = await admin.from("entregas").select("*").eq("id", entrega_id).single();
    if (!e) return json({ error: "entrega não encontrada" }, 404);
    const { data: isAdm } = await createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: "Bearer " + jwt } } }).rpc("is_admin");
    if (e.user_id !== user.id && !isAdm) return json({ error: "sem permissão" }, 403);

    const r = RUBRICA[e.task_key] || { t: e.task_titulo, c: ["Atende ao enunciado da tarefa com profundidade e exemplos concretos"] };
    const content: any[] = [];
    const outros: string[] = [];
    for (const a of (e.arquivos || []).slice(0, 6)) {
      const ext = (a.name.split(".").pop() || "").toLowerCase();
      const img: Record<string, string> = { png: "image/png", jpg: "image/jpeg", jpeg: "image/jpeg", webp: "image/webp" };
      if ((ext === "pdf" || img[ext]) && (a.size || 0) < 20e6) {
        const { data } = await admin.storage.from("entregas").download(a.path);
        if (!data) continue;
        const d = b64(await data.arrayBuffer());
        content.push(ext === "pdf"
          ? { type: "document", source: { type: "base64", media_type: "application/pdf", data: d }, title: a.name }
          : { type: "image", source: { type: "base64", media_type: img[ext], data: d } });
      } else outros.push(a.name);
    }
    content.push({ type: "text", text:
`TAREFA: ${r.t}
CRITÉRIOS:
${r.c.map((x, i) => `${i + 1}. ${x}`).join("\n")}

ENTREGA DO ALUNO (${e.nome || "aluno"}):
${e.texto || "(sem texto)"}
${e.links ? "\nLINKS ENVIADOS (você não consegue abri-los; avalie pelo que foi descrito e peça para colar o conteúdo ou exportar em PDF se for essencial): " + e.links : ""}
${outros.length ? "\nARQUIVOS QUE NÃO PUDERAM SER LIDOS (peça em PDF ou imagem se forem essenciais): " + outros.join(", ") : ""}
${e.feedback ? "\nFEEDBACK ANTERIOR (esta é uma reenvio; diga o que evoluiu): " + JSON.stringify(e.feedback) : ""}` });

    const res = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": Deno.env.get("ANTHROPIC_API_KEY")!, "anthropic-version": "2023-06-01", "content-type": "application/json" },
      body: JSON.stringify({ model: MODEL, max_tokens: 1500, system: SYS, messages: [{ role: "user", content }] }),
    });
    if (!res.ok) return json({ error: "IA indisponível", detail: await res.text() }, 502);
    const out = await res.json();
    const txt = (out.content || []).map((c: any) => c.text || "").join("");
    const fb = JSON.parse(txt.slice(txt.indexOf("{"), txt.lastIndexOf("}") + 1));
    const status = fb.status === "aprovado" ? "aprovado" : "ajustar";
    const feedback = { fortes: String(fb.fortes), melhorar: String(fb.melhorar), proximo: String(fb.proximo), nota: String(fb.nota) };
    const { data: saved, error } = await admin.from("entregas")
      .update({ status, feedback, feedback_at: new Date().toISOString(), corrigido_por: "ia" })
      .eq("id", e.id).select().single();
    if (error) return json({ error: error.message }, 500);
    return json(saved);
  } catch (err) {
    return json({ error: String(err) }, 500);
  }
});
