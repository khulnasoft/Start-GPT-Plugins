from .astronauts import get_coords_iss, get_num_astronauts


def test_astro():
    assert type(get_num_astronauts()) == int


def test_iss():
    latitude, longitude = get_coords_iss()
    assert type(latitude) == float
    assert type(longitude) == float
