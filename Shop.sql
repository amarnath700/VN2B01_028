create table Shop(
Name of Grain varchar,
Grade char,
Quantity decimal,
kg_grams varchar);
drop table Shop 

select * from Shop 

Insert into Shop values('groundnut','A','2.5','kg');
Insert into shop values('rice','B','100.0','kg');
insert into shop values('wheat','c','15.6','kg');
insert into shop values('corn','A','300.25','grams');

alter table Shop add column Price decimal;

update Shop set Price='16.6' where Grade='c';
update Shop set Price='3659.33' where Quantity=100;

delete FROM Shop where Name='groundnut';

