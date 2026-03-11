-- create DATABASE oraclesql;
-- USE oraclesql;
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL),
NAME varchar(20) NOT NULL , 
AGE Number , 
GENDER varchar(100) DEFAULT 'Male' NOT NULL,
EMAIL varchar(100) DEFAULT 'UNKNOWN' UNIQUE NOT NULL ,
MARKS Number(4,2) CHECK(MARKS>=0),
date_depart DATE DEFAULT SYSDATE,
date_arrival timestamp DEFAULT SYSTIMESTAMP
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL),
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE Student 
(
ROLL Number PRIMARY KEY ,
NAME varchar(20) NOT NULL ,
DOB DATE NOT NULL ,
GENDER varchar(10) NOT NULL ,
CLASS varchar(10) NOT NULL ,
COLLEGE varchar(50) NOT NULL,
CITY varchar(50) NOT NULL ,
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
insert into Student
values
(1,'Aarpit',to_date('2000-01-15','yyyy-mm-dd'),'Male','12th','ABC College','New York',95.5);
insert into Student
values
(2,'Bella',to_date('2001-05-22','yyyy-mm-dd'),'Female','12th','XYZ College','Los Angeles',88.0);
insert into Student
values
(3,'Charlie',to_date('1999-11-30','yyyy-mm-dd'),'Male','12th','LMN College','Chicago',92.3);
insert into Student
values
(4,'Diana',to_date('2000-07-18','yyyy-mm-dd'),'Female','12th','PQR College','Houston',85.7);
insert into Student
values
(5,'Ethan',to_date('2001-03-25','yyyy-mm-dd'),'Male','12th','DEF College','Miami',78.9);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON DELETE CASCADE,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON DELETE SET NULL,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON DELETE NO ACTION,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON DELETE RESTRICT,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON UPDATE RESTRICT,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON UPDATE CASCADE,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON UPDATE SET NULL,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
ID Number REFERENCES student(ROLL) ON UPDATE NO ACTION,
NAME varchar(20) NOT NULL , 
MARKS Number(4,2) CONSTRAINT mycheckconstraint CHECK(MARKS>=0)
);
create TABLE student
(
ROLL Number PRIMARY KEY , 
NAME varchar(20)  , 
MARKS Number(4,2)
);
create TABLE student
(
ROLL Number PRIMARY KEY, 
NAME varchar(20)  CONSTRAINT myuniqueconstraint UNIQUE, 
MARKS Number(4,2)
);
create TABLE student
(
ROLL Number PRIMARY KEY, 
NAME varchar(20)  CONSTRAINT mynotnullconstraint NOT NULL, 
MARKS Number(4,2)
);
create TABLE student
(
ROLL Number PRIMARY KEY, 
ID Number ,
NAME varchar(20) , 
MARKS Number(4,2)
);
create TABLE Emp
(
EMP_NO int PRIMARY KEY,
EMP_NAME varchar(20) NOT NULL,
DOB varchar(20) ,
SALARY Number(10,2) ,
COMMISION Number(10,2) ,
DEPT_NO NUMBER(10,2)
);
INSERT INTO Emp
VALUES
(1, 'John Doe', '1980-05-15', 50000, 5000, 10);
INSERT INTO Emp
VALUES
(2, 'Jane Smith', '1990-08-22', 60000, 6000, 20);
INSERT INTO Emp
VALUES
(3, 'Alice Johnson', '1985-12-03', 55000, 5500, 10);
INSERT INTO Emp
VALUES
(4, 'Bob Brown', '1978-03-30', 70000, 7000, 30);
create TABLE student
(
s int ,
p int
);
insert into student
values
(
5,6
);
insert into student(ROLL,ID)
values
(
2,15
);
insert into student(ROLL,MARKS)
values
(
3,45
);
insert into student(ROLL)
values
(
1
);
insert into student(ROLL)
values
(
1
);
insert into student(ROLL,NAME)
values
(
1,null
);
insert into student(ROLL,NAME)
values
(
2,'Aarpit'
);
insert into student
values
(
    1,null, 'Aarpit',5
);
insert into student
values
(
    2,1, 'fr',4
);
insert into student
values
(
    3,2, 'ff',6
);
insert into student
values
(
    4,2, 'fr',7
);
insert into student
values
(
    5,4, 'ft',8
);
insert into student(ROLL,ID,NAME) select ROLL,ID,NAME from student; -- Self Join To Insert Data From Same Table
drop TABLE student;
truncate TABLE student;
select * from student;
select * from student ORDER BY MARKS ASC;
select * from student ORDER BY MARKS DESC;
select ROLL, NAME, CLASS from student where CITY = 'New York';
select
(select count(*) from emp) as TOTAL_EMPLOYEES,(select count(*) from dept) as TOTAL_DEPARTMENTS;
select SUM(MARKS) from student;
select AVG(MARKS) from student;
select MIN(MARKS) from student;
select MAX(MARKS) from student;
select COUNT(MARKS) from student;
select COUNT(DISTINCT MARKS) from student;
select COUNT(*) from student;
select COUNT(1) from student;
select 12 + 13 as "result" from dual;
select s + p as "sum" from student;
select sysdate from dual;
select sysdate + 5 from dual;
select sysdate - 5 from dual;
select to_char(sysdate,'yyyysp'),to_char(sysdate,'day') from dual;
select to_char(sysdate,'day')from dual;
select to_char(sysdate,'yyyysp'),to_char(sysdate,'day') from dual;
select to_char(sysdate,'ddsp')from dual;
select to_char(sysdate,'am')from dual;
select next_day(sysdate,'Friday')from dual;
select add_months(sysdate,5)from dual;
select months_between(to_date('2024-12-31','yyyy-mm-dd'),to_date('2024-01-01','yyyy-mm-dd'))from dual;
select round(12.5678,2)from dual;
select ceil(12.34)from dual;
select floor(12.78)from dual;
select mod(10,3)from dual;
select power(2,3)from dual;
select sqrt(16)from dual;
select round(5.6)from dual;
select length('Aarpit')from dual;
select instr('Aarpit','p')from dual;
select substr('Aarpit',2,3)from dual;
select lower('AARPIT')from dual;
select upper('aarpit')from dual;
select replace('Aarpit Aarpit','A','X')from dual;
select concat('Aarpit',' Kumar')from dual;
select round(sysdate + 15,'month') from dual;
select trunc(sysdate,'month') from dual;
select trunc(sysdate,'year') from dual;
select round(sysdate,'year') from dual;
select to_char(sysdate+3,'day')from dual;
DESC student;
select * from USER_CONSTRAINTS WHERE TABLE_NAME = 'STUDENT';
select * from USER_CONS_COLUMNS WHERE TABLE_NAME = 'STUDENT';
select NAME, ROLL from student;
select NAME, GENDER from student where ROLL = 1;
SELECT NAME, GENDER FROM student WHERE ROLL IN (1, 2, 5);
SELECT NAME, GENDER FROM student WHERE ROLL = 1 OR ROLL = 2 OR ROLL = 5;
SELECT NAME, GENDER FROM student WHERE ROLL = 1 AND AGE = 20;
SELECT NAME, GENDER FROM student WHERE NOT ROLL = 1 OR AGE = 20;
SELECT NAME, GENDER FROM student WHERE NOT ROLL = 1 AND AGE = 20;
-- BETWEEN and AND are inclusive they include the boundary values.
-- PRECEDENCE: - NOT > Comparison Operators > AND > OR
-- PRECEDENCE: - FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY
-- PRECEDENCE: - GROUP BY does left to rigth associativity
SELECT NAME, GENDER FROM student WHERE ROLL NOT IN (1, 2, 5);
SELECT NAME, AGE FROM student WHERE AGE BETWEEN 18 AND 22;
SELECT NAME, AGE FROM student WHERE AGE NOT BETWEEN 18 AND 22;
SELECT NAME FROM student WHERE EMAIL LIKE '%@gmail.com';
SELECT NAME FROM student WHERE NAME LIKE 'A%';
SELECT NAME FROM student WHERE NAME NOT LIKE 'A%';
-- REGEXP_LIKE Function (For Advanced Pattern Matching): -
-- Purpose: Matches a string against a regular expression pattern
-- 1) ^  → Start of string
-- Purpose: Checks if value starts with a specific character
-- Example: Name starts with 'A' or 'a'
REGEXP_LIKE(ename, '^a', 'i');
-- 2) $  → End of string
-- Purpose: Checks if value ends with a specific character
-- Example: Name ends with 'A' or 'a'
REGEXP_LIKE(ename, 'a$', 'i');
-- 3) .  → Any single character
-- Purpose: Matches exactly one character
-- Example: Second character is 'B' or 'b'
REGEXP_LIKE(ename, '^.b', 'i');
-- 4) *  → Zero or more occurrences
-- Purpose: Matches preceding character 0 or more times
-- Example: Name starts with A followed by anything
REGEXP_LIKE(ename, '^a.*', 'i');
-- 5) +  → One or more occurrences
-- Purpose: At least one occurrence required
-- Example: Name contains at least one 'a'
REGEXP_LIKE(ename, 'a+', 'i');
-- 6) ?  → Zero or one occurrence
-- Purpose: Optional character
-- Example: Matches 'color' or 'colour'
REGEXP_LIKE(word, 'colou?r');
-- 7) [abc]  → Any one character from list
-- Purpose: Match one character from given set
-- Example: Name contains a, b, or c
REGEXP_LIKE(ename, '[abc]', 'i');
-- 8) [a-z]  → Character range
-- Purpose: Match any lowercase letter
-- Example: Name contains any lowercase letter
REGEXP_LIKE(ename, '[a-z]');
-- 9) [^abc] → NOT these characters
-- Purpose: Match characters except listed ones
-- Example: Name has characters other than a, b, c
REGEXP_LIKE(ename, '[^abc]', 'i');
-- 10) |  → OR operator
-- Purpose: Match either left or right pattern
-- Example: Name starts with A OR ends with Z
REGEXP_LIKE(ename, '^a|z$', 'i');
-- 11) ()  → Grouping
-- Purpose: Groups patterns together
-- Example: Name starts with A or B
REGEXP_LIKE(ename, '^(a|b)', 'i');
-- 12) .*  → Any characters (most common)
-- Purpose: Match anything (0 or more chars)
-- Example: Name contains two A's (at least)
REGEXP_LIKE(ename, 'a.*a', 'i');
-- 13) {n} → Exact count
-- Purpose: Match exactly n times
-- Example: Name contains exactly 2 digits
REGEXP_LIKE(code, '[0-9]{2}');
-- 14) {n,} → At least n times
-- Purpose: Minimum occurrence
-- Example: Name has at least 3 letters
REGEXP_LIKE(ename, '[a-z]{3,}', 'i');
-- 15) {n,m} → Between n and m times
-- Purpose: Range of occurrence
-- Example: Name length between 3 and 5
REGEXP_LIKE(ename, '^[a-z]{3,5}$', 'i');
-- 16) \d → Digit (0–9)
-- Purpose: Matches numeric digit
-- Example: Value contains a digit
REGEXP_LIKE(col, '\d');
-- 17) \D → Non-digit
-- Purpose: Matches non-numeric character
-- Example: Name contains non-digit
REGEXP_LIKE(ename, '\D');
-- 18) \w → Word character (A–Z, a–z, 0–9, _)
-- Purpose: Matches alphanumeric characters
-- Example: Username validation
REGEXP_LIKE(username, '^\w+$');
-- 19) \W → Non-word character
-- Purpose: Matches special characters
-- Example: Name contains special symbol
REGEXP_LIKE(ename, '\W');
-- 20) \s → Whitespace
-- Purpose: Matches space or tab
-- Example: Value contains space
REGEXP_LIKE(col, '\s');
-- 21) \S → Non-whitespace
-- Purpose: Matches non-space character
-- Example: Value has no spaces
REGEXP_LIKE(col, '^\S+$');
-- 22) (?i) → Case-insensitive matching
-- Purpose: Ignore case in matching
-- Example: Name contains 'abc' in any case
REGEXP_LIKE(ename, '(?i)abc');
-- 23) (?m) → Multi-line mode
-- Purpose: ^ and $ match start/end of lines
-- Example: Value has lines starting with 'A'
REGEXP_LIKE(col, '(?m)^A');
-- 24) (?s) → Dot matches newline
-- Purpose: . matches all characters including newline
-- Example: Value contains 'A' followed by anything including newlines
REGEXP_LIKE(col, '(?s)A.*B');
-- 25) \A → Start of string
-- Purpose: Matches only at the beginning of the string
-- Example: Value starts with 'Start'
REGEXP_LIKE(col, '\AStart');
-- 26) \Z → End of string
-- Purpose: Matches only at the end of the string
-- Example: Value ends with 'End'
REGEXP_LIKE(col, 'End\Z');
-- 27) \b → Word boundary
-- Purpose: Matches position between word and non-word character
-- Example: Value contains the word 'cat'
REGEXP_LIKE(col, '\bcat\b');
-- 28) \B → Non-word boundary
-- Purpose: Matches position not at a word boundary
-- Example: Value has 'cat' as part of another word
REGEXP_LIKE(col, '\Bcat\B');
-- 29) -- Up to 3 digits
REGEXP_LIKE(col, '[0-9]{,3}');

