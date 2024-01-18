-- 問題1

CREATE DATABASE exercise;

-- 問題2

CREATE TABLE day1_to_drop(
   id INTEGER PRIMARY KEY NOT NULL,
   name VARCHAR(20) NOT NULL,
   mail VARCHAR(60) NOT NULL,
   birthday DATE);

-- 問題3

CREATE TABLE companies(
   id INTEGER PRIMARY KEY NOT NULL,
   nmae VARCHAR(30) NOT NULL);

-- 問題4

ALTER TABLE day1_to_drop ADD COLUMN phone_number VARCHAR(11);

...
