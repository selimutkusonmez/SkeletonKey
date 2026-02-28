-- Creating users table --
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Creating history table --
CREATE TABLE IF NOT EXISTS history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mode VARCHAR(50) NOT NULL,
    algorithm VARCHAR(50) NOT NULL,
    key VARCHAR(255),
    input_text TEXT NOT NULL,
    output_text TEXT NOT NULL
);

INSERT INTO users (username, password) 
VALUES ('admin', '1234') 
ON CONFLICT (username) DO NOTHING;