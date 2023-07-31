from typing import List

import attr


@attr.s
class PictureType:
    large: str = attr.ib()
    medium: str = attr.ib()
    thumbnail: str = attr.ib()


@attr.s
class Street:
    number: int = attr.ib()
    name: str = attr.ib()


@attr.s
class Coordinates:
    latitude: str = attr.ib()
    longitude: str = attr.ib()


@attr.s
class Timezone:
    offset: str = attr.ib()
    description: str = attr.ib()


@attr.s
class Dob:
    date: str = attr.ib()
    age: int = attr.ib()


@attr.s
class UserIdType:
    name: str = attr.ib()
    value: str = attr.ib()


@attr.s
class Location:
    street: Street = attr.ib()
    city: str = attr.ib()
    state: str = attr.ib()
    country: str = attr.ib()
    postcode: int = attr.ib()
    coordinates: Coordinates = attr.ib()
    timezone: Timezone = attr.ib()


@attr.s
class Login:
    uuid: str = attr.ib()
    username: str = attr.ib()
    password: str = attr.ib()
    salt: str = attr.ib()
    md5: str = attr.ib()
    sha1: str = attr.ib()
    sha256: str = attr.ib()


@attr.s
class Initials:
    title: str = attr.ib()
    first: str = attr.ib()
    last: str = attr.ib()


@attr.s
class RegistrationDataType:
    date: str = attr.ib()
    age: int = attr.ib()


@attr.s
class User:
    gender: str = attr.ib()
    name: Initials = attr.ib()
    location: Location = attr.ib()
    email: str = attr.ib()
    login: Login = attr.ib()
    dob: Dob = attr.ib()
    registered: RegistrationDataType = attr.ib()
    phone: str = attr.ib()
    cell: str = attr.ib()
    id: UserIdType = attr.ib()
    picture: PictureType = attr.ib()
    nat: str = attr.ib()


@attr.s
class InfoType:
    seed: str = attr.ib()
    results: int = attr.ib()
    page: int = attr.ib()
    version: str = attr.ib()


@attr.s
class AccountType:
    results: List[User] = attr.ib()
    info: InfoType = attr.ib()
