-- 演習1

SELECT * FROM Shohin WHERE hanbai_tanka - shiire_tanka >= 300 AND (shohin_bunrui = '衣服' OR shohin_bunrui = 'キッチン用品');

-- 演習2

SELECT ROUND(m) AS m_rounded FROM SampleMath;

-- 演習3

SELECT REPLACE(str2, '太郎', '花子') AS '太郎→花子' FROM SampleStr WHERE str2 LIKE '%太郎%';

-- 演習4

SELECT COALESCE(CONCAT(CAST(m AS CHAR), ' + ', CAST(n AS CHAR)),0) AS 'm+n' FROM SampleMath;

-- 演習5

SELECT * FROM Shohin WHERE torokubi IN ('2009-09-20', '2009-09-11', '2009-01-15');

— 演習６

SELECT shohin_mei, CASE WHEN hanbai_tanka < 1000 THEN'安い' WHEN hanbai_tanka >= 1000 THEN '高い ' ELSE NULL END AS 'feels' FROM Shohin;

…
