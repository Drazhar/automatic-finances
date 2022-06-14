import pytest
from os.path import exists, join
from os import remove

from src.Bank import Bank

class TestBank:
    BANK_NAME = "test"
    STORAGE_LOCATION = join("data", "banks", f"{BANK_NAME}.pickle")

    @pytest.fixture()
    def remove_data_files(self):
        if exists(self.STORAGE_LOCATION):
            remove(self.STORAGE_LOCATION)
        yield
        if exists(self.STORAGE_LOCATION):
            remove(self.STORAGE_LOCATION)


    def test_initialize_with_name(self, remove_data_files):
        test_bank = Bank(self.BANK_NAME)

        assert test_bank.name == self.BANK_NAME

    def test_initialize_without_name_error(self):
        """Should throw error, because a name is required!"""
        with pytest.raises(Exception):
            test_bank = Bank()

    def test_save_and_load_object(self, remove_data_files):
        """
        While a new bank object is created, it should load the saved information if available.
        If no information is available, a new file for storage should be created.
        """
        assert exists(self.STORAGE_LOCATION) is False

        test_bank = Bank(self.BANK_NAME)

        assert test_bank.storage_location == self.STORAGE_LOCATION
        assert exists(self.STORAGE_LOCATION) is True

        test_bank.some_data = "bla"

        test_bank.save()

        new_bank = Bank(self.BANK_NAME)
        assert new_bank.some_data == test_bank.some_data

