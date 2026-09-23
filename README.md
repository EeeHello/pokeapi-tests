# PokéAPI Test Suite

A small pytest project testing the public PokéAPI (pokeapi.co)
Covers happy-path checks, response structure validation, and error handling (404 on invalid requests)

## Run it
pip install -r requirements.txt
pytest -v --html=report.html
