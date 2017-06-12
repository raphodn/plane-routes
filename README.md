# Air France Route Map

Initial idea
http://artsy.github.io/blog/2017/01/25/mashing-maps/

AirFrance cities & route data (JS & "API")
http://www.airfranceklm.com/fr/reseau (http://af.fltmaps.com/)

other possible sources ?
- Google Maps with Skyteam airlines, airpots & routes (JS): http://fatterflights.appspot.com/group/AF

airports & arcs animation
http://www.tnoda.com/blog/2014-04-02 & http://www.tnoda.com/js/flightanimation.js


Air France API ?
https://developer.airfranceklm.com/page/Flight_Offer_API

Air France Magazine
http://magazines.airfrance.com/en/air-france-magazine/238-february-2017/#174


# Step-by-step

## 1. Extract data

use BeautifulSoup to extract data from html
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

- cities in JSON (from http://www.airfranceklm.com/fr/reseau)
- routes in HTML ('API' from http://www.airfranceklm.com/fr/reseau)
- start with Paris (3 pages, 275 results)
- add Amsterdam (3 pages, 297 results)
- add Geneve (1 page, 5 results)
- add Londres (1 page, 5 results)
- add Rotterdam (1 page, 27 results)

- other: Francfort, Berlin, Rome, Madrid, Singapour, Bangkok



## 2. Clean data

- removed '&lrm;' from HTML

### Errors

`airfrance_amsterdam_3`
- Buenos Aires (EZE) > Buenos Aires (BUE)


## 3. Process data

- extract routes info from HTML with python (BeautifulSoup)
- return csv


## Other data

### Airlines

- Delta: http://dl.fltmaps.com/en (12 hubs, 599 cities)
- American Airlines: http://aa.fltmaps.com/en (9 hubs, 533 cities)
- Oneworld: http://fatterflights.appspot.com/group/Oneworld
- Lufthansa: http://lh.fltmaps.com/en
http://os.fltmaps.com/en
http://me.fltmaps.com/en
- Air Canada: http://ac.fltmaps.com/en
- Hainan Airlines: https://hu.fltmaps.com/en/int
- Japan Airlines: http://jl.fltmaps.com/en/japan



### Airports

- Dublin airport: https://dub.fltmaps.com/en (349 flights)
- Charlotte Douglas: http://clt.fltmaps.com/en (289 flights)
- Indianapolis: http://ind.fltmaps.com/en (116 flights)
- Hannover: http://haj.fltmaps.com/en (160 flights)
- Calgary: http://yyc.fltmaps.com/en (184)
