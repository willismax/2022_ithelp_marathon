import allure


@allure.story("輸出報表測試")  # 調用裝飾器註明此 test case 會被 allure 輸出
def test_export_report():
    with allure.step("開始運算"):  # 利用 allure.step 建立測試步驟，表示該步驟測試開始
        a = 1 + 1
        print(f"a 的數值為 {a}")  # 印出一些資訊，會被印在 allure 產生出的報表上

        b = 2 + 2
        print(f"b 的數值為 {b}")

        assert b > a  # 進行驗證
