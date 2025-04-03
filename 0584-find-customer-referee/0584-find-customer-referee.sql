# Write your MySQL query statement below


SELECT name FROM CUSTOMER WHERE id  not in (select id from customer

where REFEREE_ID = '2');