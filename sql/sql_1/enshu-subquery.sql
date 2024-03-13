演習1
SELECT                                                                                       ->   company_id, employee_id, employee_name,
    ->     (
    ->     SELECT COUNT(*)
    ->     FROM
    ->       children
    ->     WHERE
    ->       children.employee_id = employees.employee_id
    ->     )
    ->     AS
    ->       child_cnt
    ->   FROM
    ->     employees
    -> ;
