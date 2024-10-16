---
title: "ToTime()"
pathName: /docs/desktop/totime
---

## Definition

Calculates an integer value representing a time.

{% callout type="note" %}
Integer representation of time is in the format Hmmss where 7:30 AM would be 73000 and 2:15:12 PM would be 141512.
{% /callout %}

## Method Return Value

An int value representing a time structure.

## Syntax

```csharp
ToTime(DateTime time)
```

## ToTime(int hour, int minute, int second)

## Parameters

|  |  |
| --- | --- |
| time | A DateTime structure to calculate. Note: See also the [Time](/docs/desktop/time) property. |
| hour | An int value representing the hour used for the input. |
| minute | An int value representing the minute used for the input. |
| second | An int value representing the second used for the input. |

{% callout type="tip" %}
NinjaScript uses the .NET DateTime structure which can be complicated for novice programmers. If you are familiar with C# you can directly use DateTime structure properties and methods for date and time comparisons; otherwise, use this method and the [ToDay()](/docs/desktop/today) method.
{% /callout %}

## Examples

```csharp
// Only trade between 7:45 AM and 1:45 PM
if (ToTime(Time[0]) >= 74500 && ToTime(Time[0]) <= 134500)
{
    // Strategy logic goes here
}

// Store start time as an int variable to be compared
int startTime = ToTime(9, 30, 00); // 93000
// Only trade after 9:30 AM
if (ToTime(Time[0]) >= startTime)
{
    // Strategy logic goes here
}
```

