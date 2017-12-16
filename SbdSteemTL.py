######################################################################
# SbdSteemTL v1
# kodlama Murat Tatar
# Aralık 2017
######################################################################


import os
import requests
import re

def Arasi(bas,son,cumle):
    b1 = cumle.split(bas)
    b2 = b1[1].split(son)
    ar = b2[0]
    return ar


kullaniciAdi = raw_input(u"Kullanıcı Adı: ")

print "Bilgiler aliniyor..."


size = 120
fcnum = 180

if kullaniciAdi =="": kullaniciAdi = u"murattatar"
if fcnum =="": fcnum = 6*15-1
if size  =="": size  = 60


fcnum = int(fcnum)
size = int(size)




sli = unicode(str(60+2))
bsli_x = unicode(str(size / 1.2))
bsli_y = unicode(str(size / 4.0))

size = unicode(str(size))





## Steemit Cüzdanı #########################################

url = "https://steemit.com/@"+kullaniciAdi+"/transfers"
getir = requests.get(url)
gelen = getir.content



sbd1 = Arasi('STEEM DOLLARS','UserWallet',gelen)
sbd  = Arasi('-->$','<!--',sbd1)


steem1 = Arasi('can be converted to','UserWallet',gelen); 
steem = Arasi('-->',' STEEM<!',steem1)

sbd = float(sbd)
steem = float(steem)

print steem
print sbd




## BitTrex 'teki SBD / Steem  fiyatları #########################################


url = "https://coinmarketcap.com/currencies/steem/#markets"
getir = requests.get(url)
gelen = getir.content


bitSteem1 = Arasi('Bittrex','Recently',gelen); 
bitSteem2 = Arasi('price','</td>',bitSteem1); 
bitSteem  = Arasi('$','</span>',bitSteem2)




url = "https://coinmarketcap.com/currencies/steem-dollars/#markets"
getir = requests.get(url)
gelen = getir.content


bitSbd1 = Arasi('Bittrex','Recently',gelen); 
bitSbd2  = Arasi('price','</td>',bitSbd1)
bitSbd   = Arasi('$','</span>',bitSbd2)


bitSbd = float(bitSbd)
bitSteem = float(bitSteem)

print bitSbd
print bitSteem




## Döviz.com üzerinde Tcmb Dolar kuru #########################################

url = "http://xn--dviz-5qa.com/tcmb-kurlari.html"
getir = requests.get(url)
gelen = getir.content



dolar1 = Arasi('template/dolar.jpg','ada.jpg',gelen) 
dolar2  = dolar1.split('kuralsatbaslik')
dolar = Arasi('">','</span>',dolar2[2])
print dolar
dolar = float(dolar)





print "Hesaplaniyor..."






