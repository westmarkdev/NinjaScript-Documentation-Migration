---
title: ConnectOptions
pathName: connectoptions
parent: account
section: references
status: imported
---

## Definition

**ConnectOptions** is an abstract class used to configure options for a specific configured [Connection](connection). An instance of **ConnectOptions** can be passed into the **Connection.Connect()** method to initiate a connection, as seen in the example below.

{% callout type="note" %}

For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](developing_add_ons).

{% /callout %}

## Properties

Properties accessible from an instance of **ConnectOptions** include:

{% table %}

* BrandName
* CanEnableHds
* CanManageOrders
* Mode
* Name
* Provider

---

* A string representing the provider name
* A bool determining the connection can use NinjaTrader Historical Data Servers. Related properties include **HasHdsAlwaysEnabled** and **IsHdsEnabled**
* A bool determining orders can be managed on the Connection. Related properties include **IsDataProviderOnly**
* A **NinjaTrader.Cbi.Mode** object representing the current mode of the connection (**Mode.Live** or **Mode.Simulation**)
* The user-configured name of the Connection
* The provider configured in the Connection
{% /table %}

## Examples

```csharp
// Connecting to a configured connection
private Connection Connect(string connectionName)
{
    // Get the configured account connection by using the string passed into this custom Connect() method
    // We will lock the ConnectOptions collection to avoid in-flight changes causing any issues
    ConnectOptions connectOptions = null;
    lock (Core.Globals.ConnectOptions)
        connectOptions = Core.Globals.ConnectOptions.FirstOrDefault(o => o.Name == connectionName);
 
    // If connection is not already connected, connect to it
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
}
```
