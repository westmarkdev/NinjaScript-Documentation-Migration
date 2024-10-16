---
title: "ConnectionLossHandling"
pathName: /docs/desktop/connectionlosshandling
---

## Definition

Sets the manner in which your strategy will behave when a connection loss is detected.

When using `ConnectionLossHandling.Recalculate`, recalculations will only occur if the strategy was stopped based on the conditions below. Should the connection be reestablished before the strategy was stopped, the strategy will continue running without recalculating as if no disconnect occurred.

1. If data feed disconnects for longer than the time specified in [DisconnectDelaySeconds](/docs/desktop/disconnectdelayseconds), the strategy is stopped.
2. If the order feed disconnects and the strategy places an order action while disconnected, the strategy is stopped.
3. If both the data and order feeds disconnect for longer than the time specified in [DisconnectDelaySeconds](/docs/desktop/disconnectdelayseconds), the strategy is stopped.

## Property Value

An enum determining how the strategy will behave. Default value is set to `ConnectionLossHandling.Recalculate`. Possible values are:

|  |  |
| --- | --- |
| `ConnectionLossHandling.KeepRunning`  | Keeps the strategy running. When the connection is reestablished the strategy will resume as if no disconnect occurred. |
| `ConnectionLossHandling.Recalculate` | Strategies will attempt to recalculate its strategy position when a connection is reestablished. |
| `ConnectionLossHandling.StopStrategy` | Automatically stops the strategy when disconnected for more than [DisconnectDelaySeconds](/docs/desktop/disconnectdelayseconds). No action will be taken when a connection is reestablished. |

## Syntax

```csharp
ConnectionLossHandling
```

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
