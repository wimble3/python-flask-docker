FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "telethon", "run"]