-- Distinct Values
SELECT DISTINCT AGE FROM student;
SELECT NAME FROM student WHERE AGE IS NULL;
-- Intersection Without INTERSECT Keyword
SELECT col
FROM A
WHERE col IN (SELECT col FROM B);
-- Union Without UNION Keyword
SELECT col FROM A
UNION
SELECT col FROM B
WHERE col NOT IN (SELECT col FROM A);
-- Difference
SELECT col
FROM A
WHERE col NOT IN (SELECT col FROM B);
 -- Or
SELECT col FROM A
MINUS
SELECT col FROM B;
-- Symmetric Difference
-- Simple
(SELECT * FROM A MINUS SELECT * FROM B)
UNION
(SELECT * FROM B MINUS SELECT * FROM A);
-- Or
SELECT col FROM A
WHERE col NOT IN (SELECT col FROM B)
UNION
SELECT col FROM B
WHERE col NOT IN (SELECT col FROM A);
-- Exists
SELECT *
FROM A a
WHERE EXISTS (SELECT 1 FROM B b WHERE b.col = a.col);
-- Not Exists
SELECT *
FROM A a
WHERE NOT EXISTS (SELECT 1 FROM B b WHERE b.col = a.col);
-- Correlated Subquery
SELECT *
FROM A a
WHERE a.col > (SELECT AVG(col) FROM B b);
-- Inserting Data Using Subquery
INSERT INTO A (col)
SELECT col FROM B WHERE condition;
-- Updating Data Using Subquery
UPDATE A
SET col = (SELECT MAX(col) FROM B)
WHERE condition;
-- Deleting Data Using Subquery
DELETE FROM A
WHERE col IN (SELECT col FROM B WHERE condition);
ROLLBACK;
-- Gets the total number of students and their average marks
-- SELECT COUNT(ROLL) AS 'TotalStudents', AVG(MARKS) AS 'AverageMarks' FROM student;

