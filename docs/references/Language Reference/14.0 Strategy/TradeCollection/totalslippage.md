---
title: TotalSlippage
pathName: totalslippage
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the total slippage.

## Property Value

A **double** value that represents the total slippage. This is presented in points, I.E. 0.25 for 1 execution on E-mini S&P 500 Futures.

## Syntax

<`tradecollection`>.TradesPerformance.**TotalSlippage**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the total slippage of all trades
     Print("Total slippage is: " + SystemPerformance.AllTrades.TradesPerformance.TotalSlippage);
}
```
