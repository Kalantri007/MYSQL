create database car;
use car;
create table car_details(
SR int,
model varchar(255),
stock int,
launch_date date,
car_description varchar(255)
);

create table order_details(
model varchar(255),
customer varchar(255),
contact int,
price int,
payment_method varchar(255)
);

alter table order_details
add column order_no int;
ALTER TABLE order_details 
MODIFY order_no int after model;


create table post_order_details(
order_no int ,
no_plate varchar(255),
delivery_date date,
delivery_address varchar(255)
);

alter table post_order_details
add column price int after no_plate;

create table feature(
model varchar(255),
car_typr varchar(255),
price int
);

