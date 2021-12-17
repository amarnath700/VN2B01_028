create table car(
Sno integer,
vname varchar,
vni varchar)


insert into car values(2,'volvo', 'ap39 5050');
insert into car values(5,'bmw', 'ap39 0050');
insert into car values(9,'tesla', 'ap39 4050');
insert into car values(13,'jeep', 'ap39 6050');
insert into car values(15,'honda', 'ap39 8050');

select * from car 


create table onroad_price(
sn integer,
bs_price integer,
rto integer,
insurance varchar(50))

insert into onroad_price values(5,200000,5000,'relianc');
insert into onroad_price values(13,20000,2000,'tata');
insert into onroad_price values(1,2000,1000,'paytm');
insert into onroad_price values(7,2000000,4000,'phonepe');

select * from onroad_price 


/*cross join*/


select rto,vname,vni from car cross join onroad_price 

select insurance,vname,vni from car cross join onroad_price

select rto,vname,vni from onroad_price cross join car 


/*inner join*/
select rto,vname,vni from onroad_price inner join car
 on car.sno = onroad_price.sn
 
 
 /* left outer join*/
 
 select rto,vname,vni from onroad_price left outer join car
 on car.sno = onroad_price.sn
 
 
 /*full outer join*/
  select rto,vname,vni from onroad_price full outer join car
 on car.sno = onroad_price.sn
 
 /* right outer join*/
 
  select rto,vname,vni from onroad_price right outer join car
 on car.sno = onroad_price.sn
 
 /*alias*/
  select o.rto,c.vname,c.vni from onroad_price as o, car as c
     where c.sno = o.sn
/* create function*/
 create or replace function name()
 returns varchar(2222) AS $$
 
declare 
      name varchar;
      
begin
select vname into name from car ;
return vname;
end;

$$ language plpgsql;

select name();


end
       






