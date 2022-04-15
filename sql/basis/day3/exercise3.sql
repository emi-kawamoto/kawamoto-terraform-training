SELECT e.company_id, e.employee_id, employee_name, coalesce(child, 0)
FROM employees as e
  LEFT OUTER join
  (  
  SELECT company_id, employee_id, count(child) as child
  FROM children
  GROUP BY company_id, employee_id
  ) as c
ON
e.employee_id = c.employee_id AND
e.company_id = c.company_id;
