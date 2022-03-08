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

## Demoing the Server and Requests

1. **Setup your files.** You can follow along with an online environment using [binder]("https://mybinder.org/v2/gh/rzmk/fridges-api/HEAD") or locally by cloning/forking/downloading this repository.
2. **Build a new virtual environment.** Open a terminal (For binder: _File > New > Terminal_) and use commands like `virtualenv venv --python=python3` or `python -m venv venv` (may be `python3` for unix). You should see a `venv` folder generated.
3. **Activate your virtual environment.** On Windows I use `source venv\\Scripts\\activate`, another option is `source venv/bin/activate` (use this one on binder). You should see `(venv)` before your terminal prompt once activated successfully.
4. **Install required dependencies.** You can simply use `pip install -r requirements.txt` (may be `pip3` for unix). If you want to do so manually instead, do `pip install flask` for the API and `pip install requests` for the API requests script.
5. **Run the flask server.** You can do this by running the command `flask run`.
6. **Run api_test.py.** Open another terminal and run `python api_test.py` (may be `python3` for unix).

You should be able to see the requests run with outputs on the terminal running the server and the requests script! 🎉

Feel free to change values within `app.py` and `api_test.py`.

## File Details

- `app.py` - Flask API server, can be ran with command `flask run`.
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
