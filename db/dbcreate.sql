drop database if exists team01;

create database team01;

create user 'manager'@'%' identified by'1234';

grant all privileges on team01.* to 'manager'@'%' with grant option;