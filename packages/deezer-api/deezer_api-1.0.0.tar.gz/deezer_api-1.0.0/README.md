# DeezerAPI

A simple Python wrapper for the Deezer API, allowing easy access to a variety of Deezer's endpoints to fetch data about artists, albums, tracks, playlists, and more.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Importing and Initializing](#importing-and-initializing)
  - [Search for an Artist](#search-for-an-artist)
  - [Get Album Information](#get-album-information)
  - [Get Editorial Information](#get-editorial-information)
  - [Get Chart Information](#get-chart-information)
  - [Get Artist Information](#get-artist-information)
  - [Get Track Information](#get-track-information)
  - [Get Radio Stations](#get-radio-stations)
  - [Get Playlist Information](#get-playlist-information)
  - [Get Deezer Information](#get-deezer-information)
  - [Get Genres](#get-genres)
  - [Get User Information](#get-user-information)
- [Author and Contact Information](#author-and-contact-information)
- [Support the Project](#support-the-project)

## Introduction

DeezerAPI is a simple yet powerful Python wrapper for the Deezer API. It allows developers to easily access a wide range of endpoints provided by Deezer, enabling the retrieval of detailed information about artists, albums, tracks, playlists, and more. Whether you're building a music discovery app, analyzing musical trends, or just experimenting with the Deezer API, this module provides a convenient way to interact with Deezer's vast music database.

## Installation

To install the DeezerAPI module, simply use pip:


```bash
pip install deezer_api
```

## Usage

Below are examples of how to use the DeezerAPI module to access different types of data from Deezer.

### Importing and Initializing

```python
from deezer_api.deezer import DeezerAPI
```

### Initialize the API

```python
deezer = DeezerAPI()
```

### Search for an Artist
Search for an artist by name. For example, to search for "Eminem":

```python
results = deezer.search("eminem")
print(results)
```

### Get Album Information
Get information about a specific album by its ID. For example, to get the album with ID "302127":

```python
album_info = deezer.get_album("302127")
print(album_info)
```

### Get Editorial Information
Fetch the editorial information:

```python
editorial_info = deezer.get_editorial()
print(editorial_info)
```

### Get Chart Information
Fetch the chart information:

```python
chart_info = deezer.get_chart()
print(chart_info)
```

### Get Artist Information
Get information about a specific artist by their ID. For example, to get information about the artist with ID "27":

```python
artist_info = deezer.get_artist("27")
print(artist_info)
```

### Get Track Information
Get information about a specific track by its ID. For example, to get the track with ID "3135556":

```python
track_info = deezer.get_track("3135556")
print(track_info)
```

### Get Radio Stations
Fetch information about radio stations:

```python
radio_info = deezer.get_radio()
print(radio_info)
```
### Get Playlist Information
Get information about a specific playlist by its ID. For example, to get the playlist with ID "908622995":

```python
playlist_info = deezer.get_playlist("908622995")
print(playlist_info)
```
### Get Deezer Information
Fetch general information about Deezer:

```python
deezer_info = deezer.get_infos()
print(deezer_info)
```
### Get Genres
Fetch information about genres:

```python
genres_info = deezer.get_genre()
print(genres_info)
```

### Get User Information
Get information about a specific user by their ID. For example, to get information about the user with ID "5557228304":

```python
user_info = deezer.get_user("5557228304")
print(user_info)
```





## Author and Contact Information

**Name and Author**: Åndry RL  
**Username**: andryerics  
**Website**: [andryerics.com](https://www.andryerics.com)  
**WhatsApp**: [+261347262824](https://wa.me/261347262824)  

## Support the Project

If you find this project useful and would like to support its development, you can buy me a coffee:

- **PayPal**: [andryerica1@gmail.com](https://www.paypal.com/donate?business=andryerica1@gmail.com&item_name=Support+DeezerAPI+Development&currency_code=USD)

Thank you for your support!




# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.




