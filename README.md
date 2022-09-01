## Run project with docker:
    docker-compose -p airlines --file docker/dev/docker-compose.yml up -d --build


## URL: [post:] `http://localhost:8080/airplanes/api/`

## POST data format:
```json
[
    {
        "airplane_id":1,
        "passengers_count":100
    },
    {
        "airplane_id":2,
        "passengers_count":200
    }
]
```
## Response data:
```json
[
    {
        "user_id": 1,
        "airplane_id": 1,
        "passengers_count": 100,
        "fuel_consumption_per_minute": 0.2,
        "flight_limit_minutes": 1000.0
    },
    {
        "user_id": 1,
        "airplane_id": 2,
        "passengers_count": 200,
        "fuel_consumption_per_minute": 0.9545177444479562,
        "flight_limit_minutes": 419.0597841964052
    }
]
```
## OR 
```
## POST single data format:
```json

{
    "airplane_id": 1,
    "passengers_count": 100
}
```
## Response data:
```json
{
        "user_id": 1,
        "airplane_id": 1,
        "passengers_count": 100,
        "fuel_consumption_per_minute": 0.2,
        "flight_limit_minutes": 1000.0
   
``` 
## Check test coverage:
    docker exec -it airlines_web_1 bash
    coverage run --source='.' manage.py test airplane 
    coverage report
