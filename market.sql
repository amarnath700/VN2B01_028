create table market(
shop serial primary key,
name varchar,
area integer);

insert into market(name,area) values('Gubber',220);
insert into market(name,area) values('Rubber',20);
insert into market(name,area) values('Aubber',2120);
insert into market(name,area) values('Subber',320);
insert into market(name,area) values('Mubber',10);
insert into market(name,area) values('Jubber',267);


select * from market 

create table market1(
sno serial primary key,
shop integer,
seeds varchar not null,
q_tons integer,
price float,
constraint market
foreign key(shop)
references market(shop)
on delete set null
);

insert into market1(shop,seeds,q_tons,price) values(3,'groundnuts',55,23566.88);
insert into market1(shop,seeds,q_tons,price) values(2,'wheat',45,23566.88);
insert into market1(shop,seeds,q_tons,price) values(1,'maize',35,2566.88);
insert into market1(shop,seeds,q_tons,price) values(6,'paddy',25,2366.88);
insert into market1(shop,seeds,q_tons,price) values(5,'dal',15,2356.88);
insert into market1(shop,seeds,q_tons,price) values(4,'peanuts',52,3566.88);

select * from market1 





