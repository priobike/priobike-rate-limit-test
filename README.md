# Rate limit test

This is a simple script which can be used to test the rate limit of a given service.

## Usage

- `FREQUENCY`: The number of requests per second
- `METHOD`: The HTTP method to use
- `URL`: The URL to send the requests to

```bash
FREQUENCY=10 METHOD=GET URL=https://priobike.vkw.tu-dresden.de/staging/load-service/static/load_response.json python3 fire_requests.py
```