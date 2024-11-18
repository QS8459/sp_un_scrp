CREATE TABLE public.source(
    name VARCHAR(100),
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE public.category(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    label VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE public.posts(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id INTEGER,
    title VARCHAR(300),
    image_url VARCHAR(500),
    link VARCHAR(200) UNIQUE,
    description VARCHAR(650),
    source UUID,
    category UUID,
    posted_on TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source) REFERENCES source(id),
    FOREIGN KEY (category) REFERENCES category(id)
);

INSERT INTO public.source (name, id, created_at) VALUES
( 'sp', gen_random_uuid(), CURRENT_TIMESTAMP),
( 'uns', gen_random_uuid(), CURRENT_TIMESTAMP);

INSERT INTO public.category (id, label, created_at) VALUES
(gen_random_uuid(), 'BUSINESS', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'FINANCE', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'ECONOMY', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'PRIVATE_BUSINESS', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'STARTUP', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'TECH', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'ENERGY', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'BLOCKCHAIN_CRYPTO', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'GOVERNMENT', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'EDUCATION', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'TRANSPORT', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'ENTREPRENEUR', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'PERSON', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'INTERVIEW', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'MARKETING', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'SPORT', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'SOCIAL', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'ACCIDENTS', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'POLITICS', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'WEATHER', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'INDIVIDUAL BUSINESS', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'OTHER', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'CRIME', CURRENT_TIMESTAMP);
