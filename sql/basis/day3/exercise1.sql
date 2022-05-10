SELECT shohin_id, shohin_mei, hanbai_tanka
FROM `Shohin`
union ALL
SELECT shohin_id, shohin_mei, hanbai_tanka
FROM  `Shohin2`
ORDER BY hanbai_tanka DESC;
