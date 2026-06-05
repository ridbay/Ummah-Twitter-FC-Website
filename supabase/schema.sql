-- Run this in your Supabase SQL editor
-- https://supabase.com/dashboard/project/<your-project>/sql/new

create table public.checkins (
  id          uuid        not null default gen_random_uuid(),
  name        text        not null,
  twitter     text,
  email       text        not null,
  role        text        not null check (role in ('Player', 'Fan')),
  arrived     boolean     not null default false,
  arrived_at  timestamptz,
  created_at  timestamptz not null default now(),
  constraint checkins_pkey        primary key (id),
  constraint checkins_email_key   unique (email)
);

-- Enable Row Level Security
alter table public.checkins enable row level security;

-- Anyone can register (check-in form is public)
create policy "public_insert" on public.checkins
  for insert to anon with check (true);

-- Anyone can read (admin page protected by client-side PIN)
create policy "public_select" on public.checkins
  for select to anon using (true);

-- Anyone can update arrived status (admin page protected by client-side PIN)
create policy "public_update" on public.checkins
  for update to anon using (true) with check (true);

-- Enable real-time for live updates on the admin page
-- (Also enable in: Supabase Dashboard → Database → Replication → checkins table)
alter publication supabase_realtime add table public.checkins;