-- SELECT NAME, MARKS,
-- CASE 
--     WHEN MARKS >= 90 THEN 'Excellent'
--     WHEN MARKS >= 75 THEN 'Good'
--     ELSE 'Average'
-- END AS Grade
-- FROM student;

-- SELECT NAME, MARKS FROM student1 
-- WHERE MARKS > 80 
-- ORDER BY MARKS DESC LIMIT 5;

-- SELECT NAME FROM Sports_Club
-- INTERSECT
-- SELECT NAME FROM Music_Club;
delete from student;
delete from student where ROLL = 1;
delete from student where MARKS < 90;
delete from STUDENT where CITY = 'New York';
update student set ROLL = 2 where ROLL = 1;
update student set NAME = 'Welak' where ROLL = 1;
update student set NAME = 'Welak';
update student set NAME = 'Welak' where AGE = 20;
update STUDENT set MARKS = 89 where ROLL = 2;
update STUDENT set CITY = 'San Francisco', NAME = 'Welak' where ROLL = 2;
update student set EXPERIENCE = 5.6 where ROLL = 1;
alter TABLE student ADD EXPERIENCE Number(2,1);
alter TABLE student MODIFY GENDER varchar(200);
alter TABLE student DROP COLUMN GENDER;
alter TABLE student DROP PRIMARY KEY;
alter TABLE student ADD UNIQUE(ROLL);
alter TABLE student ADD PRIMARY KEY(ROLL);
alter TABLE student DISABLE PRIMARY KEY;
alter TABLE student ENABLE PRIMARY KEY;
alter TABLE student ADD CONSTRAINT my_fk FOREIGN KEY (ID) REFERENCES student(ROLL);
alter TABLE student DROP CONSTRAINT my_fk;
alter TABLE student DISABLE CONSTRAINT my_fk;
alter TABLE student ENABLE CONSTRAINT my_fk;
alter TABLE student DISABLE CONSTRAINT myuniqueconstraint;
alter TABLE student ENABLE CONSTRAINT myuniqueconstraint;
alter TABLE student DISABLE CONSTRAINT mynotnullconstraint;
alter TABLE student ENABLE CONSTRAINT mynotnullconstraint;
alter TABLE student MODIFY NAME NOT NULL;
alter TABLE student MODIFY NAME NULL;
alter TABLE student MODIFY MARKS DEFAULT 0;
ALTER TABLE student ADD EXPERIENCE1 NUMBER(4,2) DEFAULT 0;
alter TABLE student MODIFY MARKS DEFAULT NULL;
alter TABLE student ADD CONSTRAINT mycheckconstraint CHECK (MARKS >=0);
alter TABLE student DROP CONSTRAINT mycheckconstraint;
alter TABLE student RENAME COLUMN EXPERIENCE TO WORK_EXPERIENCE;
alter TABLE student RENAME TO student1;

