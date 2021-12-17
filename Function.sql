create table student1(
subject varchar(2222),
marks integer not null);

insert into student1(subject,marks) values('math',98);
insert into student1(subject,marks) values('hindi',90);
insert into student1(subject,marks) values('telugu',38);
insert into student1(subject,marks) values('kannada',88);
insert into student1(subject,marks) values('social',58);
insert into student1(subject,marks) values('biology',45);
insert into student1(subject,marks) values('social',12);

select subject from student 



create or replace function total_count()
returns integer as $$
declare 
     total integer;
     begin
     select sum(marks) into total from student1 ;
     return total;
     end;
     $$ language plpgsql;
     
    
    select total_count()
    
    
    create or replace function total_names(list varchar)
returns varchar(22222) as $$
declare 
     total varchar(22222);
     begin
	    
     select list(subject) into total from student1 ;
     return total;
     end;
     $$ language plpgsql;
     
    select total_names(list)
    
    
    select * from student 