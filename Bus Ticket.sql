CREATE table Busticket(
Name varchar(10),
Age integer,
Gender varchar)

select * FROM Busticket

INSERT INTO Busticket VALUES('Siva',60,'Male');
INSERT INTO Busticket VALUES('Passana',23,'Female');
INSERT INTO Busticket VALUES('Venu',49,'Male');
INSERT INTO Busticket VALUES('Abdul',31,'Male');
INSERT INTO Busticket Values('Sneha',08,'Female');

DELETE FROM Busticket where Name='Abdul';

ALTER TABLE Busticket ADD COLUMN seatno integer
ALTER TABLE Busticket ADD COLUMN berth varchar
ALTER TABLE Busticket ADD COLUMN id integer
ALTER TABLE Busticket ADD COLUMN boarding varchar;

UPDATE Busticket Set seatno=03,berth='Upper',id=256456,boarding='Hanumanpet' WHERE Age=49
UPDATE Busticket Set seatno=08,berth='Lower',id=698899,boarding='Rajajinagar' WHERE Name='Siva';
UPDATE Busticket Set seatno=22,berth='Lower',id=888559,boarding='Tirupathi' WHERE Name='Passana';
UPDATE Busticket Set seatno=17,berth='Upper',id=859584,boarding='Suryapet' WHERE Age=08;

INSERT INTO Busticket VALUES('Deppa',33,'Female',21,'Lower','955454','Hyderabad') 

Create table Trainticket as select * FROM Busticket 

select * from Trainticket 

