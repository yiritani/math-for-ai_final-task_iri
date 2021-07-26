# 人工知能のための数学最終レポート

*M21W0B09_入谷雄介*

1. [コンセプト](#concept)
1. [アプリ全体の流れ](#flow)
1. [使用方法](#howto)


***
<a id="concept"></a>
## <u>コンセプト</u>
自宅の家賃が妥当なのかどうか調査するため、最寄り駅の賃貸物件の家賃から学習モデルを作成。<br>
散布図と線形回帰のプロットに自宅を被せて表示するプログラムを作成。<br>
基本的には「人工知能のための数学」の講義内で教授された記法を使。

***
<a id="flow"></a>
## <u>アプリ全体の大枠の流れ</u>
#### 1.賃貸検索サイトをスクレイプ

#### 2.スクレイプしたデータからインプット用csv生成<br>
[csvレイアウト]

|  FarFromStation<br>駅徒歩  |  Age<br>築年数    |  Price<br>家賃  |  ManagementPrice<br>管理費  | TotalPrice<br>家賃 + 管理費 |
| ---- | ---- | ---- | ---- | ---- |
|  int  |  int  |  float  |  float  | float  |

#### 3.csvを読み込み自宅周辺の家賃状況を線形回帰直線と散布図で表示

#### 4.3で表示したプロットに被せて自宅のデータを表示

***
<a id="howto"></a>
## <u>使用方法</u>
#### コマンドは全てgit clone したディレクトリ内で実行する。

1.コンテナ作成<br>
```
docker compose up -d --build
```

2.学習モデル作成 & プロットのpngをコンテナ内に出力
```
docker run math-for-ai_iritani_last-task python applications/ML_learning/controller.py
```

3.コンテナ内に出力されたpngのプロットをローカルにコピーし、表示する
```
docker run math-for-ai_iritani_last-task python applications/ML_learning/controller.py
```


