# SQLチューニング1

## インデックス
インデックス　＝ 目的のレコードを効率よく取得するための索引の役割

[公式ドキュメント](https://dev.mysql.com/doc/refman/8.0/ja/mysql-indexes.html)

### 目的
- 大規模なデータから少量のデータを取り出したい
- NULLが多いデータからNULL以外の値を検索したい
- よくORDER BYやWHEREで条件指定するカラムだから検索を効率化したい

**逆にインデックスを作成しないほうがいい時もある**
- 表の規模が小さく、インデックスを呼び出したほうが処理の負荷が高い
- カラムの値がよく更新されるようなデータ
    - カラムの値が更新される→INDEXも更新が必要でデータの検索速度は高いが、更新や削除処理の時にINDEXのデータも処理しなくてはならないため速度が落ちる
    
## インデックスの扱い方
- 実行計画を確認し、インデックスを貼る位置を決める
  - 出力の「possible_keys」カラムで有効なインデックスカラムを確認する
    
- 既存のインデックスを確認する
  - `SHOW INDEX FROM <DB名>.<テーブル名>;`
  - `SHOW INDEX FROM shop.Shohin;` 
    
- インデックスを追加する
  - ALTER TABLE文を使う
  - `ALTER TABLE <テーブル名> ADD INDEX <インデックス名>(<カラム名>);` 
  - `ALTER TABLE Shohin ADD INDEX index_shohin_bunrui(shohin_bunrui);` 
    
- 作成されたインデックスを確認する
  - `SHOW INDEX FROM shop.Shohin;`
  - `index_shohin_bunrui`というKeyが作成された  
    
- 複合インデックス
  - 複数のカラムを対象としたインデックス
  - `ALTER TABLE <テーブル名> ADD INDEX <インデックス名>(<カラム名1, カラム名2, ...>);`
    
- インデックスを削除する
  - ALTER TABLE文を使う
  - `ALTER TABLE <テーブル名> DROP INDEX <インデックス名>;`
  - `ALTER TABLE Shohin DROP INDEX index_shohin_bunrui;`  
    
- インデックスが使用されているか確認する
  - 実行計画をみる

## 実行計画
「実行計画」　＝　どのような計画でクエリを実行するか

### MySQLの実行計画
EXPLAINで実行計画を表示させることができる

実行してみましょう
```sql
EXPLAIN(
  SELECT
    DISTINCT shohin_bunrui
  FROM 
    Shohin
)
;
```

#### 出力結果カラム
- id
- select_type：クエリの種類
- table
- partitions
- type
- possible_keys
- key
- key_len
- ref
- rows
- filtered
- Extra

[公式リファレンス(ver_8.0)](https://dev.mysql.com/doc/refman/8.0/ja/explain-output.html#explain-output-columns)

## チューニング時のチェックポイント
チューニングをする時に最初に疑う観点について紹介します

### インデックスがちゃんと適用されているか？
確認する項目
- possible_keys：利用可能なINDEX
- key:実際に利用されたINDEX

NULLになっている場合はINDEXが使用されていないので確認する

### テーブルをフルスキャンしていないか？
確認する項目
- type
  - ALL/indexという出力がでたら要注意
  - テーブルまたはINDEXに対してフルスキャンを行っている
    
インデックスの貼り方や設計を見直す

### 一時テーブルを作成しなければならないほど対象データが膨らんでいないか？
確認する項目
- Extra
  - Using temporary/Using filesortという出力が出たら要注意
  - 特に危険な場合はUsing filesortとUsing temporaryの組み合わせパターン
  - Using temporary : クエリ実行時に一時テーブルを作成して処理をしなければならない
  - Using filesort : メモリが足りず物理ファイルに一度書き出してからソートを行う
    
### UNION / UNION ALL使い分け
UNION : 重複行を排除

UNION ALL : 重複は排除しない

特にそれぞれのデータ量が多い場合、重複行を排除するUNIONは処理負荷が高いため、UNION ALLで足りる用件の場合はUNION ALLを使用する。
