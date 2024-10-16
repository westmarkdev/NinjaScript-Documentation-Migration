---
title: "Backtesting NinjaScript Strategies with an intrabar granularity"
pathName: /docs/desktop/backtesting_ninjascript_strate
---

You can submit orders to different Bars objects. This allows you the flexibility of submitting orders to different timeframes. Like in live trading, taking entry conditions from a 5min chart means executing your order as soon as possible instead of waiting until the next 5min bar starts building. You can achieve this by submitting your orders to a more granular secondary bar series to achieve an "intrabar" fill.

## Key concepts in this example

- Finding entry conditions on the primary bar object

- Submitting orders to the secondary bar object for an intrabar fill

## Important related documentation

- [AddDataSeries()](/docs/desktop/adddataseries)

- [BarsInProgress](/docs/desktop/barsinprogress)

- [EnterLong()](/docs/desktop/enterlong)

- [BarsArray](/docs/desktop/barsarray)

- [EnterLongLimit()](/docs/desktop/enterlonglimit)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleIntrabarBacktest_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleIntrabarBacktest_NT8.zip)

