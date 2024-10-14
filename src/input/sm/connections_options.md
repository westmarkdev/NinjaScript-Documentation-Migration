










 


Options







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?connections_options.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Connection](connection_class.htm) &gt;
Options | [Previous page](disconnect.htm)
[Return to chapter overview](connection_class.htm)










Definition
----------


The connection's configuration options


 


Properties
----------




|  |  |
| --- | --- |
| ConnectOnStartup | A bool representing if this connection auto connects on startup |
| Name | A string representing the connection's name |
| Provider | A Provider representing the connection's provider |



 


 


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
               Connection.Connections.ToList().ForEach(c =&gt; NinjaTrader.Code.Output.Process(string.Format("Connection: {0} 
                   Provider: {1}", c.Options.Name, c.Options.Provider), PrintTo.OutputTab1);
     }
 
     // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
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
 
 
 



