# -*- coding: utf-8 -*-
supported_languages = ['en', 'de', 'fr', 'cn']

trads = {
    'clear_button':
        {
            'en': 'Clear selection',
            'de': 'Auswahl aufheben',
            'fr': 'Annuler la sélection',
            'cn': '清空选区',
        },
    'bar_glaciers_selected':
        {
            'en': 'Glaciers selected: {} of {}',
            'de': 'Ausgewählte Gletscher: {} von {}',
            'fr': 'Glaciers sélectionnés: {} de {}',
            'cn': '已选择冰川：\n {}条，共计：{}条',
        },
    'bar_area':
        {
            'en': 'Area',
            'de': 'Fläche',
            'fr': 'Surface',
            'cn': '面积',
        },
    'bar_volume':
        {
            'en': 'Volume',
            'de': 'Volumen',
            'fr': 'Volume',
            'cn': '体积',
        },
    'bar_sealevel_text':
        {
            'en': 'Sea-level equivalent: ',
            'de': 'Beitrag zum Meeresspiegelanstieg:<br>',
            'fr': "Élévation du niveau de la mer:<br>",
            'cn': '对应海平面上升高度: ',
        },
    'bar_sealevel_y':
        {
            'en': 'Volume in mm sea-level equivalent',
            'de': 'Beitrag zum Meeresspiegelanstieg in mm',
            'fr': 'Élévation du niveau de la mer en mm',
            'cn': '冰川体积对应海平面上升高度（mm）',
        },
    'map_plot_x':
        {
            'en': 'Longitude',
            'de': 'Geographische Länge',
            'fr': 'Longitude',
            'cn': '经度',
        },
    'map_plot_y':
        {
            'en': 'Latitude',
            'de': 'Geographische Breite',
            'fr': 'Latitude',
            'cn': '纬度',
        },
    'temp_plot_x':
        {
            'en': 'Annual Temperature at avg. altitude (°C)',
            'de': 'Jahresdurchschnittstemperatur in mittlerer Höhe (°C)',
            'fr': "Temperature annuelle à l'altitude moyenne (°C)",
            'cn': '冰川平均高程处的年平均气温（°C）',
        },
    'trend_plot_x':
        {
            'en': 'Temperature trend 1979-2018 (°C/decade)',
            'de': 'Temperaturtrend 1979-2018 (°C/Dekade)',
            'fr': 'Tendance de température 1979-2018 (°C/décade)',
            'cn': '1979-2018年气温变化率（°C/10年）',
        },
    'trend_plot_y':
        {
            'en': 'Glacier count',
            'de': 'Gletscher Anzahl',
            'fr': 'Nombre de glaciers',
            'cn': '冰川数目',
        },
    'precip_plot_x':
        {
            'en': 'Annual Precipitation (mm/yr)',
            'de': 'Jährlicher Niederschlag (mm/Jahr)',
            'fr': 'Précipitations annuelles (mm/an)',
            'cn': '年降水量（mm/年）',
        },
    'elev_plot_x':
        {
            'en': 'Mean elevation of the glacier (m a.s.l.)',
            'de': 'Mittlere Höhe des Gletschers (m ü.M.)',
            'fr': 'Altitude moyenne du glacier (m)',
            'cn': '冰川平均海拔（m a.s.l.）',
        },
    'elev_plot_y':
        {
            'en': 'Latitude',
            'de': 'Geographische Breite',
            'fr': 'Latitude',
            'cn': '纬度',
        },
    'instructions':
        {
            'en': 'Choose your region of interest by clicking and dragging '
                  'the mouse in the map or in the other figures.<br><b>Reset '
                  'your selection with the "Clear selection"  button on the '
                  'left</b>.<br>For more information about the app and our '
                  'data sources, visit <a href="http://edu.oggm.org/en/latest/'
                  'explorer.html">edu.oggm.org</a>',
            'de': 'Wähle eine Region aus, indem du mit der Maus in der '
                  'Weltkarte oder in den anderen Graphiken klickst und ziehst. '
                  '<br><b>Setze deine Auswahl mit dem "Auswahl aufheben"-'
                  'Button auf der linken Seite zurück</b>. Für mehr '
                  'Informationen zu der App und den Datenquellen gehe auf '
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">'
                  'edu.oggm.org</a>.',
            'fr': 'Choisis une région en cliquant et sélectionnant un rectangle '
                  'sur la carte ou sur les autres figures. '
                  '<br><b>Annule la sélection avec le bouton sur la gauche</b>. '
                  "Pour plus d'informations sur l'appliquation et son utilisation, "
                  'visite <a href="http://edu.oggm.org/en/latest/explorer.html">'
                  'edu.oggm.org</a>.',
            'cn': '在任意图表中点击鼠标左键并拖拽以选择您感兴趣的区域或范围。'
		          '<br><b>单击左侧“清空选区”按钮以清空您选择的区域</b>.<br>关于本'
		          'app及其所用数据的更多信息，请访问'
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">edu.oggm.org</a>',
        },
    'abbreviations':
        {
            'en': 'Abbreviations:<br>'
                  '"asl" (above sea level): total glacier volume that is above sea level.<br>'
                  '"bsl" (below sea level): total glacier volume that is below sea level in the ocean (grounded).',
            'de': 'Abkürzungen:<br>'
                  '"asl" (above sea level): diese Rubrik umfasst das Gletschervolumen, das sich oberhalb des Meeresspiegels befindet. <br>'
                  '"bsl" (below sea level): diese Rubrik umfasst das Gletschervolumen, das sich unterhalb des Meerespiegels befindet, also bis auf den Meeresboden reicht.',
            'fr': 'Abbréviations:<br>'
                  '"asl" (above sea level): volume total de glace se trouvant au dessus du niveau de la mer.<br>'
                  '"bsl" (below sea level): volume total de glace se trouvant en dessous du niveau de la mer.',
            'cn': '"asl" (above sea level): 海平面以上，海平面以上的冰川总体积。<br>'
                  '"bsl" (below sea level): 海平面以下，海洋中海平面以下的冰川总体积。',
        },

}
