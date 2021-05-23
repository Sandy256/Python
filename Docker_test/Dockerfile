# Базовый образ из которого начинаем сборку
FROM python:3.9

# Выполнение команды при запуске
RUN mkdir -p C:\Python\Docker_test\app
# Определение рабочего каталог для контейнера
WORKDIR C:\Python\Docker_test\app
# Копирование из текущей дериктории в новую
COPY C:\Python\Docker_test C:\Python\Docker_test\app
# Определение того что нужно делать когда контейнер запуститься
CMD ["python", "app.py"]
# То же что CMD, но запуск без shell
# ENTRYPOINT ["python", "app.py"]