-- GRANT SELECT, UPDATE ON student TO 'guest_user';
-- REVOKE UPDATE ON student FROM 'guest_user';

-- START TRANSACTION;
-- DELETE FROM student WHERE ROLL = 5;
-- SAVEPOINT after_delete;             -- Set a checkpoint
-- UPDATE student SET MARKS = 100;     -- Whoops, I shouldn't have done this!
-- ROLLBACK TO after_delete;           -- Undo just the update, keep the delete
-- COMMIT;                             -- Save the final result

-- MERGE INTO student AS target
-- USING new_data AS source
-- ON (target.ROLL = source.ROLL)
-- WHEN MATCHED THEN
    -- UPDATE SET target.MARKS = source.MARKS -- Update existing student marks
-- WHEN NOT MATCHED THEN
    -- INSERT (ROLL, NAME, MARKS) 
    -- VALUES (source.ROLL, source.NAME, source.MARKS); -- Insert new students




-- Now Entire Above Code With . Operator Used(Only The Ones With Changes Mentioned): -
-- 3 to 18 and line 51, 53 to 62 lines remain same(. Not Supported for them)
-- 19 to 50 lines and line 52, 64 to 78 lines updated code: -

-- SELECT s.* FROM student s;
-- SELECT s.NAME, s.ROLL FROM student s;
-- SELECT s.NAME, s.GENDER FROM student s WHERE s.ROLL = 1;
-- SELECT s.NAME, s.GENDER FROM student s WHERE s.ROLL IN (1, 2, 5);
-- SELECT s.NAME, s.GENDER FROM student s WHERE s.ROLL NOT IN (1, 2, 5);
-- SELECT s.NAME, s.AGE FROM student s WHERE s.AGE BETWEEN 18 AND 22;
-- SELECT s.NAME FROM student s WHERE s.EMAIL LIKE '%@gmail.com';
-- SELECT s.NAME FROM student s WHERE s.NAME LIKE 'A%';
-- SELECT DISTINCT s.AGE FROM student s;
-- SELECT s.NAME FROM student s WHERE s.AGE IS NULL;

