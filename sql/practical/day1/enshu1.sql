-- (1. `sns`データベースを作成してください)
CREATE DATABASE sns;

-- ※注意：作成後`use sns`をすること
-- (1.1.  `users`テーブルを作成してください)
CREATE table users(
  id integer not null PRIMARY KEY,
  name VARCHAR(15) NOT NULL, 
  email VARCHAR(50) NOT NULL,
  age INTEGER
);


-- (1.2. `follows`テーブルを作成してください)
CREATE Table follows(
  follower_id INTEGER NOT NULL,
  followee_id INTEGER NOT NULL
);


-- (2. テーブル一覧を表示させてください)
SHOW tables FROM sns;
