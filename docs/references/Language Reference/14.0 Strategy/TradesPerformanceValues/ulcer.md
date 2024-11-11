---
status: double_check
title: Ulcer`
parent: tradesperformancevalues
pathName: ulcer
section: references
lg2m: true
---

## Definition

Returns the Ulcer.  

## Property Value

A **double** value that represents the Ulcer.

## Syntax  

<`TradeCollection`>.TradesPerformance.<`TradesPerformanceValues`>.**Ulcer**

## Examples

```csharp
protected override void OnBarUpdate()  
{  
    // Print out the Ulcer index of all trades  
    Print("Turnaround of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.Ulcer);  
}
```
