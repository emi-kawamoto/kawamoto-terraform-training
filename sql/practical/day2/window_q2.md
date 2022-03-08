# その他の頻出関数
- ROW_NUMBER
- RANK/DENSE_RANK
- FIRST/LAST_VALUE

## ROW_NUMBER

`ROW_NUMBER` 関数は、行番号を出力する関数です。  

### ROW_NUMBERの使いかた

```sql
SELECT 
  ~,
  ~,
  ROW_NUMBER() OVER(
    [PARTITION BY ~]
    [ORDER BY ~]
    ) row_num
FROM
  ~
;
```

1. 引数は取らないが、()が必要
1. `ORDER BY`で指定したカラムが複数ある場合順序が不特定になるため、一意になる組み合わせの複数のキーをセットする。

### やってみましょう

`shop`データベースの`Shohin`テーブルを使用します。

#### 1.

```sql
SELECT
  shohin_id,
  shohin_mei,
  torokubi,
  ROW_NUMBER() OVER(
    PARTITION BY torokubi
    ORDER BY shohin_id
    ) row_num
FROM 
  Shohin;
```

<details>
<summary>出力</summary>

| shohin_id | shohin_mei            | torokubi   | row_num |
|----|----|----|----|
| 0003      | カッターシャツ        | NULL       |       1 |
| 0007      | おろしがね            | 2008-04-28 |       1 |
| 0005      | 圧力鍋                | 2009-01-15 |       1 |
| 0002      | 穴あけパンチ          | 2009-09-11 |       1 |
| 0001      | Tシャツ               | 2009-09-20 |       1 |
| 0004      | 包丁                  | 2009-09-20 |       2 |
| 0006      | フォーク              | 2009-09-20 |       3 |
| 0008      | ボールペン            | 2009-11-11 |       1 |

</details>

1. `torokubi` ごとに切り分け、その中で`shohin_id`で降順に並び替えた行番号を表示するクエリです
1. `torokubi=2009-09-20`の3つの行をみてみましょう
    1. `row_num`の値が上から1.2.3とついています。そしてそれは、`shohin_id`の若い順でついていることがわかります
    1. これは、`torokubi`ごとに切り分けたとき、`torokubi=2009-09-20`のレコードは3つあり、`shohin_id`で順序づけして若い順で行番号をふっていると言うことです。
    
### 2

`sns`データベースの`activity_reports`テーブルを使用します

```sql
SELECT
  ROW_NUMBER() OVER(
    PARTITION BY user_id
    ORDER BY date 
    ) row_num,
  user_id,
  date
FROM
  activity_reports
;
```

<details>
<summary>出力</summary>

| row_num | user_id | date       |
|----|----|----|
|       1 |       1 | 2021-10-01 |
|       2 |       1 | 2021-10-02 |
|       3 |       1 | 2021-10-03 |
|       4 |       1 | 2021-10-04 |
|       5 |       1 | 2021-10-05 |
|       6 |       1 | 2021-10-06 |
|       7 |       1 | 2021-10-07 |
|       8 |       1 | 2021-10-08 |
|       9 |       1 | 2021-10-09 |
|       1 |       2 | 2021-10-01 |
|       2 |       2 | 2021-10-02 |
|       3 |       2 | 2021-10-03 |
|       4 |       2 | 2021-10-04 |
|       5 |       2 | 2021-10-05 |
|       6 |       2 | 2021-10-06 |
|       7 |       2 | 2021-10-07 |
|       8 |       2 | 2021-10-08 |
|       9 |       2 | 2021-10-09 |
|       1 |       3 | 2021-10-01 |
|       2 |       3 | 2021-10-02 |
|       3 |       3 | 2021-10-03 |
|       4 |       3 | 2021-10-04 |
|       5 |       3 | 2021-10-05 |
|       6 |       3 | 2021-10-06 |
|       7 |       3 | 2021-10-07 |
|       8 |       3 | 2021-10-08 |
|       9 |       3 | 2021-10-09 |
|       1 |       4 | 2021-10-01 |
|       2 |       4 | 2021-10-02 |
|       3 |       4 | 2021-10-03 |
|       4 |       4 | 2021-10-04 |
|       5 |       4 | 2021-10-05 |
|       6 |       4 | 2021-10-06 |
|       7 |       4 | 2021-10-07 |
|       8 |       4 | 2021-10-08 |
|       9 |       4 | 2021-10-09 |
|       1 |       5 | 2021-10-01 |
|       2 |       5 | 2021-10-02 |
|       3 |       5 | 2021-10-03 |
|       4 |       5 | 2021-10-04 |
|       5 |       5 | 2021-10-05 |
|       6 |       5 | 2021-10-06 |
|       7 |       5 | 2021-10-07 |
|       8 |       5 | 2021-10-08 |
|       9 |       5 | 2021-10-09 |

