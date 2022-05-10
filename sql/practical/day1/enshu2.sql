--(1.1. usersにデータを格納)
INSERT INTO users VALUES (1, 'タヌキ', 'pokopoko@example.com', 19);
INSERT INTO users VALUES (2, 'ウサギ', 'moonlight@example.net', 20);
INSERT INTO users VALUES (3, 'ネコ', 'alivemillion@example.com', 31);
INSERT INTO users VALUES (4, 'ネズミ', 'hedgehook@example1.jp', 23);
INSERT INTO users VALUES (5, 'アルマジロ', 'sandsandpan@example.jp', 28);



--(1.2. followsにデータを格納)
INSERT INTO follows VALUES (1, 2);
INSERT INTO follows VALUES (1, 3);
INSERT INTO follows VALUES (1, 4);
INSERT INTO follows VALUES (1, 5);
INSERT INTO follows VALUES (3, 1);
INSERT INTO follows VALUES (3, 2);
INSERT INTO follows VALUES (4, 5);
INSERT INTO follows VALUES (5, 1);
INSERT INTO follows VALUES (5, 2);
INSERT INTO follows VALUES (5, 3);
INSERT INTO follows VALUES (5, 4);


