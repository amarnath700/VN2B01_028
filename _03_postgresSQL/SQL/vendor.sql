CREATE table Vendor(
Name varchar,
Designation varchar,
leve integer,
salary number,
company varchar
);
drop table Vendor 
select * from Vendor 

INSERT INTO Vendor VALUES('AMARNATH','TECHNICAL FIELD ENGGINEER',2,'25000','QUADGEN');
INSERT INTO Vendor VALUES('SHANWIK','ADMIN',1,'15600','INFOSYS');
INSERT INTO Vendor VALUES('VANI','IT REQUITER',3,'80000','CIGNEX');

INSERT INTO Vendor VALUES('CHANDRA','TEAM LEADER',5,'150000','PUMA');
INSERT INTO Vendor VALUES('VIJAYA','CEO','','555555','IGATE');


ALTER TABLE Vendor ADD COLUMN Experience varchar

UPDATE Vendor SET Experience='5years' where leve=3;
UPDATE Vendor set Experience='1.5years' where leve=1
CREATE TABLE Vendor1 as select * from vendor
select * from vendor1

DROP TABLE Vendor