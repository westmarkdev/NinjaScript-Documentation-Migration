---
title: Disconnect()
pathName: disconnect
parent: connection_class
section: references
status: imported
---

## Definition

Disconnects from the data connection.

## Syntax

**<`connection`>.Disconnect()**

## Examples

```csharp
private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
   // If an execution triggers after 9pm, disconnect from the account's data source
   if (e.Time > new DateTime(now.Year, now.Month, now.Day, 21, 0, 0))
       myAccount.Connection.Disconnect();
}
```
