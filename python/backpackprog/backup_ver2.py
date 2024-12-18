import os
import time


# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = [ r'"C:\Program Files\untitled4"' ]
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = r'C:\Program Files\backpack'  #Подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time .strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time .strftime('%H%M%S')

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) #создание каталога
    print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = r'""C:\Program Files\GnuWin32\bin\zip.exe" zip  -r  {0} {1}"'.format(target,' '.join(source))


# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
