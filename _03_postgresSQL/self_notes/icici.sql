create database icici_sa;
create table icici_sa.saving(
name varchar(30),
age integer,
balance float,
address varchar(60)
);
select * from icici_sa.saving;
INSERT into icici_sa.saving values("amarnath",30,2500.69,"anantapur");
insert into icici_sa.saving values("vivek",27,30000.22,"tadipatri");
insert into icici_sa.saving values("vani",25,300.22,"bengaluru");
insert into icici_sa.saving (person,balance) values("vijaya",3003);


alter table icici_sa.saving add column(sex varchar(10));
alter table icici_sa.saving modify name varchar(40);
alter table icici_sa.saving change name person varchar(20);

desc icici_sa.saving;
create table icici_sa.saving1(select * from icici_sa.saving);
rename table  icici_sa.saving1 to icici_sa.saving2;
select * from icici_sa.saving2;
truncate table icici_sa.saving2;
drop table icici_sa.saving2; 


create table comment;
alter table comment comment = "hi i am Amarnath Reddy";
select * from comment;

select * from icici_sa.saving where age =27;
select * from icici_sa.saving where age in (27);
select * from icici_sa.saving where address like"%n%";
select * from icici_sa.saving order by address desc;

select * from icici_sa.saving having age <= 27;
select distinct age from icici_sa.saving;

update icici_sa.saving set age =53 where(balance = 3003);
update icici_sa.saving set sex ="male" where(person = "amarnath");
update icici_sa.saving set sex ="female" where(person = "vani");
update icici_sa.saving set sex ="male" where(person = "vivek");
update icici_sa.saving set sex ="female",address = "nandyla" where(person = "vijaya");



delete from icici_sa.saving where(sex = "male");




select * from icici_sa.saving;














