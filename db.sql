CREATE DATABASE `basic-api`;
USE `basic-api`;
CREATE TABLE events (

    id int(11) primary key,
    title varchar(255),
    content text,
    date datetime

);