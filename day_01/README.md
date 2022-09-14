# Python 與自動化測試的敲門磚_Day01_內容簡介

## 一、內容簡介
本次鐵人賽撰寫的目標為 python 與自動化測試，製作過程預計的時程如下

| 主題       | 日程          |
|:---------|:------------|
| 簡介       | day 01      |
| Pytest   | day 02 ~ 10 |
| TDD      | day 11 ~ 12 |
| Selenium | day 13 ~ 17 |
| Appium   | day 18 ~ 21 |
| CI/CD    | day 22 ~ 26 |
| Jenkins  | day 27 ~ 29 |
| 結語       | day 30      |

## 二、Pytest 簡介及撰寫方向
### (一)、Pytest 簡介
Pytest 是一種使用在 Python 語言裡面的一中單元測試框架，而 Pytest 基本上就是由 Python 原生自帶
的單元測試框架 Unittest 衍生出來的，所以可以看到有些範例可以和 Unittest 的套件互相兼容混用。

Pytest 和 Unittest 相比，有下列幾項優點：
1. 更易於上手，撰寫 testcase 時較為直覺
2. 擴展性高，可以兼容許多外掛套件
3. 可以標註某些 testcase 為失敗是正常的
4. 測試程式撰寫起來相較於 unittest 較為簡潔

### (二)、撰寫方向
本次鐵人賽針對 Pytest 的撰寫方向大約分為下面幾個目標：
1. Pytest 撰寫方式
2. Pytest 使用方式
3. Pytest Fixture 使用方式
4. Mongomock & In-memory SQLite
5. Pytest 的 SetUp and TearDown
6. Skip 和 Mark testcase
7. 利用 Pytest 產出報表

## 三、TDD 簡介及撰寫方向
### (一)、簡介
TDD 完整名稱為 Test-driven development，中譯為 "測試驅動開發"，是一種軟體開發的方式，
以這種模式開發的軟體，會需要在開發程式的同時一併撰寫測試程式，簡單來說就是一個 function
產出就要產出一個相對應的 testcase，好處是可以快速的檢查各項功能有沒有發生錯誤，也可以避免
在開發完成後再回來補血測試程式，造成某些功能遺漏沒有測到。

### (二)、撰寫方向
針對 TDD 開發模式的部分，會利用兩天的篇幅分別講解理論並且實作一份簡單的專案來進行展示。及撰寫方向及

## 四、Selenium 簡介以及撰寫方向
### (一)、簡介
相信很多人對於 Selenium 並不陌生，近年來很常被應用在網路爬蟲上，可以比較簡單的對動態網頁進行爬取，
而在這次的鐵人賽當中，我們要讓 Selenium 回歸本業，Selenium 最初被開發出來的時候，其實是拿來進行
網頁自動化測試的，下面將介紹本次鐵人賽 Selenium 的撰寫方向。

### (二)、撰寫方向
下面為本次鐵人賽中 Selenium 的撰寫方向：
1. 套件安裝與基本操作
2. 元素定位
3. 和 pytest 結合使用
4. Chrome extension 腳本錄製

## 五、Appium 簡介及撰寫方向
### (一)、簡介
Appium 顧名思義，適用於測試手機 APP 的一個自動化測試的工具，是一個 Open Source 的專案，Appium
提供跨平台的操作，亦即它可以同時測試 IOS 以及 Android 甚至是 Desktop 的 APP，本次的鐵人賽當中
會介紹該如何使用 Appium 對手機 APP 進行自動化測試。

### (二)、撰寫方向
1. 詳記介紹 & 安裝
2. 腳本錄製
3. 搭配 pytest 進行測試

## 六、CI/CD 簡介及撰寫方向
### (一)、簡介
CI/CD 是一種開發模式，其為兩個部分組成，分別為 CI 持續整合 & CD 持續部屬所組成，簡單來講就是將
程式測試、部屬自動化，可以加速軟體的開發並且由於在開發時每次對專案進行 commit 的時候都會依照寫好的
測試腳本對程式碼進行測試，也可以降低專案上線後發生錯誤的機率。

### (二)、撰寫方向
本次鐵人賽將針對下列這些方向進行撰寫：
1. CI/CD 概念探討
2. Github 和 CI
3. Gitlab 和 CI/CD

## 七、Jenkins 簡介及撰寫方向
### (一)、簡介
除了 Gitlab、Github 之外，Jenkins 也是目前主流的 CI/CD 工具之一，由於 Jenkins 也是開源專案，
因此發展速度非常快，也非常容易上手，這邊將花幾天的時間來介紹該如何進行 Jenkins 的操作以及環境的建置

### (二)、撰寫方向
1. Jenkins 安裝方式
2. Jenkins job 簡易使用方式
3. Jenkins 與 Python 的搭配