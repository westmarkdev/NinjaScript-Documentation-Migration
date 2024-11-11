---
status: double_check
pathName: values
title: Values
parent: priceseries
section: references
lg2m: true
---

## Definition

Holds an array of **ISeries<`double`>** objects holding hold the indicator's underlying calculated values. ISeries<`double`> values are added to this array when calling the [AddPlot()](addplot) method. In case of a [MultiSeries](multi_time_frame_instruments.md) indicator synched to the primary series.

## Property Value

A collection of **ISeries<`double`>** objects.

## Syntax

**Values[int index]**

## Examples

```csharp
// OnBarUpdate method of a custom indicator  
protected override void OnBarUpdate()  
{  
    // Ensures we have enough bars loaded for our indicator  
    if (CurrentBar < 1)  
        return;  
   
    // Evaluates the indicator's secondary value 1 bar ago and sets the value of the indicator  
    // for the current bar being evaluated  
    if (Values[1][1] < High[0] - Low[0])  
        Value[0] = High[0] - Low[0];  
    else  
        Value[0] = High[0] - Close[0];  
}
```
