--演習1
select * from Shohin where (shohin_bunrui = '衣服' or shohin_bunrui = 'キッチン用品') and (hanbai_tanka - shiire_tanka) >= 300;

--演習2
select round(m, -1) as m_rounded from Samplemath;

--演習3
select replace(str2, '太郎', '花子') as '太郎→花子' from SampleStr where str2 = '太郎';

--演習4
select case when m is null or n is null then '0' else concat(cast(m as char), '+', cast(n as char)) end as 'm+n' from SampleMath;

--演習5
select * from Shohin where torokubi in ('2009-09-20', '2009-09-11', '2009-01-15');

--演習6
select shohin_mei, hanbai_tanka, case when hanbai_tanka <= 500 then '安い' when hanbai_tanka > 500 then '高い' else null end as feels from Shohin;