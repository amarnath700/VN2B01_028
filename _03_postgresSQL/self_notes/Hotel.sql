CREATE TABLE Register(
Name varchar(20),
Room integer,
Phone number,
Proof varchar(20),
ID number,
location varchar(2)
);


SELECT * FROM Register 

ALTER TABLE Register ADD COLUMN time varchar(2),
ALTER TABLE Register ADD COLUMN signature varchar



INSERT INTO Register VALUES('Amarnath',101,'8892467674','adhar Card','913750677215','anantapur','11:30','AMAR');
INSERT INTO Register VALUES('viveka',103,'5555555555','pancard','32456','bengalore','15:25','viv');
INSERT INTO Register VALUES('vani',212,'6546484914','Driving Licence','254898955','tadipatri','09:45','vani');
INSERT INTO Register VALUES('shanwik',565,'7894561235','passport','7898564','Belgaum','7:35','shanwik');
INSERT INTO Register VALUES('chandra',883,'','voter id','5465645','chirala','00:10','chand');

DELETE FROM Register WHERE location='tadipatri';

UPDATE Register SET phone='4567899638' WHERE Room=883;

CREATE TABLE Register1 as select* FROM Register 

select * FROM Register1 

update Register1 set time='' WHERE signature='AMAR';

DROP table Register 

