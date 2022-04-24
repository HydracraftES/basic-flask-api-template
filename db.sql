CREATE DATABASE `basic-api`;
USE `basic-api`;
CREATE TABLE events (

    id int(11) primary key not null AUTO_INCREMENT,
    title varchar(255) not null,
    content text not null,
    date datetime

);