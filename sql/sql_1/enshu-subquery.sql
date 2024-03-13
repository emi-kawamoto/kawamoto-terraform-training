演習1
SELECT
   company_id, employee_id, employee_name,
    (
   SELECT COUNT(*)
   FROM
   children
   WHERE
   (children.employee_id = employees.employee_id AND children.company_id = employees.company_id)
   )
   AS
   children_cnt
FROM
employees
;