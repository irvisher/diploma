Задание 1
SELECT login, COUNT ("Orders".id) FROM "Couriers"
JOIN "Orders"
ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery"
GROUP BY "Couriers".id;
или
SELECT c.login,
COUNT(o.id) FROM "Couriers" AS c
LEFT OUTER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true GROUP BY c.login;
Задание 2
SELECT track,
CASE WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
END AS order_status FROM "Orders";