from pyairly import PyAirly


if __name__ == '__main__':
    apikey = open('apikey', 'r').readline()[:-1]
    airly = PyAirly(apikey, debug=True, accept_gzip_encoding=True)
    print(airly.get_installations_by_id(122))
    print(airly.get_installations_nearest(50.062006, 19.940984, 1, 2))

    print(airly.get_measurements_by_installation(122))
    print(airly.get_measurements_nearest(50.062006, 19.940984, 1))
    print(airly.get_measurements_for_point(50.062006, 19.940984))

    print(airly.get_meta_indexes())
    print(airly.get_meta_measurements())
