---

title: highestbar
pathName: highestbar
created: Thursday, October 3rd 2024, 11:24:53 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Definition

Returns the number of bars ago the highest price value occurred within the specified look-back period.

## Method Return Value

An int value representing a value of bars ago.

## Syntax

```csharp
HighestBar(ISeries<double> series, int period)
```

## Parameters

|  |  |
| --- | --- |
| period | The number of bars to include in the calculation |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |

## Examples

```csharp
protected override void OnBarUpdate()
{   
   // store the highest bars ago value
   int highestBarsAgo = HighestBar(High, Bars.BarsSinceNewTradingDay);
   
   // evaluate high price from highest bars ago value
   double highestPrice = High[highestBarsAgo];         
   
   // Printed result: Highest price of the session: 2095.5 - occurred 24 bars ago
   Print(string.Format("Highest price of the session: {0} - occurred {1} bars ago", highestPrice, highestBarsAgo));            
}
```
