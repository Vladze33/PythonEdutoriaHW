SELECT min(unit_price) AS min_price FROM products p
WHERE p.category_id = 1;

-- |min_price|
-- |---------|
-- |4,5      |

-- Если самых дешевых товаров несколько и нужно узнать их наименования
-- SELECT product_name, unit_price AS min_price FROM products p
-- WHERE p.category_id = 1 AND unit_price IN
-- (
-- 	SELECT
-- 		min(unit_price) AS min_price
-- 	FROM
-- 		products p2
-- 	WHERE
-- 		p2.category_id = p.category_id
-- );