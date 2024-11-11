---
title: Rounding values to the nearest tick size
pathName: rounding_values_to_the_nearest_tick_size
parent: reference_samples
section: guides
status: imported
---

## Rounding values to the nearest tick size

When NinjaTrader receives a request to submit an order, it automatically rounds any limit price or stop price to the nearest tick for that specific instrument.

When debugging and/or printing out order information, this may not be apparent. NinjaTrader includes a Method named **RoundToTickSize** to apply the same internal rounding to any value you wish, which can help make comparisons easier.

## Key concepts in this example

* Rounding a value to the nearest tick

## Important related documentation

* [RoundToTickSize()](roundtoticksize)
* [EnterLongLimit()](enterlonglimit)
* [ExitLong()](exitlong)
* [CrossAbove()](crossabove)
* [CrossBelow()](crossbelow)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleRoundToTickSize_NT8.zip](samples/SampleRoundToTickSize_NT8.zip)
