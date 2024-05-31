CURRENT_OS = 'windows'  # 'windows', 'linux'


class FileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class WindowsFileDialog(FileDialog):
    def __init__(self, title, path, exts):
        super().__init__(title, path, exts)


class LinuxFileDialog(FileDialog):
    def __init__(self, title, path, exts):
        super().__init__(title, path, exts)


class FileDialogFactory:

    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(*args)
        if CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(*args)

    @staticmethod
    def create_windows_filedialog(*args):
        return WindowsFileDialog(*args)

    @staticmethod
    def create_linux_filedialog(*args):
        return LinuxFileDialog(*args)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg.__dict__)