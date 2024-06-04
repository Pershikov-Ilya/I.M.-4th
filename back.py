import os

class SimpleFileSystem:
    def __init__(self, root_dir):
        if not isinstance(root_dir, (str, bytes, os.PathLike)):
            raise TypeError("root_dir should be string, bytes, or os.PathLike")
        self.root_dir = root_dir
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

    def show_info(self):
        num_files = sum([len(files) for r, d, files in os.walk(self.root_dir)])
        return f"Число файлов в системе: {num_files}"

    def create_file(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass
            return f"Файл '{file_name}' успешно создан."
        else:
            return f"Файл '{file_name}' уже существует."

    def read_file(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            return content
        else:
            return f"Файл '{file_name}' не найден."

    def write_file(self, file_name, content):
        file_path = os.path.join(self.root_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Файл '{file_name}' успешно записан."

    def delete_file(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"Файл '{file_name}' успешно удален."
        else:
            return f"Файл '{file_name}' не найден."

    def search_file(self, filename_or_file_content):
        found = False
        results = []
        for root, dirs, files in os.walk(self.root_dir):
            for name in files:
                if filename_or_file_content in name:
                    results.append(f"Найден файл: {name}")
                    found = True
        if not found:
            results.append("Файл(ы) не найдены.")
        return "\\n".join(results)

    def list_files(self):
        files_list = []
        for root, dirs, files in os.walk(self.root_dir):
            for name in files:
                files_list.append(name)
        return files_list