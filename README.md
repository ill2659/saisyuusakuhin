# オノマトペ生成AIイラストクイズアプリ

## プレイするためには以下の環境・ライブラリのインストールが必要です

【環境】
・NVIDIAのGPU(VRAMが6GB以上)
・GPUのドライバのバージョンに対応したcuda
・cudaのバージョンに対応したPythorch

【ライブラリ等】
・Python：3.10.6
・Pillow
・transformers
・diffusers
       -importlib-metadata
       -zipp
・(accelerate)
※ importlib-metadata,zippはdiffusersインストール時に自動でインストールされます
※accelerateはインストールしなくても動作します


## 【遊び方】

0.アプリをインストール
1.アプリ(AI_onomatope_illustration_quiz)を起動
2.クイズに答える
3.新しいクイズに挑戦するかゲームを終了するかを選択


##　【注意事項】

・初回プレイ時は画像を生成するのに時間がかかります


最終更新 2024/01/11

