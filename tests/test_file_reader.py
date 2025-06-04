import pytest

from src.utils.file_reader import read_json_file


class TestFileReader:
    @pytest.fixture
    def tmp_json_file(self, tmp_path):
        """Фикстура для создания временных JSON-файлов"""
        def _create_file(content):
            file_path = tmp_path / "test.json"
            file_path.write_text(content, encoding='utf-8')
            return file_path
        return _create_file

    def test_valid_json_list(self, tmp_json_file):
        # Тест с валидным JSON-списком
        file_path = tmp_json_file('[{"id": 1}]')
        assert read_json_file(str(file_path)) == [{"id": 1}]

    def test_empty_file(self, tmp_json_file):
        # Тест с пустым файлом
        file_path = tmp_json_file('')
        assert read_json_file(str(file_path)) == []

    def test_json_object_not_list(self, tmp_json_file):
        # Тест с JSON-объектом (не список)
        file_path = tmp_json_file('{"id": 1}')
        assert read_json_file(str(file_path)) == []

    def test_file_not_found(self, tmp_path):
        # Тест с несуществующим файлом
        non_existent = tmp_path / "nonexistent.json"
        assert read_json_file(str(non_existent)) == []
