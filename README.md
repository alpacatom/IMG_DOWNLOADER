IMG_DOWNLOADER
====
画像ファイルのダウンロード -> 顔検出して保存 -> リサイズしてCIFAR-10のデータセットのバイナリ形式で保存を行う3つのスクリプトです。<BR>
作ってから知りましたがTensorflowの関数でリサイズするものがありますし、PATHの指定も設定ファイルでやるほうが楽だと思います
##collect_images.py
Google Custome Search APIを使って画像をダウンロードするスクリプト with Pythonです。
<BR>
Pythonの練習用に書きました。
<BR>
（無料ですと1日10件までしかダウンロード出来ないので他のAPI使いたいですが、bingのAPIの方も無料でなくなると聞いてやむなく使ってます）

##trim_image.py
OpenCV3を使って顔を検出して保存しています。
<BR>
アニメ顔の検出をしたかったので、xmlファイルはアニメ顔用のファイルを設定しています。

##image2binary.py
リサイズしてCIFAR-10のデータセットのバイナリ形式で保存します。
