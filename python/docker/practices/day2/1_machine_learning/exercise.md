## 演習問題 機械学習をやってみよう

### 問題1
まずは、jupyter_notebook 上で、  
`exercise1.ipynb` に `sample1.ipynb` と同じ内容を書いて実行してみましょう（写経して流れを覚える）

### 問題2
説明変数（特徴量）に性別（Sex）を追加して、同様に生存予測をしてみましょう     
補足事項として、Sex は文字列なので数値に置き換えてください
```
dataset["Sex"][dataset["Sex"] == "male"] = 0
dataset["Sex"][dataset["Sex"] == "female"] = 1
```
- `exercise2.ipynb` に記載

### 問題3（任意：早く終わった方向け）
Pandas 100本ノックを実施してみましょう
- 100本ノックを実施することで、データの前処理に必要な能力が向上します
- Pandas は Python3エンジニア 認定データ分析試験 にも出題されます

![](images/pandas.jpg)
- `print(ans[問題番号：1など])` を入力すると正解が出ます

