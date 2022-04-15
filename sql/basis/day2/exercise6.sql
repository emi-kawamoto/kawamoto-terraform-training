select shohin_mei, hanbai_tanka, 
  CASE
    WHEN hanbai_tanka <= 500 THEN "安い"
    WHEN hanbai_tanka > 500 THEN "高い"
    ELSE NULL
  END AS "feels"
FROM shohin;
