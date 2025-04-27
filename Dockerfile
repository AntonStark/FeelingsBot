# Первая стадия: билд-зависимости
FROM python:3.10.0-slim as builder

WORKDIR /app

COPY requirements.txt .
# Ключ --user говорит pip установить зависимости в пользовательскую
# папку /root/.local/ вместо системной /usr/local/lib/pythonX.Y/
RUN pip install --user --no-cache-dir -r requirements.txt

# Вторая стадия: только рабочее приложение
FROM python:3.10.0-slim

WORKDIR /app

# Копируем только установленные библиотеки из первой стадии
COPY --from=builder /root/.local /root/.local
COPY feelings_bot/ feelings_bot/

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/:$PYTHONPATH

CMD ["python3", "feelings_bot/main.py"]
