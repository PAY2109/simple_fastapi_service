# Simple FastAPI service
 
A simple FastAPI service with a single handle.

## Usage

1. Clone or download the repository.
2. Build the Docker image:
```bash
docker build -t simple-fastapi-service .
```
3. Run the container with:
```bash
docker run -p 80:80 simple-fastapi-service
```
The server will be running on port 80.   
The handle`s address would be http://0.0.0.0:80/deposit/calculate/
## Example call
Request json:
```json
{
	"date": "31.01.2021",
	"periods": 3,
	"amount": 10000,
	"rate": 6
}
```
Response json:
```json
{
	"31.01.2021": 10050.0,
	"28.02.2021": 10100.25,
	"31.03.2021": 10150.75
}
```