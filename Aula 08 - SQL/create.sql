create table usuarios (
	id serial  primary key,
	created_at timestamp default now() NOT NULL,
	updated_at timestamp default now() NOT NULL,
	email      varchar unique NOT null,
	password   varchar not null,
	username   varchar not null,
	active     bool default true not null
)