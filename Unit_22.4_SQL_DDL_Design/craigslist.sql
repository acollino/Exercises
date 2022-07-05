DROP DATABASE IF EXISTS craigslist;

CREATE DATABASE craigslist;

\c craigslist

CREATE TABLE regions (
  id SERIAL PRIMARY KEY,
  name text
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text NOT NULL,
  pref_region_id int REFERENCES regions (id)
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  description text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text DEFAULT 'Title',
  content text,
  user_id int REFERENCES users (id),
  region_id int REFERENCES regions (id)
);

CREATE TABLE post_categories (
  id SERIAL PRIMARY KEY,
  post_id int REFERENCES posts (id),
  cat_id int REFERENCES categories (id)
);


INSERT INTO regions (name)
VALUES
('Los Angeles'),
('Seattle'),
('Washingtion DC'),
('Las Vegas'),
('Boston');

INSERT INTO users (username, pref_region_id)
VALUES
('NateTheGreat', 5),
('CatPerson95', 2),
('JohnJohnson', 3);

INSERT INTO categories (name, description)
VALUES
('Furniture', 'The post refers to furniture in some way.'),
('Photography', 'Posts about taking pictures.'),
('Baking', 'Posts about cooking with flour and starches.');

INSERT INTO categories (name)
VALUES
('Cats'),
('Buying/Selling'),
('Woodworking');

INSERT INTO posts (title, content, user_id, region_id)
VALUES
('My Best Cat Friends', DEFAULT, 2, 2),
('Moving to LA', 'Planning a move, looking to buy HANDMADE furniture in the area!', 1, 1),
(DEFAULT, 'Test new account post, please ignore', 3, 3);

INSERT INTO post_categories(post_id, cat_id)
VALUES
(1, 4),
(1, 2),
(2, 1),
(2, 5),
(2, 6);

SELECT p.title, p.content, u.username AS posted_by, r.name AS region
FROM posts p
JOIN users u
ON p.user_id = u.id
JOIN regions r
ON p.region_id = r.id;

SELECT p.title, c.name AS category, c.description
FROM posts p
JOIN post_categories pc
ON pc.post_id = p.id
JOIN categories c
ON pc.cat_id = c.id;

