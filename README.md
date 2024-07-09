# priobike-rate-limit-test

This is a simple script which can be used to test the rate limit of a given service.

In the PrioBike deployment we use(d) this to test the rate limit middleware of our Traefik proxy.

[Learn more about PrioBike](https://github.com/priobike)

## Quickstart

```bash
FREQUENCY=10 METHOD=GET URL=https://priobike.vkw.tu-dresden.de/staging/load-service/static/load_response.json python3 fire_requests.py
```

- `FREQUENCY`: The number of requests per second
- `METHOD`: The HTTP method to use
- `URL`: The URL to send the requests to

## Contributing

We highly encourage you to open an issue or a pull request. You can also use our repository freely with the `MIT` license. 

## Anything unclear?

Help us improve this documentation. If you have any problems or unclarities, feel free to open an issue.
