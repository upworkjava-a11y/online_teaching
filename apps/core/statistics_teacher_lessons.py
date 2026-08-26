"""
Statistika darslari — o‘qituvchi ovozida, noldan.
Har dars tahlilchi bilan gaplashgandek yozilgan; bir xil qolip takrorlanmaydi.
Urg‘u: sonni qaror tiliga o‘girish, og‘ir formula emas.
"""

LECTURES = {
    "st-nima": """
<p>Salom. Agar maktabda statistika sizni qo‘rqitgan bo‘lsa — unuting. Bu yerda formula yodlamaysiz. Siz tahlilchisiz: rahbar son so‘raydi, siz esa shu son bilan <em>nima qilish</em> kerakligini aytasiz.</p>

<p>Ishda ma’lumot har kuni keladi. Landing sahifa konversiyasi kecha 2.1% edi, bugun 2.4%. Marketing yozadi: “Yutdik, kampaniyani 10 barobar oshiramiz.” Sizning ishingiz — qo‘l qovushtirib “ha” demaslik. Avval so‘raysiz: nechta odam kirdi? Bayrammi? Faqat Toshkentmi, butun O‘zbekistonmi?</p>

<p>Tasavvur qiling, 80 kishi sahifaga kirdi, 2 tasi xarid qildi. Bu 2.5%. Ertaga 80 kishidan 1 tasi xarid qilsa — 1.25%. Bir kishi farq qilsa, foiz ikki barobar o‘zgaradi. Shunda “o'sish” emas, <strong>shovqin</strong>. Statistika shu shovqinni signal dan ajratish uchun kerak.</p>

<p>Uchta savol, har hisobotda. Birinchisi: bu son umuman nima? “O‘rtacha chek” — barcha to‘lovlarning o‘rtachasimi, faqat muvaffaqiyatli xaridlarnimi, qaytarishlarsizmi? Ta’rif yozilmasa, ikki kishi ikki xil javob chiqaradi.</p>

<p>Ikkinchisi: qanchalik barqaror? Bitta katta buyurtma, bitta sekin kuryer, bitta bayram — son sakraydi. Tarqalish va namuna hajmi shu yerda gapiradi.</p>

<p>Uchinchisi: nima qilamiz? To‘xtatamiz, kengaytiramiz, yoki yana bir hafta kutamiz. Statistika javobni “ha/yo‘q” qilib bermaydi. U noaniqlikni ochiq aytishga o‘rgatadi. Rahbar noaniqlikni yoqtirmasligi mumkin — lekin yashirish undan yomon.</p>

<p>Keyingi darslarda o‘rtacha, median, tarqalish, A/B — hammasi shu uch savolga xizmat qiladi. Hozir shuni oling: statistika — o‘rtacha chiqarish emas. Bu <strong>noaniqlik ostida qaror</strong>.</p>
""",
    "st-turlar": """
<p>Excelda hamma narsa katakchada. Lekin katakcha katakchaga o‘xshamaydi. Viloyat nomi, qoniqish bahosi va chek summasi — uch xil narsa. Ularga bir xil “o‘rtacha” qo‘llash — eng tez xato.</p>

<p>Birinchi tur — <strong>nom</strong>. Kanal: Online, Offline, Marketplace. Viloyat: Toshkent, Samarqand, Buxoro. Bularning tartibi yo‘q. Toshkent “Samarqanddan katta” emas. Shuning uchun viloyat kodining o‘rtachasi ma’nosiz. Bu yerda sanaysiz: nechtasi Online, qaysi kanal eng ko‘p. Grafik — ustun yoki oddiy jadval, pie emas (pie ko‘zni aldashi oson).</p>

<p>Ikkinchi tur — <strong>tartibli</strong>. Mijoz qoniqishi: 1 dan 5 gacha. 5 “4 dan yaxshi”, lekin 5 bilan 4 orasidagi masofa 2 bilan 1 orasidagidekmi — noma’lum. O‘rtacha 4.2 ni hisobotga yozish bahsli. Avval taqsimotni qarang: hammasi 4–5 da turibdimi, yoki yarmi 1, yarmi 5? Median bu yerda tinchroq. Mode — eng ko‘p qo‘yilgan baho.</p>

<p>Uchinchi tur — <strong>pul va son</strong>. Chek 45 000 so‘m, yetkazib berish 2 kun, yosh 28. Bularni qo‘shish, ayirish, o‘rtacha olish mumkin. Lekin dumli bo‘lsa (bitta 50 millionlik shartnoma), o‘rtacha yolg‘on gapiradi — buni keyingi modulda ko‘ramiz.</p>

<p>Kichik jadval, do‘kon misoli:</p>
<table>
  <tr><th>Ustun</th><th>Misollar</th><th>Nima qilmang</th></tr>
  <tr><td>Kanal</td><td>Click, naqd, Payme</td><td>O‘rtacha kanal</td></tr>
  <tr><td>Baholash</td><td>1, 2, 3, 4, 5</td><td>Darhol 4.37 deb yopish</td></tr>
  <tr><td>Chek</td><td>12 000 so‘m</td><td>Viloyat kabi sanash</td></tr>
</table>

<p>Qoida oddiy: avval so‘rang, bu sonni qo‘shish mumkinmi? Agar “Toshkent plus Samarqand bo‘linadi ikkiga” degani kulgili bo‘lsa — bu kategoriya. Kategoriyaga mean qo‘ymang.</p>

<p>Ishda aralash ustun ko‘p. “Status: 1, 2, 3” deb yozilgan, aslida 1 = yangi, 2 = to‘langan, 3 = qaytarilgan. Raqam ko‘rinsa ham, bu pul emas. Tahlilchi ustunni o‘qishdan oldin <em>ma’nosini</em> so‘raydi.</p>
""",
    "st-namuna": """
<p>Rahbar aytadi: “Barcha mijozlarning o‘rtacha cheki.” Siz dashboard ochasiz — oxirgi 30 kun, faqat ilova, faqat to‘langan. Bu “barcha mijozlar” emas. Bu — <strong>namuna</strong>. Ko‘p hisobotlar namuna, lekin sarlavhada “hamma” yoziladi. Shu yerdan tushunmovchilik boshlanadi.</p>

<p><strong>Populyatsiya</strong> — siz qiziqqan to‘liq to‘plam. Masalan: 2024-yilda O‘zbekistondagi barcha to‘langan buyurtmalar. <strong>Namuna</strong> — ko‘rgan qism: mart oyi, faqat Toshkent, faqat Click orqali. Namuna populyatsiyaga o‘xshasa, xulosa o‘tadi. O‘xshamasa — yo‘q.</p>

<p>Bias degani — namuna bir tomonga egilgan. Oddiy misol: qoniqish so‘rovini faqat VIP mijozlarga yubordingiz. VIP odatda tezroq yetkazib oladi, chegirma ko‘proq. Ular 4.8 baho qo‘yadi. Siz “mijozlar baxtli” deb yozasiz. Oddiy chakana xaridor hali javob bermagan. Bu — selection bias. Qulay odamlarni so‘rash (convenience sample) hammaga tanish, lekin xulosa cheklanadi.</p>

<p>Yana bir tuzoq: kim javob beradi? Norozilar yozadi, mamnunlar jim. Yoki aksincha — ilova push-xabarini ochganlar. Siz o‘lchagan narsa “barcha ovoz”, aslida “yozishga ulgurganlar ovozi”.</p>

<p>Tahlilchi tili shunday o‘zgaradi. “Barcha mijozlar” o‘rniga: “2024-yil mart, online kanal, to‘langan buyurtmalar, Toshkent va Samarqand.” Chegara uzunroq, lekin rost. Rahbar qisqa xohlasa, og‘zaki qisqartirasiz, lekin o‘zingizda chegarani yozib qo‘yasiz.</p>

<p>Kichik mashq, boshda: har bir KPI yoniga bitta jumla — “Bu kimlar?” Agar javob “dashboarddagi filtr qanday tursa, o‘sha” bo‘lsa, filtrni ochib qarang. Oxirgi 7 kun bayramga tushganmi? Bitta yirik B2B mijoz bormi? Shu savollar statistikadan oldin keladi.</p>

<p>Keyingi darsda o‘rtacha haqida gaplashamiz. Lekin o‘rtacha ham namuna ustida. Yomon namuna ustidagi chiroyli o‘rtacha — baribir yomon.</p>
""",
    "st-mean": """
<p>“O‘rtacha qancha?” — tahlilchiga eng ko‘p beriladigan savol. Mean shu: barchasini qo‘shasiz, nechtaligiga bo‘lasiz. 5 ta chek: 20, 22, 18, 25, 15 ming so‘m. Yig‘indi 100, mean 20 ming. Tanish, tushunarli, Excelda bitta tugma.</p>

<p>Muammo shundaki, mean <em>hammani</em> eshitadi — hatto o‘sha “hamma” ichida bitta g‘alati mehmon bo‘lsa ham. Chakana do‘konda 99 ta chek 50 ming so‘m atrofida. 100-chi chek — yirik ofisga 50 millionlik mebel. Mean osmonga chiqadi. Rahbar “o‘rtacha chek o‘sdi, marketing ishladi” deydi. Aslida oddiy xaridor hali ham 50 minglik nonushta oladi.</p>

<p>Bankda ham shu. Filialning o‘rtacha omonati. 200 ta odam 8–12 million qo‘ygan, bitta kompaniya 2 milliard. O‘rtacha “boy mijozlar” haqida gapirgandek ko‘rinadi. Tipik omonatchi umuman boshqa odam.</p>

<p>Mean qachon yaxshi? Taqsimot simmetrik, dum yo‘q, outlier kam. Kunlik tashrif soni ba’zan shunday bo‘ladi. Yoki bir xil narxdagi SKU. Shunda mean “markaz”ni rost aytadi.</p>

<p>Yana bir narsa: mean jami pul bilan do‘st. Kompaniya kassasiga tushgan pul — yig‘indi. Yig‘indini songa bo‘lsangiz, mean chiqadi. Reja, byudjet, “har mijozdan o‘rtacha tushum” — shu yerda mean o‘rinli. Lekin “oddiy mijoz qancha to‘laydi?” degan savol boshqacha. U savolga mean javob bermasligi mumkin.</p>

<p>Hozircha qoida: mean ni yozganingizda, ichingizda so‘rang — bitta ulkan raqam bormi? Agar shubha bo‘lsa, median ni ham oling. Keyingi darsda aytaman, nima uchun bitta katta bonus butun o‘rtacha maoshni buzadi. Shu hikoya mean ning zaif tomonini bir umrga yopishtiradi.</p>
""",
    "st-median": """
<p>Keling, maosh. Toshkentdagi kichik do‘konda 5 kishi ishlaydi. Oddiy oy:</p>
<table>
  <tr><th>Xodim</th><th>Maosh, mln so‘m</th></tr>
  <tr><td>Kassir Nodira</td><td>3.8</td></tr>
  <tr><td>Sotuvchi Javohir</td><td>4.0</td></tr>
  <tr><td>Sotuvchi Malika</td><td>4.2</td></tr>
  <tr><td>Omborchi Ali</td><td>4.5</td></tr>
  <tr><td>Direktor</td><td>6.0</td></tr>
</table>
<p>Mean taxminan 4.5. Median — o‘rtadagi odam, Malika, 4.2. Yaqin. Hech kim aldanmaydi.</p>

<p>Dekabr. Direktorga yil yakuni bo‘yicha <strong>katta bonus</strong> tushadi: o‘sha oy u 40 million oladi. Qolgan to‘rt kishi o‘z 3.8–4.5 ida qoladi. Mean endi ~11.3 million. Hisobot: “O‘rtacha maosh ikki barobar o‘sdi.” Ishchilar kuladi. Hech kimning cho‘ntagiga 11 million kirmagan. Faqat bitta odamning bonusini besh kishiga “surtib” qo‘ydik.</p>

<p>Median o‘sha oyda ham 4.2. Tartiblab qo‘yasiz, o‘rtadagi qiymat. Bitta osmondagi son uni siljitmaydi. Shuning uchun daromad, uy narxi, chek summasi — o‘ngga qiyshaygan narsalarda median “oddiy odam”ga yaqinroq.</p>

<p>Mode — eng ko‘p uchraydigan. To‘lov usuli: 70 kishi Click, 20 naqd, 10 Payme. Mode — Click. Eng mashhur SKU, eng ko‘p tanlangan viloyat. Miqdoriy uzluksizda (har chek boshqacha so‘m) mode kam foydali: hammasi deyarli bir marta uchraydi. Bin qilmasangiz, “eng ko‘p” yo‘qoladi.</p>

<p>Qisqa farq, eslab qoling. Mean — hammaga quloq soladi, boy mehmon ham. Median — navbatning o‘rtasidagi odam. Mode — eng shovqinli guruh. Tipik xodim, tipik mijoz desa — avval median.</p>

<p>Keyingi darsda hisobotga qaysi birini qo‘yishni tanlaymiz. Spoiler: ko‘pincha bitta son yetmaydi.</p>
""",
    "st-markaz-tanlash": """
<p>Rahbar bitta son xohlaydi. Sizda mean 12 million, median 3 million. Qaysi birini aytasiz? Ikkalasini ham. Farqning o‘zi xabar: dum bor, katta shartnomalar bor, “o‘rtacha mijoz” va “kassa” boshqa dunyo.</p>

<p>Qachon nima, do‘kon tilida:</p>
<table>
  <tr><th>Savol</th><th>Ko‘rsatkich</th></tr>
  <tr><td>Kassaga qancha pul tushdi?</td><td>Yig‘indi (mean ehtiyot bilan)</td></tr>
  <tr><td>Oddiy xaridor qancha to‘laydi?</td><td>Median</td></tr>
  <tr><td>Eng ko‘p qanday to‘lov, qaysi SKU?</td><td>Mode</td></tr>
</table>

<p>Jami pul kompaniyaniki. Uni yashirmang. Lekin “mijozlar boyayapti” deb mean ni ko‘rsatmang — 3 ta B2B shartnoma mean ni ko‘tarishi mumkin, chakana jim. Yonma-yon yozing: mean 12 mln, median 3 mln. Bitta jumla: “Katta shartnomalar o‘rtachani tortadi, tipik chek 3 million atrofida.”</p>

<p>Agar mean va median deyarli teng bo‘lsa — yaxshi yangilik. Taqsimot unchalik qiyshaymagan, bitta son yetishi mumkin. Vaqtni tejasiz. Teng emasligi — histogram ochish signali, keyingi modulda ko‘ramiz.</p>

<p>Mode ni mean o‘rniga qo‘ymang. “Eng mashhur mahsulot” — assortiment savoli. “O‘rtacha chek” — pul savoli. Aralashtirsangiz, marketing bitta SKU ni “o‘rtacha savdo” deb reklama qiladi.</p>

<p>Amaliy odat: har yangi KPI uchun 10 soniya. Bu jami pulmi, tipik odammi, yoki eng ko‘p kategoriya? Uch savol — uch ko‘rsatkich. Hisobotga ikkitasini sig‘dirish uyat emas. Uyat — bitta yolg‘on aniq son.</p>
""",
    "st-spread": """
<p>Ikki filial. Chilonzor va Yunusobod. Ikkalasining o‘rtacha kunlik savdosi 8 million so‘m. Rahbar: “Bir xil, bir xil reja.” Siz kunlik raqamlarni ochasiz. Chilonzor: 7.5, 8.1, 7.8, 8.2, 8.0. Yunusobod: 3, 15, 4, 14, 8. O‘rtacha teng. Hayot emas.</p>

<p>Yunusobodda dushanba bo‘sh, juma to‘lib ketadi. Kassachi yetishmaydi, ombor kechqurun bitadi, dushanba non ushlanib qoladi. Chilonzorda kishi soni barqaror. Bir xil mean, boshqa xavf. Tarqalish shu farqni o‘lchaydi.</p>

<p>Eng sodda o‘lchov — range: max minus min. Yunusobodda 15−3=12 million. Chilonzorda 8.2−7.5=0.7. Qo‘pol, lekin darhol tushunarli. Kamchiligi: bitta g‘alati kun range ni yutib yuboradi.</p>

<p>IQR va standart og‘ish keyingi darslarda. Hozir g‘oya: <strong>o‘rtacha yetmaydi</strong>. Ikki guruhning mean i teng bo‘lishi “bir xil biznes” degani emas. Tebranish katta bo‘lsa, reja, ombor, kassa, yetkazib berish — hammasi boshqacha og‘riydi.</p>

<p>Landing sahifada ham. Konversiya o‘rtacha 2.3%. Lekin dushanba 1.1%, juma 4%. Haftalik o‘rtacha “barqaror” ko‘rinadi, siz esa juma uchun server, dushanba uchun reklama boshqacha kerakligini bilmaysiz. Mean yashiradi, tarqalish ochadi.</p>

<p>Hisobotga qo‘shing: mean yonida min–max yoki “kunlar qanchalik sakraydi”. Rahbar raqamni ko‘rgach, “nima uchun ombor shikoyat qiladi?” deb so‘ramasligi kerak. Siz oldin aytasiz: o‘rtacha tinch, kunlik hayot tinch emas.</p>
""",
    "st-std": """
<p>Standart og‘ish — qo‘rqitadigan nom. Ma’nosi oddiy: raqamlar o‘rtachadan qanchalik uzoq yuradi. Birlik asl o‘zgaruvchi bilan bir xil: chek so‘mda bo‘lsa, std ham so‘mda. Shuning uchun uni “o‘rtacha og‘ishning o‘lchami” deb o‘qing, ildiz ichidagi formulani tungi tushida ko‘rmang.</p>

<p>Chilonzor savdosi 8 million atrofida, std 0.3 million — deyarli joyida. Yunusobod mean 8, std 5 million — bugun 3, ertaga 14. Kassaga qancha naqd qo‘yish, nechta kuryer chaqirish — std shu savollarga tegadi.</p>

<p>Variansiya — std ning kvadrati. Birlik “so‘m kvadrat”, odamga aytish qiyin. Hisobotda odatda std. Variansiya formula ichida yashaydi, slaydda emas.</p>

<p>Namuna vs populyatsiya. Excel va Python da std ni n ga bo‘lish yoki n−1 ga bo‘lish farqi bor (ddof). Namuna bo‘lsa odatda n−1. Populyatsiya to‘liq ma’lum bo‘lsa — n. Rahbarga aytmang. Lekin jamoa faylida qaysi ekanini bir qator izoh qiling, aks holda ikki kishi 2% farq topib, “xato” deb janjallashadi.</p>

<p>Turli o‘lchamdagi narsalarni solishtirish. Non 4 000 so‘m, std 400. Telefon 4 000 000, std 400 000. Qaysi biri “barqarorroq”? So‘mda telefon. Nisbatan — ikkalasi ham 10%. Bu <strong>CV</strong>: std / mean. Mahsulotlar, filiallar, kampaniyalar narxi turlicha bo‘lsa, CV yoki boshqa nisbiy o‘lchov. Faqat range so‘mda — adashtiradi.</p>

<p>Ehtiyot: mean nolga yaqin bo‘lsa, CV aqldan ozadi. Foyda ba’zan musbat-manfiy tebranadi. Shunda CV ni zo‘rlamang, std va grafikni ko‘rsating.</p>

<p>Tahlilchi jumlasi: “O‘rtacha 8 mln, kunlik tebranish taxminan 0.3 mln — reja ishonchli” yoki “o‘rtacha 8, tebranish 5 — ombor va kassa zaxirasisiz ishlamaydi.” Std ni shu tilda soting, ildiz belgisini emas.</p>
""",
    "st-percentile": """
<p>Yetkazib berish. Median 2 kun. Marketing yozadi: “Odatda 2 kunda.” Mijozlar Telegramda urishadi. Nima bo‘ldi? Siz p95 ni ochasiz: 8 kun. Ya’ni 100 buyurtmadan 5 tasi bir haftadan oshadi. O‘sha 5 ta odam shovqin qiladi. SLA ni o‘rtachaga qo‘yish — shu 5 tasini ko‘rmaslik.</p>

<p>Percentile oddiy. p90: 90% qiymat shu sondan kichik (yoki teng). p50 — median. Q1 (p25), Q2, Q3 (p75). IQR = Q3 minus Q1 — o‘rta 50% qanchalik keng. Dumli yetkazishda median tinch, IQR va p95 qichishadi.</p>

<table>
  <tr><th>Ko‘rsatkich</th><th>Kun</th><th>Nima deysiz</th></tr>
  <tr><td>Median</td><td>2</td><td>Yarmidan ko‘pi shu yoki tezroq</td></tr>
  <tr><td>Q3</td><td>3</td><td>75% uch kun ichida</td></tr>
  <tr><td>p95</td><td>8</td><td>Yomon dum — SLA shu yerda</td></tr>
</table>

<p>Rahbarga: “Tipik yetkazish 2 kun. Lekin yuzdan beshtasi 8 kungacha cho‘ziladi. Agar va’da 3 kun bo‘lsa, p95 ni tushirish kerak — aks holda shikoyat o‘rtachadan kelmaydi, dumdan keladi.”</p>

<p>Outlier qoidasi, qo‘pol: Q1−1.5×IQR dan tashqari yoki Q3+1.5×IQR dan tashqari. Bu avtomatik o‘chirish emas. Bu — “shu qatorni ochib ko‘r” flagi. Vergul xatosi bo‘lishi mumkin (50 000 o‘rniga 50 000 000), yoki haqiqiy to‘y buyurtmasi. Keyingi modulda siyosatni yozamiz.</p>

<p>Bankda navbat vaqti, call-markazda javob soniyasi, ilovada yuklanish — hammasi shu mantiq. Mean “yaxshi”, p95 “mijoz ko‘radigan yomon kun”. Hisobotda ikkalasi.</p>
""",
    "st-hist": """
<p>Jadvaldagi mean va median — ikkita nuqta. Histogram — butun qishloq. Qayerda odamlar to‘planadi, cho‘qqi bormi, chapda-o‘ngda dum bormi. Tahlilchi avval shaklni ko‘radi, keyin son yozadi. Teskari qilmang.</p>

<p>Simmetrik: cho‘qqi o‘rtada, chap va o‘ng deyarli oyna. Mean ≈ median. Ba’zan buyurtma soni, ba’zan ball. Kam uchraydi, lekin uchrasa — bitta markaz yetishi mumkin.</p>

<p>O‘ng dum: ko‘p kichik cheklar, bir nechta ulkan. Savdo, daromad, tashrif davomiyligi. Cho‘qqi chapda, dum o‘ngga cho‘ziladi. Mean dum tomonga tortiladi, median cho‘qqi yonida qoladi. “O‘rtacha chek” slaydida shu shakl bo‘lsa, median ni qo‘shing.</p>

<p>Ikki cho‘qqi — muhim. Amount histogramida bitta uyum 40–60 mingda, ikkinchisi 2–3 millionda. Bu “g‘alati taqsimot” emas. Bu ikki segment: B2C va B2B, yoki chakana va ulgurji, yoki Toshkent restoran va viloyat do‘koni. Ularni bir mean ga solish — yolg‘on. Ajrating, keyin har biriga o‘z o‘rtachasi.</p>

<p>Bin kengligi ham aldaydi. Juda keng qilib qo‘ysangiz, ikki cho‘qqi yopiladi. Juda mayda qilsangiz, tish-tish shovqin. Avval ko‘z, keyin bir-ikkita boshqa bin. Excelda ham, Python da ham 30 soniya o‘ynang.</p>

<p>Amal: yangi ustunni ko‘rganingizda scatter yoki hist. “Mean 180 ming” ni yozishdan oldin. Agar ikki cho‘qqi bo‘lsa, slaydga mean qo‘ymang — “ikkita olam aralashgan” deb yozing. Segment kalitini toping (kanal, viloyat, B2B flag). Keyin qayta hisoblang.</p>
""",
    "st-normal": """
<p>Maktabda qo‘ng‘iroq chizig‘i bor edi: o‘rtada ko‘p, chetlarda kam. Normal taqsimot shu. Ko‘p klassik testlar “normal deb faraz qilamiz” deb ishlaydi. Savdo cheklari odatda <em>normal emas</em>. Kichik xaridlari ko‘p, katta to‘y-to‘kilar kam. Shakl o‘ng dum.</p>

<p>Nima uchun baribir gaplashamiz? Chunki tahlilchi “test ishladi” deb xotirjam bo‘lib qolmasligi kerak. Agar cheklar qiyshaygan bo‘lsa, kichik n da t-test nozik. Avval grafik. Keyin, kerak bo‘lsa, log yoki median asosidagi usul, yoki shunchaki katta n.</p>

<p>Markaziy limit g‘oyasi, bir jumlada. Alohida chek qiyshaygan bo‘lsa ham, <em>o‘rtachalar</em>ning namuna-namuna sakrashi n katta bo‘lsa qo‘ng‘iroqqa yaqinlashadi. Ya’ni 10 000 chekning mean i haqida gapirish osonroq, bitta chekning “normal”ligini aytish emas. Rahbarga: “Cheklarning o‘zi normal emas. Lekin o‘rtacha chekning noaniqligi katta n da taxminan tushunarli.”</p>

<p>Qoida: avval hist. “Normal deb faraz qildik” ni yozing, yashirmang. Agar faraz yolg‘on va n kichik bo‘lsa, p-value ga yopishmang. Keyingi darslardagi A/B da ham shu: ulushlar uchun boshqa taxminlar bor, lekin baribir namuna hajmi va shaklni ko‘ring.</p>

<p>Ishda “normal emas” degani fojia emas. Ko‘p biznes ma’lumoti normal emas. Fojia — ko‘rmasdan test tugmasini bosish. Siz tahlilchisiz, statistik paketning mijoz i emassiz.</p>
""",
    "st-skew": """
<p>O‘ng qiyshayish: dum o‘ngda, mean median dan katta. Chap qiyshayish kamroq, lekin bo‘ladi (masalan, deyarli hammasi 100 ball, bir nechtasi 40). Chek, maosh, uy — odatda o‘ng. Directorning 40 millionlik bonusi — o‘sha dumning yorqin nuqtasi.</p>

<p>Outlier nima? Grafikda yoki IQR qoidasida “uzoqda” turgan nuqta. Ikki xil hayot: xato va haqiqat. Kassir 50 000 o‘rniga 50 000 000 yozib yuborgan — vergul. To‘y uchun 200 ta kiyim olgan restoran — haqiqiy. Birinchisini tuzatasiz. Ikkinchisini o‘chirish — savdoni yashirish.</p>

<p>Siyosat, qadam-qadam. Avval flag (IQR, yoki “mean dan 10 barobar”). Keyin manba: chek, mijoz, sana. Keyin qaror: alohida qator qilib ko‘rsatish (“top 1% shartnomalar”), yoki asosiy hisobotdan ajratib B2B deb yozish. Winsorize (dumlarni kesib qo‘yish) — ehtiyot, va faqat model uchun, asosiy kassa hisobotida emas.</p>

<p>Hech qachon sukut bilan o‘chirmang. Ertaga kimdir “o‘rtacha tushib ketdi” deb so‘raydi, siz “men 12 qatorni o‘chirdim” deb tushuntira olmaysiz. Logga yozing: nechta, nima uchun, qayerda saqlanadi.</p>

<p>Rahbarga qisqa: “O‘rtacha o‘sganining sababi 3 ta yirik buyurtma. Oddiy chek o‘zgarmagan. Yiriklarni alohida kuzatamiz, chakanani median bilan.” Qiyshayish — dushman emas. U sizga segment borligini aytadi.</p>
""",
    "st-prob-intro": """
<p>Ehtimollik — “qanchalik ishonamiz”, foiz kiyimidagi ehtiyot. Tahlilchi uni lotereya formulasi deb yodlamaydi. U filtrlangan savolga aylanadi: shu kategoriya ichida qaytarish qancha?</p>

<p>Do‘kon. Kiyim qaytarilishi 8%, oziq-ovqat 2%. Omborga “o‘rtacha 5%” deb yozsangiz, kiyim javonida joy yetmaydi, non esa ortiqcha zaxira. Aralash o‘rtacha — yolg‘on tinchlik. Segment kerak. Teng hajmda A va B bo‘lsa, aralash ~5%. Hajm teng bo‘lmasa, og‘irlik bilan. Lekin baribir ikkala foizni ham ayting.</p>

<p>Mustaqil hodisa: bir mijozning Click to‘lashi ikkinchisining naqd to‘lashiga ta’sir qilmasa. Hayotda to‘liq mustaqillik kam. Bir kunda tarmoq yiqilsa, ko‘p odam birga “xato” bo‘ladi. Shuning uchun “ehtimollik 2%, demak 50 tadan 1 tasi” deb mexanik aytish — taxmin, qonun emas.</p>

<p>Shartli ehtimollik — filtr. “Umuman qaytarish 5%.” “Faqat Toshkent, kiyim, 3 kundan keyin yetkazilgan” — boshqacha foiz. Dashboarddagi har filtr — yangi ehtimollik. Bayes tilida: oldingi bilim (umumiy 5%) + yangi ma’lumot (kiyim, kechikish). Formulani yodlash shart emas. Mantiq: yangi fakt kelganda foizni yangilang, eski aralashni ushlab o‘tirmang.</p>

<p>Landing: tashrif buyuruvchining xarid qilish ehtimoli. Yangi reklama keldi — odamlar boshqacha. Eski 2.1% ni yangi oqimga yopishtirmang. Ehtimollik populyatsiyaga bog‘liq, populyatsiya o‘zgarsa, foiz ham.</p>

<p>Bugungi olish: ehtimollik — ishonch darajasi va segment. Aralash o‘rtacha omborni aldashi mumkin. Avval kesim, keyin foiz.</p>
""",
    "st-sampling": """
<p>Har safar boshqa 100 odamni olsangiz, o‘rtacha boshqacha chiqadi. Bu xato qilganingiz emas. Bu — tanlanma xatosi. Kichik n da sakrash katta. Katta n da kichik.</p>

<p>Landing. 10 tashrif, 1 xarid = 10%. Ertaga 10 tashrif, 0 xarid = 0%. O‘rtaga 3 xarid = 30%. Siz “konversiya uch barobar o‘sdi” deb yozishingiz mumkin. Yozmang. n=10 da 10% — deyarli shovqin. 10 000 tashrifdan 1 000 xarid = 10% — ancha og‘ir, barqaror.</p>

<p>Qoida, qo‘lda: ulush uchun “nechta muvaffaqiyat” ham muhim. 1/10 va 100/1000 ikkalasi ham 10%, lekin ikkinchisi ishonchliroq. Rahbar foizni ko‘radi, siz sonni ko‘rasiz: 1 kishi teskariga o‘girsa, foiz o‘ladi.</p>

<p>Vaqt ham namuna. “Oxirgi 3 kun” — kichik n, plus dushanba-chorshanba ta’siri. “Oxirgi 90 kun” — barqarorroq, lekin ichida bayram, eski kampaniya, yangi narx aralashgan. Chegarani yozing. Qisqa oyna — tezkor, shovqinli. Uzun oyna — tinch, kechikkan.</p>

<p>Filial solishtirish. Toshkentda 8 000 chek, Buxoroda 80. Buxoro mean i sakrashi tabiiy. “Buxoro yomon ishlayapti” demay, avval n ni qo‘ying. Kichik filialni katta bilan xom mean da urishtirish — adolat emas.</p>

<p>Keyingi dars — ishonch oralig‘i. U tanlanma xatosini son oralig‘iga aylantiradi. Hozir eslab qoling: kichik n — katta og‘iz ochmang. 10 tashrifdagi 30% ni kampaniya g‘alabasi deb aytmang.</p>
""",
    "st-ci": """
<p>Nuqta baho: konversiya 2.4%. Xuddi aniq milimetr. Aslida namuna boshqacha bo‘lsa, 2.1 yoki 2.7 chiqishi mumkin edi. Ishonch oralig‘i shu “mumkin”ni chiziq qilib ko‘rsatadi.</p>

<p>95% CI ni qanday aytish. Aniq ta’rif: shu usulni ko‘p marta takrorlasak, intervallarning taxminan 95 foizi haqiqiy parametrni qoplaydi. Ishda soddaroq gap ham ishlatiladi, lekin “95% ehtimol haqiqiy son mana shu oraliqda” deb qasamyod qilmang — biroz boshqacha ma’no. Rahbarga yetadigan gap: “Hozirgi ma’lumot bilan 2.4%, lekin oqilona oraliq 1.9–2.9. Aniq 2.4 deb reja qilmang.”</p>

<p>Maqsad 3%. Sizda 2.4% (1.9–2.9). Interval 3 ni qo‘shmaydi. Xulosa: nuqta maqsaddan past, va noaniqlik ham 3 gacha yetmayapti. “Maqsad bajarildi” demaysiz. “Yaqin, lekin hali yo‘q — yoki ko‘proq tashrif, yoki boshqa o‘zgarish.”</p>

<p>Keng interval — kam ma’lumot yoki katta tarqalish. n=80 da konversiya CI si keng bo‘lishi tabiiy. n=80 000 da tor. Tor interval ham maqsaddan yiroq bo‘lishi mumkin: aniq bilamizki, 2.4, va 3 emas. Aniqlik “yaxshi yangilik” demak emas.</p>

<p>Hisobot andozasi: “2.4% (95% CI: 1.9–2.9). Maqsad 3%. Hozircha yetishmayapti.” Nuqta bahoni yolg‘iz qoldirmang. Bitta o‘nlik foiz slaydda jang chiqaradi; oraliq esa “kutamiz yoki kengaytiramiz” ni tinchroq qiladi.</p>

<p>Keyin A/B da ham CI farq ustida yuradi. p-value dan oldin shu odatni oling: son + oraliq. Rahbar o‘rganadi.</p>
""",
    "st-corr-intro": """
<p>Ikkita ustun birga raqsga tushadimi? Korrelyatsiya shu savolga −1 dan 1 gacha ball beradi. 1 — chiziq bo‘ylab tepa-tepaga. −1 — biri oshsa, ikkinchisi tushadi. 0 — chiziqli bog‘liqlik yo‘q (boshqa turdagi bog‘liqlik bo‘lishi hali mumkin).</p>

<p>Pearson — chiziqli, so‘m va so‘m, tashrif va savdo. Birlikdan mustaqil: so‘mni ming so‘m qilsangiz ham r o‘zgarmaydi. Kovariatsiya esa birlikka yopishadi: “katta son” chiqadi, solishtirish qiyin. Hisobotda odatda r, kovariatsiya emas.</p>

<p>r = 0.8 kuchli ko‘rinadi. r = 0.05, n = 5000 — deyarli yo‘q. Shunda ham p kichik chiqishi mumkin, chunki n katta. Amaliy ahamiyat yo‘q: reklama 1 million oshsa, savdo deyarli qimirlamaydi. p ni r o‘rniga qo‘ymang.</p>

<p>Spearman — o‘rinlar bo‘yicha. Chiziq emas, “biri oshsa, ikkinchisi ham oshadi” (monoton). Outlier Pearson ni buzadi: bitta ulkan nuqta r ni 0.9 qilib qo‘yishi mumkin. Spearman tinchroq. Ikkalasini ham oling, scatter bilan.</p>

<p>Do‘kon: kunlik harorat va muzqaymoq savdosi. r yuqori bo‘lishi mumkin. Reklama so‘mi va tushum ham. Keyingi darsda aytaman: birga yurish — sabab emas. Hozir o‘lcham: r qancha, n qancha, chiziqmi yoki faqat “o‘rin”.</p>

<p>Kichik n da r yolg‘onchi. 8 nuqta, r=0.92 — chiroyli, ishonchsiz. Keyingi tekshiruv darsida scatter majburiy. Hozir: korrelyatsiya — “birga”, “qanchalik”, chiziqli. Sabab so‘zini hali ochmang.</p>
""",
    "st-causation": """
<p>Yoz. Muzqaymoq savdosi oshadi. Cho‘kish ham oshadi. r yuqori. Muzqaymoqni taqiqlaymizmi? Yo‘q. Uchinchi narsa — issiq ob-havo, dam olish, suv. Ikki seriya birga yuradi, biri ikkinchisini tug‘dirmaydi.</p>

<p>Biznesda yumshoqroq, lekin shu tuzoq. Reklama budjeti oshdi, tushum ham. Shu oyda Narx.uz da ham mavsum, ramazon oldi, yangi ombor, dollarning qimirishi. “Reklama keltirdi” demay, “birga o‘sdi” deying. Sabab uchun tajriba kerak: A/B, yoki hech bo‘lmaganda vaqt va boshqa omillarni ushlab turish.</p>

<p>Tahlilchi tili. “X va Y birga harakat qiladi.” “X oshganda Y ham oshishga moyil.” “X sabab bo‘ldi” — faqat dizayn ruxsat bersa. Slayddagi o‘q (reklama → savdo) odamni ishontiradi. O‘qni chizishdan oldin so‘rang: buni teskarisiga ham aytish mumkinmi? Savdo oshgani uchun reklama ko‘paygan bo‘lishi ham mumkin.</p>

<p>Yana: o‘tkazib yuborilgan o‘zgaruvchi. Filiallar: xodim soni va savdo korrelyatsiyasi yuqori. Sabab “ko‘p kishi = ko‘p savdo”mi, yoki katta filialda ham xodim ko‘p, ham savdo ko‘pmi? Maydon, joy, trafik. Segmentlab qarang.</p>

<p>Qisqa qasamyod, ish uchun: korrelyatsiya gipoteza beradi, hukm emas. Hukm — tajriba yoki kuchli mantiq + boshqa omillar. Rahbar “demak qilamiz” desa, siz: “Bog‘liqlik bor, sababni hali o‘lchamadik. Kichik A/B yoki bir mintaqada sinab ko‘ramiz.”</p>
""",
    "st-corr-check": """
<p>r ni chiqarish — 10 soniya. Ishonish — tekshiruv. Avval scatter. Nuqtalar chiziqmi, bananmi, ikki uyummi? Bitta nuqta o‘ng yuqorida yolg‘izmi? Shu yolg‘iz nuqta Pearson ni o‘g‘irlagan bo‘lishi mumkin. Grafiksiz r — yopiq ko‘z.</p>

<p>Pearson va Spearman yonma-yon. Ikkalasi ham 0.7 — chiziqqa yaqin. Pearson 0.9, Spearman 0.3 — outlier yoki egri bog‘liqlik. Faqat Spearman yuqori — monoton, lekin to‘g‘ri chiziq emas. Modelga chiziqli regressiya qo‘ymoqchi bo‘lsangiz, bu ogohlantirish.</p>

<p>Segment. Butun O‘zbekiston bo‘yicha r=0.1. Toshkentda 0.6, viloyatda 0.0. Aralash hammasi “yo‘q” dek ko‘rinadi. Yoki aksincha: umumiy r yuqori, har viloyat ichida yo‘q — Simpsonga yaqin tuzoq. Region, kanal, B2B flag bo‘yicha alohida.</p>

<p>Vaqt kechikishi. Dushanba reklama, chorshanba savdo. Shu kunlik korrelyatsiya past, 2 kun lag bilan yuqori. Kampaniya “ishlamadi” deb yozmang, avval lag ni sinab ko‘ring. Haftalik agregat ham kunlik shovqinni yutishi mumkin.</p>

<p>n=8, r=0.92. Chiroyli slayd, yomon ilm. Bitta nuqta o‘zgarsa, r tushadi. “Ko‘proq nuqta kerak” — to‘g‘ri gap. n ni r yoniga yozing. Katta n, kichik r: “statistik jihatdan sezilarli, amaliy jihatdan yo‘q” — shu jumla sizni qutqaradi.</p>

<p>Cheklist, qisqa: scatter, ikki xil r, segment, lag, n. To‘rtinchi qadamda “sabab” hali yo‘q. Faqat “ishonchliroq bog‘liqlik bormi?”</p>
""",
    "st-h0": """
<p>Gipoteza tekshiruvi — sudga o‘xshaydi, lekin aybdorlikni isbotlamaydi. <strong>H0</strong>: “farq yo‘q”, “yangi tugma konversiyani o‘zgartirmaydi”, “ikki filial bir xil.” Siz ma’lumot bilan H0 ni qanchalik ajablantirishingizni o‘lchaysiz. H1 — “farq bor”, odatda shu narsa sizni qiziqtiradi.</p>

<p>p-value: H0 rost bo‘lsa, shunchalik yoki undan ham ekstremal natija ko‘rish ehtimoli. Qayta o‘qing. Bu “H0 rost ehtimoli” emas. Bu “biznes yutish ehtimoli” ham emas. Bu “agar hech narsa o‘zgarmagan bo‘lsa, bugungi kabi (yoki undan ham g‘alati) rasm qanchalik kam uchrardi.”</p>

<p>Kichik p — H0 ostida bu rasm g‘alati. Katta p — H0 ostida ham shunday narsa odatiy, ajablanmaymiz. Katta p “farq yo‘qligini isbotladi” degani emas. Shunchaki dalil zaif. Sud “aybsiz” demaydi, “yetarli dalil yo‘q” deydi. Tahlilchi ham shunday.</p>

<p>Landing A/B. H0: ikkala variantning haqiqiy konversiyasi teng. B da 30 ta ko‘p xarid. p kichik bo‘lsa — “tasodif deb aytish qiyin.” p katta bo‘lsa — “bu 30 ta hali shovqin bo‘lishi mumkin.” Effektning o‘zi (0.3 punkt) alohida gap — keyingi dars.</p>

<p>α = 0.05 — kelishuv. Sehrli emas. Ba’zi sohalarda 0.01, ba’zida 0.1. Muhimi: chegara oldindan. Natijaga qarab 0.05 ni 0.06 qilib “yutdik” demang.</p>

<p>Eslab qoling: H0 — “hech narsa yo‘q” deb qo‘yilgan somon odam. p — uni qanchalik qiyin hayotga duchor qilganingiz. Keyingi darsda shu p ni rahbarga qanday aytishni mashq qilamiz. Formula emas, gap.</p>
""",
    "st-pvalue": """
<p>Rahbar so‘raydi: “Yutdikmi?” Siz p=0.04 ni ko‘ryapsiz. Yomon javob: “96% ishonch bilan yutdik.” p=0.04 “H0 ning 4% rostligi” emas, “96% muvaffaqiyat” ham emas. Yaxshi javob: “Agar variantlar aslida bir xil bo‘lsa, bunqa (yoki undan zo‘r) farqni kam uchratardik. Farq taxminan +0.3 punkt, oraliq mana shu. Amaliy tomoni: oyiga taxminan 12 million. Lekin sahifa 0.4 soniya sekinlashdi.”</p>

<p>p=0.06. Yomon: “Hech narsa yo‘q, to‘xtatamiz, yutqazdik.” To‘g‘riroq: “Dalil zaifroq, odatdagi 0.05 dan o‘tmadi. Effekt yo‘qolgani emas — hali shovqindan ajralmayapti. Yana ma’lumot yoki katta effekt kerak. Hozir ‘tasdiqlandi’ deb kengaytirmayman.”</p>

<p>p=0.049 va p=0.051 — deyarli bir xil. Biri “yashil”, biri “qizil” qilish — o‘yin. α=0.05 chiziq, tabiat qonuni emas. Ikkalasini ham effekt va CI bilan bering. Chiziqdan 0.001 o‘tgani uchun kampaniyani 10x qilish — tahlil emas, sehr.</p>

<p>Ko‘p test. 20 ta KPI, biri p&lt;0.05. Tasodifan ham “yutgan” chiqishi oddiy. Oldindan <strong>bitta asosiy metrika</strong>: konversiya. Qolganlari — izoh, kashfiyot, ikkinchi navbat. “Qaysi p kichik bo‘lsa, o‘shani yutgan deb e’lon qilamiz” — p-hacking. Rahbarga: “Asosiy metrika oldindan belgilangan. Boshqalarida farq ko‘rsak, yangi gipoteza, yangi test.”</p>

<p>Peeking: har soat p ni ochib, 0.05 ga tushishi bilan to‘xtatish. Bu ham yolg‘on ijobiy ko‘paytiradi. Reja: n yetadi, keyin ochamiz. Yoki ketma-ket usullar (ular alohida qoida). Oddiy A/B da erta to‘xtatish — o‘zingizni aldash.</p>

<p>Gap andozasi, yodlang: “p = …, bu H0 ni qanchalik qiyinlashtiradi. Effekt = …, CI = …. Men shu harakatni maslahat beraman, chunki pul/xavf shunday. p yolg‘iz qaror emas.”</p>
""",
    "st-abtest": """
<p>Yangi “Xarid” tugmasi. Yashil vs ko‘k. His qilasiz — yashil yutadi. His yetmaydi. A/B: odamlarni tasodifiy ikkiga. Bitta asosiy metrika — konversiya, oldindan. “Konversiya, savdo, vaqt, bounce, 12 ta segment” — keyin 20 ta p, bittasi yashil chiqadi.</p>

<p>Dizayn. Minimal aniqlamoqchi effekt (MDE): 0.3 punkt yetadimi, yoki 0.1 ham pul beradimi? 0.1% ni ko‘rish uchun n katta kerak. n kichik, effekt kichik — power past: haqiqiy farq bo‘lsa ham “topolmaymiz.” Rahbar “nima uchun sezilmadi?” desa: “Kutilgan effektga nisbatan namuna yetmadi, yo‘qligini emas.”</p>

<p>Randomizatsiya. Dushanba hammasi A, juma hammasi B — bu test emas, hafta kuni testi. Qurilma, viloyat, yangi/eski mijoz — tasodif aralashtirsin. Peeking: kechqurun p=0.04 bo‘lishi bilan to‘xtatmang. Segmentlarni oldindan yozing (masalan, mobil), natijadan keyin 30 kesim ochib “mobil yutdi” demang.</p>

<p>Natija qanday aytiladi, formula emas. “Yashil tugma: +0.3 punkt (95% CI: +0.05 dan +0.55). p=0.02. H0 ‘farq yo‘q’ ni qiyinlashtirdi. Amaliy: hozirgi trafikda oyiga taxminan 12 million qo‘shimcha. Texnik: sahifa 0.4 soniya sekin — savdo shu sekinlikni yeb qo‘yishi ham mumkin, alohida kuzatamiz. Tavsiya: yashilni asosiy qilamiz, tezlikni alohida sprint.”</p>

<p>Yutmagan test ham javob. “Farq +0.05 punkt, CI noldan o‘tadi, p=0.4. Dalil yo‘q. Tugmani ‘yaxshi ko‘rinadi’ uchun almashtirish mumkin, lekin pul va’da qilmayman. Dizayn qarori — mahsulot, statistika emas.”</p>

<p>Sizning ishingiz — yashil chiroq yoqish emas. O‘lcham, noaniqlik, pul, yon ta’sir. Rahbar shu to‘rtlikni eshitsa, p ni so‘ramay qo‘yadi. Yaxshi.</p>
""",
    "st-linreg": """
<p>Chiziq: savdo ≈ a + b × reklama. a — reklama nol bo‘lganda modelning “boshlang‘ich”i (ko‘pincha ma’nosiz, chunki reklama nol bo‘lmaydi). b — reklama 1 birlik oshganda savdoning <em>o‘rtacha</em> o‘zgarishi, model aytishicha. Hayotda boshqa narsa doimiy emas. Shuning uchun b — bog‘liqlik o‘lchami, tugma emas.</p>

<p>b = 0.3, x — reklama million so‘m, y — savdo million so‘m. Ehtiyotkor o‘qish: “Shu ma’lumotda reklama 1 million ko‘proq bo‘lgan kunlarda savdo o‘rtacha 0.3 million yuqoriroq.” “1 million qo‘ysangiz, albatta 0.3 keladi” — sabab, tajriba yo‘q. Mavsum, narx, ombor birga yurgan bo‘lishi mumkin.</p>

<p>Qoldiq (residual): haqiqiy savdo minus chiziq. Ularni chizing. Tasodifiy nuqta — yaxshi. Dum, egri, vaqt bo‘yicha o‘sish — chiziq yolg‘on. Bitta ulkan kun butun b ni burishi mumkin. Scatter sizni yana qutqaradi.</p>

<p>Ko‘p o‘zgaruvchi keyinroq. Hozir bitta x. Ikkinchi x ni qo‘shsangiz, b o‘zgaradi: “boshqa narsa ushlanganda.” U ham hali sabab emas, faqat shartli o‘rtacha.</p>

<p>Rahbarga: “Reklama va savdo orasida musbat chiziq bor, qiyalik 0.3. Bu ‘qo‘y — ol’ emas. Sinab ko‘rish uchun budjetni bitta viloyatda oshirib, qolganini ushlab turish mumkin.” Model — gapirish usuli. Avtomatik kran emas.</p>
""",
    "st-rsq": """
<p>R² — model y o‘zgarishining qancha qismini “tushuntirdi.” 0 — chiziq o‘rtachadan yomonroq yordam bermaydi. 1 — nuqtalar chiziqda. 0.95 chiroyli. 3 nuqtada 0.95 — deyarli har doim chiziq o‘tadi. n kichik, R² katta — haddan oshirish xavfi, mukammal bashorat emas.</p>

<p>Yuqori R² yomon modelni yashirmaydi. O‘zgaruvchi oqishi: savdoni “kechagi savdo + bugungi soat” bilan tushuntirish — R² osmonda, foyda yo‘q. Yoki kelgusi tushumni o‘sha tushumning bir qismi bilan bashorat. Avval mantiq: bu x ni oldindan bilamizmi?</p>

<p>Past R² ham fojia emas. Odam xulqi shovqinli. R²=0.15, lekin b tushunarli va barqaror bo‘lsa — baribir foydali yo‘nalish. “Model yomon, tashlaymiz” = “odamlar chiziq emas.” To‘g‘ri. Shuning uchun baseline: o‘tgan oyning o‘rtachasi. Yangi model o‘rtachadan yaxshimi? R² yolg‘iz javob bermaydi, solishtirish beradi.</p>

<p>Grafik + biznes mantiq + baseline. Uchlik. R² slaydning birinchi qatori bo‘lmasin. “95% tushuntirdik” deb aytmang — odam 95% aniq bashorat deb tushunadi. Aytish: “Chiziq y o‘zgarishining katta qismini ushlaydi, lekin n=3 / oqish / outlier tekshiruvi ochiq.”</p>

<p>Qisqa: R² — moslash o‘lchami, haqiqat o‘lchami emas. Kichik n da ishonmang. Katta R² da savol bering: nima tushuntirildi, ertaga ham shu x bormi?</p>
""",
    "st-interpret": """
<p>Oxirgi dars. Yangi sehr yo‘q. Siz endi mean ni median dan, p ni “96% yutdik” dan, r ni sababdan ajratasiz. Qolgani — yozish. Rahbar p o‘qimaydi. U “nima qilamiz?” ni o‘qiydi.</p>

<p>Har hisobotni besh nafasda yozing. Avval savol va kimlar: “Mart oyida online to‘langan buyurtmalar, Toshkent+Samarqand — yangi tugma konversiyani oshirdimi?” Populyatsiya chegarasi shu jumlada.</p>

<p>Keyin ta’rif: konversiya = xarid / unikal tashrif, botlar yo‘q, qaytarish keyingi hafta. Keyin son va noaniqlik: +0.2 punkt, CI noldan o‘tadi, p=0.11, n unchalik katta emas. Keyin cheklov: faqat mobil, bayram yo‘q, bir kanal. Oxirida bitta harakat: “Hozir 10x kengaytirmaymiz. Yana ikki hafta yig‘amiz yoki effektni kattaroq qiladigan variant sinaymiz. Kuchsiz dalil — ‘yutqazdik’ ham, ‘yutdik’ ham emas.”</p>

<p>Yomon yakun: “p kichik.” Yaxshi yakun: “Shu chegara ichida shunday qilishni maslahat beraman.” Siz sudya emassiz, maslahatchisiz. Noaniqlikni yashirish — keyin ishonch yo‘qoladi. Ochiq aytish — keyin katta n da gapingiz og‘irlashadi.</p>

<p>Kurs yopilishi shu. Statistika sizga formula bermadi, til berdi. O‘rtacha aldasa — median. Ikki filial teng ko‘rinasa — tarqalish. Foiz sakrasa — n va CI. Ikki ustun raqsga tushsa — sabab emas. A/B — oldindan metrika, keyin pul tili. Regressiya — o‘rtacha chiziq, kran emas.</p>

<p>Ertaga dashboard ochiladi. Uch savol: nima o‘lchanayapti, qanchalik barqaror, nima qilamiz. Javobni rahbar tushunadigan jumlada yozing. Shu — tahlilchi.</p>
""",
}