</details>

1. 出力の最初のカラムに行番号をふっているカラムです
    1. `user_id`で切り分けて、`date`順に上から行番号をふります
    
1. `user_id=1`と`user_id=2`の表示が切り替わる9,10行目をみてみましょう
    1. `user_id`で切り分けているので、`user_id`が変わるタイミングで`row_num`もリセットされることがわかります
    
## RANK/DENSE_RANK

### RANK/DENSE_RANKの使い方
```sql
SELECT 
  ~,
  ~,
  RANK() OVER(
    [PARTITION BY ~]
    [ORDER BY ~]
    )
FROM
  ~
;
```

1. ORDER BY指定したカラムでのランクを表示する
1. 引数は取らないが、()が必要
1. 同じ値が複数存在したとき、それらは同じランクになる
    1. **RANK: 1位が2つ存在した後の次の行は3位になる**
    1. **DENSE_RANK: 1位が2つ存在した後の次の行は2位になる**
    1. 違いがあるので注意
    

### やってみましょう
`shop`データベースの`Shohin`テーブルを使用します

#### 1. 何も指定しない
windowを指定しないとどんな出力になるでしょうか？確認してみましょう

```sql
SELECT
  shohin_mei,
  hanbai_tanka,
  RANK() OVER() `rank`
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | hanbai_tanka | rank |
|----|----|----|
| Tシャツ               |         1000 |             1 |
| 穴あけパンチ          |          500 |             1 |
| カッターシャツ        |         4000 |             1 |
| 包丁                  |         3000 |             1 |
| 圧力鍋                |         6800 |             1 |
| フォーク              |          500 |             1 |
| おろしがね            |          880 |             1 |
| ボールペン            |          100 |             1 |

</details>

1. ORDER BY指定がないので`rank`の値が全て1になっています

### 2. ORDER BY指定をする

`hanbai_tanka`でランクづけするために、ORDER BY指定を追加し実行してみましょう

```sql
SELECT
  shohin_mei,
  hanbai_tanka,
  DENSE_RANK() OVER(
    ORDER BY hanbai_tanka
    ) `rank`
FROM
    Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | hanbai_tanka | rank |
|----|----|----|
| ボールペン            |          100 |    1 |
| 穴あけパンチ          |          500 |    2 |
| フォーク              |          500 |    2 |
| おろしがね            |          880 |    4 |
| Tシャツ               |         1000 |    5 |
| 包丁                  |         3000 |    6 |
| カッターシャツ        |         4000 |    7 |
| 圧力鍋                |         6800 |    8 |

</details>

1. `hanbai_tanka`が低い順にランクづけするクエリです
1. 2.3行目の`hanbai_tanka`の値が同じなので同率2位で、4行目のランクは`4`になっています
    1. DENSE_RANKに書き変えて実行し、4行目のランクがどうなっているか確認しましょう
    1. `3`になっているはずです
    
### 3. PARTITION BY指定をする

ORDER BY指定に加えて、PARTITION BY指定も追加してみましょう

```sql
SELECT 
  shohin_mei,
  shohin_bunrui,
  hanbai_tanka,
  RANK() OVER(
    PARTITION BY shohin_bunrui
    ORDER BY hanbai_tanka DESC
    ) `rank`
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | shohin_bunrui      | hanbai_tanka | rank |
|----|----|----|----|
| 圧力鍋                | キッチン用品       |         6800 |    1 |
| 包丁                  | キッチン用品       |         3000 |    2 |
| おろしがね            | キッチン用品       |          880 |    3 |
| フォーク              | キッチン用品       |          500 |    4 |
| 穴あけパンチ          | 事務用品           |          500 |    1 |
| ボールペン            | 事務用品           |          100 |    2 |
| カッターシャツ        | 衣服               |         4000 |    1 |
| Tシャツ               | 衣服               |         1000 |    2 |

</details>

1. `shohin_bunrui`の項目別に`hanbai_tanka`が高い順にランクづけするクエリです
1. `shohin_bunrui=キッチン用品、事務用品、衣服`のそれぞれの項目の中でのランクが表示されていることを確認しましょう。

## FIRST/LAST_VALUE

### FIRST/LAST_VALUEの使い方

```sql
SELECT
  ~,
  ~,
  FIRST_VALUE(~) OVER(
    [PARTITION BY ~]
    [ORDER BY ~]
    [flame]
    )
