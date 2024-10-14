










 


Connection







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connection_class.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
Connection | [Previous page](barsrequest_mergepolicy.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


The Connection class can be used to monitor connection related events as well as accessing connection related information.


 


Static Connection Class Events and Properties
---------------------------------------------




|  |  |
| --- | --- |
| [CancelAllOrders()](connection_cancelallorders.htm) | Cancels all orders |
| [Connect()](connect.htm) | Connects to a connection |
| [ConnectionStatusUpdate](connectionstatusupdate.htm) | Event handler for connection status updates |



 


 


Events and Properties from Connection instances
-----------------------------------------------




|  |  |
| --- | --- |
| [Accounts](account_class.htm) | List of accounts from the connection |
| [Disconnect()](disconnect.htm) | Disconnects from the connection |
| [Options](connections_options.htm) | The connection's configuration options |
| [PriceStatus](connections_pricestatus.htm) | A ConnectionStatus representing the status of the price feed. Possible values are:
 
ConnectionStatus.Connected
ConnectionStatus.Connecting 
ConnectionStatus.ConnectionLost
ConnectionStatus.Disconnecting
ConnectionStatus.Disconnected |
| [Status](connections_status.htm) | A ConnectionStatus representing the status of the order feed. Possible values are:
 
ConnectionStatus.Connected
ConnectionStatus.Connecting 
ConnectionStatus.ConnectionLost
ConnectionStatus.Disconnecting
ConnectionStatus.Disconnected |



 


 


Example
-------




| ns |
| --- |
| // Example of accessing information on all connected connections
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
} |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



