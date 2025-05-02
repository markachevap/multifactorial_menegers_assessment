чтобы скачать сайт и запустить его на ubuntu, вот это впишите в командную строку:

        git clone https://github.com/markachevap/multifactorial_menegers_assessment.git
        cd multifactorial_menegers_assessment
        chmod +x setup_ubuntu.sh
        ./setup_ubuntu.sh


для windows:
    Сохраните файл setup_windows.bat в удобном месте
    Двойной клик по файлу setup_windows.bat
    Нажмите "Да" при запросе UAC

После установки:

    Сервер будет доступен по адресу: http://localhost:8000
    Админ-панель: http://localhost:8000/admin
    Для остановки сервера: Ctrl+C в командной строке
