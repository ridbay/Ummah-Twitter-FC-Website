-- Run this in your Supabase SQL editor
-- https://supabase.com/dashboard/project/<your-project>/sql/new

create table public.checkins (
  id          uuid        not null default gen_random_uuid(),
  name        text        not null,
  twitter     text,
  email       text        not null,
  role        text        not null check (role in ('Player', 'Fan')),
  supporting  text        not null default 'Neutral',
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

-- Table for team statistics
create table public.team_stats (
  id          uuid        not null default gen_random_uuid(),
  name        text        not null unique,
  played      integer     not null default 0,
  gd          integer     not null default 0,
  gf          integer     not null default 0,
  pts         integer     not null default 0,
  updated_at  timestamptz not null default now(),
  constraint team_stats_pkey primary key (id)
);

-- Enable Row Level Security
alter table public.team_stats enable row level security;

-- Anyone can read
create policy "public_select_team_stats" on public.team_stats
  for select to anon using (true);

-- Anyone can update (admin page protected by client-side PIN)
create policy "public_update_team_stats" on public.team_stats
  for update to anon using (true) with check (true);

-- Anyone can insert
create policy "public_insert_team_stats" on public.team_stats
  for insert to anon with check (true);

-- Enable real-time for live updates on the schedule and admin pages
alter publication supabase_realtime add table public.team_stats;

-- Insert initial team data
insert into public.team_stats (name) values 
  ('Abubakar'), 
  ('Aliy'), 
  ('Umar'), 
  ('Uthman');
