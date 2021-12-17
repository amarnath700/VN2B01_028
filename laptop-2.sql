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



CREATE table Vendor(
id serial primary key,
sn integer,
Name varchar,
Designation varchar,
leve integer,
salary integer,
company varchar,
constraint laptop_list
 FOREIGN KEY(Sn)
REFERENCES laptop_list(Sn)
);

select * from Vendor 

INSERT INTO Vendor(Sn,name,designation,leve,salary,company) VALUES(2,'AMARNATH','TECHNICAL FIELD ENGGINEER',2,'25000','QUADGEN');
INSERT INTO Vendor(Sn,name,designation,leve,salary,company) VALUES(4,'SHANWIK','ADMIN',1,'15600','INFOSYS');
INSERT INTO Vendor(Sn,name,designation,leve,salary,company) VALUES(5,'VANI','IT REQUITER',3,'80000','CIGNEX');

INSERT INTO Vendor(Sn,name,designation,leve,salary,company) VALUES(1,'CHANDRA','TEAM LEADER',5,'150000','PUMA');
INSERT INTO Vendor(Sn,name,designation,leve,salary,company) VALUES(1,'VIJAYA','CEO',5,'555555','IGATE');


ALTER TABLE Vendor ADD COLUMN Experience varchar

UPDATE Vendor SET Experience='5years' where leve=3;
UPDATE Vendor set Experience='1.5years' where leve=1