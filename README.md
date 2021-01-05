# ATM Controller

[![Python][python_img]][python_url]

A coding test project implementing a mock ATM controller
for Bear Robotics Inc.

## Usage

Run the included `script.py` file.

## Flow

General controller flow is given as the following:

> Insert Card => Enter PIN Number => Select Account
> => See Balance/Deposit/Withdraw

To strictly follow the flow given, we make the following assumption:

* Single PIN number is tied to the inserted card and all accounts
  accessible via the card.
  * Although it may be possible to have different PINS tied to different
    accounts and have the entered PIN associated with a specific account,
    this needlessly complicates the flow and would be pretty bad for
    user experience as this would mean entering a PIN number *before*
    selecting an account.

The following is a rough overview of the flow:

![atm_controller_flow][atm_controller_flow]

Note that there are some details missing on how actions are handled.

## Session

A single session implements the flow described above.

* Once a new session is initiated, the ATM starts to wait for a card
  to be insered.
* Following the general flow, the session ends when the card is ejected
  from the ATM and is retrieved.

All information within a session should be ephemeral and be lost once
the session ends. The included script is a simple loop of running sessions.

## Notes

* Without an ATM API and/or a bank API, a sensible implementation of
  a controller is rather hard, since we do not know how much error handling
  should be delegated to other components.
* The implementation provided here is pretty lousy in terms of security.
  Initial PIN validation should serve only as initial authentication
  and subsequent transactions should use some sort of token scheme or
  encryption based on first authentication.
* General flow and display of information have been simplified greatly
  for convienence in terms of implementation.

[python_img]: https://img.shields.io/badge/Python-3.8.5-brightgreen.svg
[python_url]: https://www.python.org/

[atm_controller_flow]: ./docs/static/atm_controller_flow.png
