---
title: Positions
pathName: positions
parent: account
section: references
status: imported
---

## Definition

Holds an array of **Position** objects that represent positions managed by the strategy. This property should only be used when your strategy is executing orders against **multiple instruments**.

Index value is based on the array of Bars objects added via the **AddDataSeries()** method. For example:

First Bars is ES 1 Minute  
Secondary Bars is ES 5 Minute  
Third Bars is NQ 5 Minute

**Positions[0]** == ES position  
**Positions[1]** == Always a flat position, ES position will always be **Positions[0]**  
**Positions[2]** == NQ position

{% table %}

* Tips:
* For single instrument scripts, please see **Position** object
* For a real-world Account Positions, please see **PositionsAccount**
{% /table %}

## Property Value

An array of **Position** objects.

## Syntax

**Positions[int index]**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         AddDataSeries("ES 09-14", BarsPeriodType.Minute, 5);
         AddDataSeries("NQ 09-14", BarsPeriodType.Minute, 5);
     }
}

protected override void OnBarUpdate()
{
     Print("ES position is " + Positions[0].MarketPosition);
     Print("NQ positions is " + Positions[2].MarketPosition);

     // Alternative approach. By checking what Bars object is calling the OnBarUpdate()
     // method, we can just use the Position property since its pointing to the correct
     // position.
     if (BarsInProgress == 0)
         Print("ES position is " + Position.MarketPosition);
     else if (BarsInProgress == 2)
         Print("NQ position is " + Position.MarketPosition);
}
```
