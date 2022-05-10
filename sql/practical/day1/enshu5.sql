WITH follows_count AS (
    SELECT 
        floor(age / 10) AS age_group,
        count(f.follower_id) AS count 
    FROM 
        users AS u 
        LEFT JOIN follows AS f 
          ON u.id = f.follower_id 
        GROUP BY u.id
)

SELECT 
    concat(age_group * 10, '代') AS age_group,
    AVG(count) AS avg_count 
FROM 
    follows_count
GROUP BY 
    age_group
;