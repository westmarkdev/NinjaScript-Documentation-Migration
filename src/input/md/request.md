










 


Request()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?request.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [BarsRequest](barsrequest.htm) &gt;
Request() | [Previous page](barsrequest.htm)
[Return to chapter overview](barsrequest.htm)










Definition
----------


Performs the bars request for a [BarsRequest](barsrequest.htm) object


 


Syntax
------


BarsRequest.Request(Action<barsrequest, errorcode,="" string=""> callback)


 


Properties
----------




|  |  |
| --- | --- |
| BarsRequest | A BarsRequest representing the bars |
| ErrorCode | An ErrorCode representing error status |
| string | A string representing error message |



 


 


Example
-------




| ns |
| --- |
| // Request the bars
barsRequest.Request(new Action<barsrequest, errorcode,="" string="">((bars, errorCode, errorMessage) =&gt;
{
     if (errorCode != ErrorCode.NoError)
     {
         // Handle any errors in requesting bars here
         NinjaTrader.Code.Output.Process(string.Format("Error on requesting bars: {0}, {1}",
                                         errorCode, errorMessage), PrintTo.OutputTab1);
         return;
     }
 
     // Do something with the returned bars here.
     for (int i = 0; i &lt; bars.Bars.Count; i++)
     {
         // Output the bars
         NinjaTrader.Code.Output.Process(string.Format("Time: {1} Open: {2} High: {3} Low: {4} Close: {5} Volume: {6}",
                                         bars.Bars.GetTime(i),
                                         bars.Bars.GetOpen(i),
                                         bars.Bars.GetHigh(i),
                                         bars.Bars.GetLow(i),
                                         bars.Bars.GetClose(i),
                                         bars.Bars.GetVolume(i)), PrintTo.OutputTab1);
     }
})); |






 
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
 
 
 



</barsrequest,></barsrequest,>