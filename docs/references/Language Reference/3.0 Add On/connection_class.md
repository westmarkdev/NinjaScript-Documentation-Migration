---
title: Connection
pathName: connection_class
status: imported
section: references
parent: add_on
---

## Definition

The Connection class can be used to monitor connection related events as well as accessing connection related information.

## Static Connection Class Events and Properties

{% table %}

* Method

* Description

---

* [CancelAllOrders()](connection_cancelallorders)

* Cancels all orders

---

* [Connect()](connect)

* Connects to a connection

---

* [ConnectionStatusUpdate](connectionstatusupdate)

* Event handler for connection status updates

---

{% /table %}

## Events and Properties from Connection instances

{% table %}

* Property

* Description

---

* [Accounts](account_class)

* List of accounts from the connection

---

* [Disconnect()](disconnect)

* Disconnects from the connection

---

* [Options](connections_options)

* The connection's configuration options

---

* [PriceStatus](connections_pricestatus)

* A ConnectionStatus representing the status of the price feed. Possible values are:

* ConnectionStatus.Connected

* ConnectionStatus.Connecting

* ConnectionStatus.ConnectionLost

* ConnectionStatus.Disconnecting

* ConnectionStatus.Disconnected

---

* [Status](connections_status)

* A ConnectionStatus representing the status of the order feed. Possible values are:

* ConnectionStatus.Connected

* ConnectionStatus.Connecting

* ConnectionStatus.ConnectionLost

* ConnectionStatus.Disconnecting

* ConnectionStatus.Disconnected

---

{% /table %}

## Examples

```csharp
// Example of accessing information on all connected connections  
public class MyAddOnTab : NTTabPage  
{  
  public MyAddOnTab()  
  {  
    // Print information about all connected connections  
    lock (Connection.Connections)  
      foreach(Connection c in Connection.Connections)  
          NinjaTrader.Code.Output.Process(string.Format("Connection: {0} Provider: {1}", c.Options.Name, c.Options.Provider), PrintTo.OutputTab1);  
   
    // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.  
  }  
}
```
