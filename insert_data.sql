CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    role VARCHAR(10) CHECK (role IN ('buyer', 'artist')),
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);


INSERT INTO users (id, role, username, password, full_name, email, password_hash) VALUES
(1, 'buyer', 'buyer1', 'password123', 'John Doe', 'buyer1@example.com', 'hash1'),
(2, 'artist', 'artist1', 'password123', 'Jane Smith', 'artist1@example.com', 'hash2'),
(3, 'buyer', 'buyer2', 'password123', 'Alice Johnson', 'buyer2@example.com', 'hash3'),
(4, 'artist', 'artist2', 'password123', 'Bob Brown', 'artist2@example.com', 'hash4'),
(5, 'buyer', 'buyer3', 'password123', 'Charlie Davis', 'buyer3@example.com', 'hash5'),
(6, 'artist', 'artist3', 'password123', 'Diana Prince', 'artist3@example.com', 'hash6'),
(7, 'buyer', 'buyer4', 'password123', 'Edward Wilson', 'buyer4@example.com', 'hash7'),
(8, 'artist', 'artist4', 'password123', 'Fiona White', 'artist4@example.com', 'hash8'),
(9, 'buyer', 'buyer5', 'password123', 'George Harris', 'buyer5@example.com', 'hash9'),
(10, 'artist', 'artist5', 'password123', 'Helen Clark', 'artist5@example.com', 'hash10');
