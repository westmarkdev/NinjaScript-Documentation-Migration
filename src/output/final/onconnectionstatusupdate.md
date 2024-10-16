---
title: "OnConnectionStatusUpdate()"
pathName: /docs/desktop/onconnectionstatusupdate
---

## Definition

An event driven method used which is called for every change in connection status.

## Method Return Value

This method does not return a value.

## Syntax

```csharp
// You must override the method in your indicator with the following syntax:
protected override void OnConnectionStatusUpdate(ConnectionStatusEventArgs connectionStatusUpdate)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| connectionStatusUpdate | A [ConnectionStatusEventArgs](/docs/desktop/connectionstatuseventargs) object representing the most recent update in connection. |
| Status | Represents the status of the key adapter functionality. If the adapter supports live orders it will set Status to Disconnected when its order system is not connected. |
| PriceStatus | Represents the status of the price feed. |

## Examples

```csharp
// Prints the status of the order system
protected override void OnConnectionStatusUpdate(ConnectionStatusEventArgs connectionStatusUpdate)
{
    if (connectionStatusUpdate.Status == ConnectionStatus.Connected)
    {
        Print("Connected for orders at " + DateTime.Now);
    }
    else if (connectionStatusUpdate.Status == ConnectionStatus.ConnectionLost)
    {
        Print("Connection for orders lost at: " + DateTime.Now);
    }
}

// Prints the status of the price feed
protected override void OnConnectionStatusUpdate(ConnectionStatusEventArgs connectionStatusUpdate)
{
    if (connectionStatusUpdate.PriceStatus == ConnectionStatus.Connected)
    {
        Print("Connected to price feed at " + DateTime.Now);
    }
    else if (connectionStatusUpdate.PriceStatus == ConnectionStatus.ConnectionLost)
    {
        Print("Connection to price feed lost at: " + DateTime.Now);
    }
}
```
