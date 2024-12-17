SELECT supplier_id, max(unit_price) AS max_price FROM products p
WHERE p.supplier_id IN (1, 3, 5)
GROUP BY p.supplier_id
ORDER BY p.supplier_id ASC;

-- |supplier_id|max_price|
-- |-----------|---------|
-- |1          |19       |
-- |3          |40       |
-- |5          |38       |