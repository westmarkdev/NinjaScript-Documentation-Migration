










 


Manipulating DateTime objects







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?manipulating_datetime_objects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Manipulating DateTime objects | [Previous page](getting_indicator_values_from_.htm)
[Return to chapter overview](indicator2.htm)










An essential element of any trader's strategies or indicators is time. You may find yourself wanting a high and low marker for a certain timeframe or you might want something drawn on your charts during those choppy lunch hours. DateTime objects are included in the .NET framework, and they can be used to do any time related action, like limiting trading hours or finding the highest high between 9:30AM and 10:30AM.


 


Key concepts in this example
----------------------------


•Common manipulation of DateTime objects

 


Important related documentation
-------------------------------


•[DateTime](https://learn.microsoft.com/en-us/dotnet/api/system.datetime?view=netframework-4.8)

•[DateTime.Add()](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.add?view=netframework-4.8)

•[DateTime.Compare()](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.compare?view=netframework-4.8)

•[DateTime.Now](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.now?view=netframework-4.8)

•[DateTime.TryParse()](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.tryparse?view=netframework-4.8)

•[TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan?view=netframework-4.8)

•[DateTime.ToString(string)](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.tostring?view=netframework-4.8)

•[string.Format()](https://learn.microsoft.com/en-us/dotnet/api/system.string.format?view=netframework-4.8)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleDateTimeFunctions\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleDateTimeFunctions_NT8.zip)





 
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
 
 
 



