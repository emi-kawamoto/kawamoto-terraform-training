SELECT
event_date,
count(1) AS user_counts
FROM `flinters-base-education.analytics_282778073.events_*`
WHERE _TABLE_SUFFIX BETWEEN FORMAT_TIMESTAMP("%Y%m%d",CURRENT_DATE('Asia/Tokyo')-7) AND FORMAT_TIMESTAMP("%Y%m%d",CURRENT_DATE('Asia/Tokyo'))
AND event_name = 'page_view'
GROUP BY event_date
ORDER BY event_date