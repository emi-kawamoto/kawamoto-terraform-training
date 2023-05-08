# 1日目演習
スライドの内容をもとに実際に手を動かしてみましょう。

- SQL基礎の復習
- 綺麗なSQLをかく

## 課題提出の準備
SQL応用の課題提出用ブランチ`develop/sql-practical`を作成する

`$ git branch develop/sql-practical main`

このブランチをマージ先にしてMRを作成してください。

## SQL基礎の復習
提出前にご自身のmysqlで動作確認をしてみましょう。

作成したクエリと、その結果を[example.sql](example.sql)のような形式で提出しましょう。

### 演習１

ブランチ`develop/sql-practical`から、`feature/day1_enshu1`というブランチを生やして移動し、作業してください。

`$ git switch -c feature/day1_enshu1 develop/sql-practical`

day1フォルダの中のenshu1.sqlというファイルに、作成したクエリとその結果を記述してください。

```
sql_practical
   |- day1
        |- enshu1.sql
```

1. `sns`というデータベースを作成し、以下のテーブルを作成してください

   a.  
    - テーブル名：users
    - カラム定義：
        - id: 整数、NULLなし、主キー
        - name: 可変長文字列(15文字)、NULLなし
        - email: 可変長文字列(50文字)、NULLなし
        - age: 整数
    
   b.  
    - テーブル名：follows
    - カラム定義：
        - follower_id: 整数、NULLなし
        - followee_id: 整数、NULLなし
   
2. `sns`データベースのテーブル一覧を出力させてください

3. MRを作成して講師に共有しましょう。
   -  ブランチ`feature/day1_enshu1`からブランチ`develop/sql-practical`へのMRを作成する

### 演習２

ブランチ`develop/sql-practical`から、`feature/day1_enshu2`というブランチを生やして作業してください。

`$ git switch -c feature/day1_enshu2 develop/sql-practical`

day1フォルダの中のenshu2.sqlというファイルに、作成したクエリとその結果を記述してください。

```
sql_practical
   |- day1
        |- enshu2.sql
```

1. 演習1で作成したテーブルにデータを格納します
   1. usersテーブルに以下のデータを格納してください
      ```
      (1, 'タヌキ', 'pokopoko@example.com', 19)
      (2, 'ウサギ', 'moonlight@example.net', 20)
      (3, 'ネコ', 'alivemillion@example.com', 31)
      (4, 'ネズミ', 'hedgehook@example1.jp', 23)
      (5, 'アルマジロ', 'sandsandpan@example.jp', 28)
      ```
   2. followsテーブルに以下のデータを格納してください
      ```
      (1, 2),
      (1, 3),
      (1, 4),
      (1, 5),
      (3, 1),
      (3, 2),
      (4, 5),
      (5, 1),
      (5, 2),
      (5, 3),
      (5, 4);
      ```

2. MRを作成して講師に共有しましょう。
   - ブランチ`feature/day1_enshu2`からブランチ`develop/sql-practical`へのMRを作成する


### 演習３

ブランチ`develop/sql-practical`から、`feature/day1_enshu3`というブランチを生やして作業してください。

day1フォルダの中のenshu3.sqlというファイルに、作成したクエリとその結果を記述してください。

```
sql_practical
   |- day1
        |- enshu3.sql
```

1. `ネコ`さんがフォローしているユーザ名を一覧で表示してください
   1. タヌキさんとウサギさんの2名が表示されたら成功です
   1. ヒント1：followテーブルのデータにuserテーブルのデータを紐付けてみましょう
   1. ヒント2；内部結合

2. 誰もフォローしていないユーザ名を表示してください
   1. ウサギさんだけが表示されたら成功です
   1. ヒント1：外部結合

3. (時間あれば)相互フォローしているユーザid一覧を表示してください
   1. `1と3` `1と5` `4と5` の組み合わせが表示されたら成功です
   1. ヒント1：followテーブルのfollower_idとfollowee_idが一致している部分で結合します
   1. ヒント2：ON句には条件をANDでつなげることができます
   1. ヒント3：出力結果が`1と3` `3と1`のように内容が重複してしまう場合は、`{一つ目のカラムid1} < {二つ目のカラムid2}`のようにすると排除できます

4. MRを作成して講師に共有しましょう。
   - ブランチ`feature/day1_enshu3`からブランチ`develop/sql-practical`へのMRを作成する

## 綺麗なSQLをかく
<details>
<summary>追加で作成したテーブルのスキーマ</summary>

```sql
CREATE TABLE activity_reports(
    date DATE NOT NULL,
    user_id INTEGER NOT NULL,
    post_id VARCHAR(256) NOT NULL,
    impressions INTEGER NOT NULL,
    clicks INTEGER NOT NULL,
    PRIMARY KEY (date, user_id, post_id)
)
;

INSERT INTO activity_reports
VALUES
('2021-10-01',1,'0000a',367,38),
('2021-10-01',2,'0000b',190,31),
('2021-10-01',3,'0000c',48,12),
('2021-10-01',4,'0000d',578,240),
('2021-10-01',5,'0000e',192,45),
('2021-10-02',1,'0000a',200,45),
('2021-10-02',2,'0000b',143,50),
('2021-10-02',3,'0000c',50,20),
('2021-10-02',4,'0000d',200,36),
('2021-10-02',5,'0000e',100,34),
('2021-10-03',1,'0000a',312,34),
('2021-10-03',2,'0000b',572,200),
('2021-10-03',3,'0000c',483,28),
('2021-10-03',4,'0000d',249,15),
('2021-10-03',5,'0000e',109,49);
```
</details>

### 演習4
[enshu4.sql](enshu4.sql)の内容を綺麗に書き換えてください

1. ブランチ`develop/sql-practical`から、`feature/day1_enshu1_4`というブランチを生やして作業してください。
1. MRを作成して講師に共有しましょう。
   - ブランチ`feature/day1_enshu4`からブランチ`develop/sql-practical`へのMRを作成する

### 演習5
[enshu5.sql](enshu5.sql)の内容を綺麗に書き換えてください

1. ブランチ`develop/sql-practical`から、`feature/day1_enshu1_5`というブランチを生やして作業してください。
1. MRを作成して講師に共有しましょう。
   - ブランチ`feature/day1_enshu5`からブランチ`develop/sql-practical`へのMRを作成する

1. このクエリは、年代別のフォロー数の平均を求めるものです
1. ヒント１:サブクエリをWITH句で抜き出しましょう

### 演習6
研修メンバー同士でMRレビューしてみましょう！

講師からApproveもらったらマージしてOKです。

### 演習7(時間があれば)
演習1~3で作成したクエリを見返してみましょう。
綺麗に整形できそうなら、書き換えましょう

1. ブランチ`develop/sql-practical`から、`feature/day1_enshu7`というブランチを生やして作業してください。
1. MRを作成して講師に共有しましょう。
   - ブランチ`feature/day1_enshu7`からブランチ`develop/sql-practical`へのMRを作成する
   