---
title: "Rounding values to the nearest tick size"
pathName: /docs/desktop/rounding_values_to_the_nearest
---

When NinjaTrader receives a request to submit an order, it automatically rounds any limit price or stop price to the nearest tick for that specific instrument.

When debugging and/or printing out order information, this may not be apparent. NinjaTrader includes a method named [RoundToTickSize()](/docs/desktop/roundtoticksize) to apply the same internal rounding to any value you wish, which can help make comparisons easier.

## Key concepts in this example

- Rounding a value to the nearest tick

## Important related documentation

- [RoundToTickSize()](/docs/desktop/roundtoticksize)  
- [EnterLongLimit()](/docs/desktop/enterlonglimit)  
- [ExitLong()](/docs/desktop/exitlong)  
- [CrossAbove()](/docs/desktop/crossabove)  
- [CrossBelow()](/docs/desktop/crossbelow)  

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleRoundToTickSize_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleRoundToTickSize_NT8.zip)
