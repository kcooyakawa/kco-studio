-- Curso Tráfego Imóveis by W3W — entregas das aulas práticas + feedback
-- Rode UMA vez no Supabase: SQL Editor → New query → cole tudo → Run.
-- Usa a função is_admin() que já existe no projeto.

create table if not exists public.entregas (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  email text, nome text,
  task_key text not null,          -- ex.: "0-3" (módulo-tarefa)
  task_titulo text,
  texto text,
  links text,
  arquivos jsonb not null default '[]',  -- [{name, path, size}]
  status text not null default 'enviado' check (status in ('enviado','ajustar','aprovado')),
  feedback jsonb,                  -- {fortes, melhorar, proximo, nota}
  feedback_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (user_id, task_key)
);

alter table public.entregas enable row level security;

drop policy if exists "aluno le as proprias" on public.entregas;
create policy "aluno le as proprias" on public.entregas for select
  using (auth.uid() = user_id or public.is_admin());

drop policy if exists "aluno envia" on public.entregas;
create policy "aluno envia" on public.entregas for insert
  with check (auth.uid() = user_id and status = 'enviado' and feedback is null);

-- aluno pode reenviar (volta para 'enviado'); admin pode dar feedback
drop policy if exists "aluno reenvia ou admin avalia" on public.entregas;
create policy "aluno reenvia ou admin avalia" on public.entregas for update
  using (auth.uid() = user_id or public.is_admin())
  with check (public.is_admin() or (auth.uid() = user_id and status = 'enviado'));

-- impede o aluno de alterar o próprio feedback
create or replace function public.entregas_guard() returns trigger language plpgsql as $$
begin
  if not public.is_admin() then
    new.feedback := old.feedback; new.feedback_at := old.feedback_at;
  end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists entregas_guard on public.entregas;
create trigger entregas_guard before update on public.entregas
  for each row execute function public.entregas_guard();

-- Arquivos (bucket privado, até 25 MB por arquivo)
insert into storage.buckets (id, name, public, file_size_limit)
values ('entregas','entregas', false, 26214400)
on conflict (id) do nothing;

drop policy if exists "entregas upload proprio" on storage.objects;
create policy "entregas upload proprio" on storage.objects for insert
  with check (bucket_id = 'entregas' and (storage.foldername(name))[1] = auth.uid()::text);

drop policy if exists "entregas ler proprio ou admin" on storage.objects;
create policy "entregas ler proprio ou admin" on storage.objects for select
  using (bucket_id = 'entregas' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));

drop policy if exists "entregas apagar proprio" on storage.objects;
create policy "entregas apagar proprio" on storage.objects for delete
  using (bucket_id = 'entregas' and (storage.foldername(name))[1] = auth.uid()::text);
