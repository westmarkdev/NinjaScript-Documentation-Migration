---
title: DisconnectDelaySeconds
pathName: disconnectdelayseconds
parent: strategy
section: references
status: imported
---

## Definition

Determines the amount of time a disconnect would have to last before **connection loss handling** takes action.

## Property Value

An **int** value represents the time required for a disconnect to last before connection loss handling actions will occur. Default value is 10.

## Syntax

**DisconnectDelaySeconds**

## Examples

{% callout type="note" %}

protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Disconnect has to be at least 10 seconds
         **DisconnectDelaySeconds** = 10;
     }
}
{% /callout %}

```
