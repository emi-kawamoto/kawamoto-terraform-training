SELECT COALESCE(CONCAT(CAST(m AS CHAR), "+", CAST(n AS CHAR)), 0) AS "m+n"
from `SampleMath`; 
