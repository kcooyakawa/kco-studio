-- Rode uma vez no SQL Editor do Supabase.
create table if not exists garimpo_lotes (
  id text primary key,
  fonte text, codigo text, uf text, cidade text, bairro text, endereco text,
  tipo text, titulo text, descricao text, modalidade text,
  lance_min numeric, avaliacao numeric, desconto numeric, area numeric, dorm int,
  link text,
  status text default 'candidato',   -- candidato | analisado | aprovada | preselecionado | investigacao | descartada
  motivo text,
  analise jsonb,                      -- preenchido pelo Claude na due diligence
  rodada date, visto_em timestamptz, analisado_em timestamptz
);
create table if not exists garimpo_rodadas (
  data date primary key,
  fontes_ok text[], fontes_fora text[], triados int, candidatos int,
  por_fonte jsonb, descartes jsonb, criado_em timestamptz default now()
);
alter table garimpo_lotes enable row level security;
alter table garimpo_rodadas enable row level security;
