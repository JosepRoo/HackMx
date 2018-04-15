export const navigation = [
    {
        'id'       : 'applications',
        'title'    : 'Principal',
        'translate': 'NAV.APPLICATIONS',
        'type'     : 'group',
        'icon'     : 'apps',
        'children' : [
            {
                'id'       : 'dashboards',
                'title'    : 'Dashboards',
                'translate': 'NAV.DASHBOARDS',
                'type'     : 'collapse',
                'icon'     : 'dashboard',
                'children' : [
                    {
                        'id'   : 'analytics',
                        'title': 'Analisis',
                        'type' : 'item',
                        'url'  : '/apps/dashboards/analytics'
                    }
                ]
            }
          ]
    }
  ];
