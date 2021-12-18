create table teacher(
id integer,
tname varchar not null,
age integer,
salary integer);


insert into teacher values(1,'amar',30,15000);
insert into teacher values(11,'siva',32,150000);
insert into teacher values(12,'vinny',20,250000);
insert into teacher values(21,'vijaya',43,75000);
insert into teacher values(21,'viveka',25,18000);
insert into teacher values(31,'hari',39,19000);
insert into teacher values(41,'vani',30,10000);
insert into teacher values(61,'venu',39,22000);
insert into teacher values(16,'prasana',60,125000);

select *from teacher 

create table subject(
sno integer,
sub varchar,
class integer);


insert into subject values(11,'english',10);
insert into subject values(21,'maths',7);
insert into subject values(71,'g.k',2);
insert into subject values(16,'telugu',5);
insert into subject values(102,'physics',9);




/*cross join*/

select class,tname,age,sub from teacher cross join subject

select class,tname,age,sub from subject cross join teacher

select id,sub,salary,tname from teacher cross join subject

select id,sub,salary,tname from subject cross join teacher

select sub,id,class from subject cross join teacher

/*inner join*/

select id,sub,age from teacher inner join subject 
  on teacher.id = subject.sno
  
select sub,salary,tname from subject inner join teacher 
 on teacher.id = subject.sno
 
 /*left outer join */
 
 select id,sub,age from teacher left outer join subject /* teacher table is left*/
  on teacher.id = subject.sno
  
   select id,sub,age from subject left outer join teacher /* teacher table is right*/
  on teacher.id = subject.sno
  
  select sub,salary,tname from subject left outer join teacher 
 on teacher.id = subject.sno
 
 /* right outer join*/
 
 select id,sub,age from subject left outer join teacher /* subject table is left*/
  on teacher.id = subject.sno
  
   select id,sub,age from teacher left outer join subject /* subject table is right*/
  on teacher.id = subject.sno
  
  /* full outer join*/
  
  select id,sub,age from teacher full outer join subject 
  on teacher.id = subject.sno
  
  select id,sub,age from subject full outer join teacher 
  on teacher.id = subject.sno
  
  
  
  /*alias*/
  
 select t.id,s.sub,t.age from subject as s, teacher as t 
  where t.id = s.sno 
  
   select s.sno,t.tname,s.class from subject as s, teacher as t 
  where t.id = s.sno 
    
  
  /*truncate*/
  
  truncate table teacher 
  
  select * from teacher 
  
  
  /*transcation*/
  
  begin;
 
 update teacher set tname='vicky' where age =25
 
   select * from teacher
   
   rollback;
  
  select * from teacher 
  
  
  
  update subject set sub='hindi' where class = 5
  
  select * from subject 
  
  commit;
  rollback;
 
 
 
 /* sub quieres*/
 
 
 select * from teacher where id in (select id from teacher where salary>17000)
  
  
  
  begin;
 
  delete from teacher where salary <150000
  
  select * from teacher 
  
  rollback;
 
 
 

  


