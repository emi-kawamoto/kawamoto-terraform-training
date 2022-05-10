SELECT 
    u.id, 
    name, 
    SUM(impressions) AS impressions_total 
FROM users AS u
    LEFT JOIN activity_reports AS a_r 
    ON u.id = a_r.user_id 
GROUP BY 
    u.id,
    name
;