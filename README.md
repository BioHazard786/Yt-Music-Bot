[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BioHazard786/Yt-Music-Bot">
    <img src="images/Youtube Music.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">YT Music Bot</h3>

  <p align="center">
    A bot to download music from youtube and yt music links in best quality.
    <br />
    <br />
    <a href="https://t.me/ayane_san_bot">View Demo</a>
    ·
    <a href="https://github.com/BioHazard786/BookMyMovie/issues">Report Bug</a>
    ·
    <a href="https://github.com/BioHazard786/BookMyMovie/issues">Request Feature</a>
  </p>
</div>

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Features](#features)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

#### Required Variables

- `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

- `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)

- `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)

- `DUMP_CHANNEL`: Create a Telegram Channel. Get its ID from [Rose](https://t.me/MissRose_bot)

- `LOG_CHANNEL`: Create a Telegram Channel. Get its ID from [Rose](https://t.me/MissRose_bot)

- `MONGODB`: MongoDB Connection URL. Get this value from [MondoDB](https://mongodb.com)

#### Required Softwares

- `Python`: Get this from [python.org](https://www.python.org/downloads/)

- `FFmpeg`: Get this from [ffmpeg.org](https://www.ffmpeg.org/download.html)

### Installation

#### 1. Clone Repo

```bash
git clone https://github.com/BioHazard786/Yt-Music-Bot.git
```

#### 2. Setting up config.env file

- Create config.env file in root folder with the following [variables](#required-variables).

#### 2. Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Locally
python -m Ayane
```

#### 3. Running Locally using Docker

- Start Docker daemon (SKIP if already running, mostly you don't need to do this):

```bash
sudo dockerd
```

- Build Docker image:

```bash
sudo docker build . -t Ayane
```

- Run the image:

```bash
sudo docker run Ayane
```

- To stop the running image:

```bash
# Get running Image IDs
sudo docker ps

# Stop Docker Image
sudo docker stop id
```

## Features

- [x] Highest Quality music output in mp3
- [x] Metadata Embedded in music file with thumbnail
- [x] Inline searching
- [x] Dump Channel
- [x] Log Channel
- [x] Docker Support

## Built With

- [Pyrogram](https://pyrogram.org/) - The python telegram framework used

- [MongoDB](https://mongodb.com/) - The Database used

- [Yt-dlp](https://github.com/yt-dlp/yt-dlp) - A youtube-dl fork with additional features and fixes

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Mohd Zaid - [@LuLu786](https://t.me/LuLu786) - bzatch70@gmail.com

Project Link : [https://github.com/BioHazard786/Yt-Music-Bot](https://github.com/BioHazard786/Yt-Music-Bot)

## Acknowledgments

- Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
- Thanks to yt-dlp team for ther awesome [Library](https://github.com/yt-dlp/yt-dlp)
- Thanks To All Everyone In This Journey

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/BioHazard786/Yt-Music-Bot.svg?style=for-the-badge
[contributors-url]: https://github.com/BioHazard786/Yt-Music-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BioHazard786/Yt-Music-Bot.svg?style=for-the-badge
[forks-url]: https://github.com/BioHazard786/Yt-Music-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/BioHazard786/Yt-Music-Bot.svg?style=for-the-badge
[stars-url]: https://github.com/BioHazard786/Yt-Music-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/BioHazard786/Yt-Music-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/BioHazard786/Yt-Music-Bot/issues
[license-shield]: https://img.shields.io/github/license/BioHazard786/Yt-Music-Bot.svg?style=for-the-badge
[license-url]: https://github.com/BioHazard786/Yt-Music-Bot/blob/master/LICENSE
