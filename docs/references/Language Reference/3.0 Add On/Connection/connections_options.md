---
title: Options
pathName: connections_options
parent: connection_class
section: references
status: changed
---

## Definition

The connection's configuration options

## Properties

{% table %}

* ConnectOnStartup
* Name
* Provider

---

* A bool representing if this connection auto connects on startup
* A string representing the connection's name
* A Provider representing the connection's provider
{% /table %}

## Examples

```csharp
// Example of accessing information on all connected connections
public class MyAddOnTab : NTTabPage
{
    public MyAddOnTab()
    {
        // Print information about all connected connections
        lock (Connection.Connections)
            Connection.Connections.ToList().ForEach(c => NinjaTrader.Code.Output.Process(string.Format("Connection: {0} Provider: {1}", c.Options.Name, c.Options.Provider), PrintTo.OutputTab1);
    }

    // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
}
```
