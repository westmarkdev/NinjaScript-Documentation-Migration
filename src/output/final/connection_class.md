---
title: "Connection"
pathName: /docs/desktop/connection_class
---

## Definition

The Connection class can be used to monitor connection related events as well as accessing connection related information.

## Static Connection Class Events and Properties

|  |  |
| --- | --- |
| [CancelAllOrders()](/docs/desktop/connection_cancelallorders) | Cancels all orders |
| [Connect()](/docs/desktop/connect) | Connects to a connection |
| [ConnectionStatusUpdate](/docs/desktop/connectionstatusupdate) | Event handler for connection status updates |

## Events and Properties from Connection instances

|  |  |
| --- | --- |
| [Accounts](/docs/desktop/account_class) | List of accounts from the connection |
| [Disconnect()](/docs/desktop/disconnect) | Disconnects from the connection |
| [Options](/docs/desktop/connections_options) | The connection's configuration options |
| [PriceStatus](/docs/desktop/connections_pricestatus) | A ConnectionStatus representing the status of the price feed. Possible values are: {% <br> %} ConnectionStatus.Connected{% <br> %} ConnectionStatus.Connecting{% <br> %} ConnectionStatus.ConnectionLost{% <br> %} ConnectionStatus.Disconnecting{% <br> %} ConnectionStatus.Disconnected |
| [Status](/docs/desktop/connections_status) | A ConnectionStatus representing the status of the order feed. Possible values are: {% <br> %} ConnectionStatus.Connected{% <br> %} ConnectionStatus.Connecting{% <br> %} ConnectionStatus.ConnectionLost{% <br> %} ConnectionStatus.Disconnecting{% <br> %} ConnectionStatus.Disconnected |

## Example

```csharp
// Example of accessing information on all connected connections
public class MyAddOnTab : NTTabPage
{
    public MyAddOnTab()
    {
        // Print information about all connected connections
        lock (Connection.Connections)
            foreach(Connection c in Connection.Connections)
                NinjaTrader.Code.Output.Process(string.Format("Connection: {0} Provider: {1}", c.Options.Name, c.Options.Provider), PrintTo.OutputTab1);
        // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
    }
}
```

