---
title: "IsNewSession()"
pathName: /docs/desktop/isnewsession
---

## Definition

Indicates a specified time is greater than the [ActualSessionEnd](/docs/desktop/actualsessionend) property on the configured Trading Hours template.

## Property Value

A bool value when true indicates the specified time is later than ActualSessionEnd; otherwise false.

## Parameters

|  |  |
| --- | --- |
| time | The DateTime value used to compare |
| includesEndTimeStamp | A bool determining if a timestamp of <n>:00 should fall into the current session. {% <br> %} (e.g., used for time based intraday series such as minute or second). |

## Syntax

```csharp
<sessioniterator>.IsNewSession(DateTime time, bool includesEndTimeStamp)
```

## Example

```csharp
bool takeTrades;
protected override void OnBarUpdate()
{
    // Switch a bool named takeTrades to false when IsNewSession() returns true.
    if (Bars.SessionIterator.IsNewSession(DateTime.Now, true))
    {
        Alert("EOS", Priority.Medium, String.Format("New session beginning. Waiting until {0} to begin trading again"), " ", 5, Brushes.Black, Brushes.White);
        takeTrades = false;
    }
    // Set the bool back to true on the first bar of the new session
    if (Bars.IsFirstBarOfSession)
        takeTrades = true;
}
```
