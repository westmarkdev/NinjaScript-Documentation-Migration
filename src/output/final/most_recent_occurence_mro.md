---
title: "Most Recent Occurrence (MRO)"
pathName: /docs/desktop/most_recent_occurence_mro
---

## Definition

Returns the number of bars ago that the test condition evaluated to true within the specified look back period expressed in bars. The MRO() method starts from the current bar and works backwards from it.

{% callout type="note" %}
This method does NOT work on [multi-series](/docs/desktop/multi-time_frame__instruments) strategies and indicators.
{% /callout %}

## Method Return Value

An `int` value representing the number of bars ago. Returns a value of -1 if the specified test condition did not evaluate to true within the look-back period.

## Syntax

```csharp
MRO(Func<bool> condition, int instance, int lookBackPeriod)
```

{% callout type="warning" %}
1. The "instance" parameter MUST be greater than 0.  
2. The "lookBackPeriod" parameter MUST be greater than 0.  
3. Please check the Log tab for any other exceptions that may be thrown by the condition function parameter.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| condition | A true/false expression |
| instance | The occurrence to check for (1 is the most recent, 2 is the 2nd most recent, etc...) |
| lookBackPeriod | The number of bars to look back to check for the test condition. The test evaluates on the current bar and the bars within the look-back period. |

{% callout type="tip" %}
The syntax for the "condition" parameter uses [lambda expression](http://msdn.microsoft.com/en-us/library/bb397687.aspx) syntax.
{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Prints the high price of the most recent up bar over the last 10 bars (current bar + look back period's 9 bars before that)
    int barsAgo = MRO(() => Close[0] > Open[0], 1, 9);
    if (barsAgo > -1)
        Print("The bar high was " + High[barsAgo]);
}
```

See Also

[Least Recent Occurrence (LRO)](/docs/desktop/least_recent_occurence_lro)

