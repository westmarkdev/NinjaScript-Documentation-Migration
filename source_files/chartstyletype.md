










 


ChartStyleType







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartstyletype.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
ChartStyleType | [Previous page](barwidthui.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


Defines a unique identifier value used to register a custom ChartStyle.  There are 11 default ChartStyles which come with NinjaTrader which are reserved per the table on this page under the Parameters section of this page.


 




|  |
| --- |
| Note: The ChartStyle property can allow a large number of ChartStyles to be registered on a single user's installation (up to 2,147,483,647).  However it's important to note that it is still possible for two installed ChartStyles on a user's computer to conflict should they be register to the same enumerator value. In this case, NinjaTrader will ignore the conflicting ChartStyle type and information pertaining to this conflict will be displayed on the [Log tab](log_tab2.htm) of the  NinjaTrader Control Center.
 
Added 1/31/2018 : We advise users to use values larger then 1023 when selecting an enum. As NinjaTrader from time to time may add a new enum value in that range which may cause conflicts.    |



 


Property  Value
---------------


A enum value representing the ChartStyle to be registered. 


 




|  |
| --- |
| Tip: It is recommended to pick high, unique enumeration value to avoid conflict from other ChartStyles that may be used by a single installation.   |



 


Syntax
------


You must cast ChartStyleType from an int using the following syntax:


(ChartStyleType) 80;


 


 
Parameters
------------


Reserved enumeration values are listed below:


 




|  |  |
| --- | --- |
| 0 | Box |
| 1 | CandleStick |
| 2 | LineOnClose |
| 3 | OHLC |
| 4 | PointAndFigure |
| 5 | KagiLine |
| 6 | OpenClose |
| 7 | Mountain |
| 8 | Volumetric |
| 9 | HollowCandleStick |
| 10 | Equivolume |




 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name           = "Example ChartStyle";            
     ChartStyleType = (ChartStyleType) 80;
     BarWidth       = 1;
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
 
 
 



