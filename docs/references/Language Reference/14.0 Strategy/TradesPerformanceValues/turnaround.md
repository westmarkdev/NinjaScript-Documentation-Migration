---
status: double_check
title: Turnaround
parent: tradesperformancevalues
pathName: turnaround
section: references
lg2m: true
---

## Definition

Returns the amount of turnaround.  

## Property Value

A **double** value that represents the amount of turnaround.

## Syntax  

<`TradeCollection`>.TradesPerformance.<`TradesPerformanceValues`>.**Turnaround**

## Examples

```csharp
protected override void OnBarUpdate()  
{  
    // Print out the turnaround of all trades  
    Print("Turnaround of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.Turnaround);  
}
```
