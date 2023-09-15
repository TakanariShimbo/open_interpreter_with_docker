
# 前提

GPU使用する場合は以下が必須  

* Nvidia Driver がインストール済み
* WSL に Nvidia Container Toolkit がインストール済み


# 初回起動時

1. devcontainer に移動し編集
  ```
  cd .devcontainer
  ```

  devcontainer.json の3行目を書き換えどちらを使用するかを決める
  ```
  "dockerComposeFile": ["docker-compose-gpu.yml"], # cpu or gpu
  ```

  .env.sample を copy し、.env を作成する

2. コンテナを起動しターミナルに入る
  ```
  # VS Code の場合
  # 以下コマンドで VS Code を開き、左下の><をクリックし、コンテナで再度開くを選択
  code .
  
  # それ以外の場合
  docker-compose up -d
  docker exec -it container_python39_with_cuda /bin/bash
  ```

3. 仮想環境作成
  ```
  python3 -m venv ./myenv
  ```

4. 仮想環境アクティベート
  ```
  # VS Code の場合
  # 右下から次の仮想環境を使用するように選択: /work/myenv/bin/python3
  # 選択後に新しいターミナルを起動
  
  # それ以外の場合
  source myenv/bin/activate
  ```

5. 仮想環境を初期化
  ```
  pip install --upgrade pip
  pip install --upgrade setuptools
  ```

6. お好みで必要なライブラリのインストール
  ```
  pip install xxxx

  # 以下サンプル
  # pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  # もし lit install 時にエラーが発生する場合は以下コマンドで先にインストールしておき、再度上記コマンドを実行
  # pip install lit==15.0.7
  # torch install 時に Killed と表示される場合は、pip --no-cache-dir install xxxx のように no-cache を加える
  # pip install jupyter
  ```

# 使用時

まず、初回起動時同様に1, 2, 4 を実施   
3, 5, 6 は仮想環境は作成ずみなのでスキップ

```
# VS Code の場合
# そのまま開発開始

# jupyter の場合
jupyter lab --ip 0.0.0.0 --no-browser --allow-root

# それ以外の場合
# Work内のファイルをそのまま編集する
```
