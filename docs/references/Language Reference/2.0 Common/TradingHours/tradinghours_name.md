---
status: double_check
title: Name
parent: tradinghours
pathName: tradinghours_name
section: references
lg2m: true
---

## Definition

Indicates the name of the trading hours template applied to the Bars series object.  
 

## Property Value

A **string** representing the name of the trading hours template.

## Syntax  

**Bars.TradingHours.Name**

## Examples

```csharp
protected override void OnBarUpdate()  
{                    
  Print(TradingHours.Name);  
  //Output if applied to the ES with 'use instrument settings':  CME US Index Futures ETH  
}
```
