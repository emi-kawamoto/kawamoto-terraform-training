--問題１
CREATE DATABASE exercise;

--問題２
USE exercise;
CREATE TABLE day1_to_drop( 
    id INTEGER NOT NULL PRIMARY KEY, 
    name VARCHAR(20) NOT NULL, 
    mail VARCHAR(60) NOT NULL, 
    birthday DATE 
    );

--問題３
CREATE TABLE companies( 
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL 
    );

--問題４
ALTER TABLE day1_to_drop ADD COLUMN tellphone CHAR(11);
