-- 演習1

CREATE DATABASE exercise;

-- 演習2

CREATE TABLE day1_to_drop (
     id INTEGER NOT NULL PRIMARY KEY,
     name VARCHAR(20) NOT NULL,
     mail VARCHAR(60) NOT NULL,
     birthday DATE
);

-- 演習3

CREATE TABLE companies (
     id INTEGER NOT NULL,
     name VARCHAR(30) NOT NULL
);

-- 演習4

ALTER TABLE day1_to_drop ADD COLUMN phone_number CHAR(11) UNIQUE;

-- 演習5

SELECT * FROM day1_to_drop;

-- 演習6

SELECT id AS ユーザーID, name AS ユーザー氏名 FROM day1_to_drop;

-- 演習7

DROP TABLE day1_to_drop;

-- 演習8

SHOW COLUMNS FROM companies;

-- 演習9

MySQLのinformation_schemaとはデータベースやテーブル等に関するメタデータが格納されているデータベースのこと。
このデータベースの中にはメタデータの情報ごとに下記のテーブルに格納されている。
- SCHEMATA: データベース自体のメタデータを格納しているテーブル
- TABLES: テーブルのメタデータを格納しているテーブル
- COLUMNS: カラムのメタデータを格納しているテーブル
- KEY_COLUMN_USAGE: キーの制約


