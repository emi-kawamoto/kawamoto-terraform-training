--演習1
select shohin_id, shohin_mei, hanbai_tanka from Shohin
    -> union all select shohin_id, shohin_mei, hanbai_tanka from Shohin2 order by hanbai_tanka desc;