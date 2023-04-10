-- 演習1

SELECT
    shohin_id,
    shohin_mei,
    hanbai_tanka
FROM
    Shohin
UNION ALL
SELECT
    shohin_id,
    shohin_mei,
    hanbai_tanka
FROM
    Shohin2
ORDER BY
    hanbai_tanka DESC
;

-- 演習2

-- enshu-day3-q2.md に記載

-- 演習3

SELECT
    employees.company_id,
    employees.employee_id,
    employees.employee_name,
    CASE WHEN child_cnt IS NULL THEN 0 ELSE child_cnt END AS child_cnt
FROM employees
Left JOIN
    (
        SELECT
            company_id,
            employee_id,
            COUNT(company_id) AS child_cnt
        FROM
            children
        GROUP BY company_id, employee_id
    ) AS child_cnts
    ON employees.company_id = child_cnts.company_id
    AND employees.employee_id = child_cnts.employee_id
;