FROM
 ~
;
```

1. 引数で与えたカラムまたは式の
    1. FIRST_VALUE: 一番上の値を表示する
    1. LAST_VALUE: 一番最後の値を表示する
    
1. LAST_VALUE使用時にはflame(ROWS BETWEEN等範囲を指定するもの)を入れる必要がある
    
### やってみましょう
`shop`データベースの`Shohin`テーブルを使用します

#### 1. 何も指定しない

```sql
SELECT
  shohin_mei,
  hanbai_tanka,
  FIRST_VALUE(shohin_mei) OVER() first_mei
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | hanbai_tanka | first_mei  |
|----|----|----|
| Tシャツ               |         1000 | Tシャツ    |
| 穴あけパンチ          |          500 | Tシャツ    |
| カッターシャツ        |         4000 | Tシャツ    |
| 包丁                  |         3000 | Tシャツ    |
| 圧力鍋                |         6800 | Tシャツ    |
| フォーク              |          500 | Tシャツ    |
| おろしがね            |          880 | Tシャツ    |
| ボールペン            |          100 | Tシャツ    |

</details>

1. `shohin_mei`の一番上にある値を持ってくるクエリです。
1. 今回は特に並び替えの指定はしていないので、上にあった`Tシャツ`を出力しています

### 2. ORDER BY指定をする

```sql
SELECT
  shohin_mei,
  hanbai_tanka,
  FIRST_VALUE(shohin_mei) OVER(
    ORDER BY hanbai_tanka DESC 
    ) first_mei
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | hanbai_tanka | first_mei |
|----|----|----|
| 圧力鍋                |         6800 | 圧力鍋    |
| カッターシャツ        |         4000 | 圧力鍋    |
| 包丁                  |         3000 | 圧力鍋    |
| Tシャツ               |         1000 | 圧力鍋    |
| おろしがね            |          880 | 圧力鍋    |
| 穴あけパンチ          |          500 | 圧力鍋    |
| フォーク              |          500 | 圧力鍋    |
| ボールペン            |          100 | 圧力鍋    |

</details>

1. `hanbai_tanka`を高い順に並べたとき一番上に来る`shohin_mei`の値を持ってくるクエリです
1. 今回`hanbai_tanka`が一番高いのは`shohin_mei=圧力鍋な`ので、この値が表示されています
    
### 3. PARTITION BY指定をする

```sql
SELECT
  shohin_mei,
  shohin_bunrui,
  hanbai_tanka,
  FIRST_VALUE(shohin_mei) OVER(
    PARTITION BY shohin_bunrui
    ORDER BY hanbai_tanka DESC 
    ) first_mei
FROM
  Shohin
