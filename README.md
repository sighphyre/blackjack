# A Game of BlackJack

This is a simple game of BlackJack written in Python.

## Getting Started

You'll need a Python 3.8 interpreter if you want to run this.

Start by setting up a virtual environment:

`python3 -m venv venv`

Activate your virtual environment:

`source venv/bin/activate`

These commands are for a Linux system, if you're on another OS, you'll need to modify these for your use case.

Then you can install the requirements and the dev requirements:

`pip install -r requirements.txt`

`pip install -r dev-requirements.txt`

If you don't feel like doing any of this or hunting down a version of Python for this usecase then a docker file is provided. You can build it with:

`docker build . -t blackjack`

And then run it with:

`docker run blackjack`

The container uses an ENV var for specifying the URL, you can override it like this:

`docker run -e URL=<YOUR URL> blackjack`

You can run the tests from the root directory by invoking the following:

`python -m unittest discover test`

You can run the type checking by invoking:

`mypy app/`

Note that there are a few type errors currently. These are caused the type checker not being smart enough to discern the actual types but ideally these should be resolved in future work.

You can run the actual project by invoking:

`python main.py`

If you want to set an alternative URL for the card source this can be done by calling:

`python main.py --url <YOUR_URL>`

If you'd like to see the (limited) command line options you can call the following:

`python main.py -h`

## Notable Edge Cases And Missing Implementations

- Currently we've specified the value of an Ace to be 11, whereas in standard BlackJack rules this can either be an 11 or a 1
- Because of the above, it's possible that the dealer or player can hit to 22 on the draw. This will then cause the player to play out the second round and immediately go into a bust state
- Currently only a single player is specified and the name is hardcoded to my own name (Simon)

## Things That Need Doing

- Primary implementation is exercised through integration tests, this really needs some more unit testing along the core game logic
- The URL source for cards validates a URL but will reject an IP address. This is a half way option for now. Ideally we'd only accept HTTPS sources
- There's no authentication possible for the card API and this will raise an error if this is required
- Cards being returned from the card API are assumed to be deserialsed by the requests library in order, however the JSON spec does not guarantee this. This needs some unittesting and probably some fuzz testing to ensure that the card order is preserved correctly
