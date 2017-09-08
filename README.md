# Gitlab Uploader file V1.0

Программа для создания новогое issue для проекта с приклеплением файла на gitlab.com

## Начало
Для работы с нашей программой нам понадобится:
- Python 2.7 или 3.5
- Виртуальное окружение
- Библиотеки sys, requests, datatime, optparse
- Проект на gitlab.com

##### Создания виртуального окружения
Чтобы создать виртуальное окружение, введите в терминале следующее:
```sh
$ virtualenv myenv # Создаем виртуальное окружение
$ source myenv/bin/activate # Активируем виртуальное окружение
```

##### Установка зависимостей
Теперь нам надо установить нужные зависимости для работы с нашей программой. Чтобы установить все зависимости которые нам нужны, введите в терминале следующее:
```sh
$ pip install -r requirements.txt # Установит все нужные нам зависимости
```

проверим все установленные зависимости в виртуальном окружении командой:
```sh
$ pip list
```
Вы должны получить следующее:
```sh
$ pip list
certifi (2017.7.27.1)
chardet (3.0.4)
idna (2.6)
pip (9.0.1)
requests (2.18.4)
setuptools (36.4.0)
urllib3 (1.22)
wheel (0.24.0)
```
## Работа с программой

### #1. Сгенерируем наш персональный токен на gitlab.com
1. Перейдем по [ссылке](https://gitlab.com/profile/personal_access_tokens) для генерации токена.
![](https://cdn1.savepice.ru/uploads/2017/9/7/4b29132615197796182a5f2bb1ad121e-full.png)
2. В поле **Name** введем имя нашего приватного токена
3. В поле **Expires at** назначим срок жизни токена
4. В **Scopes** отметим **api Access your API**
5. Сгенерируем наш ключ кликая на кнопку **Create personal access token**
После всех выполненых пунктов вы должны получить в поле **Your New Personal Access Token** ваш токен, у меня такой:
```sh
cvrw5LbxAkzy3yJsWyef
```


## Параметры
Доступные параметры для программы:

* **--gitlab_token** [ токен на gitlab.com ]
* **-f, --file** [ файл в текущей директории ]
* **-p, --project** [ ID проекта на gitlab.com ]
* **-t, --title** [ Заголовок issue ]

##### Пример

* --gitlab_token=**cvrw5LbxAkzy3yJsWyef** токен пользователя для доступа
* --file=**example-file.txt** файл который будет загружен на gitlab.com
* -project=**4072792** ID вашего проекта на gitlab.com2
* -title=**Issue** название вашего нового issue
### Пример использования программы
```sh
python gitlab-upload.py --gitlab_token=cvrw5LbxAkzy3yJsWyef --file example-file.txt --project 4072792 --title Issue
```