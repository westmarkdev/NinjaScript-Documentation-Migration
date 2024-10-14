










 


Manipulating string objects







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?manipulating_string_objects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Manipulating string objects | [Previous page](manipulating_datetime_objects.htm)
[Return to chapter overview](indicator2.htm)










Dealing with strings and other related concepts are essential to many computer programs. This sample is a collection of some of the most common string and text related functions including splitting a string, replacing a string with another string, and a few other string functions.


 


Key concepts in this example
----------------------------


•Simple text/string manipulation ideas

 


Important related documentation
-------------------------------


C#


•[string.IndexOf()](https://learn.microsoft.com/en-us/dotnet/api/system.string.indexof?view=netframework-4.8)

•[string.Replace()](https://learn.microsoft.com/en-us/dotnet/api/system.string.replace?view=netframework-4.8)

•[string.Split()](https://learn.microsoft.com/en-us/dotnet/api/system.string.split?view=netframework-4.8)

•[Escape characters](http://msdn.microsoft.com/en-us/library/h21280bw.aspx)

•[Foreach iterator](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements)

•[String literals](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/strings/)

NinjaTrader


•[ClearOutputWindow()](http://www.ninjatrader.com/support/helpGuides/nt8/en-us/clearoutputwindow.htm?zoom_highlightsub=ClearOutputWindow)

 




|  |
| --- |
| Note: A related sample demonstrating how to format numbers can be found [here](formatting_numbers.htm). |



 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleStringFunctions\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleStringFunctions_NT8.zip)





 
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
 
 
 



