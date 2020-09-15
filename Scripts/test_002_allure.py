import allure

class Test_001:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test_001(self):
        print('\n test_001')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        print('\n test_002')
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        print('\n test_003')

    @allure.severity(allure.severity_level.MINOR)
    def test_004(self):
        print('\n test_004')

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_005(self):
        print('\n test_005')