---
title: Block Volume
pathName: block_volume
parent: system_indicator_methods
section: references
status: review
---

## Description

Block volume detects block trades and display how many occurred per bar. This can be displayed either as trades or volume. Historical tick data is required to plot historically.

## Syntax

**BlockVolume(int blockSize, CountType countType)**

**BlockVolume(ISeries<`double`> input, int blockSize, CountType countType)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* Indicator source data

---

* blockSize
* The minimum volume a trade must be to be considered a block trade

---

* countType
* The format to count the block trades. By number of block trades that occurred or total block trade volume
{% /table %}

## Examples

```csharp
// A 1 tick data series must be added to OnStateChange() as this indicator runs off of tick data
else if (State == State.Configure)
{
   AddDataSeries(Data.BarsPeriodType.Tick, 1);
}
 
// Prints the current value of an 80 block trade size counted in volume for the Block Volume
if (BarsInProgress == 0)
{
double value = BlockVolume(80, CountType.Volume)[0];
Print("The current Block Volume value is " + value.ToString());
}
```
