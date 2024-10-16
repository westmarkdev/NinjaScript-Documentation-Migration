---
title: "Resetting values at the beginning of new trading sessions"
pathName: /docs/desktop/resetting_values_at_the_beginn
---

Normally calculated values are carried over between trading sessions, but sometimes you may want to reset these values to begin a trading session fresh. The technique demonstrated in this reference sample can be useful to do things like resetting counters you may be running or clearing bool flags you may have set.

## Key concepts in this example

- Resetting a variable at the beginning of a new trading session
- Limiting the number of trades a strategy can make per trading session

## Important related documentation

- [IsFirstBarOfSession](/docs/desktop/isfirstbarofsession)
- [IsFirstTickOfBar](/docs/desktop/isfirsttickofbar)
- [EnterLong()](/docs/desktop/enterlong)
- [ExitLong()](/docs/desktop/exitlong)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

{% callout type="note" %}
For additional information, you can view the sample file here: [Sample Trade Limiter](https://helpguides.ninjatrader.com/nt8/samples/sampletradelimiter_nt8.zip).
{% /callout %}

