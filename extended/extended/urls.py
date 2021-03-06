from django.conf.urls import patterns
from stats import views, cookies, imgviews

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^consistency/(.*)', views.consistency),
    (r'^sgoyt/(.*)', views.sgoyt),
    (r'^playlogging/(.*)', views.playLogging),
    (r'^dimesbydesigner/(.*)', views.dimesByDesigner),
    (r'^selections/(.*)', views.viewSelections),
    (r'^selector/(.*)', views.selector),
    (r'^collection/(.*)', views.collection),    
    (r'^collections/(.*)', views.manageCollections),
    (r'^editCollection/(.*)', views.editCollection),
    (r'^deleteCollection/(.*)', views.deleteCollection),
    (r'^viewCollection/(.*)', views.viewCollection),
    (r'^saveManageCollection/$', views.saveManageCollection),
    (r'^submit/$', views.ajaxSubmit),
    (r'^calendar/(.*)', views.gamesCalendar),
    (r'^choose/(.*)', views.choose),
    (r'^gini/(.*)', views.gini),
    (r'^json/(.*)', views.json),
    (r'^features/(.*)', views.featureList),
    (r'^locations/(.*)', views.locations),
    (r'^ipod/(.*)', views.ipod),
    (r'^trade/(.*)', views.trade),
    (r'^mobile/(.*)', views.ipod),
    (r'^playscsv/(.*)', views.playscsv),
    (r'^whatif/(.*)', views.whatif),
    (r'^cookies/$', cookies.cookies),
    (r'^rankings/(.*)', views.rankings),
    (r'^normrankings/(.*)', views.normrankings),
    (r'^geeks/$', views.listOfGeeks),
    (r'^updates/(.*)', views.updates),
    (r'^refreshPage/(.*)', views.refresh),
    (r'^quickRefresh/(.*)', views.quickRefresh),
    (r'^result/(.*)', views.result),
    (r'^tabbed/(.*)', views.tabbed),
    (r'^favourites/(.*)', views.favourites),
    (r'^generic/(.*)', views.generic),
    (r'^favourites2/(.*)', views.favourites2),
    (r'^unusual/(.*)', views.unusual),
    (r'^multiyear/(.*)', views.multiyear),
    (r'^yearcomparison/(.*)', views.comparativeYears),
    (r'^plays/(.*)', views.plays),
    (r'^catgraphs/(.*)', views.categoryGraphs),
    (r'^year/(.*)', views.year),
    (r'^server/(.*)', views.server),
    (r'^checklist/(.*)', views.checklist),
    (r'^crazy/(.*)', views.crazy),
    (r'^meta/$', views.meta),
    (r'^numplayers/(.*)', views.numplayers),
    (r'^series/(.*)', views.series),
    (r'^cat/(.*)', views.category),
    (r'^playrate/(.*)', views.playrate),
    (r'^image/lag/(.*)', imgviews.lagHistogram),    
    (r'^image/newPlays/(.*)', imgviews.newPlays),    
    (r'^image/fpvr/(.*)', imgviews.firstPlayVsRating),    
    (r'^image/mpct/(.*)', imgviews.mostPlayedCumulativeTimeline),
    (r'^image/rbpy/(.*)', imgviews.ratingByPublishedYear),
    (r'^image/rbpyu/(.*)', imgviews.ratingByPublishedYearUpsideDown),
    (r'^image/pogo/(.*)', imgviews.pogo),
    (r'^image/pbm/(.*)', imgviews.pbmGraph),
    (r'^image/pbq/(.*)', imgviews.playsByQuarter),
    (r'^image/morgan/(.*)', imgviews.morgansPieCharts),
    (r'^image/morepie/(.*)', imgviews.morePieCharts),
    (r'^image/cat/(.*)', imgviews.category),
    (r'^image/playrate/(.*)', imgviews.playrate),
    (r'^image/playrateown/(.*)', imgviews.playrateown),
    (r'^image/lifetime/(.*)', imgviews.lifetime),
    (r'^image/lbr/(.*)', imgviews.lifetimeByRating),
    (r'^index.html$', views.frontPage),
    (r'^australia.html$', views.australiaFrontPage),
    (r'^$', views.frontPage)
    # Example:
    # (r'^dynamic/', include('dynamic.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
