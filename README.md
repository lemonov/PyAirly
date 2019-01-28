# PyAirly
Python binding of https://developer.airly.eu/ REST api

```python
    airly = PyAirly(apikey, debug=True, accept_gzip_encoding=True)
    print(airly.get_measurements_by_installation(122))
    print(airly.get_measurements_nearest(50.062006, 19.940984, 5))
    print(airly.get_measurements_for_point(50.062006, 19.940984))
    print(airly.get_meta_indexes())
    print(airly.get_meta_measurements())
```
