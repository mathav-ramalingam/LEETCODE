-- Method1
-- SELECT name as Customers
-- FROM Customers 
-- WHERE id NOT IN (SELECT customerId FROM Orders)


-- method 2
SELECT c.name as Customers
FROM Customers as c
LEFT JOIN Orders as o
ON c.id = o.customerId
WHERE o.id IS NULL