# 人工知能のための数学 最終レポート

### <シリコンバレーエンジニアの酒井潤さんにコードレビューしていただきました！><br>
![Screenshot 2023-12-26 at 11 47 37](https://github.com/yiritani/math-for-ai_final-task_iri/assets/74131902/9ac3f1eb-aa7b-43e7-886c-d4eba4f478bd)
[コードレビュー動画1](https://www.youtube.com/watch?v=TTatRa6fjIA&t=311s)<br>
[コードレビュー動画2](https://www.youtube.com/watch?v=OEvD9gSWf20&t=57s)<br>
mainリポジトリはレビュー内容未反映です

<hr>

*M21W0B09*

1. [コンセプト](#concept)
1. [アプリケーション使用方法](#howto)
1. [アプリ全体の流れ](#flow)
1. [結果](#todo)


***
<a id="concept"></a>
## <u>コンセプト</u>
劣化版[Boston house price]です。<br>

自宅の家賃が妥当なのかどうか調査するため、最寄り駅の賃貸物件の家賃から学習モデルを作成。<br>
散布図と線形回帰のプロットに自宅を被せて表示するプログラムを作成。<br>
基本的には「人工知能のための数学」の講義内で教授された記法を使う。<br>


***
<a id="howto"></a>
## <u>アプリ使用方法</u>

git cloneしたディレクトリでdocker composeし、コンテナ作成
```
docker compose up
```

[localhost:5000](http://localhost:5000)をブラウザで開く<br><br>


***
<a id="flow"></a>
## <u>アプリ全体の大枠の流れ</u>

1.賃貸検索サイトをスクレイプ

2.スクレイプしたデータからインプット用csv生成<br>
[csvレイアウト]

|  FarFromStation<br>駅徒歩  |  Age<br>築年数    |  Price<br>家賃  |  ManagementPrice<br>管理費  | TotalPrice<br>家賃 + 管理費 |
| ---- | ---- | ---- | ---- | ---- |
|  int  |  int  |  float  |  float  | float  |

3.csvを読み込み自宅周辺の家賃状況を線形回帰直線と散布図で表示

4.3で表示したプロットに被せて自宅のデータを表示

5.4で作成したプロットをpngで保存

6.pngを画面表示する


***
<a id="result"></a>
### 結果
回帰直線よりも上に位置しているため、このエリア内では多少割高な家賃であると言える。<br>
築年数や駅徒歩、設備や立地の悪さを加味するときっと相場よりは安いだろうという感覚があったのだが、個人的にはややがっかりな結果となった。<br>
今後転居する際などはこのアプリを用いて試算するのも1つ良いかもしれない。

