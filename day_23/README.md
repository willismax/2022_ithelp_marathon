# Python 與自動化測試的敲門磚_Day23_Github Actions yaml 介紹

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon)
如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

今天我們要來介紹用來控制 CI 流程的 yml 檔，我們採逐行介紹的方式進行

## 一、python-app.yml
為了方便大家對應程式碼，在開頭先放上 python-app.yml 全部內容

```yaml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
      
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        
    - name: Test with pytest
      run: |
        pytest -s -v ./day_22/test_demo.py
```

## 二、運行於指定的 branch 上
我們可以透過 on 參數來設定當哪個 branch 被推上 Github 上時要進行 CI 的動作，由於 CI 的進行也是需要耗費一定的資源，
因此不太可能讓所有瑣碎的 branch 被推上去時都自動進行一次，透過設定 branches 可以指定那些 branch 被推上來時要執行 CI

補充：可以看到 on 底下有分為 push 以及 pull_request 兩個層級，分別代表著 Github 上的兩種協作方式
```yaml
on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]
```

## 三、建立 CI 任務
- runs-on：為 CI 執行時最底下的一個 docker image 名稱，設定完成後 CI 會於執行時使用該 image 建立環境
- steps：為實際 CI 執行的細項，每一個細項開頭都會使用 "-" 來表示
- uses：為運行此 steps 時啟動的服務，為 docker image 名稱
- name：為此 step 的名稱
- run：為此 step 要執行的命令
```yaml
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
      
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    
    - name: Test with pytest
      run: |
        pytest -s -v ./day_22/test_demo.py
```

## 四、內容預告
今天我們介紹了在 github 上運行 Actions 所需要的 yaml 檔案該如何編輯，明天我們會進入到 GitLab 的 CI/CD 介紹，
明天會先介紹該如何建立 GitLab CI/CD 所需要的 runner