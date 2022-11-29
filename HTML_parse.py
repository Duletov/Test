from bs4 import BeautifulSoup

html = """

<!DOCTYPE html>
<html prefix="og: http://ogp.me/ns#" lang="ru">
<head>
<title>Лучшие песни в жанре «Русский рок»  на русском языке</title>
<meta charset="UTF-8" />
<meta name="keywords" content="100 лучших песен всех времен рейтинг топ сто" />
<meta name="description" content="100 лучших песен всех времен, online голосование" />
<meta name=viewport content="width=device-width, initial-scale=1.0" />
<meta property="og:title" content="Лучшие песни в жанре «Русский рок»  на русском языке" />
<meta property="og:type" content="website" />
<meta property="og:url" content="http://www.100bestsongs.ru/index.php?lang_id=21&time_id=0&tag_id=73&avail=0&page=3&main_list=1&sort=points" />
<meta property="og:image" content="http://www.100bestsongs.ru/img/logo-fb.jpg" />
<meta property="og:description" content="100 лучших песен всех времен, online голосование" />
<link rel="icon" href="/img/favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="/img/favicon.ico" type="image/x-icon">
<link rel="alternate" media="only screen and (max-width: 640px)" href="http://www.100bestsongs.ru/m/index.php?page=3" >
<link rel="stylesheet" href="script/jquery-ui-1.11.4.others/jquery-ui.min.css" type="text/css"/>
<meta name='yandex-verification' content='7c34ea3eca8d53bb'>
<meta name="google-site-verification" content="aX6f8oSL952Yq-Bu_9unxfyhqawEcqmn5FY2F4wBQug">
<link rel="stylesheet" type="text/css" href="/style/100songs.css">

<script type="text/javascript" src="//vk.com/js/api/openapi.js?121"></script>
<script type="text/javascript">
  VK.init({apiId: 5288510, onlyWidgets: true});
</script>
<script src="script/jquery-1.11.0.min.js" type="text/javascript"></script>
<script src="script/jquery-ui-1.11.4.others/jquery-ui.min.js " type="text/javascript"></script>
 
</head>
<body onload="showHighlighted()">
    <script type="text/javascript">
        function showHighlighted() {
            var el = document.getElementById('scroll_point');
            if (el != null) {
                el.scrollIntoView(true);
            }
        }

        function copyList() {
            $("#copyDialog").dialog();
        }

        function showListToCopy() {
            var frmt = "text";
            var o = document.getElementsByName("listFormat");
            for (var i = 0; i < o.length; i++) {
                if (o[i].checked) {
                    frmt = o[i].value;
                    break;
                }
            }
            if (frmt == "text") {
                $.get('list_txt.php', function (data) {
                    showListCallBack(data);
                });
            } else {
                $.get('list_html.php', function (data) {
                    showListCallBack(data);
                });
            }
            $("#copyDialog").dialog('close');
        }

        function showListCallBack(data) {
            var obj = $("#copyListArea");
            obj.text(data);
            $("#copyListDialog").dialog();
        }
    </script>
    	<div style="background: url('/img/fon-top.jpg') top left repeat-x;">
		<img src="/img/p.gif" width="52" height="117" alt="" style="border: 0px">
	</div>
	<div class="wall">
		<img src="/img/wall.png" width="400" height="400" alt="" class="iePNG">
	</div>
	<div style="z-index:100;background-color: black; color: white; position:absolute; top: 3px; left:50px; padding: 3px 10px 3px 10px; font-family: Arial">
		<a href="/m/index.php" title="Мобильная версия" class="mobile">Мобильная версия</a>
	</div>
	<script type="text/javascript" src="/script/utils.js"></script>
	<form action="/search.php" method="post" name="searchForm">
	<input type="hidden" name="back" value="0">
	<table class="table-menu">
		<tr>
			<td class="col-mainmenu">
				<div class="mainmenu">
					<table style="border-spacing: 0px; border: 0px; padding: 0px; width:100%">
						<tr>
							<td><img src="/img/p.gif" width="43" height="14" alt=""></td>
							<td class='menu-item-select'><b>100 лучших песен</b></td>
							<td class='menu-item'><a href='/add_item.php'  title='Добавить песню'><b>Добавить песню</b></a></td>
							<td class='menu-item'><a href='/start_vote.php'  title='Проголосовать за песни из списка лучших песен всех времен'><b>Проголосовать</b></a></td>
							<td class='menu-item'><a href='/index.php?main_list=0' class='notmain' title='Список песен&ndash;кандидатов на включение в основной список лучших'><b>Список кандидатов</b></a></td>
							<td class='menu-item'><a href='/names.php' class='notmain' title='Лучшие исполнители'>Лучшие исполнители</a></td>
							<td class='menu-item'><a href='/news.php' class='notmain' title='Новости'>Новости</a></td>
							<td class='menu-item'><a href='/ratings.php' class='notmain' title='Другие музыкальные рейтинги и топы'>Другие рейтинги песен</a></td>
							<td class="menu-search" style="padding-left:5px"><input type="text" maxlength="200" id="searchText" name="q" class="" value="поиск..." onKeyPress="return onEnterKey(event, 'searchText', 'поиск...')" onFocus="clearText('searchText', 'поиск...')" onBlur="setText('searchText', 'поиск...')"></td>
							<td><a href="javascript:doSearch('searchText', 'searchForm', 'поиск...')"><img src="/img/icon-search.gif" width="14" height="14" alt="Найти" title="Найти" style="border: 0px"></a></td>
						</tr>
					</table>
				</div>
				<img src="/img/menu-shadow.png" height="39" class="iePNG" style="width: 100%" alt="">
            </td>
		</tr>
	</table>
	</form>
    <div id="copyDialog" title="Копировать список" style="display:none" >
        <p>Выберите формат списка для копирования</p>
        <input type="radio" value="html" id="htmlFormat" name="listFormat" checked>&nbsp;<label for="htmlFormat">HTML (для вставки в блог)</label><br>
        <input type="radio" value="text" id="textFormat" name="listFormat"><label for="textFormat">Текст</label><br><br>
        <input type="button" value="Ok" onclick="showListToCopy()">&nbsp;
        <input type="button" value="Отмена" onclick="$('#copyDialog').dialog('close')">

    </div>
    <div id="copyListDialog" title="Копировать список" style="display:none" >
        <p>Скопируйте список из формы ниже</p>
        <textarea rows="10" cols="30" id="copyListArea"></textarea>
        <br><br>
        <input type="button" value="Закрыть" onclick="$('#copyListDialog').dialog('close')">
    </div>

    <table class="table-main" itemscope itemtype="http://schema.org/ItemList">
        <tr>
    <td colspan="2" class="col-adv">
<!--script type="text/javascript"><!--
google_ad_client = "pub-4958342012590043";
/* Песни: верхний баннер 728x90 */
google_ad_slot = "2501303439";
google_ad_width = 728;
google_ad_height = 90;
//->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script-->
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Песни: верхний баннер адапт -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-4958342012590043"
     data-ad-slot="1979694025"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
	</td>
	<td class="col-intro-adv">
    </td>
</tr>
        <tr style="vertical-align: top">
            <td style="width: 33%" class="col-logo">
                <meta itemprop="itemListOrder" content="http://schema.org/ItemListOrderDescending" />
                <a href="index.php?tag_id=0&time_id=0&lang_id=0" title="100 лучших песен всех времен">
                    <img itemprop="image" src="img/logo.gif" class="logo-project" alt="Рейтинг 100 лучших песен всех времен" />
                </a>
                <p>Представляем вам рейтинг 100 лучших песен всех времен. Список, который вы&nbsp;видите ниже, составлен по&nbsp;итогам голосования посетителей нашего сайта. Голосование является открытым для всех, свободным и&nbsp;бессрочным, т.е. не&nbsp;имеющим даты окончания.</p>
            </td>
            <td style="width: 33%" class="col-intro">
                <p>В&nbsp;голосовании может принять участие абсолютно любой желающий, для этого не&nbsp;требуется какая-либо регистрация. Добавлять в&nbsp;рейтинг и&nbsp;голосовать можно за&nbsp;все, что называется песней в&nbsp;общепринятом понимании этого слова. Добавляйте, голосуйте, участвуйте.</p>
                <p>Добро пожаловать в&nbsp;мир 100 лучших песен всех времен!</p>
            </td>
            <td style="width: 33%" class="col-intro">
                

            </td>
        </tr>
            <tr>
                <td colspan="2" style="padding-left: 50px; padding-top: 40px; ">
                    <h1><span itemprop="name">Лучшие песни в жанре «Русский рок»  на русском языке</span>
                                                    <sup title="Сбросить фильтр"><a href="index.php?time_id=0&lang_id=0&tag_id=0" style="color: red; text-decoration: none; font-size: 16px; font-family: Arial">x</a></sup>
                                            </h1>
                </td>
                <td>&nbsp;</td>
            </tr>
        <tr style="vertical-align: top">
            <td colspan="2" class="col-content">
                    <div class="settings-opened">
                        <div class="settings-btn">
                            <a href="index.php?sett=0"><img src="img/btn-settings-close.gif" class="s-close-btn" alt="+" /></a>
                        </div>
                        <div class="settings-txt">
                            <div class="settings-name">По языкам:</div>                            <div class="settings-name">По времени:</div>
<div class='s-pad'><b>Все</b></div><div class='s-pad'><a href='index.php?time_id=49' class='s-settings'>2010-е</a></div><div class='s-pad'><a href='index.php?time_id=13' class='s-settings'>2000-е</a></div><div class='s-pad'><a href='index.php?time_id=14' class='s-settings'>1990-е</a></div><div class='s-pad'><a href='index.php?time_id=15' class='s-settings'>1980-е</a></div><div class='s-pad'><a href='index.php?time_id=16' class='s-settings'>1970-е</a></div><div class='s-pad'><a href='index.php?time_id=17' class='s-settings'>1960-е</a></div><div class='s-pad'><a href='index.php?time_id=18' class='s-settings'>1950-е</a></div><div class='s-pad'><a href='index.php?time_id=47' class='s-settings'>1940-е</a></div><div class='s-pad'><a href='index.php?time_id=48' class='s-settings'>1930-е</a></div>                        </div>
                    </div>
                <table class="table-rating">
                    <tr>
                        <th style="width:1%">&nbsp;</th>
                        <th class="th-name">
                            <b>Песня</b>
                            <i><a href="javascript:void(0);" onclick="copyList()">Копировать список</a></i>
                        </th>
                        <th class="th-year" style="color: #999;">Год</th>
                        <th class="th-aver" style="color: #999;"><a href="index.php?sort=av" class="sort-columns" title="Сортировать по этой колонке">Средний балл</a></th>
                        <th class="th-votes" style="color: #999;">Проголосовало</th>
                        <th class="th-balls" style="color: #999;"><a href="index.php?sort=points" class="sort-columns" title="Сортировать по этой колонке"><b>Баллы</b></a></th>
                    </tr>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>201</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16355'><span itemprop='name'>Птицы белые мои</span></a><meta  itemprop='datePublished' content='1996'/></TD><TD class='vline-year'>1996</TD><TD class='vline'>4.16</TD><TD>30</TD><TD class='vline'><b>125</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>202</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2568' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ночные снайперы</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=8715'><span itemprop='name'>Я люблю того, кто не придет ...</span></a><meta  itemprop='datePublished' content='1999'/></TD><TD class='vline-year'>1999</TD><TD class='vline'>1.47</TD><TD>85</TD><TD class='vline'><b>125</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>203</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7213'><span itemprop='name'>Аллергия</span></a><meta  itemprop='datePublished' content='1989'/></TD><TD class='vline-year'>1989</TD><TD class='vline'>1.59</TD><TD>77</TD><TD class='vline'><b>123</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>204</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3751' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Вадим Самойлов</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7096'><span itemprop='name'>Медленный снег</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>1.47</TD><TD>82</TD><TD class='vline'><b>121</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>205</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7097'><span itemprop='name'>Пантера</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>0.85</TD><TD>142</TD><TD class='vline'><b>121</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>206</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=148' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Кино</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16360'><span itemprop='name'>Вопрос</span></a><meta  itemprop='datePublished' content='2000'/></TD><TD class='vline-year'>2000</TD><TD class='vline'>4.61</TD><TD>26</TD><TD class='vline'><b>120</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>207</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16316'><span itemprop='name'>Матерь богов</span></a><meta  itemprop='datePublished' content='1997'/></TD><TD class='vline-year'>1997</TD><TD class='vline'>4.61</TD><TD>26</TD><TD class='vline'><b>120</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>208</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16327'><span itemprop='name'>Цветок</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>4.44</TD><TD>27</TD><TD class='vline'><b>120</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>209</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16311'><span itemprop='name'>Я покидаю землю</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>4.44</TD><TD>27</TD><TD class='vline'><b>120</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>210</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16320'><span itemprop='name'>Атлантида</span></a><meta  itemprop='datePublished' content='1997'/></TD><TD class='vline-year'>1997</TD><TD class='vline'>4.72</TD><TD>25</TD><TD class='vline'><b>118</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>211</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16324'><span itemprop='name'>Иван Человеков</span></a><meta  itemprop='datePublished' content='1991'/></TD><TD class='vline-year'>1991</TD><TD class='vline'>4.72</TD><TD>25</TD><TD class='vline'><b>118</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>212</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16312'><span itemprop='name'>Могилы младших сестёр</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>4.72</TD><TD>25</TD><TD class='vline'><b>118</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>213</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16332'><span itemprop='name'>Невесомость</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>4.72</TD><TD>25</TD><TD class='vline'><b>118</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>214</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=12742'><span itemprop='name'>Подмога</span></a><meta  itemprop='datePublished' content='2002-2013'/></TD><TD class='vline-year'>2002-2013</TD><TD class='vline'>2.74</TD><TD>43</TD><TD class='vline'><b>118</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>215</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16342'><span itemprop='name'>Музыка на песке</span></a><meta  itemprop='datePublished' content='1989'/></TD><TD class='vline-year'>1989</TD><TD class='vline'>4.10</TD><TD>28</TD><TD class='vline'><b>115</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>216</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16314'><span itemprop='name'>Скалолазы</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>4.75</TD><TD>24</TD><TD class='vline'><b>114</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>217</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=5817' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">СерьГа</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=11820'><span itemprop='name'>Берегите лес</span></a><meta  itemprop='datePublished' content='2011'/></TD><TD class='vline-year'>2011</TD><TD class='vline'>2.03</TD><TD>56</TD><TD class='vline'><b>114</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>218</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16329'><span itemprop='name'>10 шагов</span></a><meta  itemprop='datePublished' content='2012'/></TD><TD class='vline-year'>2012</TD><TD class='vline'>4.82</TD><TD>23</TD><TD class='vline'><b>111</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>219</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16310'><span itemprop='name'>Колесницегонитель</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>4.82</TD><TD>23</TD><TD class='vline'><b>111</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>220</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7063'><span itemprop='name'>Грязь</span></a><meta  itemprop='datePublished' content='1997'/></TD><TD class='vline-year'>1997</TD><TD class='vline'>1.60</TD><TD>69</TD><TD class='vline'><b>111</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>221</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7058'><span itemprop='name'>Второй фронт</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>1.09</TD><TD>101</TD><TD class='vline'><b>111</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>222</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16811'><span itemprop='name'>Возьми меня с собой</span></a><meta  itemprop='datePublished' content='2014'/></TD><TD class='vline-year'>2014</TD><TD class='vline'>4.78</TD><TD>23</TD><TD class='vline'><b>110</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>223</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16817'><span itemprop='name'>Всё, что нужно</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>4.95</TD><TD>22</TD><TD class='vline'><b>109</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>224</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16350'><span itemprop='name'>Прятки</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>4.54</TD><TD>24</TD><TD class='vline'><b>109</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>225</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16375'><span itemprop='name'>Ударная любовь</span></a><meta  itemprop='datePublished' content='2001'/></TD><TD class='vline-year'>2001</TD><TD class='vline'>4.36</TD><TD>25</TD><TD class='vline'><b>109</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>226</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16338'><span itemprop='name'>Воздух</span></a><meta  itemprop='datePublished' content='1994'/></TD><TD class='vline-year'>1994</TD><TD class='vline'>3.75</TD><TD>29</TD><TD class='vline'><b>109</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>227</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7208'><span itemprop='name'>Пинкертон</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>1.11</TD><TD>98</TD><TD class='vline'><b>109</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>228</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16309'><span itemprop='name'>Эхолов</span></a><meta  itemprop='datePublished' content='2004'/></TD><TD class='vline-year'>2004</TD><TD class='vline'>4.69</TD><TD>23</TD><TD class='vline'><b>108</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>229</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16812'><span itemprop='name'>Чёрная птица - белые крылья</span></a><meta  itemprop='datePublished' content='2014'/></TD><TD class='vline-year'>2014</TD><TD class='vline'>4.86</TD><TD>22</TD><TD class='vline'><b>107</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>230</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16341'><span itemprop='name'>20 000</span></a><meta  itemprop='datePublished' content='1994'/></TD><TD class='vline-year'>1994</TD><TD class='vline'>4.65</TD><TD>23</TD><TD class='vline'><b>107</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>231</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16326'><span itemprop='name'>Чистый плюс</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>4.45</TD><TD>24</TD><TD class='vline'><b>107</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>232</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16319'><span itemprop='name'>Во время дождя</span></a><meta  itemprop='datePublished' content='1997'/></TD><TD class='vline-year'>1997</TD><TD class='vline'>4.03</TD><TD>26</TD><TD class='vline'><b>105</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>233</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16306'><span itemprop='name'>Человек без имени</span></a><meta  itemprop='datePublished' content='1989'/></TD><TD class='vline-year'>1989</TD><TD class='vline'>3.62</TD><TD>29</TD><TD class='vline'><b>105</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>234</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=7859' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Градусы</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=15782'><span itemprop='name'>Режиссёр</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>2.14</TD><TD>49</TD><TD class='vline'><b>105</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>235</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16815'><span itemprop='name'>Река Небесная</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>4.33</TD><TD>24</TD><TD class='vline'><b>104</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>236</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7054'><span itemprop='name'>Его Там не Было</span></a><meta  itemprop='datePublished' content='1990 - 1991'/></TD><TD class='vline-year'>1990 - 1991</TD><TD class='vline'>1.52</TD><TD>68</TD><TD class='vline'><b>104</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>237</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=151' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">ДДТ</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7328'><span itemprop='name'>Милиционер в рок-клубе</span></a><meta  itemprop='datePublished' content='1990'/></TD><TD class='vline-year'>1990</TD><TD class='vline'>0.47</TD><TD>219</TD><TD class='vline'><b>104</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>238</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16330'><span itemprop='name'>Во сне</span></a><meta  itemprop='datePublished' content='2004'/></TD><TD class='vline-year'>2004</TD><TD class='vline'>4.68</TD><TD>22</TD><TD class='vline'><b>103</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>239</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16356'><span itemprop='name'>Воскресенье</span></a><meta  itemprop='datePublished' content='1996'/></TD><TD class='vline-year'>1996</TD><TD class='vline'>4.12</TD><TD>25</TD><TD class='vline'><b>103</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>240</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7417'><span itemprop='name'>Танцы на грани весны</span></a><meta  itemprop='datePublished' content='1986'/></TD><TD class='vline-year'>1986</TD><TD class='vline'>0.90</TD><TD>113</TD><TD class='vline'><b>102</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>241</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=14177'><span itemprop='name'>Люди на холме</span></a><meta  itemprop='datePublished' content='&nbsp;'/></TD><TD class='vline-year'>&nbsp;</TD><TD class='vline'>1.32</TD><TD>76</TD><TD class='vline'><b>101</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>242</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3741' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Мифы</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7073'><span itemprop='name'>Что будет завтра</span></a><meta  itemprop='datePublished' content='1994'/></TD><TD class='vline-year'>1994</TD><TD class='vline'>1.58</TD><TD>63</TD><TD class='vline'><b>100</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>243</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16814'><span itemprop='name'>Пусть будет так</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>4.50</TD><TD>22</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>244</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16816'><span itemprop='name'>Юпитериада</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>4.30</TD><TD>23</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>245</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16813'><span itemprop='name'>Иду к тебе</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>4.12</TD><TD>24</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>246</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16358'><span itemprop='name'>Спи, душа моя</span></a><meta  itemprop='datePublished' content='1992'/></TD><TD class='vline-year'>1992</TD><TD class='vline'>3.96</TD><TD>25</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>247</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16376'><span itemprop='name'>Что же я такого?</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>3.96</TD><TD>25</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>248</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=5305' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Lumen</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=10911'><span itemprop='name'>Три пути</span></a><meta  itemprop='datePublished' content='&nbsp;'/></TD><TD class='vline-year'>&nbsp;</TD><TD class='vline'>3.09</TD><TD>32</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>249</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7059'><span itemprop='name'>Коммунальный блюз</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>1.04</TD><TD>95</TD><TD class='vline'><b>99</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>250</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7099'><span itemprop='name'>Наша Правда</span></a><meta  itemprop='datePublished' content='1987'/></TD><TD class='vline-year'>1987</TD><TD class='vline'>0.70</TD><TD>134</TD><TD class='vline'><b>94</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>251</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=12961'><span itemprop='name'>Старик Козлодоев</span></a><meta  itemprop='datePublished' content='1981'/></TD><TD class='vline-year'>1981</TD><TD class='vline'>0.41</TD><TD>229</TD><TD class='vline'><b>94</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>252</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16353'><span itemprop='name'>Мне только снится жизнь моя</span></a><meta  itemprop='datePublished' content='2007'/></TD><TD class='vline-year'>2007</TD><TD class='vline'>4.04</TD><TD>23</TD><TD class='vline'><b>93</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>253</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7053'><span itemprop='name'>Дворник</span></a><meta  itemprop='datePublished' content='1995'/></TD><TD class='vline-year'>1995</TD><TD class='vline'>1.70</TD><TD>54</TD><TD class='vline'><b>92</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>254</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16357'><span itemprop='name'>Прошедший день</span></a><meta  itemprop='datePublished' content='1992'/></TD><TD class='vline-year'>1992</TD><TD class='vline'>4.28</TD><TD>21</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>255</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16325'><span itemprop='name'>Летучий фрегат</span></a><meta  itemprop='datePublished' content='1983'/></TD><TD class='vline-year'>1983</TD><TD class='vline'>3.10</TD><TD>29</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>256</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16315'><span itemprop='name'>Падший ангел</span></a><meta  itemprop='datePublished' content='1989'/></TD><TD class='vline-year'>1989</TD><TD class='vline'>3.10</TD><TD>29</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>257</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16336'><span itemprop='name'>Все, кто нёс</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>2.90</TD><TD>31</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>258</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=6338' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Борис Гребенщиков</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=12951'><span itemprop='name'>Русская симфония</span></a><meta  itemprop='datePublished' content='1992'/></TD><TD class='vline-year'>1992</TD><TD class='vline'>1.55</TD><TD>58</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>259</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3751' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Вадим Самойлов</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7095'><span itemprop='name'>Будем, как все</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>1.45</TD><TD>62</TD><TD class='vline'><b>90</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>260</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16347'><span itemprop='name'>Буги с косой</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>4.04</TD><TD>21</TD><TD class='vline'><b>85</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>261</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7057'><span itemprop='name'>Шпала</span></a><meta  itemprop='datePublished' content='1990 -1991'/></TD><TD class='vline-year'>1990 -1991</TD><TD class='vline'>1.02</TD><TD>82</TD><TD class='vline'><b>84</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>262</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7078'><span itemprop='name'>Инспектор по...</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>0.46</TD><TD>168</TD><TD class='vline'><b>78</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>263</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2567' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16377'><span itemprop='name'>Звезда рок-н-ролла</span></a><meta  itemprop='datePublished' content='2001'/></TD><TD class='vline-year'>2001</TD><TD class='vline'>4.22</TD><TD>18</TD><TD class='vline'><b>76</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>264</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2567' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16380'><span itemprop='name'>Оркестр</span></a><meta  itemprop='datePublished' content='2014'/></TD><TD class='vline-year'>2014</TD><TD class='vline'>4.16</TD><TD>18</TD><TD class='vline'><b>75</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>265</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=1995' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Константин Никольский</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16359'><span itemprop='name'>Я бреду по бездорожью</span></a><meta  itemprop='datePublished' content='1992'/></TD><TD class='vline-year'>1992</TD><TD class='vline'>2.96</TD><TD>25</TD><TD class='vline'><b>74</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>266</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7056'><span itemprop='name'>Эпидемия</span></a><meta  itemprop='datePublished' content='1990 - 1991'/></TD><TD class='vline-year'>1990 - 1991</TD><TD class='vline'>1.08</TD><TD>68</TD><TD class='vline'><b>74</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>267</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16333'><span itemprop='name'>Терновник</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>3.38</TD><TD>21</TD><TD class='vline'><b>71</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>268</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16335'><span itemprop='name'>Сердце камня</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>4.05</TD><TD>17</TD><TD class='vline'><b>69</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>269</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3740' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Зоопарк</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7079'><span itemprop='name'>Уездный город N</span></a><meta  itemprop='datePublished' content='1983'/></TD><TD class='vline-year'>1983</TD><TD class='vline'>1.76</TD><TD>39</TD><TD class='vline'><b>69</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>270</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16810'><span itemprop='name'>Гудгора</span></a><meta  itemprop='datePublished' content='2014'/></TD><TD class='vline-year'>2014</TD><TD class='vline'>4.00</TD><TD>17</TD><TD class='vline'><b>68</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>271</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2567' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16378'><span itemprop='name'>Моя любовь</span></a><meta  itemprop='datePublished' content='1997'/></TD><TD class='vline-year'>1997</TD><TD class='vline'>3.40</TD><TD>20</TD><TD class='vline'><b>68</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>272</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16343'><span itemprop='name'>Ястребиная свадьба</span></a><meta  itemprop='datePublished' content='1983'/></TD><TD class='vline-year'>1983</TD><TD class='vline'>3.42</TD><TD>19</TD><TD class='vline'><b>65</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>273</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7101'><span itemprop='name'>Ближе</span></a><meta  itemprop='datePublished' content='2002'/></TD><TD class='vline-year'>2002</TD><TD class='vline'>1.26</TD><TD>50</TD><TD class='vline'><b>63</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>274</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7092'><span itemprop='name'>Щекотно</span></a><meta  itemprop='datePublished' content='1990 - 1991'/></TD><TD class='vline-year'>1990 - 1991</TD><TD class='vline'>0.76</TD><TD>81</TD><TD class='vline'><b>62</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>275</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16313'><span itemprop='name'>Скажи мне, птица</span></a><meta  itemprop='datePublished' content='2008'/></TD><TD class='vline-year'>2008</TD><TD class='vline'>4.06</TD><TD>15</TD><TD class='vline'><b>61</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>276</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16472'><span itemprop='name'>Русский рок</span></a><meta  itemprop='datePublished' content='1995'/></TD><TD class='vline-year'>1995</TD><TD class='vline'>3.22</TD><TD>18</TD><TD class='vline'><b>58</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>277</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16328'><span itemprop='name'>Исполин</span></a><meta  itemprop='datePublished' content='2008'/></TD><TD class='vline-year'>2008</TD><TD class='vline'>3.18</TD><TD>16</TD><TD class='vline'><b>51</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>278</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16394'><span itemprop='name'>212-85-06</span></a><meta  itemprop='datePublished' content='1986'/></TD><TD class='vline-year'>1986</TD><TD class='vline'>1.82</TD><TD>28</TD><TD class='vline'><b>51</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>279</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=5313' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин/Александр Башлачев</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=10959'><span itemprop='name'>Петербургская Свадьба</span></a><meta  itemprop='datePublished' content='1998'/></TD><TD class='vline-year'>1998</TD><TD class='vline'>2.77</TD><TD>18</TD><TD class='vline'><b>50</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>280</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=5305' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Lumen</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=14757'><span itemprop='name'>Синяя птица</span></a><meta  itemprop='datePublished' content='2003'/></TD><TD class='vline-year'>2003</TD><TD class='vline'>1.33</TD><TD>36</TD><TD class='vline'><b>48</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>281</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=148' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Кино</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=12845'><span itemprop='name'>Я хочу быть (кочегаром)</span></a><meta  itemprop='datePublished' content='1983'/></TD><TD class='vline-year'>1983</TD><TD class='vline'>0.92</TD><TD>52</TD><TD class='vline'><b>48</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>282</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2408' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Пикник</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=15074'><span itemprop='name'>Дай себя сорвать</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>1.41</TD><TD>29</TD><TD class='vline'><b>41</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>283</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=12950'><span itemprop='name'>Кардиограмма</span></a><meta  itemprop='datePublished' content='2002'/></TD><TD class='vline-year'>2002</TD><TD class='vline'>0.69</TD><TD>59</TD><TD class='vline'><b>41</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>284</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16470'><span itemprop='name'>Люди</span></a><meta  itemprop='datePublished' content='1989'/></TD><TD class='vline-year'>1989</TD><TD class='vline'>3.54</TD><TD>11</TD><TD class='vline'><b>39</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>285</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2789' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аукцыон</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7941'><span itemprop='name'>Заведующий</span></a><meta  itemprop='datePublished' content='2002'/></TD><TD class='vline-year'>2002</TD><TD class='vline'>1.58</TD><TD>24</TD><TD class='vline'><b>38</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>286</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2026' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Жанна Агузарова</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=3039'><span itemprop='name'>Звёзды всегда хороши, особенно ночью</span></a><meta  itemprop='datePublished' content='1993'/></TD><TD class='vline-year'>1993</TD><TD class='vline'>0.64</TD><TD>56</TD><TD class='vline'><b>36</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>287</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2567' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16666'><span itemprop='name'>Рики-тики-тави</span></a><meta  itemprop='datePublished' content='2001'/></TD><TD class='vline-year'>2001</TD><TD class='vline'>2.50</TD><TD>14</TD><TD class='vline'><b>35</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>288</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2567' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Сплин</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16667'><span itemprop='name'>Всего хорошего</span></a><meta  itemprop='datePublished' content='2001'/></TD><TD class='vline-year'>2001</TD><TD class='vline'>3.40</TD><TD>10</TD><TD class='vline'><b>34</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>289</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=150' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Аквариум</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=17099'><span itemprop='name'>Мама, я не могу больше пить</span></a><meta  itemprop='datePublished' content='&nbsp;'/></TD><TD class='vline-year'>&nbsp;</TD><TD class='vline'>2.26</TD><TD>15</TD><TD class='vline'><b>34</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>290</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16818'><span itemprop='name'>Апокалиптическая</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>2.90</TD><TD>11</TD><TD class='vline'><b>32</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>291</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16819'><span itemprop='name'>Потоп</span></a><meta  itemprop='datePublished' content='2015'/></TD><TD class='vline-year'>2015</TD><TD class='vline'>2.90</TD><TD>11</TD><TD class='vline'><b>32</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>292</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=3857' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Ю-Питер</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16334'><span itemprop='name'>Глаза</span></a><meta  itemprop='datePublished' content='2010'/></TD><TD class='vline-year'>2010</TD><TD class='vline'>2.66</TD><TD>12</TD><TD class='vline'><b>32</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>293</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=151' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">ДДТ</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7705'><span itemprop='name'>Свобода (боль на душе...)</span></a><meta  itemprop='datePublished' content='2011'/></TD><TD class='vline-year'>2011</TD><TD class='vline'>0.58</TD><TD>55</TD><TD class='vline'><b>32</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>294</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2497' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Агата Кристи</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7048'><span itemprop='name'>Нисхождение</span></a><meta  itemprop='datePublished' content='1993'/></TD><TD class='vline-year'>1993</TD><TD class='vline'>0.38</TD><TD>84</TD><TD class='vline'><b>32</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>295</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=4160' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Александр Башлачев</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=7944'><span itemprop='name'>В чистом поле дожди косые</span></a><meta  itemprop='datePublished' content='1988'/></TD><TD class='vline-year'>1988</TD><TD class='vline'>1.76</TD><TD>17</TD><TD class='vline'><b>30</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>296</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=2521' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Янка Дягилева</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=4049'><span itemprop='name'>Особый резон</span></a><meta  itemprop='datePublished' content='&nbsp;'/></TD><TD class='vline-year'>&nbsp;</TD><TD class='vline'>0.63</TD><TD>47</TD><TD class='vline'><b>30</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>297</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=16469'><span itemprop='name'>Морской змей</span></a><meta  itemprop='datePublished' content='1991'/></TD><TD class='vline-year'>1991</TD><TD class='vline'>3.22</TD><TD>9</TD><TD class='vline'><b>29</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>298</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=18873'><span itemprop='name'>Она есть</span></a><meta  itemprop='datePublished' content='1985'/></TD><TD class='vline-year'>1985</TD><TD class='vline'>4.00</TD><TD>6</TD><TD class='vline'><b>24</b></TD></TR>
<TR style='text-align: center'  itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>299</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=18912'><span itemprop='name'>Железнодорожник</span></a><meta  itemprop='datePublished' content='1995'/></TD><TD class='vline-year'>1995</TD><TD class='vline'>2.87</TD><TD>8</TD><TD class='vline'><b>23</b></TD></TR>
<TR style='text-align: center'  class='chet' itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><TD class='vline' style='text-align: right; white-space: nowrap' title='Песня из списка кандидатов, не входит в основной список лучших песен'><span itemprop='position'>300</span> <sup><a href='javascript:void(0)' style='color: green; text-decoration: none; font-size: 11px; font-family: Arial'>&nbsp;?</a></sup></TD><TD class='vline' style='text-align: left' itemprop="item" itemscope itemtype="http://schema.org/MusicComposition"><a href='name_info.php?id=153' itemprop="producer" itemscope itemtype="http://schema.org/MusicGroup"><span itemprop="name">Наутилус Помпилиус</span></a>&nbsp;&mdash;&nbsp;<a href='item_info.php?id=18869'><span itemprop='name'>Анабасис</span></a><meta  itemprop='datePublished' content='1982'/></TD><TD class='vline-year'>1982</TD><TD class='vline'>4.40</TD><TD>5</TD><TD class='vline'><b>22</b></TD></TR>
                    <tr>
                        <td colspan="6" class="table-bottom">
                            <div class="table-line"><img src="img/p.gif" width="1" height="2" alt=""></div>
                            <img src="img/table-shadow.png" style="width: 100%" height="25" class="iePNG" alt="">
                        </td>
                    </tr>
                    <tr>
                        <td class="table-bottom" colspan="3">
Страницы:&nbsp;<a href='index.php?page=1'>1</a>&nbsp;<a href='index.php?page=2'>2</a>&nbsp;<b>3</b>&nbsp;<a href='index.php?page=4'>4</a>                        </td>
                        <td class="table-bottom" colspan="3">
                            <meta itemprop="numberOfItems" content="365" />
                                                            <i><a href="index.php?main_list=0" title="Список песен&ndash;кандидатов на включение в основной список лучших">Список кандидатов</a></i><br>
                                                        <i><a href="javascript:void(0);" title="Скопировать список 100 лучших песен всех времен" onclick="copyList()">Копировать список</a></i><br>
                            <i><a href="start_vote.php"  title="Проголосовать за песни из списка лучших песен всех времен">Проголосовать</a></i>
                        </td>
                    </tr>

                </table>
            </td>
            
            <td class="col-right" rowspan="2">

                <div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ru_RU/sdk.js#xfbml=1&version=v2.5";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<table style="width: 300px; margin-left: -5px;">
	<tr>
		<td>
			<div class="fb-like" data-href="http://www.100bestsongs.ru" data-layout="button_count" data-action="like" data-show-faces="true" data-share="false"></div>
		</td>
		<td>
			<div id="vk_like"></div>
			<script type="text/javascript">
			VK.Widgets.Like("vk_like", {type: "button", height: 20});
			</script>
		</td>
	</tr>
</table>
<br>                <div class="block-header">
	<div class="header">Все списки лучших</div>
</div>
<br style="clear: both">
<div class="other-sites">
<a href="http://www.100bestbooks.ru" rel="nofollow">100 лучших книг</a><br><a href="http://www.100bestpoems.ru" rel="nofollow">100 лучших стихотворений</a><br><a href="http://www.100bestmovies.ru" rel="nofollow">100 лучших фильмов</a><br><a href="http://www.100bestalbums.ru" rel="nofollow">100 лучших альбомов</a><br><b>100 лучших песен</b><br></div>
<br>
                                                                    <div class="block-header">
        <div class="header">
            Результаты за неделю        </div>
    </div>
    <div class="block-notice-t">
        <table>
            <tr>
                <th colspan="2">Место</th>
                <th></th>
                <th colspan="2" style="text-align: right">Баллы</th>
            </tr>
                <tr>
                    <td class="rr-1">
                        19                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=2764">The Tremeloes &ndash; Silence Is Golden</a>
                                            </td>
                    <td title="+60 баллов" class="rr-4">
                        <b style="color:green">+60</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        18                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=2773">The Searchers &ndash; Sweets For My Sweet</a>
                                            </td>
                    <td title="+60 баллов" class="rr-4">
                        <b style="color:green">+60</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        190                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=8288">Пол Маккартни &ndash; Live and Let Die</a>
                                            </td>
                    <td title="+60 баллов" class="rr-4">
                        <b style="color:green">+60</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        160                    </td>
                    <td class="rr-2">
<img alt="" class="btn-vote" src="img/res-up.png"><sup style="color: green">+2</sup>                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=8360">The Beatles &ndash; Drive My Car</a>
                                            </td>
                    <td title="+60 баллов" class="rr-4">
                        <b style="color:green">+60</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        161                    </td>
                    <td class="rr-2">
<img alt="" class="btn-vote" src="img/res-up.png"><sup style="color: green">+2</sup>                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=8365">The Beatles &ndash; All  My Loving</a>
                                            </td>
                    <td title="+60 баллов" class="rr-4">
                        <b style="color:green">+60</b>
                    </td>
                </tr>
            <tr><td></td><td></td><td><b>...</b></td><td></td></tr>
                <tr>
                    <td class="rr-1">
                        263                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=2614">Валерий Ободзинский &ndash; Восточная песня</a>
                                            </td>
                    <td title="--24 баллов" class="rr-4">
                        <b style="color: red">-24</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        256                    </td>
                    <td class="rr-2">
<img alt="" class="btn-vote" src="img/res-up.png"><sup style="color: green">+1</sup>                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=6735">Николай Караченцов, Елена Шанина &ndash; Я тебя никогда не забуду</a>
                                            </td>
                    <td title="--24 баллов" class="rr-4">
                        <b style="color: red">-24</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        231                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=10760">ДДТ &ndash; В последнюю осень</a>
                                            </td>
                    <td title="--24 баллов" class="rr-4">
                        <b style="color: red">-24</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        260                    </td>
                    <td class="rr-2">
                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=5099">Любэ &ndash; Позови меня тихо по имени</a>
                                            </td>
                    <td title="--24 баллов" class="rr-4">
                        <b style="color: red">-24</b>
                    </td>
                </tr>
                <tr>
                    <td class="rr-1">
                        207                    </td>
                    <td class="rr-2">
<img alt="" class="btn-vote" src="img/res-up.png"><sup style="color: green">+1</sup>                    </td>
                    <td class="rr-3">
                                                <a href="item_info.php?id=5065">Олег Митяев &ndash; Как здорово, что все мы здесь сегодня собрались</a>
                                            </td>
                    <td title="--24 баллов" class="rr-4">
                        <b style="color: red">-24</b>
                    </td>
                </tr>
        </table>
    </div>
                



<div class="right-column-item">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Песни: главная1 (300x600) -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-4958342012590043"
     data-ad-slot="8166770972"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>




                                <div class="block-header">
    <div class="header">
        Последние отзывы    </div>
</div>
<br>
<div class="block-notice-t">
        <div itemscope itemtype="http://schema.org/MusicComposition">
            <meta itemprop="name" content="Ветерок"/>
            <meta itemprop="producer" content="Аркадий Кобяков"/>
            <div itemprop="review" itemscope itemtype="http://schema.org/Review">
                <div>
                    <a href="comments.php?id=20819#c16096">
                        <span itemprop="author">
                            Гость                        </span>
                    </a>&nbsp;
                    <span class="t-gray"><small style="white-space: nowrap;">04.06.2022</small></span>
                    <meta itemprop="datePublished" content="2022-06-04" />
                    <br>                    <b><a href="item_info.php?id=20819">Аркадий Кобяков&nbsp;&ndash;&nbsp;Ветерок</a></b>
                                    </div>
                <div style="padding-top: 5px;">
                    <a class="block-link-t" title="" href="comments.php?id=20819#c16096">
                        <span itemprop="reviewBody">Пидарас ебаный . Сидел  в красной хате ломал людей залупа.</span>
                    </a>
                </div>
            </div>
        </div>
        <br>
        <div itemscope itemtype="http://schema.org/MusicComposition">
            <meta itemprop="name" content="Звезда по имени Солнце"/>
            <meta itemprop="producer" content="Кино"/>
            <div itemprop="review" itemscope itemtype="http://schema.org/Review">
                <div>
                    <a href="comments.php?id=242#c16088">
                        <span itemprop="author">
                            Цой топ                        </span>
                    </a>&nbsp;
                    <span class="t-gray"><small style="white-space: nowrap;">21.04.2022</small></span>
                    <meta itemprop="datePublished" content="2022-04-21" />
                    <br>                    <b><a href="item_info.php?id=242">Кино&nbsp;&ndash;&nbsp;Звезда по имени Солнце</a></b>
                                    </div>
                <div style="padding-top: 5px;">
                    <a class="block-link-t" title="" href="comments.php?id=242#c16088">
                        <span itemprop="reviewBody">Песня очень хорошая. Не пойму почему ее все критикуют.</span>
                    </a>
                </div>
            </div>
        </div>
        <br>
        <div itemscope itemtype="http://schema.org/MusicComposition">
            <meta itemprop="name" content="Как здорово, что все мы здесь сегодня собрались"/>
            <meta itemprop="producer" content="Олег Митяев"/>
            <div itemprop="review" itemscope itemtype="http://schema.org/Review">
                <div>
                    <a href="comments.php?id=5065#c16087">
                        <span itemprop="author">
                            Гость                        </span>
                    </a>&nbsp;
                    <span class="t-gray"><small style="white-space: nowrap;">18.04.2022</small></span>
                    <meta itemprop="datePublished" content="2022-04-18" />
                    <br>                    <b><a href="item_info.php?id=5065">Олег Митяев&nbsp;&ndash;&nbsp;Как здорово, что все мы здесь сегодня собрались</a></b>
                                    </div>
                <div style="padding-top: 5px;">
                    <a class="block-link-t" title="" href="comments.php?id=5065#c16087">
                        <span itemprop="reviewBody">Хорошая душевная песня</span>
                    </a>
                </div>
            </div>
        </div>
        <br>
        <div itemscope itemtype="http://schema.org/MusicComposition">
            <meta itemprop="name" content="Дорога без конца"/>
            <meta itemprop="producer" content="Альберт Асадуллин"/>
            <div itemprop="review" itemscope itemtype="http://schema.org/Review">
                <div>
                    <a href="comments.php?id=6506#c16086">
                        <span itemprop="author">
                            Лариса                        </span>
                    </a>&nbsp;
                    <span class="t-gray"><small style="white-space: nowrap;">18.04.2022</small></span>
                    <meta itemprop="datePublished" content="2022-04-18" />
                    <br>                    <b><a href="item_info.php?id=6506">Альберт Асадуллин&nbsp;&ndash;&nbsp;Дорога без конца</a></b>
                                    </div>
                <div style="padding-top: 5px;">
                    <a class="block-link-t" title="" href="comments.php?id=6506#c16086">
                        <span itemprop="reviewBody">Шикарная песня в шикарном исполнении. Всегда слёзы на глазах, когда её слушаю.</span>
                    </a>
                </div>
            </div>
        </div>
        <br>
        <div itemscope itemtype="http://schema.org/MusicComposition">
            <meta itemprop="name" content="Белой акации гроздья душистые"/>
            <meta itemprop="producer" content="Людмила Зыкина"/>
            <div itemprop="review" itemscope itemtype="http://schema.org/Review">
                <div>
                    <a href="comments.php?id=10793#c16084">
                        <span itemprop="author">
                            Гость                        </span>
                    </a>&nbsp;
                    <span class="t-gray"><small style="white-space: nowrap;">09.04.2022</small></span>
                    <meta itemprop="datePublished" content="2022-04-09" />
                    <br>                    <b><a href="item_info.php?id=10793">Людмила Зыкина&nbsp;&ndash;&nbsp;Белой акации гроздья душистые</a></b>
                                    </div>
                <div style="padding-top: 5px;">
                    <a class="block-link-t" title="" href="comments.php?id=10793#c16084">
                        <span itemprop="reviewBody">Не Людмила Зыкина! Елена Камбурова.</span>
                    </a>
                </div>
            </div>
        </div>
        <br>
</div>
                

<div class="right-column-item">
<div class="vk-wrapper">
<script type="text/javascript" src="//vk.com/js/api/openapi.js?110"></script>
<!-- VK Widget -->
<div id="vk_groups"></div>
<script type="text/javascript">
VK.Widgets.Group("vk_groups", {
    mode: 0, 
    width: "298", 
    height: "298", 
    color1: 'FFFFFF', 
    color2: '2B587A', 
    color3: '5B7FA6'
}, 69336032);
</script>
</div>
</div>


                





                <div class="block-header">
    <div class="header">
        <a href="news.php" class="no-vis">Новости</a>
    </div>
</div>
<br>
    <div class="block-notice-h">
        <b><a href="read_news.php?id=73">
                Песни-кандидаты на звание лучших            </a></b>
        <br>
        <span class="t-gray"><small style="white-space: nowrap;">26.02.2015</small></span>
    </div>
    <div class="block-notice-t">С сегодняшнего дня у нас есть два списка песен. Список <a href='index.php?main_list=1'>лучших песен всех времен</a> и <a href='index.php?main_list=0'>список песен-кандидатов</a> на попадание в основной список. Теперь все новые песни, которые пользователи добавляют на сайт, сначала попадают в список кандидатов. Время от времени песни из верхней части списка кандидатов будут добавляться в основной список, а нижняя часть основного списка будет отправляться обратно в список претендентов. 
<br><br>
...</div>
    <div class="block-notice-h">
        <b><a href="read_news.php?id=65">
                Вопросы к песням            </a></b>
        <br>
        <span class="t-gray"><small style="white-space: nowrap;">02.04.2014</small></span>
    </div>
    <div class="block-notice-t">Знаете интересные факт о песне? Тогда придумайте вопрос и пришлите его нам. Он будет опубликован на странице песни. Сделать это просто. Зайдите на страницу описания песни и далее смотрите секцию "Вопросы". Пример можно посмотреть <a href="http://www.100bestsongs.ru/questions.php?item_id=214">здесь</a></div>
                


                                

<div class="right-column-item">
<div class="fb-page" data-href="https://www.facebook.com/100bestsongs" data-width="300" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"><div class="fb-xfbml-parse-ignore"><blockquote cite="https://www.facebook.com/100bestsongs"><a href="https://www.facebook.com/100bestsongs">100 лучших песен всех времен</a></blockquote></div></div>
</div>

                

<div class="right-column-item">
<!--div id="n4p_6797">Loading...</div>
<script type="text/javascript" charset="UTF-8" src="http://js.grt02.com/ticker_6797.js"></script-->

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Песни главная 2 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:250px"
     data-ad-client="ca-pub-4958342012590043"
     data-ad-slot="7219162170"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>



            </td>
        </tr>
        <tr>
    <td colspan="2" style="padding-left:50px; padding-top:20px">
        <script type="text/javascript"><!--
google_ad_client = "pub-4958342012590043";
/* Песни: футер 728x90 */
google_ad_slot = "8491909541";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
        <br><br>
        <div id="vk_comments"></div>
<script type="text/javascript">
VK.Widgets.Comments("vk_comments", {limit: 10, width: "728", attach: "*"});
</script>
<br>        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Песни рек конт -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:200px"
     data-ad-client="ca-pub-4958342012590043"
     data-ad-slot="1582784976"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
    </td>
    <td></td>
</tr>
<tr>
    <td colspan="3" class="bottom">
        <div class="bottom-line"><img src="/img/p.gif" width="1" height="2" alt="" /></div>
    </td>
</tr>
<tr style="vertical-align: top">
    <td class="bottom-copyright">
        &copy; 2009&ndash;2022 <a href="/index.php">&laquo;100 лучших песен&raquo;</a>&nbsp;
        При  частичном или полном цитировании материалов сайта ссылка на <a href='http://100bestsongs.ru'>100bestsongs.ru</a> обязательна<br>
        <script type="text/javascript">
                var login  = 'admin';
                var srvr = '100bestsongs.ru';
                var addr  = login+'@'+srvr;
                var url = 'mailto:'+ addr;
                document.write('<a href="'+url+'">'+ 'Напишите нам' +'</a>');
        </script>
        &nbsp;|&nbsp;<a href="/about.php">О&nbsp;проекте</a>&nbsp;|&nbsp;<a href="/message_for_oss.pdf">Уведомление о рекламе</a>
    </td>
    <td>


<!--LiveInternet counter--><script type="text/javascript"><!--
document.write("<a href='http://www.liveinternet.ru/click' "+
"target=_blank><img src='//counter.yadro.ru/hit?t14.3;r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";"+Math.random()+
"' alt='' title='LiveInternet: number of pageviews for 24 hours,"+
" of visitors for 24 hours and for today is shown' "+
"border='0' width='88' height='31'><\/a>")
//--></script><!--/LiveInternet-->

<!-- Rating@Mail.ru counter -->
<script type="text/javascript">
var _tmr = window._tmr || (window._tmr = []);
_tmr.push({id: "1894285", type: "pageView", start: (new Date()).getTime()});
(function (d, w, id) {
  if (d.getElementById(id)) return;
  var ts = d.createElement("script"); ts.type = "text/javascript"; ts.async = true; ts.id = id;
  ts.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//top-fwz1.mail.ru/js/code.js";
  var f = function () {var s = d.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ts, s);};
  if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
})(document, window, "topmailru-code");
</script><noscript><div style="position:absolute;left:-10000px;">
<img src="//top-fwz1.mail.ru/counter?id=1894285;js=na" style="border:0;" height="1" width="1" alt="Рейтинг@Mail.ru" />
</div></noscript>
<!-- //Rating@Mail.ru counter -->
<!-- Rating@Mail.ru logo -->
<a href="http://top.mail.ru/jump?from=1894285">
<img src="//top-fwz1.mail.ru/counter?id=1894285;t=487;l=1"
style="border:0;" height="31" width="88" alt="Рейтинг@Mail.ru" /></a>
<!-- //Rating@Mail.ru logo -->

<!--Openstat--><span id="openstat2116721"></span><script type="text/javascript">
var openstat = { counter: 2116721, image: 5042, next: openstat }; document.write(unescape("%3Cscript%20src=%22http" +
(("https:" == document.location.protocol) ? "s" : "") +
"://openstat.net/cnt.js%22%20defer=%22defer%22%3E%3C/script%3E"));
</script><!--/Openstat-->

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-15391107-6']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

        </td>
        <td class="bottom-xpanda">
    </td>
</tr>
    </table>
</body>
</html>

"""

soup = BeautifulSoup(html, 'html.parser')
fdadf = soup.find_all(itemprop="name")
dd = fdadf[::2]
print(*dd, sep = "\n")