<div align="center" style="display:grid;place-items:center;">
<p>
    <img width="100" src="./src/x4tweaker/resources/x4tweaker.png" alt="Statusify Logo">
</p>

<h1>X4 Tweaker</h1>

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Orphoros/X4Tweaker?label=latest%20release)

![GitHub](https://img.shields.io/github/license/Orphoros/X4Tweaker)
![GitHub contributors](https://img.shields.io/github/contributors/Orphoros/X4Tweaker)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Orphoros/X4Tweaker)
![GitHub last commit](https://img.shields.io/github/last-commit/Orphoros/X4Tweaker)

<h4>Cross platform desktop mod template generator for X4: Foundations</h4>
</div>

<p align="middle">
    <img src="./img/x4-tweaker-macos-screenshot-v0.0.1.png" width="40%" />
</p>


## About

X4 Tweaker enables you to easily create your own mod configs for X4: Foundations with a simple desktop application.

> [!NOTE]
> This project is a work in progress and no releases are available yet. If you wish to use the tool, you can build it from the source code by cloning the repository and following the developer's guide.

## Supported Platforms

X4 Tweaker is available for the following platforms:

<p align="left">
    <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
    <img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" />
    <img src="https://img.shields.io/badge/Linux-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
</p>

## Technologies

<p align="left">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/BeeWare-666666?style=for-the-badge&logo=python&logoColor=white" />
</p>

## Developer's guide

### 0. Prerequisites

- Install Python 3.8+

### 1. Setup

#### Make a Python virtual environment:

<details><summary>macOS</summary>

```bash
python3 -m venv beeware-venv
```

</details>

<details><summary>Windows</summary>

```bash
py -m venv beeware-venv
```

</details>

<details><summary>Linux</summary>

```bash
python3 -m venv beeware-venv
```

</details>

#### Activate the virtual environment:

<details><summary>macOS</summary>

```bash
source beeware-venv/bin/activate
```

</details>

<details><summary>Windows</summary>

```bash
beeware-venv\Scripts\activate
```

</details>

<details><summary>Linux</summary>

```bash
source beeware-venv/bin/activate
```

</details>

#### Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run

Run in watch mode:

```bash
watchmedo auto-restart -p "*.py" -R briefcase dev
```

Run in dev mode:

```bash
briefcase dev
```

Run in production mode:

```bash
briefcase run -u
```

### 3. Update dependencies:

```bash
pip freeze > requirements.txt
```

### 4. Build the app:

Create the application scaffold

```bash
briefcase create
```

Build the application

```bash
briefcase build
```

Update the built application

```bash
briefcase update
```

---

## Disclaimer

> [!WARNING]
> X4 Tweaker is a fan-made tool for modifying X4: Foundations for educational purposes only. It is not affiliated with or endorsed by Egosoft. The purpose of this project is to demonstrate how cross platform desktop native applications can be built using Python and to educate the community by providing examples. This tool shall never be used for cheating in the game. Use it at your own risk.
