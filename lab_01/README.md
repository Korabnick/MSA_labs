# Лабораторная работа №1

### Инструкции по запуску в конце

## Содержание работы

Проектируем структуру backend приложения: 

1. Реализация распределения (балансировки) входящих запросов по эндпоинтам :heavy_check_mark:
2. Реализация протокола RPC для взаимодействия внутренних микросервисов :heavy_check_mark:
3. Реализация системы мониторинга (логи, метрики) с использованием Grafana :heavy_check_mark:

### Load Balancer (сервис балансировки)
- Должен принимать внешние запросы по протоколу HTTP :heavy_check_mark:
- POST запросы к эндпоинту /rpc проксируем в микросервис rpc-gateway :heavy_check_mark:
- GET запросы к эндпоинту /static проксируем в микросервис static-gateway :heavy_check_mark:

### RPC Gateway
- Должен принимать HTTP запросы с методом POST :heavy_check_mark:
- В теле запроса (body) передается JSON объект для вызова RPC метода: :heavy_check_mark:
```json
{
   "method":"<название RPC метода (функции)>",
   "data":{},
   "requestId":"<уникальный идентификатор запроса>"
}
```
- В поле "data" JSON-объекта передается набор параметров для выполнения :heavy_check_mark:
  
**ПРИМЕР**: допустим у вас есть функция, которая получает на вход массив чисел и суммирует все значения, тогда запрос может выглядеть вот так:
```json
{
   "method":"calc.summ",
   "data":{
      "args":[1,5,-8,156,-24]
   },
   "requestId":"5545abec-aab1-4efa-80ef-b3491cb4b6c5"
}
```
- В зависимости от названия метода, нужно проксировать запрос дальше в микросервис, который выполняет этот метод :heavy_check_mark:


# Инструкция:
## 1. Запустить команду:
```bash
docker compose up --build
```

## 2. Проверить запросы через Postman:
#### 1. 
   ```
   curl --location 'http://localhost/rpc' \
   --header 'Content-Type: application/json' \
   --data '{
   "method": "calc.summ",
   "data": {
      "args": [1, 2, 3]
   },
   "requestId": "123e4567-e89b-12d3-a456-426614174000"
   }'
   ```

#### 2. 
   ```
   curl --location 'http://localhost/static'
   ```

#### 3.
   ```
   curl --location 'http://localhost:5002/rpc' \
   --header 'Content-Type: application/json' \
   --data '{
   "method": "calc.summ",
   "data": {
      "args": [1, 2, 3]
   },
   "requestId": "123e4567-e89b-12d3-a456-426614174000"
   }'
   ```

#### 4.
   ```
   curl --location 'http://localhost:5000/rpc' \
   --header 'Content-Type: application/json' \
   --data '{
   "method": "calc.summ",
   "data": {
      "args": [1, 2, 3]
   },
   "requestId": "123e4567-e89b-12d3-a456-426614174000"
   }'
   ```


## 3. Grafana:
### ``` http://localhost:3000/ ```
