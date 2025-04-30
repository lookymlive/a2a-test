-- Esquema SQL para Supabase: users y videos

create table users (
  id uuid primary key default uuid_generate_v4(),
  email text unique not null,
  role text check (role in ('usuario', 'comercio')) not null,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

create table videos (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  url text not null,
  uploaded_at timestamp with time zone default timezone('utc'::text, now())
);
