from unittest.mock import MagicMock, patch
import pandas as pd

from src.file_readers.universal_reader import read_csv_file, read_excel_file

class TestUniversalReader:
    @patch('pandas.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        mock_data = MagicMock()
        mock_data.to_dict.return_value = [{'id': 1, 'amount': 100.0}]
        mock_read_csv.return_value = mock_data

        result = read_csv_file()  # без аргументов
        assert result == [{'id': 1, 'amount': 100.0}]
        mock_read_csv.assert_called_once()

    @patch('pandas.read_excel')
    def test_read_excel_file(self, mock_read_excel):
        mock_data = MagicMock()
        mock_data.to_dict.return_value = [{'id': 2, 'amount': 200.0}]
        mock_read_excel.return_value = mock_data

        result = read_excel_file()  # без аргументов
        assert result == [{'id': 2, 'amount': 200.0}]
        mock_read_excel.assert_called_once()

    @patch('pandas.read_csv')
    def test_read_csv_file_empty(self, mock_read_csv):
        mock_read_csv.side_effect = pd.errors.EmptyDataError
        result = read_csv_file()  # без аргументов
        assert result == []

    @patch('pandas.read_excel')
    def test_read_excel_file_empty(self, mock_read_excel):
        mock_read_excel.side_effect = pd.errors.EmptyDataError
        result = read_excel_file()  # без аргументов
        assert result == []
