---
title: Resetting values at the beginning of new trading sessions
pathName: resetting_values_at_the_beginning_of_new_trading_sessions
parent: reference_samples
section: guides
status: imported
---

## Resetting values at the beginning of new trading sessions

Normally calculated values are carried over between trading sessions, but sometimes you may want to reset these values to begin a trading session fresh. The technique demonstrated in this reference sample can be useful to do things like resetting counters you may be running or clearing bool flags you may have set.

### Key concepts in this example

* Resetting a variable at the beginning of a new trading session
* Limiting the number of trades a strategy can make per trading session

### Important related documentation

* [IsFirstBarOfSession](isfirstbarofsession)
* [IsFirstTickOfBar](isfirsttickofbar)
* [EnterLong()](enterlong)
* [ExitLong()](exitlong)

### Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file
