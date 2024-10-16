---
title: "Monitoring for and trading a breakout"
pathName: /docs/desktop/monitoring_for_and_trading_a_breakout
---

A common concept many traders use is the idea of a breakout. Points of interest are when the price breaks out from a consolidation range or from previous highs and lows.

## Key concepts in this example

- Determining and storing the first 30 bar high

- Submitting a long stop order to be filled when price breaks out from the 30 bar high

- Closing positions after a certain amount of bars have passed

- Resetting the 30 bar high at the start of every new trading session

## Important related documentation

- [IsFirstBarOfSession](/docs/desktop/isfirstbarofsession)

- [BarsSinceNewTradingDay](/docs/desktop/barssincenewtradingday)

- [BarsSinceEntryExecution()](/docs/desktop/barssinceentryexecution)

- [BarsSinceExitExecution()](/docs/desktop/barssinceexitexecution)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop

2. From the Control Center window, select the menu Tools > Import > NinjaScript

3. Select the downloaded file

[SampleBreakoutStrategy_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleBreakoutStrategy_NT8.zip)

{% callout type="note" %}
Make sure to follow the import process carefully to avoid any issues.
{% /callout %}

{% callout type="tip" %}
After importing the strategy, test it in a simulated environment before deploying it live.
{% /callout %}
