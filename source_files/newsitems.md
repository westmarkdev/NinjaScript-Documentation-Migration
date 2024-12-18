﻿










 


NewsItems







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?newsitems.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
NewsItems | [Previous page](marketdepth.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


NewsItems can be used to store news articles.


 


Properties
----------




|  |  |
| --- | --- |
| Items | Collection of NewsEventArgs representing news articles |
| NewsToMaintain | An int representing the number of articles to maintain |
| Update() | For storing news articles |



 


Syntax
------


NewsItems


 


 


Example
-------




| ns |
| --- |
| /* Example of storing and accessing news items from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
     private NewsSubscription newsSubscription;
     private NewsItems        newsItems;
 
     public MyAddOnTab()
     {
          // Subscribe to news
          newsSubscription         = new NewsSubscription();
          newsSubscription.Update += OnNews;
          newsItems                = new NewsItems(10);
 
          // Print news
          PrintNews(newsItems);
     }
 
     // This method is fired as new News events come in. Old News events are not provided when you subscribe.
     private void OnNews(object sender, NewsEventArgs e)
     {
          // Store the news items
          newsItems.Update(e);
     }
 
     // Loop through the stored news articles and output them
     private void PrintNews(NewsItems news)
     {
         for (int x = 0; x &lt; news.Items.Count; x++)
          {
               NinjaTrader.Code.Output.Process(string.Format("ID: {0} News Provider: {1} Headline: {2}",
                    news.Items[x].Id,
                    news.Items[x].NewsProvider,
                    news.Items[x].Headline), PrintTo.OutputTab1);
          }
     }
 
     // Called by TabControl when tab is being removed or window is closed
     public override void Cleanup()
     {
          // Make sure to unsubscribe to the News subscription
        if (newsSubscription != null)
               newsSubscription.Update -= OnNews;
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
 
 
 



