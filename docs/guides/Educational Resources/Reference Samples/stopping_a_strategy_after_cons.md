---
title: Stopping a strategy after consecutive losers
pathName: stopping_a_strategy_after_consecutive_losers
parent: reference_samples
section: guides
status: imported
---

## Stopping a strategy after consecutive losers

Trending days or ranging days can make or break a strategy. If you have a system that does extremely well on trending days, you may look for a way to turn that system off during range-bound days. A simple filter you may use could be something like, "If the last three trades were consecutive losers, stop trading for the rest of the session."

### Key concepts in this example

* Obtaining previous trade information to decide whether or not to keep trading for the day

### Important related documentation

* [SystemPerformance](systemperformance)
* [TradeCollection](tradecollection)
* [AllTrades](alltrades)
* [EnterLong()](enterlong)
* [ExitLong()](exitlong)
* [IsFirstBarOfSession](isfirstbarofsession)
* [IsFirstTickOfBar](isfirsttickofbar)

* This reference sample uses the **.AllTrades** property. This property will include all historical virtual trades as well as real-time trades. If you wish to only make calculations based on real-time trades you can use the **.RealtimeTrades** property.

### Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleTradeObjects_Nt8.zip](samples/SampleTradeObjects_Nt8.zip)
