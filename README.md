<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rzmk/fridges-api">
    <img src="fridge.svg" alt="Fridge" width="80" height="80">
  </a>

  <h3 align="center">fridges-api</h3>
  <div align="center">
    <a href="#"><strong>Try this server using Binder! »</strong></a>
    <br />
  </div>
</div>

# Fridges API

A REST API of fridges with various foods like fruits built with Flask using Python.

Built from the Backend (**Rest APIs and FLASK**) Workshop by [@lucentfong](https://github.com/lucentfong) for [@HackRU](https://github.com/HackRU).

![Preview](preview.gif)

## File Details

- `api.py` - Flask API server, can be ran with command `flask run`.
- `api_test.py` - Various HTTP requests using the `requests` module to test the local flask server endpoints. You can also instead use [Postman](https://www.postman.com/) or [Thunder Client on VSCode](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client).
- `requirements.txt` - can be used with command `pip install -r requirements.txt` to install all virtual environment dependencies (run this command _after activating your virtual environment_). You can instead solely install `flask` for the server.

## Dependencies to Install

For the Flask server:

- `flask`

For the API testing script:

- `requests`

## Acknowledgements/Credits

- [@lucentfong](https://github.com/lucentfong)
- [@HackRU](https://github.com/HackRU)