-- Gets the total number of students and their average marks
-- SELECT COUNT(s.ROLL) AS TotalStudents, AVG(s.MARKS) AS AverageMarks FROM student s;

-- SELECT s.NAME, s.MARKS,
-- CASE 
--     WHEN s.MARKS >= 90 THEN 'Excellent'
--     WHEN s.MARKS >= 75 THEN 'Good'
--     ELSE 'Average'
-- END AS Grade
-- FROM student s;

-- SELECT s1.NAME, s1.MARKS FROM student1 s1 
-- WHERE s1.MARKS > 80 
-- ORDER BY s1.MARKS DESC LIMIT 5;

--(INTERSECT,UNION and EXCEPT are Multi - Table Operations):-

-- SELECT sc.NAME FROM Sports_Club sc
-- INTERSECT
-- SELECT mc.NAME FROM Music_Club mc;

-- SELECT s.NAME FROM student s
-- UNION
-- SELECT sc.NAME FROM Sports_Club sc;

-- SELECT s.NAME FROM student s
-- EXCEPT
-- SELECT sc.NAME FROM Sports_Club sc;

-- In WHERE
-- SELECT s.NAME, s.MARKS 
-- FROM student s 
-- WHERE s.MARKS > (SELECT AVG(s2.MARKS) FROM student s2);

