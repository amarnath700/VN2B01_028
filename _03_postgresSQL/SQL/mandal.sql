create table mandal_population(
village"Name"  varchar,
mens number,
womens number,
kids number
);


insert into mandal_population values('whitefield', 212,290,500);
insert into mandal_population values('brookfield', 152,211,350);
insert into mandal_population values('marthalli', 2221,1900,6500);
insert into mandal_population values('kr puram', 22,29,50);
insert into mandal_population values('tadipatri', 2012,3290,4500);
insert into mandal_population values('anantapur', 2132,2090,5050);

select * from mandal_population 

alter table mandal_population add column total float;

update mandal_population set total=25.9 where kids=5050;
update mandal_population set total=95.9 where mens=2221;


delete from mandal_population where womens=29


