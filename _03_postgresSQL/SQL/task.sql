create table t_task(
Sno serial primary key,
name  varchar
);
insert into t_task(name) values('Amarnath');
insert into t_task(name) values('Reddy');
insert into t_task(name) values('Siva Reddy');
insert into t_task(name) values('Anand');
insert into t_task(name) values('Raja');
insert into t_task(name) values('Murali');
insert into t_task(name) values('Viswa');

select * from t_task 

create table task1(
ID serial primary key,
sno integer,
project varchar,
days integer,
finaldate varchar,
constraint t_task
FOREIGN KEY(Sno)
REFERENCES t_task(Sno)
on delete set null);


insert into task1(sno,project,days,finaldate) values(3,'asdf',99,'12/12/12');
insert into task1(sno,project,days,finaldate) values(5,'asdf',09,'12/12/22');
insert into task1(sno,project,days,finaldate) values(6,'asdf',79,'12/12/18');
insert into task1(sno,project,days,finaldate) values(1,'zsdf',98,'12/12/19');
insert into task1(sno,project,days,finaldate) values(2,'msdf',96,'12/12/17');
insert into task1(sno,project,days,finaldate) values(7,'3sdf',9454,'12/12/32');
insert into task1(sno,project,days,finaldate) values(4,'gsdf',777,'12/12/22');

select * from task1 
delete from task1 where days=09
delete from t_task where sno=4
drop table t_task