-- In FROM(Derived Table)
-- SELECT Temp.NAME, Temp.MARKS
-- FROM (SELECT s.NAME, s.MARKS FROM student s WHERE s.AGE > 18) AS Temp;

-- In HAVING 
-- SELECT s.GENDER, AVG(s.MARKS) 
-- FROM student s 
-- GROUP BY s.GENDER 
-- HAVING AVG(s.MARKS) > (SELECT AVG(s2.MARKS) FROM student s2);


-- DELETE FROM student s WHERE s.ROLL = 1;
-- UPDATE student s SET s.NAME = 'Welak' WHERE s.ROLL = 1;
-- UPDATE student s SET s.NAME = 'Welak';
-- UPDATE student s SET s.NAME = 'Welak' WHERE s.AGE = 20;
-- UPDATE student s SET s.EXPERIENCE = 5.6 WHERE s.ROLL = 1;

-- START TRANSACTION;
-- DELETE FROM student s WHERE s.ROLL = 5;
-- SAVEPOINT after_delete;             
-- UPDATE student s SET s.MARKS = 100;     
-- ROLLBACK TO after_delete;           
-- COMMIT;  

-- MERGE INTO student AS target
-- USING new_data AS source
-- ON (target.ROLL = source.ROLL)
-- WHEN MATCHED THEN
--     UPDATE SET target.MARKS = source.MARKS
-- WHEN NOT MATCHED THEN
--     INSERT (ROLL, NAME, MARKS) 
--     VALUES (source.ROLL, source.NAME, source.MARKS);

-- More Multi - Table Operations: -
-- Let's Create Another Table First: -

-- CREATE TABLE course_enrollment (
--     ENROLL_ID Number PRIMARY KEY,
--     STUDENT_ROLL Number, -- This links to student.ROLL (Foreign Key)
--     COURSE_NAME varchar(50),
--     FEES Number(10,2)
-- );
-- -- Adding data to link with your existing student (Aarpit, ROLL 1)
-- INSERT INTO course_enrollment VALUES (101, 1, 'Java Full Stack', 5000.00);
-- INSERT INTO course_enrollment VALUES (102, 1, 'Data Science', 7000.00);
-- INSERT INTO course_enrollment VALUES (103, 2, 'Python AI', 6000.00); -- ROLL 2 doesn't exist yet

