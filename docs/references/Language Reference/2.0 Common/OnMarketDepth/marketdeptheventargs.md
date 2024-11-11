---
title: MarketDepthEventArgs
pathName: marketdeptheventargs
parent: onmarketdepth
section: references
status: review
---

## Definition

Represents a change in level two market data also known as market depth and is passed as a parameter in the **OnMarketDepth()** method.

## Methods and Parameters

{% table %}

* Instrument
* IsReset
* MarketDataType
* MarketMaker
* Operation
* Position
* Price
* Time
* ToString()
* Volume

---

* A **Instrument** object representing the instrument of the market data
* A bool value representing if a UI reset is needed after a manual disconnect.  
Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset.
* Possible values are:  
**MarketDataType.Ask**  
**MarketDataType.Bid**
* A string representing the market maker id
* Represents the action you should take when building a level two book.  
Possible values are:  
**Operation.Add**  
**Operation.Update**  
**Operation.Remove**
* An **int** value representing the zero based position in the depth ladder.
* A **double** value representing the price
* A **DateTime** structure representing the time
* A string representation of the **MarketDataEventArgs** object
* A long value representing volume
{% /table %}

## Examples

```csharp
protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate)
{
     // Print some data to the Output window
     if (marketDepthUpdate.MarketDataType == MarketDataType.Ask && marketDepthUpdate.Operation == Operation.Update)
         Print("The most recent ask change is " + marketDepthUpdate.Price + " " + marketDepthUpdate.Volume);
}
```

{% callout type="note" %}

Tip: For an example of how to use **IsReset** please see \MarketAnalyzerColumns\AskPrice.cs

{% /callout %}
