---
status: double_check
title: Sessions
parent: tradinghours
pathName: tradinghours_sessions
section: references
lg2m: true
---

## Definition

A collection of session definitions of the configured Trading Hours template.  

## Available Properties

{% table %}

* Parameter

* Description

---

* BeginDay

* A [DayOfWeek](https://msdn.microsoft.com/en-us/library/system.dayofweek(v=vs.90).aspx) value representing the begin day

---

* BeginTime

* An int value representing the begin time

---

* EndDay

* A [DayOfWeek](https://msdn.microsoft.com/en-us/library/system.dayofweek(v=vs.90).aspx) value representing the end day

---

* EndTime

* An int value representing the end time

---

* TradingDay

* A [DayOfWeek](https://msdn.microsoft.com/en-us/library/system.dayofweek(v=vs.90).aspx) value representing the trading day this session belongs to

---

{% /table %}

## Syntax  

**Bars.TradingHours.Sessions[int idx]**

{% callout type="note" %}

**Tip**:  Each index value will represent a new defined session for the Trading Hours template. For example, accessing Bars.TradingHours.Sessions[0] would provide you with information for the first trading session configured in the Trading Hours template:

- `Bars.TradingHours.Sessions[0].TradingDay = DayOfWeek.Monday`,  
- `Bars.TradingHours.Sessions[1].TradingDay = DayOfWeek.Tuesday`,  
- `Bars.TradingHours.Sessions[2].TradingDay = DayOfWeek.Wednesday`, etc.

{% /callout % }

## Examples

```csharp
// Print details for all sessions in the Trading Hours template  
for (int i = 0; i < TradingHours.Sessions.Count; i++)  
{  
  Print(String.Format("Session {0}: {1} at {2} to {3} at {4}", i, TradingHours.Sessions[i].BeginDay, TradingHours.Sessions[i].BeginTime,  
    TradingHours.Sessions[i].EndDay, TradingHours.Sessions[i].EndTime));  
}
```
