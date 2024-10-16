---
title: "Stopping a strategy after consecutive losers"
pathName: /docs/desktop/stopping_a_strategy_after_cons
---

Trending days or ranging days can make or break a strategy. If you have a system that does extremely well on trending days, you may look for a way to turn that system off during range-bound days. A simple filter you may use could be something like, "If the last three trades were consecutive losers, stop trading for the rest of the session."

## Key concepts in this example

- Obtaining previous trade information to decide whether or not to keep trading for the day

## Important related documentation

- [SystemPerformance](/docs/desktop/systemperformance)
- [TradeCollection](/docs/desktop/tradecollection)
- [AllTrades](/docs/desktop/alltrades)
- [EnterLong()](/docs/desktop/enterlong)
- [ExitLong()](/docs/desktop/exitlong)
- [IsFirstBarOfSession](/docs/desktop/isfirstbarofsession)
- [IsFirstTickOfBar](/docs/desktop/isfirsttickofbar)

{% callout type="note" %}
This reference sample uses the .AllTrades property. This property will include all historical virtual trades as well as real-time trades. If you wish to only make calculations based on real-time trades you can use the .RealtimeTrades property.
{% /callout %}

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleTradeObjects_Nt8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleTradeObjects_Nt8.zip)
