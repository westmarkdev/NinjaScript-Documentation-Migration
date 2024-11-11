---
title: ConnectionLossHandling
pathName: connectionlosshandling
parent: strategy
section: references
status: imported
---

## Definition

Sets the manner in which your strategy will behave when a connection loss is detected.

When using **ConnectionLossHandling.Recalculate**, recalculations will only occur if the strategy was stopped based on the conditions below. Should the connection be reestablished before the strategy was stopped, the strategy will continue running without recalculating as if no disconnect occurred.

* If data feed disconnects for longer than the time specified in [DisconnectDelaySeconds](disconnectdelayseconds), the strategy is stopped.
* If the order feed disconnects and the strategy places an order action while disconnected, the strategy is stopped.
* If both the data and order feeds disconnect for longer than the time specified in **DisconnectDelaySeconds**, the strategy is stopped.

## Property Value

An enum determining how the strategy will behave. Default value is set to

**ConnectionLossHandling.Recalculate**. Possible values are:

{% table %}

* **ConnectionLossHandling.KeepRunning**
* Keeps the strategy running. When the connection is reestablished the strategy will resume as if no disconnect occurred.

---

* **ConnectionLossHandling.Recalculate**
* Strategies will attempt to recalculate its strategy position when a connection is reestablished.

---

* **ConnectionLossHandling.StopStrategy**
* Automatically stops the strategy when disconnected for more than [DisconnectDelaySeconds](disconnectdelayseconds). No action will be taken when a connection is reestablished.
{% /table %}

## Syntax

ConnectionLossHandling

## Examples

```csharp

protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Keeps the strategy running as if no disconnect occurred
         ConnectionLossHandling = ConnectionLossHandling.KeepRunning;
     }
}
```
