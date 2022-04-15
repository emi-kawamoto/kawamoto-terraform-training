select *
from shohin where (shohin_bunrui = "衣服" OR shohin_bunrui = "キッチン用品") AND (hanbai_tanka - shiire_tanka) >= 300;
