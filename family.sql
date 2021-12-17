create table amar_family(
Name varchar,
Age integer,
Relation varchar,
Occupation varchar,
height decimal)

insert into amar_family values('Lali Reddy',80,'grand father','farmer',5.5);
insert into amar_family values('Chandrasekhar Reddy',60,'father','farmer',5.8);
insert into amar_family values('Vijaya',55,'Mother','house-wife',5.0);
insert into amar_family values('Nagamma',75,'grand mother','House-wife',5.2);
insert into amar_family values('Vivekananda Reddy',28,'Younger Brother','IT Requiter',5.10);
insert into amar_family values('Vani',20,'wife','House-wife',5.5,'');
insert into amar_family values('Lali Reddy',1,'son','',2,'');
select * from amar_family 

Alter table amar_family add column native varchar;

update amar_family set native ='kadapa' where age=20
update amar_family set Occupation='Teacher' where height=5.8



delete from amar_family where Name='Lali Reddy'
