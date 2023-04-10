-- 演習1

SELECT 
    * 
FROM 
    Shohin 
WHERE 
    hanbai_tanka - shiire_tanka >= 300 
    AND (shohin_bunrui = '衣服' or shohin_bunrui = 'キッチン用品')
;

-- 演習2

SELECT 
    ROUND(m, -1) 
FROM 
    SampleMath
;

-- 演習3

SELECT 
    REPLACE(str2, '太郎', '花子') AS 太郎→花子 
FROM 
    SampleStr 
WHERE 
    str2 = '太郎'
;

-- 演習4

SELECT 
    CASE WHEN m IS NULL OR n IS NULL  THEN 0 
         ELSE CONCAT(CAST(m AS CHAR), ' + ', CAST(n AS CHAR)) END 
	 AS 'm+n' 
FROM 
    SampleMath
;

-- 演習5

SELECT 
    * 
FROM 
    SHohin 
WHERE 
    torokubi in ('2009-09-20', '2009-09-11', '2009-01-15');

-- 演習6

SELECT 
    shohin_mei, 
    hanbai_tanka, 
    CASE WHEN hanbai_tanka <= 500 THEN '安い' 
         ELSE '高い' END 
         AS feels 
FROM 
    Shohin
;

