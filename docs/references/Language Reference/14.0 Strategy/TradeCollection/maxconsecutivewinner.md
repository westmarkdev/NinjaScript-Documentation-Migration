---
title: MaxConsecutiveWinner
pathName: maxconsecutivewinner
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the maximum number of consecutive winners seen.

## Property Value

An **int** value that represents the maximum number of consecutive winners seen.

## Syntax

<`tradecollection`>.TradesPerformance.**MaxConsecutiveWinner**

## Examples

```csharp

protected override void OnBarUpdate()
{
     // Print out the max consecutive winners of all trades
     Print("Max # of consecutive winners is: " + SystemPerformance.AllTrades.TradesPerformance.MaxConsecutiveWinner);
}
```
