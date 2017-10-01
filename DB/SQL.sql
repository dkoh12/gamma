
relation(table)
- schema (description)
- instance (data satisfying schema)
attribute (col)
tuple (record, row)

schema is fixed
instance can change.


ACID
Atomicity - each transaction is all or nothing
Consistency - DB will be in valid state. data written is valid
Isolation - concurrent execution results as if transactions were executed serially
Durability - committed transaction will remain so even if DB crashes




CREATE TABLE Sailors (
	sid INTEGER,
	sname CHAR(20),
	rating INTEGER,
	age REAL,
	PRIMARY KEY (sid)
);

CREATE TABLE Boats (
	bid INTEGER,
	bname CHAR(20),
	color CHAR(10),
	PRIMARY KEY (bid)
);

CREATE TABLE Reserves (
	sid INTEGER,
	bid INTEGER,
	day DATE,
	PRIMARY KEY (sid, bid, day),
	FOREIGN KEY (sid) REFERENCES Sailors,
	FOREIGN KEY (bid) REFERENCES Boats
);


INSERT INTO Sailors VALUES
(1, "Fred", 7, 22),
(2, 'Jim', 2, 39);


/* find all 27 year old sailors */
SELECT *
FROM Sailors as S
WHERE S.age = 27;


SELECT [DISTINCT] <expression>
FROM <table>
[WHERE <predicate>]
[GROUP BY <column list>]
	[HAVING <predicate>]
[ORDER BY <col list>] ;


DISTINCT removes duplicates


-- find 10th highest employee salary

SELECT TOP(1) salary 
FROM (
	SELECT DISTINCT TOP(10) salary
	FROM employee
	ORDER BY salary DESC
)
AS Emp
ORDER BY salary

-- OR

SELECT salary
FROM (
	SELECT DISTINCT salary
	FROM employee
	ORDER BY salary
	DESC LIMIT 10
)
AS Emp 
ORDER BY salary LIMIT 1;




SELECT DISTINCT S.name, S.gpa
FROM students S
WHERE S.dept = 'CS'
ORDER BY S.gpa DESC, S.name ASC;


Aggregates: SUM(), COUNT(), MAX(), MIN(), AVG()


SELECT AVG(S.gpa), S.dept
FROM students S
GROUP BY S.dept -- produces aggregate per group
HAVING COUNT(*) > 5; -- only used w/ GROUP BY

SELECT S.dept, AVG(S.gpa), COUNT(*)
FROM students S
WHERE S.gender = 'F'
GROUP BY S.dept
HAVING COUNT(*) > 2
ORDER BY S.dept;

SELECT s.sname
FROM Sailors S, Reserves R
WHERE S.sid = R.sid AND R.bid = 102

SELECT x.sname, x.age, y.sname, y.age
FROM Sailors AS x, Sailors AS y
WHERE x.age > y.age;


WHERE S.sname LIKE 'P_p%' -- compares strings

UNION ALL 
INTERSECT
EXCEPT


-- find sids of sailors who've reserved a red and green boat

SELECT S.sid
FROM Sailors S, Boats B, Reserves R
WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red'

INTERSECT

<same thing above except B.color = 'green'>

OR

SELECT R1.sid
FROM Boats B1, Reserves R1, Boats B2, Reserves R2
WHERE R1.sid = R2.sid AND R1.bid = B1.bid AND R2.bid = B2.bid
AND (B1.color = 'red' AND B2.color = 'green')


-- find sids of sailrs who have not reserved a boat

SELECT S.sid
FROM Sailors S

EXCEPT

SELECT S.sid
FROM Sailors S, Reserves R
WHERE S.sid = R.sid;

-- nested queries

SELECT S.sname
FROM Sailors S
WHERE S.sid IN (NOT IN)
	(SELECT R.sid
	FROM Reserves R
	WHERE R.bid=102)


(EXISTS)
subquery must be recomputed for each Sailors tuple
ANY ALL

-- find sailor with highest rating

SELECT *
FROM Sailors S
WHERE S.rating > ALL
	(SELECT S2.rating
	FROM Sailors S2);

SELECT *
FROM Sailors S
ORDER BY S.rating DESC
LIMIT 1;


True, False, Unknown

From table [INNER | {LEFT | RIGHT | FULL} {OUTER}] JOIN table
ON something

-- inner is default
LEFT OUTER JOIN -- right can have NULL VALUES


CREATE VIEW Redcount
AS SELECT b.bid, COUNT(*) AS scount
	FROM Boats2 b, Reserves2 r
	WHERE r.bid = b.bid AND b.color = 'red'
GROUP BY b.bid

select views on the fly

SELECT bname, scount
from Boads2 b,
	(SELECT b.bid, COUNT(*)
		FROM Boats2 b, Reserves2 r
		WHERE r.bid=b.bid AND b.color='red'
		GROUP BY b.bid) AS Reds(bid, scount)
WHERE Reds.bid=b.bid AND scount < 10;


WITH Reds(bid, scount) AS
	(SELECT b.bid, COUNT(*)
		FROM Boats2 b, Reserves2 r
		WHERE r.bid=b.bid AND b.color='red'
		GROUP BY b.bid) AS Reds(bid, scount)
SELECT bname, scount
FROM Boads2 b, Reds
WHERE Reds.bid=b.bid AND scount < 10; 


integrity constraints
- domain constraints, primary key constraints, foreign key constraints


keys are way to look up associated tuple
set of fields is superkey if no 2 distinct tuples can have same values in all key fields


candidate keys specified using UNIQUE


set of fields is superkey if no 2 distinct typles can have same values in all key fields

set of fields is key for a relation if it is minimal:
- superkey
- no subset of fields is superkey

what if >1 key for relation?
- one key is primary key, others are candidate keys

primary key uniquely identifies each record in DB table
primary keys must contain unique values and not NULL
only 1 primary key of single or multiple fields


foreign key = "logical ptr"
-set of fields in tuple in one relation that refer to tuple in another
reference to primary key of other relation
- used to link 2 tables together


Index is used to retrieve data from DB very fast.
- duplicate values are allowed

CREATE INDEX idx
ON Persons (LastName, FirstName)

updating a table w/ index takes more time than one w/o idnex. 
so only create indexes on columns that will be frequently searched against


purpose of Index & primary key?

think of index in a book.

IN database, index contains a ptr to the row containing the value you are searching for.


in clustered index:
- index data entries are stored in approximate order by value of search keys in data records

only 1 clustered index per table
clustered index is faster than non clustered index
clustered index determines storage order of rows in table







