CREATE table laptop_list(
Sn SERIAL PRIMARY KEY,
Brand varchar,
model integer,
price integer,
adpator varchar)
select *from laptop_list 

insert into laptop_list(Brand,model,price,adpator) values('lenovo',123,126500,'yes');
insert into laptop_list(Brand,model,price,adpator) values('dell',269,96500,'yes');
insert into laptop_list(Brand,model,price,adpator) values('acer',895,78500,'yes');
insert into laptop_list(Brand,model,price,adpator) values('samsung',698,158500,'yes');
insert into laptop_list(Brand,model,price,adpator) values('apple',126,222220,'yes');
insert into laptop_list(Brand,model,price,adpator) values('realme',444,68840,'yes');


update laptop_list set price=159500 where Sn=4


alter table laptop_list add column Manufactur varchar

update laptop_list  set Manufactur='newyork' where Brand='apple';
update laptop_list  set Manufactur='china' where Brand='realme';

update laptop_list  set Manufactur='hongkong' where Brand='samsung';
update laptop_list  set Manufactur='japan' where Sn=1;
update laptop_list  set Manufactur='korea' where price=78500;
update laptop_list  set Manufactur='uk' where Model=269;


create table laptop as select * from laptop_list 

select * from laptop_list 
select * from laptop
drop table laptop_list