html =  u"""<!DOCTYPE html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
<title>TL olarak toplam Sbd + Steem değeri</title> <head>
<style class="cp-pen-styles"> 
body, 
html { 
  padding: 0 10px;
  margin: 0;
  background: #0e0f11;
  color: #ecf0f1;
  font-family: "Open Sans", sans-serif;
  min-height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  width: 95%;
}
* {
}
h1, p { text-align: center;}

html,body{background: url("bg.jpg") no-repeat fixed center; }

a:link,
a:hover,
a:active,
a:visited {
  -webkit-transition: color 150ms;
  transition: color 150ms;
  color: #95a5a6;
  text-decoration: none;
}
a:hover {
  color: #5f5c5d;
  text-decoration: none;


}
.contain { 
	width: auto;
	margin-left: 7%;
	margin-right: 7%;
	
}
.row {
	overflow: auto;
	width: 83%;
	margin-right: auto;
	margin-left: 50px;
}
.row__inner {
	-webkit-transition: 400ms -webkit-transform;
	transition: 400ms -webkit-transform;
	transition: 400ms transform;
	transition: 400ms transform, 400ms -webkit-transform;
	font-size: 0;
	white-space: normal;
	margin: 100px 0;
	padding-bottom: 10px;
}
.tile { white-space: nowrap;
  position: relative;
  display: inline-block;
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  margin-right: 8px;
  font-size: 5px;
  cursor: pointer;
  -webkit-transition: 400ms all;
  transition: 400ms all;
  -webkit-transform-origin: center left;
          transform-origin: center left;
}
.tile__img {border-radius:50%; /* opacity: 0.15; */
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  -o-object-fit: cover;
     object-fit: cover;
}
.tile__details {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  font-size: 5px;
  opacity: 0;
 /* background: -webkit-linear-gradient(bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);*/
  -webkit-transition: 400ms opacity;
  transition: 400ms opacity;
}
.tile__details:after,
.tile__details:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  /*display: #000;*/
}
.tile__details:after {
  margin-top: -""" + sli + u"""px;
  margin-left: -""" + sli + u"""px;
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  /* border: 4px solid #ecf0f1; */
  border: 2px solid #06d6a9;
  line-height: 60px;
  text-align: center;
  border-radius: 100%;
  
 
}
.tile__details:before { 
  /* content: "▶"; */
  left: 0;
  width: 100%;
  font-size: 5px;
  margin-left: 7px;
  margin-top: -18px;
  text-align: center;
  /* background: rgba(0,0,0,0.1); */

}
.tile:hover .tile__details { z-index:9999;
  opacity: 1; 
}
.tile__title { text-align:center; color:#06d6a9;
font-size:5px;


  position: absolute;
  bottom: 40%;
  width:100%;
  margin-left:auto; margin-right:auto;
}




.row__inner:hover .tile:hover {
  -webkit-transform: scale(1.7);
          transform: scale(1.7);
  z-index:9999;

  
}




.tile:hover ~ .tile {


  -webkit-transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);
          transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);

}







</style></head><body>


<div class="contain">

  <h1>@"""+ kullaniciAdi + u"""'a ait <br> SBD ve STEEM'lerin TL olarak toplam değeri</h1>


<span style="white-space:nowrap">Kodlama</span> <a style="white-space:nowrap" href="https://steemit.com/@murattatar">Murat Tatar</a>. Suggest by <a href="https://steemit.com/@omeratagun">Ömer Atagün</a>. 
  Efekt <a href="https://codepen.io/joshhunt/pen/LVQZRa">joshhunt</a>. Arkaplan <a href="https://pixabay.com/tr/users/Uki_71-1547363/">Uki_71</a>
  


  
<div class="row__inner">




<div class="tile" onclick="window.open('https://steemit.com/@""" + unicode(kullaniciAdi) +u"""','myw');">
      <div class="tile__media">
        <img class="tile__img" src="https://img.busy.org/@""" + unicode(kullaniciAdi) + u"""?crop=limit&s=800" />
      </div>
      <div class="tile__details">
        <div class="tile__title">
          <div style="font-size: 12px; position: relative; top: 38px;">""" + unicode(kullaniciAdi) + u"""</div>
        </div>
      </div>
    </div>





<div class="tile" onclick="window.open('https://bittrex.com/Market/Index?MarketName=BTC-SBD','myw');">
      <div class="tile__media">
        <div style="font-size: 9px; position: relative;bottom: 30px; left:20px;text-align:center">
""" +unicode(str(sbd))+ u""" SBD = """+unicode(str(round(sbd*bitSbd*dolar,2)))+u""" TL
<br>
""" +unicode(str(steem))+ u""" Steem = """+unicode(str(round(steem*bitSteem,2)))+u""" TL
<br><br>
Toplam
<br>
<span style="font-size: 10px; font-weight: 900">"""+unicode(str(round((steem*bitSteem*dolar)+(sbd*bitSbd*dolar),2)))+u""" TL</span>

        <div>
      </div>
      <div class="tile__details">
        <div class="tile__title">
          """ + u"""<div style="font-size: 12px; position: relative; top: 40px;">BitTrex'e göre</div>""" + u"""
        </div>
      </div>
    </div>









    </div>





</div>



</body>





</html>"""



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


o = open("SbdSteemTL.html","w"); o.write(html.encode("utf-8")); o.close()
os.startfile("SbdSteemTL.html")






