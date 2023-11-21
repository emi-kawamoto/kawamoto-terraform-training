# ROWS BETWEEN
下記のクエリを実行し、問題に答えましょう。
## (1)

```sql
SELECT
  shohin_id,
  shohin_mei,
  hanbai_tanka,
  SUM(hanbai_tanka) OVER(
    ORDER BY shohin_id
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW 
    ) sum 
FROM
  Shohin
;
```
<details>
<summary>出力</summary>

| shohin_id | shohin_mei     | hanbai_tanka | sum  |
| --------- | -------------- | ------------ | ---- |
| 0001      | Tシャツ        | 1000         | 1000 |
| 0002      | 穴あけパンチ   | 500          | 1500 |
| 0003      | カッターシャツ | 4000         | 4500 |
| 0004      | 包丁           | 3000         | 7000 |
| 0005      | 圧力鍋         | 6800         | 9800 |
| 0006      | フォーク       | 500          | 7300 |
| 0007      | おろしがね     | 880          | 1380 |
| 0008      | ボールペン     | 100          | 980  |

</details>

### 問題1: これはどんなクエリでしょうか？言葉で表現してみましょう。
```回答欄
ここに回答を書きます
```

## (2)
```sql
SELECT
  shohin_id,
  shohin_mei,
  shiire_tanka,
  AVG(shiire_tanka) OVER(
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 
    ) avg 
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_id | shohin_mei     | shiire_tanka | avg       |
| --------- | -------------- | ------------ | --------- |
| 0001      | Tシャツ        | 500          | 2035.0000 |
| 0002      | 穴あけパンチ   | 320          | 2035.0000 |
| 0003      | カッターシャツ | 2800         | 2035.0000 |
| 0004      | 包丁           | 2800         | 2035.0000 |
| 0005      | 圧力鍋         | 5000         | 2035.0000 |
| 0006      | フォーク       | NULL         | 2035.0000 |
| 0007      | おろしがね     | 790          | 2035.0000 |
| 0008      | ボールペン     | NULL         | 2035.0000 |

</details>

### 問題2: これはどんなクエリですか？言葉で表してみましょう。

```回答欄
ここに回答を書きます
```

### 問題3: この分析範囲を前後1行(現在列の前の1行~現在列の後ろの1行、全部で3行)にするにはどのように書き換えたら良いでしょうか？  
下記のクエリを変更してください
```sql
SELECT
  shohin_id,
  shohin_mei,
  shiire_tanka,
  AVG(shiire_tanka) OVER(
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) avg
FROM
  Shohin
;
```

## (3)
```sql
SELECT 
  shohin_id, 
  shohin_bunrui,
  torokubi,
  MAX(torokubi) OVER(
    PARTITION BY shohin_bunrui 
    ORDER BY shohin_id 
    ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING
    ) max 
FROM 
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_id | shohin_bunrui | torokubi   | max        |
| --------- | ------------- | ---------- | ---------- |
| 0004      | キッチン用品  | 2009-09-20 | 2009-09-20 |
| 0005      | キッチン用品  | 2009-01-15 | 2009-09-20 |
| 0006      | キッチン用品  | 2009-09-20 | 2009-09-20 |
| 0007      | キッチン用品  | 2008-04-28 | 2008-04-28 |
| 0002      | 事務用品      | 2009-09-11 | 2009-11-11 |
| 0008      | 事務用品      | 2009-11-11 | 2009-11-11 |
| 0001      | 衣服          | 2009-09-20 | 2009-09-20 |
| 0003      | 衣服          | NULL       | NULL       |

</details>

### 問題4: このクエリはどんなクエリですか？言葉で表してみましょう。
 ```回答欄
 ここに回答を書きます。
 ```

### 問題5 出力の4行め(shohin_id = 0007の行)のmaxカラムはなぜ`2008-04-28`となっているのでしょうか？説明してみましょう。
 ```回答欄
 ここに回答を書きます。
 ```

<details>
<summary>ヒント</summary>
ヒント：5行目(shohin_id = 0002)の列と比較したら、5行目の登録日の方が新しいので4行目のmaxの値は`2009-11-11`になりそうです。    

なぜ、古いほうの値である`2008-04-28`の値が出力されているのでしょうか？OVER句の指定内容を確認してみましょう。
</details>