-- -- INNER JOIN: Only shows students who have enrolled in a course
-- SELECT s.NAME, c.COURSE_NAME 
-- FROM student s
-- INNER JOIN course_enrollment c ON s.ROLL = c.STUDENT_ROLL;
-- -- LEFT JOIN: Shows ALL students, even those with NO courses (course columns will be NULL)
-- SELECT s.NAME, c.COURSE_NAME 
-- FROM student s
-- LEFT JOIN course_enrollment c ON s.ROLL = c.STUDENT_ROLL;
-- -- RIGHT JOIN: Shows ALL courses, even if no matching student exists
-- SELECT s.NAME, c.COURSE_NAME 
-- FROM student s
-- RIGHT JOIN course_enrollment c ON s.ROLL = c.STUDENT_ROLL;
-- -- CROSS JOIN: Every student paired with every course (Cartesian Product)
-- SELECT s.NAME, c.COURSE_NAME FROM student s CROSS JOIN course_enrollment c;
-- -- SELF JOIN: Joining a table to itself, often used for hierarchical data
-- -- Code Below Is Not For This Another Table just assume it as an example: -
-- -- Assume 'MENTOR_ID' column exists in student table referring to another student's ROLL
-- SELECT s.NAME AS Student, m.NAME AS Mentor
-- FROM student s
-- JOIN student m ON s.MENTOR_ID = m.ROLL;

-- -- GROUP BY and HAVING: -
-- -- Used for summarizing data (counting, averaging). HAVING is like a WHERE clause but for groups
-- -- Finds total fees paid by each student, but only shows students who paid more than 6000
-- SELECT STUDENT_ROLL, SUM(FEES) AS Total_Paid
-- FROM course_enrollment
-- GROUP BY STUDENT_ROLL
-- HAVING SUM(FEES) > 6000;

-- -- Window Functions: -
-- -- Window functions perform calculations across rows that are related to the current row, without collapsing them into a single line
-- -- RANKING: Ranks students based on MARKS from highest to lowest
-- SELECT NAME, MARKS,
-- RANK() OVER (ORDER BY MARKS DESC) AS Student_Rank,
-- DENSE_RANK() OVER (ORDER BY MARKS DESC) AS Dense_Rank -- No gaps in ranking
-- FROM student;

-- -- LEAD/LAG: Compare current student's marks with the one ranked just below them
-- SELECT NAME, MARKS,
-- LEAD(MARKS) OVER (ORDER BY MARKS DESC) AS Next_Highest_Mark
-- FROM student;

-- -- CTE's: -
-- -- A CTE is a temporary result set that you can reference within another statement. It makes complex queries much cleaner
-- -- This CTE first calculates total fees, then we join it to the student names
-- WITH Student_Fees_CTE AS (
--     SELECT STUDENT_ROLL, SUM(FEES) AS Total_Spent
--     FROM course_enrollment
--     GROUP BY STUDENT_ROLL
-- )
-- SELECT s.NAME, f.Total_Spent
-- FROM student s
-- JOIN Student_Fees_CTE f ON s.ROLL = f.STUDENT_ROLL;

-- -- Recursive CTE's: -
-- -- Example: Finding the hierarchy level of mentors
-- WITH RECURSIVE MentorHierarchy AS (
--     -- Anchor member: The top-level mentors (those without a mentor)
--     SELECT s.ROLL, s.NAME, 0 AS Level
--     FROM student s
--     WHERE s.MENTOR_ID IS NULL
--     UNION ALL
--     -- Recursive member: Join the table with the CTE to find the next level
--     SELECT s.ROLL, s.NAME, mh.Level + 1
--     FROM student s
--     JOIN MentorHierarchy mh ON s.MENTOR_ID = mh.ROLL
-- )
-- SELECT * FROM MentorHierarchy;


