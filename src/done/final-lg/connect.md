---
title: "Connect()"
pathName: connect
---

## Definition

Connects to a connection.

## Syntax

`Connection.Connect(ConnectOptions options)`

## Parameters

|  |  |
| --- | --- |
| options | The connection option of what you want to connect to |

## Example

```csharp
/* Example of subscribing/unsubscribing to execution update events from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
    private Connection connection;
    
    public MyAddOnTab()
    {
        // Connect to Kinetick EOD
        if (connection == null)
            connection = Connect("Kinetick - End Of Day (Free)");
    }

    private Connection Connect(string connectionName)
    {
        // Output the execution
        try
        {
            // Get the configured account connection
            ConnectOptions connectOptions = null;
            lock (Core.Globals.ConnectOptions)
                connectOptions = Core.Globals.ConnectOptions.FirstOrDefault(o => o.Name == connectionName);
            if (connectOptions == null)
            {
                NinjaTrader.Code.Output.Process("Could not connect. No connection found.", PrintTo.OutputTab1);
                return null;
            }
            // If connection is not already connected, connect.
            lock (Connection.Connections)
                if (Connection.Connections.FirstOrDefault(c => c.Options.Name == connectionName) == null)
                {
                    Connection connect = Connection.Connect(connectOptions);
                    // Only return connection if successfully connected
                    if (connect.Status == ConnectionStatus.Connected)
                        return connect;
                    else
                        return null;
                }
            return null;
        }
        catch (Exception error)
        {
            NinjaTrader.Code.Output.Process("Connect exception: " + error.ToString(), PrintTo.OutputTab1);
            return null;
        }
    }

    // Called by TabControl when tab is being removed or window is closed
    public override void Cleanup()
    {
        // Disconnect from our connection
        if (connection != null)
            connection.Disconnect();
    }

    // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
}
```
