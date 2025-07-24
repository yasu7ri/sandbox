# sandbox

このリポジトリには PowerPoint ファイルをページごとに画像化するツールが含まれています。

## ツールの使い方

1. `tools/ppt_to_images.py` を実行します。
2. 第一引数に変換したい `.pptx` ファイルのパス、第二引数に画像を出力するディレクトリを指定してください。

```bash
python tools/ppt_to_images.py sample.pptx output_dir
```

LibreOffice がインストールされている必要があります。初回実行時は `apt-get install libreoffice-impress` でインストールしてください。

## Codespaces での使用

GitHub Codespaces で開くと自動的に devcontainer が構築され、必要な Python 環境と LibreOffice がインストールされます。
初回起動時には `requirements.txt` の内容も自動でインストールされます。

