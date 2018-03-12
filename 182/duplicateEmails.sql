# Write your MySQL query statement below
SELECT Email FROM
(
  SELECT Email, COUNT(1) AS num
  FROM Person
  GROUP BY Email
) AS temp
WHERE num > 1