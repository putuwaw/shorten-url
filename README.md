# ![](static/images/logo.svg) Shorten URL

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

Shorten URL is a free, simple, and open-source URL shortener. It is a web based application that allows you to shorten your long URLs.

## Features 💡

Using Shorten URL, you can:

- [x] Shorten your long URLs.
- [x] Create custom short URLs.

## Prerequisites 📋

- Python 3.10 or higher
- MySQL 8.0.32 or higher
- Node.js v18.13.0 or higher
- Docker 24.0.4 or higher (optional)
- docker-compose 1.29.2 or higher (optional)

## Installation 🛠

### Manual Installation

- Clone the repository:

```bash
git clone https://github.com/putuwaw/shorten-url.git
```

- Install the requirements:

```bash
make init
make install
```

- Create .env file and set the environment variables for database connection:

```bash
make env
```

- Install Tailwind CSS, configure it, and watch for changes:

```bash
make tw-install
make tw-watch
```

- Run the application:

```bash
make run
```

### Docker Installation

- Clone the repository:

```bash
git clone https://github.com/putuwaw/shorten-url.git
```

- Run docker-compose:

```bash
docker-compose up
```

## Contributing 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
