SELECT c.login,
       COUNT(*)
FROM "Orders" AS o
LEFT OUTER JOIN "Couriers" AS c ON o."courierId" = c.id
WHERE o."inDelivery" = TRUE
GROUP BY c.login;