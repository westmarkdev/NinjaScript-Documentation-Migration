---
title: TimeZoneInfo
pathName: timezoneinfo
parent: tradinghours
section: references
status: review
---

## Definition

Indicates a time zone that is configured by a Trading Hours template  

## Property Value

A **TimeZoneInfo** object that represents the time zone for a configured Trading Hours template.

## Syntax

**Bars.TradingHours.TimeZoneInfo**

## Examples

```csharp
// Print the timezone before printing all sessions
Print(String.Format("All sessions are in {0}", Bars.TradingHours.TimeZoneInfo));

// Print details for all sessions in the Trading Hours template
for (int i = 0; i < TradingHours.Sessions.Count; i++)
{
   Print(String.Format("Session {0}: {1} at {2} to {3} at {4}", i, TradingHours.Sessions[i].BeginDay, TradingHours.Sessions[i].BeginTime,
     TradingHours.Sessions[i].EndDay, TradingHours.Sessions[i].EndTime));
}
```
