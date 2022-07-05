DROP DATABASE IF EXISTS league;

CREATE DATABASE league;

\c league

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name text NOT NULL
);

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  team_id int REFERENCES teams(id)
);

CREATE TABLE referees (
  id SERIAL PRIMARY KEY,
  name text NOT NULL
);

CREATE TABLE seasons (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  start_date date NOT NULL,
  end_date date NOT NULL
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  season_id int REFERENCES seasons(id),
  team1_id int REFERENCES teams(id),
  team1_score int NOT NULL,
  team2_id int REFERENCES teams(id),
  team2_score int NOT NULL
);

CREATE TABLE match_referees (
  id SERIAL PRIMARY KEY,
  match_id int REFERENCES matches(id),
  referee_id int REFERENCES referees(id)
);

CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  scorer_id int REFERENCES players(id),
  match_id int REFERENCES matches(id)
);

INSERT INTO teams(name)
VALUES
('Tigers'),
('Lions'),
('Bears');

INSERT INTO players(name, team_id)
VALUES
('Child1A', 1),
('Child2A', 1),
('Child3A', 1),
('Child4A', 1),
('Child1B', 2),
('Child2B', 2),
('Child3B', 2),
('Child4B', 2),
('Child1C', 3),
('Child2C', 3),
('Child3C', 3),
('Child4C', 3);

INSERT INTO referees(name)
VALUES
('Referee1'),
('Referee2'),
('Referee3'),
('Referee4');

INSERT INTO seasons(name, start_date, end_date)
VALUES
('2022 Youth Soccer', '2022-02-01', '2022-09-30');

INSERT INTO matches(season_id, team1_id, team1_score, team2_id, team2_score)
VALUES
(1, 1, 4, 2, 3),
(1, 1, 5, 3, 1),
(1, 2, 1, 3, 2),
(1, 2, 1, 1, 3);

INSERT INTO match_referees(match_id, referee_id)
VALUES
(1, 2),
(1, 1),
(1, 3),
(2, 1),
(2, 4),
(3, 4),
(3, 2),
(3, 1);

INSERT INTO goals(scorer_id, match_id)
VALUES
(1, 1),
(2, 1),
(1, 1),
(1, 1),
(5, 1),
(6, 1),
(7, 1),
(1, 2),
(2, 2),
(1, 2),
(3, 2),
(3, 2),
(9, 2),
(6, 3),
(10, 3),
(9, 3),
(9, 4),
(1, 4),
(4, 4),
(1, 4);


--To display match results
SELECT t1.name, m.team1_score, t2.name, m.team2_score,
CASE
  WHEN (m.team1_score > m.team2_score) THEN t1.name
  WHEN (m.team1_score < m.team2_score) THEN t2.name
  END AS winner
FROM matches m
JOIN teams t1
ON m.team1_id = t1.id
JOIN teams t2
ON m.team2_id = t2.id;

--To display standings
SELECT t.name, COUNT(winner) AS wins
FROM (
  SELECT 
  CASE
    WHEN (m.team1_score > m.team2_score) THEN t1.name
    WHEN (m.team1_score < m.team2_score) THEN t2.name
    END AS winner
  FROM matches m
  JOIN teams t1
  ON m.team1_id = t1.id
  JOIN teams t2
  ON m.team2_id = t2.id
) AS standings
RIGHT JOIN teams t
ON standings.winner = t.name
GROUP BY t.name
ORDER BY wins DESC;