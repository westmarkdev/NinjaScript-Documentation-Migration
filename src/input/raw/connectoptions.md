










 


ConnectOptions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connectoptions.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
ConnectOptions | [Previous page](connection.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


ConnectOptions is an abstract class used to configure options for a specific configured [Connection](connection.htm). An instance of ConnectOptions can be passed into the Connection.Connect() method to initiate a connection, as seen in the example below.


 




|  |
| --- |
| Note:  For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |



 


 


 


Properties accessible from an instance of ConnectOptions include:


 




|  |  |
| --- | --- |
| BrandName | A string representing the provider name |
| CanEnableHds | A bool determining the connection can use NinjaTrader Historical Data Servers. Related properties include HasHdsAlwaysEnabled and IsHdsEnabled |
| CanManageOrders | A bool determining orders can be managed on the Connection. Related properties include IsDataProviderOnly |
| Mode | A NinjaTrader.Cbi.Mode object representing the current mode of the connection (Mode.Live or Mode.Simulation) |
| Name | The user-configured name of the Connection |
| Provider | The provider configured in the Connection |




Examples
--------




| ns |
| --- |
| // Connecting to a configured connection
private Connection Connect(string connectionName)
{
   // Get the configured account connection by using the string passed into this custom Connect() method
   // We will lock the ConnectOptions collection to avoid in-flight changes causing any issues
   ConnectOptions connectOptions = null;
   lock (Core.Globals.ConnectOptions)
       connectOptions = Core.Globals.ConnectOptions.FirstOrDefault(o =&gt; o.Name == connectionName);
 
   // If connection is not already connected, connect to it
   lock (Connection.Connections)
       if (Connection.Connections.FirstOrDefault(c =&gt; c.Options.Name == connectionName) == null)
       {
           Connection connect = Connection.Connect(connectOptions);
 
           // Only return connection if successfully connected
           if (connect.Status == ConnectionStatus.Connected)
               return connect;
           else
               return null;
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
 
 
 



