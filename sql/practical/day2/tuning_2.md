# SQLチューニング2
Oracle MySQL8.0 チューニング入門セミナーの内容を要約 

## データベースの設定を変更しデータベースそのものを最適化する

### 設定を確認する
- 全てのシステム変数を表示する
  - `SHOW VARIABLES;`
  - https://dev.mysql.com/doc/refman/5.6/ja/server-system-variables.html
  
### パフォーマンススキーマ
- MySQLサーバ内のイベントごとの処理時間を記録している
- パフォーマンススキーマのテーブル一覧を確認する
  - `SHOW TABLES FROM performance_schema;`
- パフォーマンススキーマのグローバル変数一覧を確認する
  - `SELECT * FROM performance_schema.global_variables;`
  - 要確認指標
    - max_connections
    - thread_cache_size
    - query_cache_size
    - sort_buffer_size
  
#### max_connections
- `SELECT * FROM performance_schema.global_variables WHERE VARIABLE_NAME = 'max_connections';`
- サーバが許容できるコネクションの数
- デフォルト：151
- スループットが低い時はここを増やすことでパフォーマンスの改善につながる
  - 増やすとサーバメモリの使用量が大きくなる

#### thread_cache_size
- `SELECT * FROM performance_schema.global_variables WHERE VARIABLE_NAME = 'thread_cache_size';`
- スレッドをキャッシュする数 = コネクション切断後にもスレッドを隠し持っておく(キャッシュする)
- デフォルト：9
- レスポンスタイムが長い場合はここを増やすことで改善につながる可能性がある
  - 増やすとメモリ使用量が大きくなる
  
#### query_cache_size
- `SELECT * FROM performance_schema.global_variables WHERE VARIABLE_NAME = 'query_cache_size';`
- 直近に似たようなクエリが叩かれているとこのキャッシュが使用できる
- 近い内容のクエリを頻繁に叩く場合は利用を検討する

#### sort_buffer_size
- `SELECT * FROM performance_schema.global_variables WHERE VARIABLE_NAME = sort_buffer_size;`
- 並べ替え処理のメモリサイズ
- このサイズを超えるとディスクで処理される
  - ディスクとのやりとりは時間がかかるのであらかじめ大量のソートがわかっている場合には設定値をあげておく
  


  
