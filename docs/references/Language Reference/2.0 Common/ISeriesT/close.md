---
title: Close
pathName: close
parent: iseriest
section: references
status: review
---

## Definition

A collection of historical bar close prices.

## Property Value

A **ISeries`<double>`** type object. Accessing this property via an index value **int barsAgo** returns A **double** value representing the price of the referenced bar.

{% callout type="note" %}

When an indicator uses another indicator as input series, Close will represent the closing price of the input series' input series. For example, if MyCustomIndicator uses an ADX as input series, then referencing **Close[0]** in MyCustomIndicator will provide the Close price for the ADX's input series.

{% /callout %}

## Syntax

**Close**  

**Close[int barsAgo]**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Evaluates if the current close is greater than the prior bar close
     if (Close[0] > Close[1])
         Print("We had an up day");
}
```