;
```

<details>
<summary>出力</summary>

| shohin_mei            | shohin_bunrui      | hanbai_tanka | first_mei             |
|----|----|----|----|
| 圧力鍋                | キッチン用品       |         6800 | 圧力鍋                |
| 包丁                  | キッチン用品       |         3000 | 圧力鍋                |
| おろしがね            | キッチン用品       |          880 | 圧力鍋                |
| フォーク              | キッチン用品       |          500 | 圧力鍋                |
| 穴あけパンチ          | 事務用品           |          500 | 穴あけパンチ          |
| ボールペン            | 事務用品           |          100 | 穴あけパンチ          |
| カッターシャツ        | 衣服               |         4000 | カッターシャツ        |
| Tシャツ               | 衣服               |         1000 | カッターシャツ        |

</details>

1. shohin_bunruiの項目ごとに、hanbai_tankaが高い順の一番上のshohin_meiの値を表示しています

### LAST_VALUE
使い方の部分でもあるように、一番最後の行を持ってくるLAST_VALUEはwindowの中で範囲指定する必要があります。  
実際、2.3.のクエリのFIRST_VALUEの部分をLAST_VALUEに書き換えて実行してみましょう。

<details>
<summary>出力2'</summary>

| shohin_mei            | hanbai_tanka | first_mei             |
|----|----|----|
| 圧力鍋                |         6800 | 圧力鍋                |
| カッターシャツ        |         4000 | カッターシャツ        |
| 包丁                  |         3000 | 包丁                  |
| Tシャツ               |         1000 | Tシャツ               |
| おろしがね            |          880 | おろしがね            |
| 穴あけパンチ          |          500 | フォーク              |
| フォーク              |          500 | フォーク              |
| ボールペン            |          100 | ボールペン            |

</details>



<details>
<summary>出力3'</summary>

| shohin_mei            | shohin_bunrui      | hanbai_tanka | first_mei             |
|----|----|----|----|
| 圧力鍋                | キッチン用品       |         6800 | 圧力鍋                |
| 包丁                  | キッチン用品       |         3000 | 包丁                  |
| おろしがね            | キッチン用品       |          880 | おろしがね            |
| フォーク              | キッチン用品       |          500 | フォーク              |
| 穴あけパンチ          | 事務用品           |          500 | 穴あけパンチ          |
| ボールペン            | 事務用品           |          100 | ボールペン            |
| カッターシャツ        | 衣服               |         4000 | カッターシャツ        |
| Tシャツ               | 衣服               |         1000 | Tシャツ               |

</details>

flameを指定していないので、自身の`shohin_mei`カラムの値を返しています。

ではなぜ、エラーになるわけでもなくただ自分自身の値を返すのでしょうか？ご自身で考察して、下の答えのプルダウンを開いてください。

<details>
<summary>なぜLAST_VALUEで最後の行を返してくれないのか</summary>
これは、OVER句にデフォルトで入れられるflameが関係しています。

OVER句でROWS BETWEENなどのflameを指定しないと、以下のように見なされて処理が実行されます。

```sql
OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

このwindowはつまり、「一番最初の行から現在行までで集計する」という意味です。  

ORDER BY指定だけしたSUM()の動作などがわかりやすい例です。
> *ランニングSUM*  
> 上から順番に合算を実行していく

flameを指定していないとき、処理側から見た最終行は現在行となるため出力に現在行の値が返ってくるというわけです。

なので、今回のように一番最初の行から一番最後の行までを見てLAST_VALUEを出力して欲しい場合には、
```sql
OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
```

を指定してあげればいいということです。
</details>

では、flameを指定してLAST_VALUEを実行してみましょう

1. 2.のクエリをLAST_VALUEにして実行してみましょう

    <details>
    <summary>出力</summary>

   | shohin_mei            | hanbai_tanka | last_mei        |
   |----|----|----|
   | 圧力鍋                |         6800 | ボールペン      |
   | カッターシャツ        |         4000 | ボールペン      |
   | 包丁                  |         3000 | ボールペン      |
   | Tシャツ               |         1000 | ボールペン      |
   | おろしがね            |          880 | ボールペン      |
   | 穴あけパンチ          |          500 | ボールペン      |
   | フォーク              |          500 | ボールペン      |
   | ボールペン            |          100 | ボールペン      |
   
    </details>
   
    <details>
    <summary>クエリ例</summary>
    
    ```sql
    SELECT
      shohin_mei,
      hanbai_tanka,
      LAST_VALUE(shohin_mei) OVER(
        ORDER BY hanbai_tanka DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) last_mei
    FROM
      Shohin
    ;
    ```
    </details>
   
1. 3.のクエリをLAST_VALUEに書き換えて実行してみましょう
    <details>
    <summary>出力</summary>
   
    | shohin_mei            | shohin_bunrui      | hanbai_tanka | last_mei        |
    |----|----|----|----|
    | 圧力鍋                | キッチン用品       |         6800 | フォーク        |
    | 包丁                  | キッチン用品       |         3000 | フォーク        |
    | おろしがね            | キッチン用品       |          880 | フォーク        |
    | フォーク              | キッチン用品       |          500 | フォーク        |
    | 穴あけパンチ          | 事務用品           |          500 | ボールペン      |
    | ボールペン            | 事務用品           |          100 | ボールペン      |
    | カッターシャツ        | 衣服               |         4000 | Tシャツ         |
    | Tシャツ               | 衣服               |         1000 | Tシャツ         |
   
    </details>
   
    <details>
    <summary>クエリ例</summary>
    
    ```sql
    SELECT
      shohin_mei,
      shohin_bunrui,
      hanbai_tanka,
      LAST_VALUE(shohin_mei) OVER(
        PARTITION BY shohin_bunrui
        ORDER BY hanbai_tanka DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) last_mei
    FROM
      Shohin
    ;
    ```
    </details>
