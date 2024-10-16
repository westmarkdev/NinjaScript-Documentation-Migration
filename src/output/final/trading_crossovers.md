---
title: "Trading Crossovers"
pathName: /docs/desktop/trading_crossovers
---

Similar in concept to a breakout, many traders like to trade crossovers. This can be a crossover of price from a certain threshold or even an indicator crossing over another indicator.

## Key Concepts in This Example

- Determining and storing the first 15 bar high and low values for the current session
- Submitting long or short entry orders depending on which threshold is crossed
- Using a trail stop to exit positions

{% callout type="tip" %}
This reference sample sets Calculate to OnEachTick. The reason we are doing this is so we can submit orders as soon as a crossover occurs instead of waiting for the bar to close before submitting the order.
{% /callout %}

## Important Related Documentation

- [Calculate](/docs/desktop/calculate)
- [CrossAbove()](/docs/desktop/crossabove)
- [CrossBelow()](/docs/desktop/crossbelow)
- [SetTrailStop()](/docs/desktop/settrailstop)
- [SetStopLoss()](/docs/desktop/setstoploss)
- [SetProfitTarget()](/docs/desktop/setprofittarget)

## Import Instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleHighLowCross_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleHighLowCross_NT8.zip)

