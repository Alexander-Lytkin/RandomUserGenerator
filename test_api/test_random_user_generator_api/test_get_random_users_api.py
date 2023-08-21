from common.types.user import AccountType


class TestGetRandomUsers:
    def test_get_users(self, api):
        res = api.get_users().structure(AccountType)
        assert res.status_code == 200
