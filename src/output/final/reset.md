---
title: "Reset()"
pathName: /docs/desktop/reset
---

## Definition

Resets the internal marker which is used for [IsValidDataPoint()](/docs/desktop/isvaliddatapoint) back to false. Calling the Reset() method is unique and can be very powerful for custom indicator development. [Series&lt;t&gt;](/docs/desktop/seriest) objects will always contain a value which is assigned, however calling Reset() simply means you effectively ignore the value of the current bar for plotting purposes. For calculation purposes you will want to use [IsValidDataPoint()](/docs/desktop/isvaliddatapoint) to ensure you are not calculating off of any reset values assigned by the Reset() method.

|  |  |
| --- | --- |
| Series Type | Value after Reset() |
| Series&lt;bool&gt; | false |
| Series&lt;double&gt; | 0.00 |
| Series&lt;datetime&gt; | DateTime.MinValue |
| Series&lt;float&gt; | 0 |
| Series&lt;int&gt; | 0 |
| Series&lt;long&gt; | 0 |
| Series&lt;string&gt; | null |

## Method Return Value

This method does not return a value.

## Syntax

```
Reset()
Reset(int barsAgo)
```

## Parameters

|  |  |
| --- | --- |
| barsAgo | An `int` representing from the current bar the number of historical bars the method will check. If no barsAgo value is supplied, the current bar value will be reset instead (barsAgo 0). |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // set MyPlot to Low of current bar minus 1 tick
    MyPlot[0] = Low[0] - (1 * TickSize);
    //reset MyPlot every 10 bars
    if(CurrentBar % 10 == 0)
        MyPlot.Reset();
    // only calculate MyPlot value if it has not been reset
    if(MyPlot.IsValidDataPoint(0))
        Print(CurrentBar + " Value is: " + MyPlot[0]);
}
```
