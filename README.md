# ATM Controller

A coding test project implementing a mock ATM controller
for Bear Robotics Inc.

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

[atm_controller_flow]: ./docs/static/atm_controller_flow.png
